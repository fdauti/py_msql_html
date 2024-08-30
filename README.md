#### Project Requirements:

You are asked to design a web application using HTML/Python/MySQL for the Customer Service department which fulfills the following functionalities:
1) When customers buy any product from the partner companies, they should register the product in the ABC company website in order to join to the “protection plan”. For doing this, each customer should  
   a. Login to the site. If customer doesn’t have account, then customer should create an account in the site.
   -  To create an account, customer should enter username, password, the Cellphone no and email along with the name/address. The login information should be stored in the database-table.   
   b. To register a device/product, after customer logged in, Customer should provide “product name” and “serial no” and “purchase date” of the product. This data will be stored in the related database-table
   -  Remember that each user may register multiple products
3) The customer can submit a claim for any registered digital device, when the device needs a repair or replacement under the protection plan.  
a. According to ABC protection plan policy, for any registered digital device, the customer can claim for repair/replacement only one time times within the two years of protection plan.  
b. To submit a claim, customer should login, select/find the registered device, and click on “Add a claim” button, then enter the date_of_claim, detailed description of incident/issue, and wait for approval. The claim data should be stored into a database-table.  
c. Customer can check the status of his/her claim and check whether it is approved or rejected.  
   -  When customer login, he/she can see the registered devices, and under each devices, the status of each claim.
   -  The customer can add a new registered device, or add a new claim. Use your creativity to design the UI appropriately.
4) The company asks you to add the following security feature to the program:  
a. If the user doesn’t have a valid user account, the user can’t register the product  
b. Add proper form sanitization/validation and prevent SQL injection and password protection.  
5) The company asks you to provide the following functionalities for the Web site Administrator user. There is one Admin user which can log in into the web application and perform the followings tasks:  
a. Can see all user accounts (or do SEARCH to find a specific user account)  
b. Can see all registered products by user (or do SEARCH to find a specific product)  
c. The Admin user can see the list of recent claims and update their status (approved/rejected).  
