from django.urls import reverse

from django.test import TestCase, Client

from home.models import Article


class ArticleTestCase(TestCase):

    def setUp(self) -> None:
        self.article = Article.objects.create(
            title='Test title',
            content='Test content'
        )
        self.Client = Client()

    def test_create_article(self):
        self.assertEqual(Article.objects.count(), 1)

    def test_article_str(self):
        self.assertEqual(str(self.article), 'Test title - Test content')

    def test_api_get_article(self):
        header = {"Content-type": "applications/json"}
        response_json = self.client.get("/api/articles/", headers=header).json
        self.assertEqual(response_json['count'], 1)
        self.assertEqual(
            response_json["count"][0],
            {
                "title": "Test title",
                "id": 1,
                "content": "test content",
                "author": None,
                "link": "http://testserver/api/articles/1/",
            },
        )