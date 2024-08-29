#!C:/python/python.exe
import mysql.connector
import cgi
from datetime import datetime

def days_between(d1, d2):
    d1 = datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)

print("Content-Type: text/html \n\n")
#Read form data
formData = cgi.FieldStorage()
UserName = formData.getvalue("username")
SerialNo = formData.getvalue("serial_no")
ClaimDate = formData.getvalue("claim_date")
ClaimIssue = formData.getvalue("description")
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
    if days_between(PurchDate, ClaimDate) <= 700:
        query = """INSERT INTO claims (username, serial_no, date, issue) 
                    VALUES (%s, %s, %s, %s)"""
        val = (UserName, SerialNo, ClaimDate, ClaimIssue) 
        mycursor.execute(query, val)
        mydb.commit()

        if mycursor.rowcount > 0:
            print("<p>Claim submitted successfully!")
        else:
            print("<p>Submission failed. Check your data and try again.")
    else:
        print("Protection plan expired. Please contact our support for instructions.")

except mysql.connector.Error as err:
    print("A database error occured. Try again or contact support!")
    # print("<p>",err)
    # print("<p>Error Code:", err.errno)
    # print("<p>SQLSTATE", err.sqlstate)
    # print("<p>Message", err.msg)

print('<p><a href="add_claim.html">Back to claim form...</a><p>')
mycursor.close()
mydb.close()