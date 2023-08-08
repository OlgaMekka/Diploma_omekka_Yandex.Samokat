# Файл «sender_stand_request.py» необходим для хранения всех запросов

# Импорт необходимых пакетов
import sender_stand_request

# 1. Получение заказа по треку
def get_track_number_order():
    track_number = sender_stand_request.post_create_new_order()
    return track_number.json()["track"]

# 2. Проверка, что код ответа равен 200
def test_create_and_track_new_order():
    track_number = get_track_number_order()
    get_response = sender_stand_request.get_info_order(track_number)
    assert get_response.status_code == 200