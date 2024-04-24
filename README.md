### Stock Management System using Python and MySQL

This Python script provides a basic Stock Management System implemented using MySQL as the database backend. The system allows three types of users - Admin, Customer, and Supplier - to interact with the database to perform various tasks related to managing stock.

#### Features:

1. **Admin Interface:**
   - Admins can log in using their username and password.
   - After successful login, admins can:
     - Check existing stock.
     - Place orders for stock.
     - Exit the system.

2. **Customer Interface:**
   - Customers can log in using their username and password.
   - Upon successful login, customers can:
     - View existing stock.
     - Add items to their cart.
     - Checkout and pay for the selected items.

3. **Supplier Interface:**
   - Suppliers can log in using their username and password.
   - Once logged in, suppliers can:
     - View remaining orders.
     - Choose to supply ordered items or not.

#### Usage:

1. **Setup:**
   - Ensure that Python and MySQL are installed on your system.
   - Install the required Python packages using `pip install -r requirements.txt`.
   - Create a MySQL database named `stockmgmt`.
   - Import the provided SQL schema (`stockmgmt.sql`) to set up the database structure.

2. **Running the Script:**
   - Run the Python script (`stock_management.py`).
   - Follow the prompts to log in and perform tasks based on your user role.

#### Dependencies:
- `mysql-connector-python`: Python driver for MySQL database connectivity.
- `prettytable`: Used for displaying data in tabular format.

#### Note:
- Ensure that MySQL is running and accessible.
- Modify the database connection details (host, username, password) in the script according to your MySQL setup.
- This is a basic implementation and can be extended further as per specific requirements.
