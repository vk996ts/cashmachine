

from django.conf.urls import patterns, include, url
from django.contrib import admin


from accounts.views import HomePageView, PinPageView, MainPageView, AccountPageView, CashPageView, ResultView, ExitView, PinWrongView, CashSuccessView


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^pin/wrong/$', PinWrongView.as_view(), name='pin_wrong'),
    url(r'^pin/$', PinPageView.as_view(), name='pin'),
    url(r'^main/$', MainPageView.as_view(), name='main'),
    url(r'^account/$', AccountPageView.as_view(), name='account'),
    url(r'^cash/$', CashPageView.as_view(), name='cash'),
    url(r'^success/$', CashSuccessView.as_view(), name='cash_success'),
    url(r'^result/(?P<code>\d+)/$', ResultView.as_view(), name='result'),
    url(r'^exit/$', ExitView.as_view(), name='exit'),
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
