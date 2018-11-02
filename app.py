from flask import Flask
from service.database.database import db


# DB Models - import required to create tables
from service.models.base import Base  # noqa F401
from service.models.example import Example  # noqa F401

# API Endpoints
from service.api.hello import hello_api
from service.api.index import index_api

app = Flask(__name__)
app.config[
    "SQLALCHEMY_DATABASE_URI"
] = f"postgresql+pg8000://$USER:$PASSWORD@$URL:$PORT/$DB_NAME"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["ENV"] = "DEBUG"

app.register_blueprint(hello_api)
app.register_blueprint(index_api)

db.init_app(app)

# TODO: Uncomment when database is configured
# @app.before_first_request
# def setup_db():
#    # create tables if not exists
#    Base.metadata.create_all(bind=db.engine)
#    db.session.commit()


def run():
    app.run(host="0.0.0.0", port=5000)


if __name__ == "__main__":
    run()
