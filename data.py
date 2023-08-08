# Файл «data.py» необходим для хранения данных

# Заголовок
headers = {
    "Content-Type": "application/json",
    "Authorization": ""
}

# Тело запроса на создание заказа
body_order = {
    "firstName": "Ольга",
    "lastName": "Мекка",
    "address": "пр-кт Просвещения, дом 15, квартира 959",
    "metroStation": 5,
    "phone": "+7 921 555 55 55",
    "rentTime": 5,
    "deliveryDate": "2023-08-07",
    "comment": "Не звоните в дверь",
    "color": [
        "BLACK"
    ]
}