#!C:/python/python.exe
import mysql.connector
import cgi
print("Content-Type: text/html \n\n")

#Read form data
formData = cgi.FieldStorage()
Name = formData.getvalue("name")
UserName = formData.getvalue("username")
Password = formData.getvalue("passwd")
Phone = formData.getvalue("phone")
Email = formData.getvalue("email")
Address = formData.getvalue("addr")

try: 
    #1 Connect to Sql server
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="proj_2"
    )
    #print("Connected to SQL \n<p><p>")

    #2 Create cursor object to run Sql queries
    mycursor = mydb.cursor(buffered=True)

    #3 Exececute queries
    query = """INSERT INTO accounts (name, username, password, phone, email, address) 
                VALUES (%s, %s, %s, %s, %s, %s)"""
    val = (Name, UserName, Password, Phone, Email, Address) 
    mycursor.execute(query, val)
    mydb.commit()

    print("<p>Account registered succesfully!")

except mysql.connector.Error as err:
    print("Registration failed. Try using a diffrent username or contact support!")
    # print("<p>",err)   
    # print("<p>Error Code:", err.errno)
    # print("<p>SQLSTATE", err.sqlstate)
    # print("<p>Message", err.msg)

print('<p><a href="login.html">Proceed to login page...</a>')

mycursor.close()
mydb.close()