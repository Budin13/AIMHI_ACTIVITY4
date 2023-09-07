from app import db


class Conversion(db.Model):
    __tablename__ = "Conversion"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    volume = db.Column(db.String(200), nullable=True, unique=True)  # str
    area = db.Column(db.String(200), nullable=True, unique=True)
    fuel = db.Column(db.String(200), nullable=True, unique=True)
    length = db.Column(db.String(200), nullable=True, unique=True)
    mass_weight = db.Column(db.String(200), nullable=True, unique=True)
    lumber = db.Column(db.String(200), nullable=True, unique=True)

    # conversion_type = db.Column(db.String(200), nullable=False)  # str
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


# from app import db


# class DataSource(db.Model):
#     __tablename__ = "DataSource"

#     id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
#     Ref = db.Column(db.String(200), nullable=False)  # str
#     Status = db.Column(db.String(250), nullable=False)  # str
#     Location = db.Column(db.String(250), nullable=False)  # str
#     Name = db.Column(db.String(250), nullable=False)  # str
#     Created = db.Column(db.String(250), nullable=False)  # datetime
#     Type = db.Column(db.String(250), nullable=False)  # str
#     Status_Changed = db.Column(db.String(250), nullable=False)  # datetime
#     Open_Actions = db.Column(db.String(250), nullable=False)  # int
#     Total_Actions = db.Column(db.String(250), nullable=False)  # int
#     Association = db.Column(db.String(250), nullable=True)  # str
#     OverDue = db.Column(db.String(250), default=True, nullable=False)  # bool
#     Images = db.Column(db.String(250), default=True, nullable=False)  # bool
#     Comments = db.Column(db.String(250), default=True, nullable=False)  # bool
#     Documents = db.Column(db.String(250), default=True, nullable=False)  # bool
#     Project = db.Column(db.String(250), nullable=False)  # int
#     Report_Forms_Status = db.Column(db.String(250), nullable=False)  # str
#     Report_Forms_Group = db.Column(db.String(250), nullable=False)  # str
