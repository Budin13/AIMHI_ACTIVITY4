from flask import render_template, request, session, redirect, url_for, flash
from app import app, db
from app.models import Conversion, MassWeightConversion, import_models
from app.crud.insert import upload

app.secret_key = "hehe"


@app.route("/home", methods=["POST", "GET"])
@app.route("/", methods=["POST", "GET"])
def home():
    return render_template("index.html")


@app.route("/file", methods=["POST", "GET"])
def file():
    if request.method == "POST":
        upload(request.form["role"])
        return redirect(url_for("home"))
    else:
        if session.permanent:
            return render_template("upload.html")
        return render_template("upload.html")


@app.route("/data")
def data():
    if session.permanent:
        table_data = Conversion.Conversion.query.all()
        return render_template("ShowData.html", table_data=table_data)
    else:
        return redirect(url_for("file"))


@app.route("/delete")
def delete():
    if session.permanent:
        db.session.query(Conversion.Conversion).delete()
        db.session.commit()
        session.permanent = False
        flash("Data has been deleted", "info")
    else:
        flash("Upload the CSV file first", "info")
    return redirect(url_for("home"))


def Configure():
    import_models()


Configure()

if __name__ == "__main__":
    app.run(debug=True)
