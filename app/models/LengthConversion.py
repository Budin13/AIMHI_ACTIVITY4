from app import db


class LengthConversion(db.Model):
    __tablename__ = "LengthConversion"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    length = db.Column(
        db.String(200),
        db.ForeignKey("Conversion.length", ondelete="cascade", onupdate="cascade"),
        nullable=False,
    )
    meter = db.Column(db.Numeric, nullable=False)
    centimeter = db.Column(db.Numeric, nullable=False)
    millimeter = db.Column(db.Numeric, nullable=False)
    foot = db.Column(db.Numeric, nullable=False)
    inch = db.Column(db.Numeric, nullable=False)
    yard = db.Column(db.Numeric, nullable=False)
