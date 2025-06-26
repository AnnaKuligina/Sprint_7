import requests
from faker import Faker

from curl import Urls, Endpoints


class CreateCourierData:

    @staticmethod
    def generate_valid_data_to_create_courier(): # Создание валидных данных
        fake = Faker("ru_RU")

        login = fake.user_name()
        password = fake.password()
        first_name = fake.first_name()

        data = {
            "login": login,
            "password": password,
            "firstName": first_name
        }

        return data

    @staticmethod
    def generate_invalid_data_to_create_courier_without_login(): # Создание данных без поля "login"
        fake = Faker("ru_RU")

        password = fake.password()
        first_name = fake.first_name()

        data = {
            "login": "",
            "password": password,
            "firstName": first_name
        }

        return data


    @staticmethod
    def generate_invalid_data_to_create_courier_without_password(): # Создание данных без поля "password"
        fake = Faker("ru_RU")

        login = fake.user_name()
        first_name = fake.first_name()

        data = {
            "login": login,
            "password": "",
            "firstName": first_name
        }

        return data


class Courier:


    @staticmethod
    def create_new_courier_and_get_courier_data(): # Регистрация с возвратом кода ответа и данных курьера
        data = CreateCourierData.generate_valid_data_to_create_courier()
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.courier}', data=data)
        return {"response_text": response.text, "status_code": response.status_code, "data": data}

    @staticmethod
    def courier_login_and_get_id(data): # Логин в системе с возвратом кода ответа и id курьера
        response = requests.post(f'{Urls.SCOOTER_URL}{Endpoints.courier_login}', data=data)
        return {"id": str(response.json()["id"]), "response_text": response.text, "status_code": response.status_code}

    @staticmethod
    def courier_delete(courier_id): # Удаление курьера
        response = requests.delete(f'{Urls.SCOOTER_URL}{Endpoints.courier}{courier_id}')
        return {"response_text": response.text, "status_code": response.status_code}




from allure_commons import _allure

Step = _allure.step
Check = _allure.step