import logging
from flask import jsonify


logger = logging.getLogger("log.log")


class Model:

    def __init__(self, data):
        self.data = data


    def _check_data(self):

        try:
            pass
        except Exception as e:
            logger.error(e)
            return False

        return True


    def process(self):

        if not self._check_data():
            return jsonify({"code": "201", "msg": "wrong data"})

        try:
            pass
        except Exception as e:
            logger.error(e)
            return jsonify({"code": 202, "msg": "process error"})

        return jsonify({"code": 200})
