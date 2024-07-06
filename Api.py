import requests
import allure
from URL import Urls


class CourierMethods:
    @staticmethod
    @allure.step('Создание курьера')
    def create_courier(payload):
        response = requests.post(Urls.url_main + Urls.url_create_courier, data=payload)
        return response

    @staticmethod
    @allure.step('Создание курьера c существующим логином')
    def create_courier_existing_login(payload):
        requests.post(Urls.url_main + Urls.url_create_courier, data=payload)
        response_two = requests.post(Urls.url_main + Urls.url_create_courier, data=payload)
        return response_two

    @staticmethod
    @allure.step('Создание и логин курьера')
    def create_and_login_courier(payload):
        requests.post(Urls.url_main + Urls.url_create_courier, data=payload)
        response = requests.post(Urls.url_main + Urls.url_login_courier, data=payload)
        return response

    @staticmethod
    @allure.step('Логин курьера')
    def login_courier(payload):
        response = requests.post(Urls.url_main + Urls.url_login_courier, data=payload)
        return response


class OrderMethods:
    @staticmethod
    @allure.step('Создать заказ')
    def create_order(payload):
        response = requests.post(Urls.url_main + Urls.url_order, data=payload)
        return response


