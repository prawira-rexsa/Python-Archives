import mysql.connector

def connect_to_db():
    db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = "db_prawira"
        )
    return db;

def insertData(db):
    name = input("Masukan nama : ")
    address = input("Masukan alamat : ")

    values =  (name, address)
    cursor = db.cursor()
    sql = "INSERT INTO customer (name, address) VALUES (%s, %s)"
    cursor.execute(sql, values)
    db.commit()

    print("{} data berhasil disimpan".format(cursor.rowcount))

def showData(db):
    cursor = db.cursor()
    sql = "SELECT * FROM customer"
    cursor.execute(sql)
    result = cursor.fetchall()

    if cursor.rowcount < 0:
        print("Data tidak ada\n")
    else:
        print("- Data Tersimpan -")
        for data in result :
            print(data)

def updateData(db):
    cursor = db.cursor()
    showData(db)

    customer_id = input("Pilih ID Customer : ")
    name = input("Masukan Nama Baru : ")
    address = input("Masukan Alamat Baru : ")

    sql = "UPDATE customer SET name=%s, address=%s WHERE customer_id=%s"
    val = (name, address, customer_id)
    cursor.execute(sql, val)
    db.commit()

    print("{} Data Berhasil Diperbarui".format(cursor.rowcount))


def deleteData(db):
    cursor = db.cursor()
    showData(db)
  
    #val = (1, ) //tanpa inputan
    val = input("Pilih ID Customer : ")
    val = (val, )
    sql = "DELETE FROM customer WHERE customer_id=%s"
    cursor.execute(sql, val)
    #cursor.execute(sql, val) //lebih simpel tanpa inputan but cool

    db.commit()

    print(f"data dengan ID {val} berhasil dihapus.")

def searchData(db):
    cursor = db.cursor()
    keyword = input("Masukan Kata Kunci : ")
    sql = "SELECT * FROM customer WHERE name LIKE %s OR address LIKE %s"
    val = ("%{}%".format(keyword), "%{}%".format(keyword))
    cursor.execute(sql, val)
    result = cursor.fetchall()

    if not result:
        print("Tidak Ada Data yang Anda Maksut!")
    else:
        for data in result:
            print(data)
