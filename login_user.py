#!C:/python/python.exe
import mysql.connector
import cgi
# import webbrowser
# import os
print("Content-Type: text/html \n\n")

#Read form data
formData = cgi.FieldStorage()
UserName = formData.getvalue("username")
Passwd = formData.getvalue("passwd")

try: 
    #1 Connect to Sql server
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="",
    database="proj_2"
    )
    #2 Create cursor object to run Sql queries
    mycursor = mydb.cursor(buffered=True)

    #3 Exececute queries
    query = "Select * From accounts Where username=%s and password=%s"
    val = (UserName, Passwd) 
    mycursor.execute(query, val)
    
    if mycursor.rowcount > 0:
        print(f"Login user '{UserName}' successful...<p>")
        # path = os.path.abspath('user/user.html')
        # url = 'file://' + path
        # webbrowser.open(url)
        print("Choose an option:<p>")
        print("<a href='user/reg_prod.html' target='_blank' rel='noopener noreferrer'>Register a new product</a><p>")
        print("<a href='user/add_claim.html' target='_blank' rel='noopener noreferrer'>Add a new claim</a><p>")

        print("<h3>Your registered products:</h3>")
        query = "Select prod_name,serial_no,purch_date From products Where username=%s"
        val = (UserName,)
        mycursor.execute(query, val)
        data = mycursor.fetchall()
        print("<table border='1'>")
        print("<tr align='left'>")
        print("<th>","Product Name","</th>")
        print("<th>","Serial Number","</th>")
        print("<th>","Puchase Date","</th>")
        print("</tr>")
        for row in data:
            print("<tr>")
            for item in row:
                print("<td>",item,"</td>")
            print("</tr>")
        print("</table>")

        print("<h3>Your submitted claims:</h3>")
        query = "Select claim_id,serial_no,date,issue,approval From claims Where username=%s"
        val = (UserName,)
        mycursor.execute(query, val)
        data = mycursor.fetchall()
        print("<table border='1'>")
        print("<tr align='left'>")
        print("<th>","Claim ID","</th>")
        print("<th>","Serial Number","</th>")
        print("<th>","Claim Date","</th>")
        print("<th>","Claim Description","</th>")
        print("<th>","Claim Status","</th>")
        print("</tr>")
        for row in data:
            print("<tr>")
            for item in row:
                print("<td>",item,"</td>")
            print("</tr>")
        print("</table>")

    else:
        print(f"Login '{UserName}' failed. User not found of incorret password.<p>")

except mysql.connector.Error as err:
    print("<p>A database error occured. Try again or contact support!")
    # print("<p>",err)
    # print("<p>Error Code:", err.errno)
    # print("<p>SQLSTATE", err.sqlstate)
    # print("<p>Message", err.msg)

print('<p><a href="login.html">Back to login page...</a><p>')
mycursor.close()
mydb.close()
