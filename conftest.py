import requests
import pytest
from URL import Urls
from helpers import RandomCourierGeneration


@pytest.fixture(scope='function')
def create_courier():
    data_payload = RandomCourierGeneration().generate_random_courier_data()
    yield data_payload
    requests.post(Urls.url_main + Urls.url_create_courier, data=data_payload)