import allure
import pytest
from helpers import OrderDataGeneration
from Api import OrderMethods


@allure.feature('Ручка /api/v1/orders')
class TestOrders:
    @pytest.mark.parametrize('color', [['BLACK'], ['GREY'], ['BLACK', 'GREY'], []])
    @allure.description('Проверка создания заказа с выбором любого цвета и без')
    def test_create_order_color(self, color):
        order_data = OrderDataGeneration.generate_order_data(color)
        response = OrderMethods.create_order(order_data)
        assert response.status_code == 201 and response.json()['track'] != 0
