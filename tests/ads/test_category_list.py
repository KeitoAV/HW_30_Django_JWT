import warnings

import pytest

from ads.models.category import Category



@pytest.mark.django_db
def test_category_list(client):
    category = Category.objects.create(
        name="Test category",
        slug=None,
    )

    expected_response = {
        "count": 1,
        "next": None,
        "previous": None,
        "results": [{
            "id": category.id,
            "name": "Test category",
            "slug": None,
        }]
    }

    response = client.get("/cat/")

    assert response.status_code == 200
    assert response.data == expected_response
