import json

import allure
from hamcrest import assert_that, equal_to, has_entries
from requests import codes

from framework.helper import parse_url_path


def _response_general_check(response, expected_code=codes.ok):
    assert_that(response.status_code, equal_to(expected_code),
                f'Expected status code: {expected_code}. Actual code: {response.status_code}. Url: {response.url}')


def _compare_response_and_request_body(response):
    request_body = json.loads(response.request.body)
    assert_that(response.json(), has_entries(request_body),
                f'Request body: {request_body}. Response body: {response.json()}')


def _compare_request_id_and_response_id(response, response_key: str, path_index: int):
    id = int(parse_url_path(response, path_index))
    body = response.json() if isinstance(response.json(), list) else [response.json()]
    for i in body:
        assert_that(i[response_key], equal_to(id),
                    f'Response id: {i[response_key]}. Request id: {response.json()}')


@allure.step
def check_get_all_posts_response(response):
    _response_general_check(response)
    assert_that(len(response.json()), equal_to(100))


@allure.step
def check_get_post_by_id_response(response):
    _response_general_check(response)
    _compare_request_id_and_response_id(response, response_key='id', path_index=-1)


@allure.step
def check_get_post_by_user_id_response(response):
    _response_general_check(response)
    assert_that(len(response.json()), equal_to(10))


@allure.step
def check_get_post_comments_response(response):
    _response_general_check(response)
    _compare_request_id_and_response_id(response, response_key='postId', path_index=-2)
    assert_that(len(response.json()), equal_to(5))


@allure.step
def check_write_posts_response(response):
    _response_general_check(response, expected_code=201)
    _compare_response_and_request_body(response)


@allure.step
def check_edit_posts_response(response):
    _response_general_check(response, expected_code=200)
    _compare_response_and_request_body(response)
