from app import db


class Conversion(db.Model):
    __tablename__ = "Conversion"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    conversion_type = db.Column(db.String(200), nullable=False)  # str
    to_convert = db.Column(db.String(200), nullable=False)
    meter = db.Column(db.Float, nullable=True)
    centimeter = db.Column(db.Float, nullable=True)
    millimeter = db.Column(db.Float, nullable=True)
    foot = db.Column(db.Float, nullable=True)
    inch = db.Column(db.Float, nullable=True)
    kilometer = db.Column(db.Float, nullable=True)
    mile = db.Column(db.Float, nullable=True)
    hectare = db.Column(db.Float, nullable=True)
    yard = db.Column(db.Float, nullable=True)
    liter = db.Column(db.Float, nullable=True)
    milliliter = db.Column(db.Float, nullable=True)
    gallons = db.Column(db.Float, nullable=True)
    quarts = db.Column(db.Float, nullable=True)
    board_foot = db.Column(db.Float, nullable=True)
