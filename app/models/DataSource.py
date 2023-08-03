from app import db


class DataSource(db.Model):
    __tablename__ = "DataSource"

    id = db.Column(db.Integer, primary_key=True, nullable=False, autoincrement=True)
    Ref = db.Column(db.String(200), nullable=False)  # str
    Status = db.Column(db.String(250), nullable=False)  # str
    Location = db.Column(db.String(250), nullable=False)  # str
    Name = db.Column(db.String(250), nullable=False)  # str
    Created = db.Column(db.String(250), nullable=False)  # datetime
    Type = db.Column(db.String(250), nullable=False)  # str
    Status_Changed = db.Column(db.String(250), nullable=False)  # datetime
    Open_Actions = db.Column(db.String(250), nullable=False)  # int
    Total_Actions = db.Column(db.String(250), nullable=False)  # int
    Association = db.Column(db.String(250), nullable=True)  # str
    OverDue = db.Column(db.String(250), default=True, nullable=False)  # bool
    Images = db.Column(db.String(250), default=True, nullable=False)  # bool
    Comments = db.Column(db.String(250), default=True, nullable=False)  # bool
    Documents = db.Column(db.String(250), default=True, nullable=False)  # bool
    Project = db.Column(db.String(250), nullable=False)  # int
    Report_Forms_Status = db.Column(db.String(250), nullable=False)  # str
    Report_Forms_Group = db.Column(db.String(250), nullable=False)  # str
