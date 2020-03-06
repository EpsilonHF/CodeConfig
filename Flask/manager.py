import unittest
from flask_script import Manager
from src import create_app


app = create_app()
manager = Manager(app)

@manager.command
def test():
    """
    运行测试脚本
    """
    tests = unittest.TestLoader().discover("test", pattern="test*.py")
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


if __name__ == "__main__":
    manager.run()


