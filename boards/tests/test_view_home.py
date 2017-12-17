from django.test import TestCase
from django.urls import resolve, reverse

from ..models import Board
from ..views import BoardListView


class HomeTests(TestCase):
    def setUp(self):
        self.board = Board.objects.create(name='Django', description='Django board.')
        url = reverse('home')
        self.response = self.client.get(url)

    # Testing if Django is returning a status code 200 (success) for the home page
    def test_home_view_status_code(self):
        self.assertEquals(self.response.status_code, 200)

    # Testing if Django is using the correct view function to render the home page
    def test_home_url_resolves_home_view(self):
        view = resolve('/')
        self.assertEquals(view.func.view_class, BoardListView)

    # Testing if home view has links to the topic pages
    def test_home_view_contains_link_to_topic_page(self):
        board_topics_url = reverse('board_topics', kwargs={'pk': self.board.pk})
        self.assertContains(self.response, 'href="{0}"'.format(board_topics_url))
