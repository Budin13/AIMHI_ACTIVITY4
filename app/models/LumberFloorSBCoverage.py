from app import db


class LumberFloorSBCoverage(db.Model):
    __tablename__ = "LumberFloorSBCoverage"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    board_length_in = db.Column(db.Float, nullable=False)
    board_width_in = db.Column(db.Float, nullable=False)
    effective_width_m = db.Column(db.Float, nullable=False)
    bdft_per_sqm = db.Column(db.Float, nullable=False)
