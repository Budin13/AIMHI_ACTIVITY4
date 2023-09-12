from flask import request, redirect, url_for, flash, session
from app.models.AreaConversion import AreaConversion
from app.models.FuelConversion import FuelConversion
from app.models.LengthConversion import LengthConversion
from app.models.LumberConversion import LumberConversion
from app.models.MassWeightConversion import MassWeightConversion
from app.models.VolumeConversion import VolumeConversion
from app.models.MaterialPrice import MaterialPrice
from app import db
import csv


def upload(type):
    # if type == "Conversion":
    #     csv_file = request.files["csv_file"]
    #     if csv_file:
    #         # Read the CSV file and insert data into the database
    #         csv_data = csv.reader(csv_file.read().decode("utf-8").splitlines())
    #         for row in csv_data:
    #             # Check each cell for empty or NULL values
    #             cleaned_row = []
    #             for cell in row:
    #                 if cell.strip() == "":
    #                     cleaned_row.append(None)  # Insert None for empty cells
    #                 else:
    #                     cleaned_row.append(cell)

    #             # Create a Conversion object with cleaned data
    #             data = Conversion(
    #                 type=cleaned_row[0],
    #                 unit=cleaned_row[1],
    #                 # fuel=cleaned_row[2],
    #                 # length=cleaned_row[3],
    #                 # mass_weight=cleaned_row[4],
    #                 # lumber=cleaned_row[5],
    #                 # inch=cleaned_row[6],
    #                 # kilometer=cleaned_row[7],
    #                 # mile=cleaned_row[8],
    #                 # yard=cleaned_row[9],
    #                 # hectare=cleaned_row[10],
    #                 # liter=cleaned_row[11],
    #                 # milliliter=cleaned_row[12],
    #                 # gallon=cleaned_row[13],
    #                 # quart=cleaned_row[14],
    #                 # board_foot=cleaned_row[15],
    #             )
    #             db.session.add(data)
    #             db.session.commit()
    #             flash("File Uploaded", "info")
    #     else:
    #         flash("File Already Uploaded", "info")

    if type == "Area":
        csv_file = request.files["csv_file"]
        if csv_file:
            # Read the CSV file and insert data into the database
            csv_data = csv.reader(csv_file.read().decode("utf-8").splitlines())
            if db.session.query(AreaConversion).first() is None:
                for row in csv_data:
                    data = AreaConversion(
                        area=row[0],
                        hectare=row[1],
                        square_meter=row[2],
                        square_kilometer=row[3],
                        square_centimeter=row[4],
                        square_millimeter=row[5],
                        square_mile=row[6],
                        square_yard=row[7],
                        square_foot=row[8],
                        square_inch=row[9],
                    )
                    db.session.add(data)
                    db.session.commit()
                flash("File Uploaded", "info")
            else:
                flash("File Already Uploaded", "info")

    elif type == "Fuel":
        csv_file = request.files["csv_file"]
        if csv_file:
            # Read the CSV file and insert data into the database
            csv_data = csv.reader(csv_file.read().decode("utf-8").splitlines())
            if db.session.query(FuelConversion).first() is None:
                for row in csv_data:
                    data = FuelConversion(
                        fuel=row[0],
                        gallon=row[1],
                        liter=row[2],
                        milliliter=row[3],
                        quart=row[4],
                        # square_millimeter=row[4],
                        # square_mile=row[5],
                        # square_yard=row[6],
                        # square_foot=row[7],
                        # square_inch=row[8],
                    )
                    db.session.add(data)
                    db.session.commit()
                flash("File Uploaded", "info")
            else:
                flash("File Already Uploaded", "info")

    elif type == "Length":
        csv_file = request.files["csv_file"]
        if csv_file:
            # Read the CSV file and insert data into the database
            csv_data = csv.reader(csv_file.read().decode("utf-8").splitlines())
            if db.session.query(LengthConversion).first() is None:
                for row in csv_data:
                    data = LengthConversion(
                        length=row[0],
                        meter=row[1],
                        centimeter=row[2],
                        millimeter=row[3],
                        foot=row[4],
                        inch=row[5],
                        yard=row[6],
                    )
                    db.session.add(data)
                    db.session.commit()
                flash("File Uploaded", "info")
            else:
                flash("File Already Uploaded", "info")

    elif type == "Lumber":
        csv_file = request.files["csv_file"]
        if csv_file:
            # Read the CSV file and insert data into the database
            csv_data = csv.reader(csv_file.read().decode("utf-8").splitlines())
            if db.session.query(LumberConversion).first() is None:
                for row in csv_data:
                    data = LumberConversion(
                        lumber=row[0],
                        board_foot=row[1],
                        cubic_foot=row[2],
                        cubic_inch=row[3],
                    )
                    db.session.add(data)
                    db.session.commit()

                flash("File Uploaded", "info")
            else:
                flash("File Already Uploaded", "info")

    elif type == "MassWeight":
        csv_file = request.files["csv_file"]
        if csv_file:
            # Read the CSV file and insert data into the database
            csv_data = csv.reader(csv_file.read().decode("utf-8").splitlines())
            if db.session.query(MassWeightConversion).first() is None:
                for row in csv_data:
                    data = MassWeightConversion(
                        mass_weight=row[0],
                        kilogram=row[1],
                        gram=row[2],
                        milligram=row[3],
                        metric_ton=row[4],
                        long_ton=row[5],
                        short_ton=row[6],
                        pound=row[7],
                        ounce=row[8],
                    )
                    db.session.add(data)
                    db.session.commit()
                flash("File Uploaded", "info")
            else:
                flash("File Already Uploaded", "info")

    elif type == "Volume":
        csv_file = request.files["csv_file"]
        if csv_file:
            # Read the CSV file and insert data into the database
            csv_data = csv.reader(csv_file.read().decode("utf-8").splitlines())
            if db.session.query(VolumeConversion).first() is None:
                for row in csv_data:
                    data = VolumeConversion(
                        volume=row[0],
                        liter=row[1],
                        milliliter=row[2],
                        cubic_meter=row[3],
                        cubic_kilometer=row[4],
                        cubic_centimeter=row[5],
                        cubic_millimeter=row[6],
                        cubic_mile=row[7],
                        cubic_yard=row[8],
                        cubic_foot=row[9],
                        cubic_inch=row[10],
                    )
                    db.session.add(data)
                    db.session.commit()
                flash("File Uploaded", "info")
            else:
                flash("File Already Uploaded", "info")

    if type == "MaterialPrice":
        csv_file = request.files["csv_file"]
        if csv_file:
            # Read the CSV file and insert data into the database
            csv_data = csv.reader(csv_file.read().decode("utf-8").splitlines())
            if db.session.query(MaterialPrice).first() is None:
                for row in csv_data:
                    data = MaterialPrice(
                        description=row[0],
                        material=row[1],
                        unit=row[2],
                        ave_price_luzon=row[3],
                        ave_price_visayas=row[4],
                        ave_price_mindanao=row[5],
                    )
                    db.session.add(data)
                    db.session.commit()
                flash("File Uploaded", "info")
            else:
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
