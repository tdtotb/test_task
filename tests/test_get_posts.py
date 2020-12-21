import allure
import pytest

from framework.check import check_get_all_posts_response, check_get_post_by_id_response, \
    check_get_post_by_user_id_response
from framework.jsonplaceholder_client import Client


@allure.suite('GET /posts')
class TestGetPosts:

    @allure.title('Positive. Get all posts')
    def test_get_all_posts(self):
        response = Client().get_all_posts()
        check_get_all_posts_response(response)

    @allure.title('Positive. Get posts by id')
    def test_get_post_by_id(self):
        response = Client().get_post_by_id(1)
        check_get_post_by_id_response(response)

    @allure.title('Positive. Get posts by userId')
    def test_get_post_by_user_id(self):
        response = Client().get_post_by_user_id(3)
        check_get_post_by_user_id_response(response)

    @pytest.mark.xfail
    @allure.title('Negative. Get posts by userId')
    def test_get_post_by_user_id_failed(self):
        response = Client().get_post_by_user_id(100)
        check_get_post_by_user_id_response(response)
