from flask import render_template, url_for, redirect
from app.forms import FormLaporan
from app.docxUtils import CreadDocx, Humas
from app import app


@app.route('/')
def index():
    return render_template('base.html')


@app.route('/laporan', methods=['POST','GET'])
def laporan():
    form = FormLaporan()
    daftar_laporan = Humas.ambil_list()
    print(daftar_laporan)
    if form.validate_on_submit():
        print(f"[INPUT INFO] Date: {form.inputDate.data} type: {type(form.inputDate.data)}")
        print(f"[INPUT INFO] Judul: {form.judulLaporan.data} type: {type(form.judulLaporan.data)}")
        print(f"[INPUT INFO] Nama File: {form.namaFile.data} type: {type(form.namaFile.data)}")
        print(f"[INPUT INFO] Heading: {form.heading.data} type: {type(form.heading.data)}")
        print(f"[INPUT INFO] Isi Laporan: {form.isiLaporan.data} type: {type(form.isiLaporan.data)}")
        document = CreadDocx()
        document.tambahkan_judul(form.judulLaporan.data, form.inputDate.data)
        document.tambahkan_heading(form.heading.data, 1)
        document.tambahkan_quote(form.isiLaporan.data)
        document.buat(f"Humas/{form.namaFile.data}")
        return redirect(url_for('laporan'))
    return render_template('laporan.html', form=form, daftar_laporan=daftar_laporan)


@app.route('/pembelajaran/laporan')
def pembelajaran_laporan():
    return render_template('pembelajaran/laporan.html')


@app.route('/pembelajaran/pertemuan')
def pembelajaran_pertemuan():
    return render_template('pembelajaran/pertemuan.html')