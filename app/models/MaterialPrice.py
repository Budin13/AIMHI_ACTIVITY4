from app import db


class MaterialPrice(db.Model):
    __tablename__ = "MaterialPrice"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    description = db.Column(db.String(200), nullable=False)
    material = db.Column(db.String(200), nullable=False)
    unit = db.Column(db.String(200), nullable=False)
    ave_price_luzon = db.Column(db.Float, nullable=False)
    ave_price_visayas = db.Column(db.Float, nullable=False)
    ave_price_mindanao = db.Column(db.Float, nullable=False)
