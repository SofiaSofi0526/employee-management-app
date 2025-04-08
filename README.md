# Employee Management Web App

A simple web application to manage employee records using **Flask**, **MySQL**, **SQLAlchemy**, and **WTForms**.

## 🚀 Features
- Add new employees
- Edit existing employee details
- Delete employees
- View all employee records

## 🧰 Tech Stack
- Flask (Backend)
- SQLAlchemy (ORM)
- MySQL (Database)
- HTML, CSS (Frontend)
- Bootstrap (Optional for better UI)

## 📸 Screenshots
> Add screenshots of:
- Home page
- Add Employee form
- Employee table

## 📦 Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/SofiaSofi0526/employee-management-app.git
cd employee-management-app


2. Set Up a Virtual Environment
Create a virtual environment to manage your Python dependencies.

python -m venv venv
# On Windows
.\venv\Scripts\activate
# On MacOS/Linux
source venv/bin/activate

3. Install Dependencies
Once the virtual environment is activated, install the required Python packages.

pip install -r requirements.txt

4. Set Up the Database
Ensure your MySQL server is running and create a database for the app.

CREATE DATABASE employee_management;
5. Configure the Application
In config.py, update your database credentials as follows:

SQLALCHEMY_DATABASE_URI = 'mysql://root:Sofia@2605@localhost/employee_management'

6. Run the Application
Now you're ready to start the Flask app:
flask run

This will start the server, and you can access the app at http://127.0.0.1:5000/ in your browser.

📜 How to Use
Add Employee: Go to the "Add Employee" page to add a new employee.

Edit Employee: Click on an employee's name to edit their details.

Delete Employee: Click on the "Delete" button next to an employee's name to remove them from the database.

View Employees: All employees are listed on the home page.

⚙️ Configuration
You can modify the application’s configuration, such as the database URI, in the config.py file.

👥 Contributing
If you want to contribute to the project, feel free to fork the repository and submit a pull request with your improvements.

📝 License
This project is licensed under the MIT License – see the LICENSE file for details.

💬 Contact
If you have any questions, feel free to reach out to me at [sofiasofi0526@gmail.com].

Made with ❤️ by Sofia

Just copy and paste this into your `README.md` file. If you need to adjust anything (like your email or other details), feel free to do so. Let me know if you need further assistance!

