from app import db


class VolumeConversion(db.Model):
    __tablename__ = "VolumeConversion"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    volume = db.Column(
        db.String(200),
        db.ForeignKey("Conversion.volume", ondelete="cascade", onupdate="cascade"),
        nullable=False,
    )
    liter = db.Column(db.Numeric, nullable=False)
    milliliter = db.Column(db.Numeric, nullable=False)
    cubic_meter = db.Column(db.Numeric, nullable=False)
    cubic_kilometer = db.Column(db.Numeric, nullable=False)
    cubic_centimeter = db.Column(db.Numeric, nullable=False)
    cubic_millimeter = db.Column(db.Numeric, nullable=False)
    cubic_mile = db.Column(db.Numeric, nullable=False)
    cubic_yard = db.Column(db.Numeric, nullable=False)
    cubic_foot = db.Column(db.Numeric, nullable=False)
    cubic_inch = db.Column(db.Numeric, nullable=False)
