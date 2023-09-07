from app import db


class AreaConversion(db.Model):
    __tablename__ = "AreaConversion"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    area = db.Column(
        db.String(200),
        db.ForeignKey("Conversion.area", ondelete="cascade", onupdate="cascade"),
        nullable=False,
    )
    hectare = db.Column(db.Numeric, nullable=False)
    square_meter = db.Column(db.Numeric, nullable=False)
    square_kilometer = db.Column(db.Numeric, nullable=False)
    square_centimeter = db.Column(db.Numeric, nullable=False)
    square_millimeter = db.Column(db.Numeric, nullable=False)
    square_mile = db.Column(db.Numeric, nullable=False)
    square_yard = db.Column(db.Numeric, nullable=False)
    square_foot = db.Column(db.Numeric, nullable=False)
    square_inch = db.Column(db.Numeric, nullable=False)

    # centimeter = db.Column(db.Numeric, nullable=True)
    # millimeter = db.Column(db.Numeric, nullable=True)
    # foot = db.Column(db.Numeric, nullable=True)
    # inch = db.Column(db.Numeric, nullable=True)
    # kilometer = db.Column(db.Numeric, nullable=True)
    # mile = db.Column(db.Numeric, nullable=True)
    # yard = db.Column(db.Numeric, nullable=True)
    # hectare = db.Column(db.Numeric, nullable=True)
    # liter = db.Column(db.Numeric, nullable=True)
    # milliliter = db.Column(db.Numeric, nullable=True)
    # gallon = db.Column(db.Numeric, nullable=True)
    # quart = db.Column(db.Numeric, nullable=True)
    # board_foot = db.Column(db.Numeric, nullable=True)
