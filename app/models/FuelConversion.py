from app import db


class FuelConversion(db.Model):
    __tablename__ = "FuelConversion"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    fuel = db.Column(db.String(200), nullable=False)
    gallon = db.Column(db.Numeric, nullable=False)
    liter = db.Column(db.Numeric, nullable=False)
    milliliter = db.Column(db.Numeric, nullable=False)
    quart = db.Column(db.Numeric, nullable=False)
