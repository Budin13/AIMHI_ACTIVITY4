from app import db


class EquipmentProductivity(db.Model):
    __tablename__ = "EquipmentProductivity"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    equipment_id = db.Column(db.String(200), nullable=True)
    sow_id = db.Column(db.String(200), nullable=True)
    prod_rate_desc = db.Column(db.String(200), nullable=True)
    output_per_day = db.Column(db.String(200), nullable=False)
    unit = db.Column(db.String(200), nullable=False)
    status = db.Column(db.String(200), nullable=True)
