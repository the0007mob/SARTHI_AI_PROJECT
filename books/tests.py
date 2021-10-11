from django.test import TestCase
import mock

# Create your tests here.
from django.urls import reverse
from rest_framework.test import APITestCase


MockMultipleResponse = mock.Mock(
    status_code=200,
    status="success",
    json=mock.Mock(
        return_value=[{
            "name": "A Game of Thrones",
            "isbn": "978-0553103540",
            "authors": [
                "George R. R. Martin"
            ],
            "publisher": "Bantam Books",
            "numberOfPages": 694,
            "country": "United States",
            "released": "1996-08-01T00:00:00Z"
        },
        {
            "name": "A Clash of Kings",
            "isbn": "978-0553108033",
            "authors": [
                "George R. R. Martin"
            ],
            "publisher": "Bantam Books",
            "numberOfPages": 768,
            "country": "United States",
            "released": "1999-02-02T00:00:00Z"
        }]
    )
)

MockSingleResponse = mock.Mock(
    status_code=200,
    status="success",
    json=mock.Mock(
        return_value=[{
            "name": "A Game of Thrones",
            "isbn": "978-0553103540",
            "authors": [
                "George R. R. Martin"
            ],
            "publisher": "Bantam Books",
            "numberOfPages": 694,
            "country": "United States",
            "released": "1996-08-01T00:00:00Z"
        }]
    )
)

MockEmptyBookResponse = mock.Mock(
    status_code=200,
    status="success",
    json=mock.Mock(
        return_value=[]
    )
)


class ExternalBooksTests(APITestCase):
    url = reverse('api:external-books')

    @mock.patch('requests.get', return_value=MockMultipleResponse)
    def test_get_books_from_api(self, mock_object):
        response = self.client.get(self.url)
        mocked_response = response.json()
        self.assertEquals(mocked_response.get('status'), 'success')
        self.assertEquals(mocked_response.get('status_code'), 200)
        self.assertGreater(len(mocked_response.get('data')), 1)
        self.assertIn(mocked_response.get('data')[0].get('name'), 'A Game of Thrones')
        self.assertIn(mocked_response.get('data')[1].get('name'), 'A Clash of Kings')

    @mock.patch('requests.get', return_value=MockSingleResponse)
    def test_get_book_from_api(self, mock_object):
        response = self.client.get(self.url)
        mocked_response = response.json()
        self.assertEquals(mocked_response.get('status'), 'success')
        self.assertEquals(mocked_response.get('status_code'), 200)
        self.assertEquals(len(mocked_response.get('data')), 1)
        self.assertIn(mocked_response.get('data')[0].get('name'), 'A Game of Thrones')
        self.assertIn(mocked_response.get('data')[0].get('publisher'), 'Bantam Books')

    @mock.patch('requests.get', return_value=MockEmptyBookResponse)
    def test_get_empty_response_from_api(self, mock_object):
        response = self.client.get(self.url)
        mocked_response = response.json()
        self.assertEquals(mocked_response.get('status'), 'success')
        self.assertEquals(mocked_response.get('status_code'), 200)
        self.assertEquals(len(mocked_response.get('data')), 0)
