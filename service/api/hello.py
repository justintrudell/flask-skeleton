from flask import Blueprint


hello_api = Blueprint("hello_api", __name__)


@hello_api.route("/hello/<string:param>", methods=["GET"])
def say_hello(param: str) -> str:
    return f"Hello {param}!"
