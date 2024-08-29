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

    if UserName=='admin' and Passwd=='admin123':
    #3 Exececute queries
        query = "Select * From accounts Where username=%s and password=%s"
        val = (UserName, Passwd) 
        mycursor.execute(query, val)

        if mycursor.rowcount > 0:
            print(f"Login administrator '{UserName}' successful...<p>")
            # path = os.path.abspath('admin/admin.html')
            # url = 'file://' + path
            # webbrowser.open(url)
            print("Choose an option:<p>")
            print("<a href='admin/update_claim.html' target='_blank' rel='noopener noreferrer'>Update a user claim</a><p>")
            print("<a href='admin/search_claim.html' target='_blank' rel='noopener noreferrer'>Search for a claim</a><p>")
            print("<a href='admin/search_prod.html' target='_blank' rel='noopener noreferrer'>Search for a product</a><p>")

            print("<h3>Database accounts:</h3>")
            query = "Select * From accounts"
            mycursor.execute(query)
            data = mycursor.fetchall()
            print("<table border='1'>")
            print("<tr align='left'>")
            print("<th>","Name","</th>")
            print("<th>","UserName","</th>")
            print("<th>","Password","</th>")
            print("<th>","Phone","</th>")
            print("<th>","Email","</th>")
            print("<th>","Address","</th>")
            print("</tr>")
            for row in data:
                print("<tr>")
                for item in row:
                    print("<td>",item,"</td>")
                print("</tr>")
            print("</table>")

            print("<h3>Registered products:</h3>")
            query = "Select * From products"
            mycursor.execute(query)
            data = mycursor.fetchall()
            print("<table border='1'>")
            print("<tr align='left'>")
            print("<th>","UserName","</th>")
            print("<th>","Product","</th>")
            print("<th>","Serial Number","</th>")
            print("<th>","Purhase Date","</th>")
            print("</tr>")
            for row in data:
                print("<tr>")
                for item in row:
                    print("<td>",item,"</td>")
                print("</tr>")
            print("</table>")

            print("<h3>Most recent claims (3):</h3>")
            query = "Select * From claims Order By date Desc Limit 3"
            mycursor.execute(query)
            data = mycursor.fetchall()
            print("<table border='1'>")
            print("<tr align='left'>")
            print("<th>","Claim ID","</th>")
            print("<th>","UserName","</th>")
            print("<th>","Serial Number","</th>")
            print("<th>","Claim Date","</th>")
            print("<th>","Description","</th>")
            print("<th>","Status","</th>")
            print("</tr>")
            for row in data:
                print("<tr>")
                for item in row:
                    print("<td>",item,"</td>")
                print("</tr>")
            print("</table>")

            print("<h3>All claims:</h3>")
            query = "Select * From claims"
            mycursor.execute(query)
            data = mycursor.fetchall()
            print("<table border='1'>")
            print("<tr align='left'>")
            print("<th>","Claim ID","</th>")
            print("<th>","UserName","</th>")
            print("<th>","Serial Number","</th>")
            print("<th>","Claim Date","</th>")
            print("<th>","Description","</th>")
            print("<th>","Status","</th>")
            print("</tr>")
            for row in data:
                print("<tr>")
                for item in row:
                    print("<td>",item,"</td>")
                print("</tr>")
            print("</table>")

        else:
            print("Account not found. Check account info in database.<p>")
    else:
        print(f"Login '{UserName}' failed. Check login info and try again.<p>")

except mysql.connector.Error as err:
    print("<p>",err)
    print("<p>Error Code:", err.errno)
    print("<p>SQLSTATE", err.sqlstate)
    print("<p>Message", err.msg)   

print('<p><a href="login.html">Back to login page...</a><p>')
mycursor.close()
mydb.close()
