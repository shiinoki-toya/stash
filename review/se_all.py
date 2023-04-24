from platform import python_branch
import mysql.connector

cnx = None

try:
    cnx = mysql.connector.connect(
        user='root',  # ユーザー名
        password='eV9RW!_C',  # パスワード
        host='127.0.0.1',  # ホスト名(IPアドレス）
        database ='WEBSCRAPING'
    )

    if cnx.is_connected:
        print("Connected!")
        
    cursor = cnx.cursor()
    
    cursor.execute("SELECT * FROM mst_business")
    rows = cursor.fetchall()
    print(rows)
    cnx.commit()
    cursor.close()


except Exception as e:
    print(f"Error Occurred: {e}")

finally:
    if cnx is not None and cnx.is_connected():
        cnx.close()