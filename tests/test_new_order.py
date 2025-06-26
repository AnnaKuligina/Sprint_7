import allure
import pytest
import requests
import json
from helper import Step, Check
from data import DataOrder, ResponseText, OrderColors
from curl import Urls, Endpoints


class TestOrder:

    @allure.title('Создание заказа с разными вариантами цветов')
    @pytest.mark.parametrize('color_data, test_case', [
        ({"color": OrderColors.SINGLE_COLOR_BLACK}, "Только BLACK"),
        ({"color": OrderColors.SINGLE_COLOR_GRAY}, "Только GREY"),
        ({"color": OrderColors.COLOR_COMBINATIONS[0]}, "Оба цвета (BLACK и GREY)"),
        ({"color": []}, "Без указания цвета"),
        (None, "Цвет не указан в запросе")
    ])
    def test_order_with_different_colors(self, color_data, test_case): #Проверка создания заказа с различными вариантами указания цвета
        with allure.step(f"Тестовый случай: {test_case}"):
            with Step('Подготовка данных заказа'):
                headers = {"Content-type": "application/json"}
                order_data = DataOrder.data.copy()

                if color_data is not None:
                    order_data.update(color_data)

                payload = json.dumps(order_data)

            with Step('Отправка запроса на создание заказа'):
                response = requests.post(
                    url=f'{Urls.SCOOTER_URL}{Endpoints.order}',
                    headers=headers,
                    data=payload,
                    timeout=10
                )

            with Check('Заказ создан'):
                assert response.status_code == 201 and ResponseText.TRACK in response.text