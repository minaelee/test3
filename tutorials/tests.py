from django.test import TestCase
from django.urls import reverse
import pytest
from tutorials.models import Tutorial


@pytest.mark.django_db
def test_homepage_access(client):
    url = reverse('home')
    response = client.get(url)
    assert response.status_code == 200


@pytest.fixture
def tutorial(db):

    new_tutorial = Tutorial.objects.create(
        title='Pytest',
        tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
        description='Tutorial on how to apply pytest to a Django application',
        published=True
    )
    return new_tutorial


@pytest.mark.django_db
def test_create_tutorial(tutorial):
    # new_tutorial = Tutorial.objects.create(
    #     title='Pytest',
    #     tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
    #     description='Tutorial on how to apply pytest to a Django application',
    #     published=True
    # )
    assert tutorial.title == "Pytest"


def test_search_tutorials(tutorial):
    # new_tutorial = Tutorial.objects.create(
    #     title='Pytest',
    #     tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
    #     description='Tutorial on how to apply pytest to a Django application',
    #     published=True
    # )
    assert Tutorial.objects.filter(title='Pytest').exists()


def test_update_tutorial(tutorial):
    # new_tutorial = Tutorial.objects.create(
    #     title='Pytest',
    #     tutorial_url='https://pytest-django.readthedocs.io/en/latest/index.html',
    #     description='Tutorial on how to apply pytest to a Django application',
    #     published=True
    # )
    # new_tutorial.title = 'Pytest-Django'
    # new_tutorial.save()
    tutorial.title = 'Pytest-Django'
    tutorial.save()
    # updated_tutorial = Tutorial.objects.get(title='Pytest-Django')
    # assert updated_tutorial.title == 'Pytest-Django'
    assert Tutorial.objects.filter(title='Pytest-Django').exists()
