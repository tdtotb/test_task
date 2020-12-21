import allure
import requests as r
from config import JSONPLACEHOLDER_HOST


class Client:

    def _get(self, path: str):
        return r.get(url=JSONPLACEHOLDER_HOST + path)

    def _get_with_params(self, path: str, params: dict):
        return r.get(url=JSONPLACEHOLDER_HOST + path, params=params)

    def _post(self, path: str, body: object):
        return r.post(url=JSONPLACEHOLDER_HOST + path, json=body)

    def _patch(self, path: str, body: object):
        return r.patch(url=JSONPLACEHOLDER_HOST + path, json=body)

    @allure.step
    def get_all_posts(self):
        return self._get(path=f'/posts')

    @allure.step
    def get_post_by_id(self, post_id: int):
        return self._get(path=f'/posts/{post_id}')

    @allure.step
    def get_post_by_user_id(self, id: int):
        return self._get_with_params(path=f'/posts', params={"userId": id})

    @allure.step
    def get_post_comments(self, post_id: int):
        return self._get(path=f'/posts/{post_id}/comments')

    @allure.step
    def post_write_posts(self, body: dict):
        return self._post(path=f'/posts', body=body)

    @allure.step
    def patch_edit_posts(self, post_id: int, body: dict):
        return self._patch(path=f'/posts/{post_id}', body=body)
