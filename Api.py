import requests
import allure
from URL import Urls


class CourierMethods:
    @staticmethod
    @allure.step('Создание курьера')
    def create_courier(payload):
        response = requests.post(Urls.URL_MAIN + Urls.URL_CREATE_COURIER, data=payload)
        return response

    @staticmethod
    @allure.step('Создание курьера c существующим логином')
    def create_courier_existing_login(payload):
        requests.post(Urls.URL_MAIN + Urls.URL_CREATE_COURIER, data=payload)
        response_two = requests.post(Urls.URL_MAIN + Urls.URL_CREATE_COURIER, data=payload)
        return response_two

    @staticmethod
    @allure.step('Создание и логин курьера')
    def create_and_login_courier(payload):
        requests.post(Urls.URL_MAIN + Urls.URL_CREATE_COURIER, data=payload)
        response = requests.post(Urls.URL_MAIN + Urls.URL_LOGIN_COURIER, data=payload)
        return response

    @staticmethod
    @allure.step('Логин курьера')
    def login_courier(payload):
        response = requests.post(Urls.URL_MAIN + Urls.URL_LOGIN_COURIER, data=payload)
        return response


class OrderMethods:
    @staticmethod
    @allure.step('Создать заказ')
    def create_order(payload):
        response = requests.post(Urls.URL_MAIN + Urls.URL_ORDER, data=payload)
        return response


