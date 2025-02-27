import pymysql

def get_db_connection():
    return pymysql.connect(
        host="127.0.0.1",  # veya "localhost"
        user="root",  # Eğer farklı bir MySQL kullanıcısı belirlediysen değiştir.
        password="root",  # MySQL şifreni buraya yaz.
        database="maas_sayaci",
        cursorclass=pymysql.cursors.DictCursor
    )
