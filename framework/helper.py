import json


def load_params_from_json(json_path):
    with open(json_path) as f:
        return json.load(f)


def parse_url_path(response, path_index):
    return response.url.split('/')[path_index]