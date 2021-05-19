from django.test import TestCase
from django.contrib.auth.models import User
from .models import Blog 


class BlogTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username='testuser1', 
            password='abc123'
        )

        test_blog = Blog.objects.create(
            author=testuser1, 
            title='Blog title', 
            body='Body content...'
        )

    def test_blog_content(self):
        post = Blog.objects.get(id=1)
        author = f'{post.author}'
        title = f'{post.title}'
        body = f'{post.body}'
        self.assertEqual(author, 'testuser1')
        self.assertEqual(title, 'Blog title')
        self.assertEqual(body, 'Body content...')