from app import db


class LumberConversion(db.Model):
    __tablename__ = "LumberConversion"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    lumber = db.Column(db.String(200), nullable=False)
    board_foot = db.Column(db.Numeric, nullable=False)
    cubic_foot = db.Column(db.Numeric, nullable=False)
    cubic_inch = db.Column(db.Numeric, nullable=False)
