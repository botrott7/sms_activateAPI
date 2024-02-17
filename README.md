# sms_activateAPI

Класс SMSActivateAPI имеет следующие методы:

1. `__init__(self, api_key)`: Конструктор класса, инициализирует экземпляр класса с указанным API-ключом.

2. `get_balance(self)`: Метод для получения текущего баланса на аккаунте.

3. `get_numbers_status(self, country=None, operator=None)`: Метод для получения количества доступных номеров для активации в указанной стране и/или операторе.

4. `get_number(self, service, operator='any', forward=0, country=0)`: Метод для заказа номера для активации. Принимает параметры service (название сервиса, для которого нужно получить номер), operator (название оператора, по умолчанию 'any'), forward (параметр для переадресации, по умолчанию 0) и country (код страны, по умолчанию 0).

5. `set_status(self, activation_id, status, forward=0)`: Метод для установки статуса активации. Принимает параметры activationid (идентификатор активации), status (новый статус) и forward (параметр для переадресации, по умолчанию 0).

6. `getstatus(self, activationid)`: Метод для получения текущего статуса активации по идентификатору.

7. `getcode(self, id, wait=3, maxwait=60)`: Метод для получения кода активации. Принимает параметры id (идентификатор активации), wait (время ожидания между запросами статуса, по умолчанию 3 секунды) и maxwait (максимальное время ожидания, по умолчанию 60 секунд).

8. `def get_operators(self, country=None)`: Метод для получения списка доступных операторов РФ=0, Украина=1, Казахстан=2.

Класс использует библиотеку requests для отправки HTTP-запросов к API сервиса SMS активации. Ответы сервера обрабатываются, и результаты возвращаются в виде соответствующих данных или кода состояния HTTP.

### Пример использования:

```python
api_key = "your_api_key"
api = SMSActivateAPI(api_key)

balance = api.get_balance()
print("Баланс аккаунта:", balance)

numbers_status = api.get_numbers_status(country="RU", operator="MTC")
print("Количество доступных номеров:", numbers_status)

number = api.get_number(service="gmail", operator="any", forward=0, country=0)
print("Номер для активации:", number)

activation_id = "your_activation_id"
status = api.get_status(activation_id)
print("Статус активации:", status)

code = api.get_code(activation_id)
print("Код активации:", code)

operator = api.sms_activate.get_operators(0)
print("Cписок операторов для РФ:", ', '.join(operator['countryOperators'][0]))
```


#### Обратите внимание, перед использованием модуля вам потребуется зарегистрироваться на сайте sms-activate.ru и получить API-ключ.