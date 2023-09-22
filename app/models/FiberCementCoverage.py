from app import db


class FiberCementCoverage(db.Model):
    __tablename__ = "FiberCementCoverage"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    item = db.Column(db.String(200), nullable=False)
    width = db.Column(db.Float, nullable=False)
    length = db.Column(db.Float, nullable=False)
    area_sq = db.Column(db.Float, nullable=False)
    volume_cu = db.Column(db.Float, nullable=False)
    unit = db.Column(db.String(200), nullable=False)
