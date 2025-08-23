import pytest
from django.contrib.auth.models import User
from api.models import Category, Item

@pytest.mark.django_db
def test_create_item():
    user = User.objects.create_user(username="john", password="password123")
    category = Category.objects.create(name="Books")

    item = Item.objects.create(
        name="Django for Beginners",
        description="Learning Django step by step",
        category=category,
        owner=user
    )

    assert item.name == "Django for Beginners"
    assert item.owner.username == "john"
    assert item.category.name == "Books"
