# Файл «sender_stand_request.py» необходим для хранения всех запросов

# Импорт необходимых пакетов
import requests
import configuration
import data

# 1. POST-запрос на создание нового заказа
def post_create_new_order():
    return requests.post(configuration.URL_SERVICE + configuration.POST_CREATE_NEW_ORDER,
           json=data.body_order)

# 1. GET-запрос на получение информации о заказе по его номеру
def get_info_order(track_number):
    return requests.get(configuration.URL_SERVICE + configuration.GET_INFO_ORDER,
           params={"t": track_number})