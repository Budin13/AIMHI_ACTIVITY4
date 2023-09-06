from app import db


class Conversion(db.Model):
    __tablename__ = "Conversion"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    conversion_type = db.Column(db.String(200), nullable=False)  # str
    to_convert = db.Column(db.String(200), nullable=False)
    meter = db.Column(db.Numeric, nullable=True)
    centimeter = db.Column(db.Numeric, nullable=True)
    millimeter = db.Column(db.Numeric, nullable=True)
    foot = db.Column(db.Numeric, nullable=True)
    inch = db.Column(db.Numeric, nullable=True)
    kilometer = db.Column(db.Numeric, nullable=True)
    mile = db.Column(db.Numeric, nullable=True)
    yard = db.Column(db.Numeric, nullable=True)
    hectare = db.Column(db.Numeric, nullable=True)
    liter = db.Column(db.Numeric, nullable=True)
    milliliter = db.Column(db.Numeric, nullable=True)
    gallon = db.Column(db.Numeric, nullable=True)
    quart = db.Column(db.Numeric, nullable=True)
    board_foot = db.Column(db.Numeric, nullable=True)
