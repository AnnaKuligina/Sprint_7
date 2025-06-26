import allure
import pytest
import requests
from helper import Step, Check
from curl import Urls, Endpoints


class TestGetOrderList:
    """Тесты получения списка заказов"""

    @allure.title('Получение списка заказов')
    def test_get_orders_list_success(self): #Проверка получения непустого списка заказов
        with Step('Отправка запроса на получение списка заказов'):
            response = requests.get(
                url=f'{Urls.SCOOTER_URL}{Endpoints.order}',
                timeout=10
            )

        with Check('Проверка успешного получения списка'):
            assert response.status_code == 200, (
                f"Ожидался статус 200, получен {response.status_code}"
            )

            response_data = response.json()
            assert isinstance(response_data.get("orders"), list), (
                "В ответе отсутствует ключ 'orders' или он не является списком"
            )
            assert len(response_data["orders"]) > 0, (
                "Получен пустой список заказов"
            )