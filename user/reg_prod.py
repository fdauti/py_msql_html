#!C:/python/python.exe
import mysql.connector
import cgi
print("Content-Type: text/html \n\n")

#Read form data
formData = cgi.FieldStorage()
UserName = formData.getvalue("username")
ProdName = formData.getvalue("prod_name")
SerialNo = formData.getvalue("serial_no")
PurchDate = formData.getvalue("purch_date")

try: 
    #1 Connect to Sql server
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="proj_2"
    )
    #2 Create cursor object to run Sql queries
    mycursor = mydb.cursor()

    #3 Exececute queries
    query = """INSERT INTO products (username, prod_name, serial_no, purch_date) 
                VALUES (%s, %s, %s, %s)"""
    val = (UserName, ProdName, SerialNo, PurchDate) 
    mycursor.execute(query, val)
    mydb.commit()

    print("<p>Product registered successfully!")

except mysql.connector.Error as err:
    print("A database error occured. Try again or contact support!")
    # print("<p>",err)
    # print("<p>Error Code:", err.errno)
    # print("<p>SQLSTATE", err.sqlstate)
    # print("<p>Message", err.msg)

print('<p><a href="reg_prod.html">Back to product registration form...</a><p>')
mycursor.close()
mydb.close()