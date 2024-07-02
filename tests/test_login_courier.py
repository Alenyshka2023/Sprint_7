import allure
import pytest
from helpers import RandomCourierGeneration
from Api import CourierMethods


@allure.feature('Ручка /api/v1/courier/login')
class TestLoginCourier:
    @allure.description('Проверка авторизации курьера с корректными данными')
    def test_login_correct_login_success(self, create_courier):
        login_courier = CourierMethods.create_and_login_courier(create_courier)
        assert login_courier.status_code == 200 and login_courier.json()['id'] != 0

    @allure.description('Проверка авторизации с пустым вводом логина или пароля')
    @pytest.mark.parametrize('field_key, field_value', [('login', ''), ('password', '')])
    def test_login_empty_input_error(self, field_key, field_value):
        user_data = RandomCourierGeneration().generate_random_courier_data()
        payload = user_data.copy()
        payload[field_key] = field_value
        response = CourierMethods.create_and_login_courier(payload)
        assert response.status_code == 400 and response.json()['message'] == 'Недостаточно данных для входа'

    @allure.description('Проверка авторизации с несуществующим логином')
    def test_login_not_exist_login_error(self):
        user_data = RandomCourierGeneration().generate_random_courier_data()
        response = CourierMethods.login_courier(user_data)
        assert response.status_code == 404 and response.json()['message'] == 'Учетная запись не найдена'
