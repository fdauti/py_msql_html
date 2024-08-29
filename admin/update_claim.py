#!C:/python/python.exe
import mysql.connector
import cgi
print("Content-Type: text/html \n\n")

#Read form data
formData = cgi.FieldStorage()
ClaimId = formData.getvalue("claim_id")
Approval = formData.getvalue("approval")

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
    query = "Update claims SET approval=%s Where claim_id=%s"
    val = (Approval, ClaimId) 
    mycursor.execute(query, val)
    mydb.commit()

    if mycursor.rowcount > 0:
        print("<p>Claim updated successfully!")
    else:
        print("<p>No claim found. Check claim ID an try again")
    
except mysql.connector.Error as err:
    print("<p>",err)
    print("<p>Error Code:", err.errno)
    print("<p>SQLSTATE", err.sqlstate)
    print("<p>Message", err.msg)

print('<p><a href="update_claim.html">Back to claim update form...</a><p>')
mycursor.close()
mydb.close()