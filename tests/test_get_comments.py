import allure
import pytest

from framework.check import check_get_post_comments_response
from framework.jsonplaceholder_client import Client


@allure.suite('GET /comment')
class TestGetComments:

    @allure.title('Positive. Get post comments')
    def test_get_post_comments(self):
        response = Client().get_post_comments(99)
        check_get_post_comments_response(response)

    @pytest.mark.xfail
    @allure.title('Negative. Get post comments')
    def test_get_post_comments(self):
        response = Client().get_post_comments(999)
        check_get_post_comments_response(response)