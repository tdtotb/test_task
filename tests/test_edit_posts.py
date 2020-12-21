import allure
import pytest

from framework.check import check_edit_posts_response
from framework.jsonplaceholder_client import Client


@allure.suite('PATCH /posts')
class TestPostPosts:

    @allure.title('Positive. Edit post title and body')
    @pytest.mark.parametrize("attributes", [({'title': 'New title'}), ({'body': 'New Body'})])
    def test_edit_post(self, attributes):
        response = Client().patch_edit_posts(post_id=1, body=attributes)
        check_edit_posts_response(response)

    # Негативный тест на изменнеие я не смогла придумать.
    # У сервиса нет валидации и запись можно все, что угодно
