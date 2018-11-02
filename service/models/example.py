from service.database.database import db
from service.models.base import Base


class Example(Base):
    __tablename__ = "example"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
