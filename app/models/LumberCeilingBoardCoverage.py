from app import db


class LumberCeilingBoardCoverage(db.Model):
    __tablename__ = "LumberCeilingBoardCoverage"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    board_size_length_cm = db.Column(db.String(200), nullable=False)
    board_size_width_cm = db.Column(db.Float, nullable=False)
    covering_per_board = db.Column(db.Float, nullable=False)
    piece_per_sqm = db.Column(db.Float, nullable=False)
