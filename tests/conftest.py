import pytest

from helper import Courier

@pytest.fixture()
def courier(): # Регистрация, авторизация и удаление курьера
    create_courier = Courier.create_new_courier_and_get_courier_data()
    courier_login = Courier.courier_login_and_get_id(create_courier["data"])
    yield create_courier
    Courier.courier_delete(courier_login["id"])