import pytest
import docker
import requests

name = "ctomcatapp"

@pytest.fixture

def error_fixture():
    assert 0

def test_container():
    client = docker.from_env()
    container = client.containers.get(name)
    assert container.status == "running"

def test_app():
    response = requests.get('http://localhost:8080/sample')
    assert response.status_code == 200



# ----------------------------------------------------------
# import requests
# import logging
#
# baseUrl = "http://localhost:8080/"
# LOGGER = logging.getLogger(__name__)
#
# def test_sample_app() :
#     path = "sample"
# #    LOGGER.info('Site response')
#     response = requests.get(url=baseUrl+path,timeout = 0.5)
#     assert response.status_code == 200
