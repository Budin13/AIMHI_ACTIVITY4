from app import db


class MassWeightConversion(db.Model):
    __tablename__ = "MassWeightConversion"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    mass_weight = db.Column(db.String(200), nullable=False)
    kilogram = db.Column(db.Float, nullable=True)
    gram = db.Column(db.Float, nullable=True)
    milligram = db.Column(db.Float, nullable=True)
    metric_ton = db.Column(db.Float, nullable=True)
    long_ton = db.Column(db.Float, nullable=True)
    short_ton = db.Column(db.Float, nullable=True)
    pound = db.Column(db.Float, nullable=True)
    ounce = db.Column(db.Float, nullable=True)
