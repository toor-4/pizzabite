# Pizzabite

Pizzabite is a Django-based web application for a fictional pizza restaurant called Bella Citrus. The application allows users to view the menu, book a table, and learn more about the restaurant.

Visit site: https://alfredd.pythonanywhere.com/

## Project Structure

```
pizzabite/
├── manage.py
├── pizzabite/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── apps/
│   ├── orders/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   └── views.py
│   └── ...
├── static/
│   ├── css/
│   └── js/
├── templates/
│   ├── base.html
│   └── ...
├── requirements.txt
└── checks.yml
```

## Features

- **Home Page**: Displays the restaurant's operating hours and a list of menu items.
- **About Page**: Provides information about the restaurant and its founders.
- **Menu Page**: Lists all available pizzas with descriptions and prices.
- **Menu Item Page**: Displays detailed information about a specific menu item.
- **Booking Form**: Allows users to book a table by filling out a reservation form.

## Technologies Used

- **Django**: Backend framework for building the web application.
- **Tailwind CSS**: Utility-first CSS framework for styling the application.
- **SQLite**: Database for storing menu items and reservations.
- **AWS S3**: Used for storing static and media files.
- **Django Storages**: Integration with AWS S3 for managing static and media files.

## Setup Instructions

1. **Clone the repository**:

   ```sh
   git clone https://github.com/yourusername/pizzabite.git
   cd pizzabite
   ```

2. **Create a virtual environment and activate it**:

   ```sh
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the dependencies**:

   ```sh
   pip install -r requirements.txt
   ```

4. **Apply the migrations**:

   ```sh
   python manage.py migrate
   ```

5. **Run the development server**:

   ```sh
   python manage.py runserver
   ```

6. **Access the application**:
   Open your web browser and go to `http://127.0.0.1:8000`.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
