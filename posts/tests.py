# from django.test import TestCase
# from .models import Post
#
#
# class TodoModelTest(TestCase):
#
#     @classmethod
#     def setUpTestData(cls):
#         Post.objects.create(title='first todo', body='a body here')
#     def test_title_content(self):
#         post = Post.objects.get(id=1)
#         expected_object_name = f'{post.title}'
#         self.assertEqual(expected_object_name, 'first todo')
#     def test_body_content(self):
#         post = Post.objects.get(id=1)
#         expected_object_name = f'{post.body}'
#         self.assertEqual(expected_object_name, 'a body here')