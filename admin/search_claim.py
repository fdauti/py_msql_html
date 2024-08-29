#!C:/python/python.exe
import mysql.connector
import cgi
print("Content-Type: text/html \n\n")

#Read form data
formData = cgi.FieldStorage()
ClaimId = formData.getvalue("claim_id")

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
    query = "Select * From claims Where claim_id=%s"
    val = (ClaimId,) 
    mycursor.execute(query, val)

    if mycursor.rowcount > 0:
        print("<h3>Claim found:</h3>")
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
        print("Claim ID not found.<p>")

except mysql.connector.Error as err:
    print("<p>",err)
    print("<p>Error Code:", err.errno)
    print("<p>SQLSTATE", err.sqlstate)
    print("<p>Message", err.msg)   

print('<p><a href="search_claim.html">Back to claim search form...</a><p>')
mycursor.close()
mydb.close()
