class Urls:
    SCOOTER_URL = "https://qa-scooter.praktikum-services.ru"


class Endpoints:
    courier = "/api/v1/courier"  # Создание курьера
    courier_login = f'{courier}/login'  # Логин курьера
    order = "/api/v1/orders"  # Создание заказа и получение списка заказов