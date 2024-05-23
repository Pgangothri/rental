# Rental Blog using Django
This project is a Django-based web application that allows Users can register, log in,profile creation,edit profile,logout,passwordreset.
## Getting Started
To run this project locally using Docker, follow these steps:
1. Clone the repository:
   ```bash
   git clone https://github.com/Pgangothri/rental.git
   create virtual environment virtualenv venv
   cd your-project
   
2. Now we have to create superuser:
   ```bash
   python manage.py createsuperuser
3. Now it will ask for the username, name and password:
   ```bash
   PS E:\health-blog\health-blog>  python manage.py createsuperuser
   Email: admin@gmail.com
   Name: admin
   Password: ******
   Password (again):*****
4. now we can log in to the admin panel by using the end point  [http://localhost:8000/admin/](url):
5. The application should now be accessible at http://localhost:8000/.
6. SignUp,Login,logout etc all functionalities are there in the url  http://localhost:8000/
