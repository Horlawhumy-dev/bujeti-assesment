
import pytest
import json
from rest_framework.test import APIClient

client = APIClient()


@pytest.mark.django_db
def test_get_african_urban_areas():
    response = client.get('/api/v1/african/countries/urban_areas/')
    assert json.loads(response)["count"] >= 8
    assert response["status_code"] == 200
    

@pytest.mark.django_db
def test_get_african_urban_area():
    response = client.get('/api/v1/african/countries/urban_area/cairo/')
    assert json.loads(response)["data"]["continent"] == "Africa"
    assert response["status_code"] == 200