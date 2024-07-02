import requests
import pytest
from URL import Urls
from helpers import RandomCourierGeneration


@pytest.fixture(scope='function')
def create_courier():
    data_payload = RandomCourierGeneration().generate_random_courier_data()
    yield data_payload
    requests.post(Urls.URL_MAIN + Urls.URL_CREATE_COURIER, data=data_payload)