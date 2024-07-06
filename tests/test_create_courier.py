import allure
import pytest
from helpers import RandomCourierGeneration
from Api import CourierMethods


@allure.feature('Ручка /api/v1/courier')
class TestCreateCourier:
    @allure.title('Проверка создания курьера c корректными данными')
    def test_create_courier_success(self, create_courier):
        create_courier = CourierMethods.create_courier(create_courier)
        assert create_courier.status_code == 201 and create_courier.text == '{"ok":true}'

    @allure.title('Проверка создания курьера с существующим логином')
    def test_create_courier_existing_login_error(self, create_courier):
        user_data = CourierMethods.create_courier_existing_login(create_courier)
        assert user_data.status_code == 409 and user_data.json()[
            'message'] == 'Этот логин уже используется. Попробуйте другой.'

    @allure.title('Проверка создания курьера с незаполненными обязательными полями')
    @pytest.mark.parametrize('field', ['login', 'password'])
    def test_create_courier_empty_input_error(self, field):
        user_data = RandomCourierGeneration().generate_random_courier_data()
        user_data.pop(field)
        response = CourierMethods.create_courier(user_data)
        assert response.status_code == 400
        assert response.json()['message'] == 'Недостаточно данных для создания учетной записи'
