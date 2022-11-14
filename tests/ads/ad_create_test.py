import pytest


@pytest.mark.django_db
def test_create_ad(client, user_id_token, category):
    user_id, user_token = user_id_token
    expected_response = {
        "author": user_id,
        "id": 1,
        "is_published": False,
        "name": "Test ad create",
        "price": 1000,
        "description": "Test ad create - description.",
        "image": None,
        "category": category.pk,
    }

    data = {
        "author": user_id,
        "is_published": False,
        "name": "Test ad create",
        "price": 1000,
        "description": "Test ad create - description.",
        "image": None,
        "category": category.pk,
    }

    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Token " + user_token
    )

    assert response.status_code == 201
    assert response.data == expected_response


@pytest.mark.django_db
def test_create_ad_incorrect_published_status(client, user_id_token, category):
    user_id, user_token = user_id_token

    data = {
        "author": user_id,
        "is_published": True,
        "name": "Test ad create",
        "price": 1000,
        "description": "Test ad create - description.",
        "image": None,
        "category": category.pk,
    }

    expected_response = {
        "is_published": [
            "Некорректный статус."
        ]

    }
    response = client.post(
        "/ad/create/",
        data,
        content_type='application/json',
        HTTP_AUTHORIZATION="Token " + user_token
    )

    assert response.status_code == 400
    assert response.data == expected_response


