from flask import Blueprint, render_template

# from service.models.example import Example
# from service.database.database import db


index_api = Blueprint("index_api", __name__, template_folder="../templates")


@index_api.route("/", methods=["GET"])
def index() -> str:
    # TODO: Uncomment when db is set up
    # models = db.session.query(Example).all()
    models = ["a", "b", "c"]
    return render_template("index.html", models=models)
