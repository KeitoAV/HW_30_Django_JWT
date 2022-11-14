import factory

from ads.models.ad import Ad
from ads.models.category import Category

from users.models import User


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = "Category test"


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    role = 'member'
    first_name = "Test first_name"
    last_name = "Test last_name"
    username = factory.Faker("name")


class AdFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Ad

    name = "Ad test"
    author = factory.SubFactory(UserFactory)
    price = 500
    description = "New Ad test description"
    is_published = False
    image = None
    category = factory.SubFactory(CategoryFactory)
