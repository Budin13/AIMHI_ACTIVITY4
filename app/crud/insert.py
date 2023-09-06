from flask import request, redirect, url_for, flash, session
from app.models.Conversion import Conversion
from app import db
import csv


def upload():
    csv_file = request.files["csv_file"]
    if csv_file:
        # Read the CSV file and insert data into the database
        csv_data = csv.reader(csv_file.read().decode("utf-8").splitlines())
        for row in csv_data:
            # Check each cell for empty or NULL values
            cleaned_row = []
            for cell in row:
                if cell.strip() == "":
                    cleaned_row.append(None)  # Insert None for empty cells
                else:
                    cleaned_row.append(cell)

            # Create a Conversion object with cleaned data
            data = Conversion(
                conversion_type=cleaned_row[0],
                to_convert=cleaned_row[1],
                meter=cleaned_row[2],
                centimeter=cleaned_row[3],
                millimeter=cleaned_row[4],
                foot=cleaned_row[5],
                inch=cleaned_row[6],
                kilometer=cleaned_row[7],
                mile=cleaned_row[8],
                yard=cleaned_row[9],
                hectare=cleaned_row[10],
                liter=cleaned_row[11],
                milliliter=cleaned_row[12],
                gallon=cleaned_row[13],
                quart=cleaned_row[14],
                board_foot=cleaned_row[15],
            )
            db.session.add(data)
            db.session.commit()
            session.permanent = True
            flash("File Uploaded", "info")
    else:
        session.permanent = True
        flash("File Already Uploaded", "info")

    # try:
    #     csv_file = request.files["csv_file"]
    #     if csv_file:
    #         # Read the CSV file and insert data into the database
    #         csv_data = csv.reader(csv_file.read().decode("utf-8").splitlines())
    #         if db.session.query(DataSource).first() is None:
    #             for row in csv_data:
    #                 data = DataSource(
    #                     Ref=row[0],
    #                     Status=row[1],
    #                     Location=row[2],
    #                     Name=row[3],
    #                     Created=row[4],
    #                     Type=row[5],
    #                     Status_Changed=row[6],
    #                     Open_Actions=row[7],
    #                     Total_Actions=row[8],
    #                     Association=row[9],
    #                     OverDue=row[10],
    #                     Images=row[11],
    #                     Comments=row[12],
    #                     Documents=row[13],
    #                     Project=row[14],
    #                     Report_Forms_Status=row[15],
    #                     Report_Forms_Group=row[16],
    #                 )
    #                 db.session.add(data)
    #                 db.session.commit()
    #             session.permanent = True
    #             flash("File Uploaded", "info")
    #         else:
    #             session.permanent = True
    #             flash("File Already Uploaded", "info")
    # except:
    #     flash("Wrong File Uploaded", "info")
