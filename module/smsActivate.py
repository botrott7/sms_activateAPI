import json
import time
import requests


class SMSActivateAPI:
    __base_url = "https://sms-activate.ru/stubs/handler_api.php"

    def __init__(self, api_key):
        self.__api_key = api_key

    def get_balance(self):
        '''Получить баланс'''
        params = {
            'api_key': self.__api_key,
            'action': 'getBalance',
        }
        res = requests.post(self.__base_url, params=params)
        if res.status_code == 200:
            return float(res.text.split(':')[1])
        return res.status_code

    def get_numbers_status(self, country=None, operator=None):
        '''Получить кол-во свободных номеров'''
        params = {
            'api_key': self.__api_key,
            'action': 'getNumbersStatus',
            'country': country,
            'operator': operator,
        }
        res = requests.post(self.__base_url, params=params)
        if res.status_code == 200:
            return json.loads(res.text)
        return res.status_code

    def get_number(self, service, operator='any', forward=0, country=0):
        '''Заказать номер'''
        params = {
            'api_key': self.__api_key,
            'action': 'getNumber',
            'service': service,
            'operator': operator,
            'forward': forward,
            'country': country,

        }
        res = requests.post(self.__base_url, params=params)
        if res.status_code == 200 and 'ACCESS_NUMBER' in res.text:
            print(res.text)
            list = res.text.split(':')[1:3]
            return list
        return res.status_code

    def set_status(self, activation_id, status, forward=0):
        '''Установить статус'''
        params = {
            "api_key": self.__api_key,
            "id": activation_id,
            "status": status,
            "action": "setStatus",
        }
        res = requests.post(self.__base_url, params=params)
        if res.status_code == 200:
            return res.text
        return res.status_code

    def get_status(self, activation_id):
        '''Получить статус'''
        params = {
            "api_key": self.__api_key,
            "id": activation_id,
            "action": "getStatus",
        }
        res = requests.post(self.__base_url, params=params)
        if res.status_code == 200:
            return res.text.split(":")
        return res.status_code

    def get_code(self, id, wait=3, max_wait=60):
        '''Получаем код'''
        wait_time = 0
        status = self.get_status(id)
        for i in range(max_wait):
            status = self.get_status(id)
            print(f'Status activate:  {status[0]}')
            if 'STATUS_OK' in status:
                return status
            time.sleep(wait)
            wait_time += wait
            if wait_time >= max_wait:  # если время которое мы прождали >= допустимого
                print(f'Timeout: {max_wait} sec')
                return None
