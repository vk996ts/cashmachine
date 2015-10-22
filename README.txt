1. Setup

$ virtualenv env
$ source env/bin/activate
$ pip install -r requirements.txt
$ cd app
$ ./manage.py migrate
$ ./manage.py loaddata accounts.json
$ ./manage.py runserver

2. Test Data:

Card Number: 1111222233334444 PIN: 1234 Is Admin: True
Card Number: 3333444455556666 PIN: 1234 Is Admin: False
