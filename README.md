# Puddle
Puddle is a Full-Stack e-commerce application built with Django. It includes user authentication, product listings functionality, item uploads, personal dashboard and communication.

## Features
* User registration and authentication
* Product listing and detail pages
* Admin panel for managing products, orders, and users

## Tech Stack
* Backend: Django, Django REST framework
* Frontend: HTML, CSS
* Database: SQLite (Development), PostgreSQL/MySQL (Production)

## Todo
* Shopping cart management
* Checkout functionality
* Payment gateway integration (e.g., Stripe, PayPal)
* Order processing and history
* Dark Mode
* Visual Overhaul

## Installation
1. Clone the repository
```bash
git clone https://github.com/gagoalaverdyan/Puddle.git
cd Puddle
```
2. Set up a virtual environment
```bash
python3 -m venv .venv
source .venv/bin/activate
```
3. Install the dependencies
```bash
pip install -r requirements.txt
```
4. Create a `.env` file and add the necessary environment variables
```plaintext
SECRET_KEY=your_secret_key
DEBUG=True
```
5. Create a superuser for the admin panel and apply the DB migrations
```bash
python manage.py createsuperuser
python manage.py migrate
```
6. Run the development server
```bash
python manage.py runserver
```

## Contributing
Pull requests are very welcome. For major changes, please open an issue first
to discuss what you would like to change.

## License
The program is licensed under [GPLv3](https://www.gnu.org/licenses/gpl-3.0.en.html) and is free to download, use or distribute.