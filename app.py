# created by ekin varli
#!/usr/bin/python3
# coding: utf-8


# flask core
from flask import Flask
from flask import render_template
from flask import request
from flask import url_for
from flask import redirect

# additional modules
import sqlite3
import string
import random
import time
import os


server = Flask(__name__, template_folder='public')
server.static_folder = 'static'


# routes
@server.route('/')
def index():
    connection = sqlite3.connect('./databases/ilanlar.db')
    cursor = connection.cursor()

    cursor.execute('SELECT * FROM ilanlar')
    datas = cursor.fetchall()

    return render_template('home.html', datas=datas)


@server.route('/p/<posting>')
def page(posting):
    connection = sqlite3.connect('./databases/ilanlar.db')
    cursor = connection.cursor()

    cursor.execute(f'SELECT * FROM ilanlar WHERE aciklama="{posting}"')
    datas = cursor.fetchall()

    return render_template('details.html', posting=posting, datas=datas)


@server.route('/about')
def view_about():
    return render_template('about.html')


@server.route('/new')
def new_posting():
    return render_template('new.html')


@server.route('/search', methods=['POST'])
def view_results():
    city = request.form.get('city')
    lang = request.form.get('lang')

    connection = sqlite3.connect('./databases/ilanlar.db')
    cursor = connection.cursor()

    cursor.execute(
        f'SELECT * FROM ilanlar WHERE sehir="{city}" AND yetenek="{lang}"')
    datas = cursor.fetchall()

    return render_template('result.html', datas=datas)


@server.route('/add', methods=['POST'])
def add():
    connection = sqlite3.connect('./databases/basvuru.db')
    cursor = connection.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS basvuru(ad TEXT, soyad TEXT, yetenek TEXT, aciklama TEXT, sehir TEXT, iletisim TEXT, ucret TEXT)')
    if request.method == 'POST':
        ad = request.form.get('ad')
        soyad = request.form.get('soyad')
        yetenek = request.form.get('yetenek')
        aciklama = request.form.get('aciklama')
        sehir = request.form.get('sehir')
        iletisim = request.form.get('iletisim')
        ucret = request.form.get('ucret')

        cursor.execute(
            f'INSERT INTO basvuru VALUES("{ad}","{soyad}","{yetenek}","{aciklama}","{sehir}","{iletisim}","{ucret}")')
        connection.commit()
        connection.close()

        return 'Your application has been forwarded to the management team.'
    else:
        return 'Post Error!'


@server.route('/remove', methods=['POST'])
def remove():
    connection = sqlite3.connect('./databases/basvuru.db')
    cursor = connection.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS basvuru(ad TEXT, soyad TEXT, yetenek TEXT, aciklama TEXT, sehir TEXT, iletisim TEXT, ucret TEXT)')
    if request.method == 'POST':
        ad = request.form.get('dataad')
        soyad = request.form.get('datasoyad')
        yetenek = request.form.get('dataskill')
        aciklama = request.form.get('datadesc')
        sehir = request.form.get('datasehir')
        iletisim = request.form.get('datailetisim')
        ucret = request.form.get('dataucret')

        cursor.execute(
            f'DELETE FROM basvuru WHERE ad="{ad}" AND soyad="{soyad}" AND aciklama="{aciklama}" AND sehir="{sehir}" AND iletisim="{iletisim}" AND ucret="{ucret}"')
        connection.commit()
        connection.close()

        return 'Application has been removed.'
    else:
        return 'Post Error!'


@server.route('/panel')
def panel_login():
    return render_template('panel-login.html')


@server.route('/view-panel', methods=['POST'])
def view_panel():
    if request.method == 'POST':
        admin_id = request.form.get('adminid')
        connection = sqlite3.connect('./databases/basvuru.db')
        cursor = connection.cursor()

        # admin-login
        if admin_id == 'ENTER_YOUR_ADMINISTRATOR_PASSWORD':
            cursor.execute('SELECT * FROM basvuru')
            datas = cursor.fetchall()

            return render_template('view-panel.html', datas=datas)
        else:
            return 'Wrong Password!'
    else:
        return 'Post Error!'


@server.route('/approve', methods=['POST'])
def access():
    connection = sqlite3.connect('./databases/ilanlar.db')
    cursor = connection.cursor()
    cursor.execute(
        'CREATE TABLE IF NOT EXISTS ilanlar(ad TEXT, soyad TEXT, yetenek TEXT, aciklama TEXT, sehir TEXT, iletisim TEXT, ucret TEXT)')
    if request.method == 'POST':
        ad = request.form.get('dataad')
        soyad = request.form.get('datasoyad')
        yetenek = request.form.get('dataskill')
        aciklama = request.form.get('datadesc')
        sehir = request.form.get('datasehir')
        iletisim = request.form.get('datailetisim')
        ucret = request.form.get('dataucret')

        cursor.execute(
            f'INSERT INTO ilanlar VALUES("{ad}","{soyad}","{yetenek}","{aciklama}","{sehir}","{iletisim}","{ucret}")')
        connection.commit()
        connection.close()

        return 'Application Approved!'
    else:
        return 'Post Error!'


@server.route('/rss')
def rss():
    rss_feed = open('rss.xml', 'r')
    return f'{rss_feed}'


# run app
if __name__ == '__main__':
    server.run(debug=True)
