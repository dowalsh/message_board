from django.test import TestCase
from .models import Post

class PostModelTest(TestCase):
    def setUp(self):
        Post.objects.create(title='Test Post', content='Test Content')

    def test_post_content(self):
        post = Post.objects.get(id=1)
        expected_object_name = f'{post.title}'
        self.assertEqual(expected_object_name, 'Test Post')
        # test content
        expected_object_content = f'{post.content}'
        self.assertEqual(expected_object_content, 'Test Content')
