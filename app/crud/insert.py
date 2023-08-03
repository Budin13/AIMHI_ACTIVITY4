from flask import request, redirect, url_for, flash, session
from app.models.DataSource import DataSource
from app import db
import csv


def upload():
    try:
        csv_file = request.files["csv_file"]
        if csv_file:
            # Read the CSV file and insert data into the database
            csv_data = csv.reader(csv_file.read().decode("utf-8").splitlines())
            if db.session.query(DataSource).first() is None:
                for row in csv_data:
                    data = DataSource(
                        Ref=row[0],
                        Status=row[1],
                        Location=row[2],
                        Name=row[3],
                        Created=row[4],
                        Type=row[5],
                        Status_Changed=row[6],
                        Open_Actions=row[7],
                        Total_Actions=row[8],
                        Association=row[9],
                        OverDue=row[10],
                        Images=row[11],
                        Comments=row[12],
                        Documents=row[13],
                        Project=row[14],
                        Report_Forms_Status=row[15],
                        Report_Forms_Group=row[16],
                    )
                    db.session.add(data)
                    db.session.commit()
                session.permanent = True
                flash("File Uploaded", "info")
            else:
                session.permanent = True
                flash("File Already Uploaded", "info")
    except:
        flash("Wrong File Uploaded", "info")
