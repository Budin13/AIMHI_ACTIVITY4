from app import db


class EngineeredWoodCoverage(db.Model):
    __tablename__ = "EngineeredWoodCoverage"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    material = db.Column(db.String(200), nullable=False)
    width_ft = db.Column(db.Float, nullable=False)
    length_ft = db.Column(db.Float, nullable=False)
    thickness_mm = db.Column(db.Float, nullable=False)
    area_sqft = db.Column(db.Float, nullable=False)
    volume_cuft = db.Column(db.Float, nullable=False)
