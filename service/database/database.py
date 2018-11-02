
"""
This class exists to solve circular dependencies with the 'db' variable in views.
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
