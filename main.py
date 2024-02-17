import os

from module.smsActivate import SMSActivateAPI
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

sms_activate = SMSActivateAPI(API_KEY)

count_of_num = sms_activate.get_numbers_status(country=0, operator='any')
print(count_of_num)
balance = sms_activate.get_balance()
print(balance)

operator = sms_activate.get_operators(0)
print(', '.join(operator['countryOperators'][0]))

if int(count_of_num['fb_0']) > 0 and balance >= 5:
    id, num = sms_activate.get_number('fb', 'any')
    print(f'Получили номер: {num}')

    sms_activate.set_status(id, 1)

    code = sms_activate.get_code(id, max_wait=250)
    if code is not None and code[0] == 'STATUS_OK':
        print(sms_activate.set_status(id, status=6))
