from django.test import TestCase
from .forms import CommentForm


class TestCommentForm(TestCase):

    def test_form_is_valid(self):
        comment_form = CommentForm({'body': 'test_form_is_valid'})
        self.assertTrue(comment_form.is_valid())

    def test_form_is_invalid(self):
        Comment_form = CommentForm({'body': ''})
        self.assertTrue(comment_form.is_valid(), msg='Form is valid')
