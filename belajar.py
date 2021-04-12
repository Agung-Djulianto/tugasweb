from flask import Flask, render_template, request, url_for, redirect
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'toko_barokah'
mysql = MySQL(app)

@app.route("/",)
def main():
	return render_template('index.html')

@app.route("/barangtoko", methods=['POST', 'GET'])
def barangtoko():
	if request.method == 'GET':
		cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cur.execute("SELECT * FROM barang")
		dt = cur.fetchall()
		cur.close()
		return render_template('barang.html', menu='data', submenu='barang', data=dt)
	elif request.method == 'POST':
		id_barang = request.form['id_barang']
		nama_barang = request.form['nama_barang']
		harga_barang = request.form['harga_barang']
		jumlah_barang = request.form['jumlah_barang']
		cur = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
		cur.execute("INSERT INTO barang (id_barang, nama_barang, harga_barang, jumlah_barang) VALUES (%s, %s, %s, %s)", (id_barang, nama_barang, harga_barang, jumlah_barang))
		mysql.connection.commit()
		return redirect(url_for('barangtoko'))
	else:
		return redirect(url_for('barangtoko'))

@app.route("/karyawantoko")
def karyawantoko():
	return render_template('karyawan.html', menu='data', submenu='karyawan')

@app.route("/penjualantoko")
def penjualantoko():
	return render_template('penjualan.html', menu='data', submenu='penjualan')

@app.route("/Suppliertoko")
def Suppliertoko():
	return render_template('supplier.html', menu='data', submenu='supplier')


if __name__ == "__main__":
	app.run(debug=True)  