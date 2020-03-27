from flask_testing import TestCase
from src import create_app
import json 

app = create_app()


class Test(TestCase):
    # 必须指定create_app方法，并且返回flask app实例
    def create_app(self):
        app.config.from_object("src.conf.TestingConfig")
        return app

    def test_process(self):
        data = {"test": None}
        url = "/model"
        response = self.client.post(url, json=data, follow_redirects=True)
        resp_json = response.data
        resp_dict = json.loads(resp_json)
        code = resp_dict.get("code")
        self.assertEqual(code, 200)
