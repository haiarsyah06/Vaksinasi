import os
from cs50 import sql
from flask import Flask, flash, jsonify, redirect, render_template, request, session

app = Flask (__name__)

db = sql("sqlite://vaksin.db")
db = sql("sqlite://riwayat.db")

@app.route("/", methods=["GET", "POST"])
def index():

    if request.method == "POST":
        id = request.form.get("id_regristasi")
        nama = request.form.get("nama")
        no_ktp = request.form.get("no_ktp")
        jk = request.form.get("jenis_kelamin")
        tempat_lahir = request.form.get("tempat_lahir")
        tgl_lahir = request.form.get("tangga_lahir")
        alamat_domisili=request.form.get("alamat_domisili")
        file_ktp = request.form.get("ktp")

        riwayat = request.form.get("riwayat")

        db.execute("INSERT INTO vaksin(id, nama, no_ktp, jk, tempat_lahir, tgl_lahir, alamat_domisili, file_ktp) VALUES (?,?,?,?,?,?,?,?)", id, nama, no_ktp, jk, tempat_lahir, tgl_lahir, alamat_domisili, file_ktp)
        
        db.execute("INSERT INTO riwayat(no_ktp, riwayat) VALUES (?,?)", no_ktp, riwayat)
        return redirect("/")
    
    else:
        vaksin = db.execute("SELECT * FROM vaksin")
        riwayat = db.execute("SELECT * FROM riwayat")

        return render_template("index.html", vaksin=vaksin, riwayat=riwayat)

