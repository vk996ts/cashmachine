# -*- coding: utf-8 -*-
__author__ = 'vitaliy'


from django.views.generic import FormView, TemplateView, View
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.shortcuts import redirect


from braces.views import LoginRequiredMixin
from helpers.lists import get_display
from transactions.models import OPERATION_CODES


from .forms import CardLoginForm, PinForm, CashForm
from .models import Card


class HomePageView(FormView):
    template_name = 'card.html'
    success_url = '/pin/'
    form_class = CardLoginForm

    def form_valid(self, form):
        self.request.session['number'] = form.cleaned_data['number']
        return super(HomePageView, self).form_valid(form)


class PinPageView(FormView):
    template_name = 'pin.html'
    success_url = '/main/'
    form_class = PinForm

    def form_valid(self, form):
        pin = form.cleaned_data['number']
        number = self.request.session.get('number')
        user = authenticate(username=number, password=pin)
        number_user = Card.objects.get(number=number)
        if user is None:
            attempts = self.request.session.get('attempts', 0)
            if attempts < 4:
                attempts+=1
                number_user.create_operation(4)
                self.request.session['attempts'] = attempts
                return redirect('/pin/wrong/')
            else:
                number_user.access(is_active=False)
                number_user.save()
                number_user.create_operation(5)
                return redirect('/result/5/')

        if not user.is_active:
            return redirect('/result/6/')
        login(self.request, user)
        self.request.session['attempts'] = 0
        return super(PinPageView, self).form_valid(form)


class PinWrongView(PinPageView):

    def get_context_data(self, **kwargs):
        context = super(PinWrongView, self).get_context_data(**kwargs)
        context['error'] = u'Wrong PIN. Attempts left: %d' % (4-int(self.request.session.get('attempts')))
        return context


class MainPageView(LoginRequiredMixin, TemplateView):
    template_name = 'main.html'


class AccountPageView(LoginRequiredMixin, TemplateView):
    template_name = 'account.html'


class CashPageView(LoginRequiredMixin, FormView):
    template_name = 'cash.html'
    form_class = CashForm

    def form_valid(self, form):
        amount = int(form.cleaned_data['number'])
        if amount < self.request.user.amount:
            self.request.user.create_operation(1)
            self.request.user.amount -= amount
            self.request.user.save()
            self.request.session['amount'] = amount
            return redirect('/success/')
        else:
            self.request.user.create_operation(3)
            return redirect('/result/3/')


class CashSuccessView(LoginRequiredMixin, TemplateView):
    template_name = 'result.html'

    def get_context_data(self, **kwargs):
        context = super(CashSuccessView, self).get_context_data(**kwargs)
        context['success'] = True
        context['cash'] = self.request.session.get('amount')
        context['error'] =  get_display(1, OPERATION_CODES)
        return context

class ResultView(TemplateView):
    template_name = 'result.html'

    def get_context_data(self, **kwargs):
        context = super(ResultView, self).get_context_data(**kwargs)
        context['error'] = get_display(int(self.kwargs['code']), OPERATION_CODES)
        context['code'] = self.kwargs['code']
        return context


class ExitView(LoginRequiredMixin, View):

    def dispatch(self, request, *args, **kwargs):
        logout(request)
        return redirect('/')