import pytest

from users.models import Location


@pytest.mark.django_db
def test_category_list(client):
    location = Location.objects.create(
        name="Test location",
        lat=None,
        lng=None
    )

    expected_response = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [{
            "id": location.id,
            "name": "Test location",
            "lat": None,
            "lng": None
        }]
    }

    response = client.get("/location/")

    assert response.status_code == 200
    assert response.data == expected_response
