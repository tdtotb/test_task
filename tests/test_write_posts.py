import allure
import pytest

from framework.check import check_write_posts_response
from framework.jsonplaceholder_client import Client


@allure.suite('POST /posts')
class TestPostPosts:

    @allure.title('Positive. Write post')
    @pytest.mark.parametrize('name', [('Masha'), ('Ivan'), ('Sasha')])
    def test_write_post(self, get_body_from_json):
        response = Client().post_write_posts(get_body_from_json)
        check_write_posts_response(response)

    # Негативный тест на запись я не смогла придумать.
    # У сервиса нет валидации и запись можно все, что угодно
