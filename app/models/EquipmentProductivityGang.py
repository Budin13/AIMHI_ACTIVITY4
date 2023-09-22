from app import db


class EquipmentProductivityGang(db.Model):
    __tablename__ = "EquipmentProductivityGang"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    manpower_id = db.Column(db.String(200), nullable=False)
    sow_id = db.Column(db.String(200), nullable=False)
    manpower_quantity = db.Column(db.Float, nullable=False)
    equipment_id = db.Column(db.String(200), nullable=True)
