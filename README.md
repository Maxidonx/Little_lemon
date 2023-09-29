# This is my first Django project.
*as a pertial fulfillment to my study in **coursera** taught by **Meta** staff*

# About This Project.

This project is about a resturant app, desinged to create serve customers around USA.

## Functionalities.
this project is designed to handle the following task:
- show menu items of the resturent for the day.
- make reservations.
- make an order for food displayed on the menu item.
- Allwos for customers reviews
- Show prices for menu items
- Provides discounts  for regular customers.

# Getting Started
- **Clone the repository**
```bash
https://github.com/Maxidonx/Little_lemon.git
```

- **Install necessary packages**
    - pipenv | `python -m install pipenv`
    - Django | `pip install django`
    - requirements.txt | `pip install -r requirements.txt` or `pip freeze > requirements.txt`

- **Run the following commands**
```bash
python manage.py makemigrations
            or
python3 manage.py makemigrations
```
```bash
python manage.py migrate
            or
python3 manage.py migrate
```
- **Create a superuser**
```bash
python manage.py createsuperuser
```
*fill in the details available on the terminal, e.g email, username, password*
- **Run the server at port 8000**
```bash
python manage.py runserver
```
Now you can view the project on ur browser on `localhost:127.0.0.1:8000`

# Endpoints for the Project

## Home Page

**URL: /**

**Description:** *The home page of the restaurant website. Provides general information about the restaurant.*

**Methods:** GET

**Usage:** *Visit the root URL of the website to access the home page.*

## About Page

**URL:** /about/

**Description:** *The about page of the restaurant website. Contains information about the history and mission of the restaurant.*

**Methods:** GET

**Usage:** *Access this page by visiting /about/ in the URL.*

## Book a Table Page

**URL:** /book/

**Description:** *This page allows customers to book a table at the restaurant. It may include a form to fill out for reservation details.*
**Methods:** GET, POST
**Usage:**
GET: Visit /book/ to access the table booking page.
POST: Submit a reservation form to book a table.

## Menu Page

**URL:** /menu/
**Description:** *The menu page displays the restaurant's menu, including various food items and their descriptions.*

**Methods:** GET

**Usage:** *Access this page by visiting /menu/ in your browser.*

## Display Menu Item

**URL:** /menu_item/int:pk/

**Description:** *This endpoint displays detailed information about a specific menu item. The <int:pk> in the URL represents the unique identifier of the menu item.*

**Methods:** GET

**Usage:**
*Replace <int:pk> with the ID of the menu item you want to view. For example, /menu_item/1/ would show details for the menu item with ID 1.*

*Use the GET method to retrieve menu item details.*

### Usage

*To access the different pages and endpoints of this restaurant website, follow the provided URLs and descriptions above. You can use a web browser to navigate to these pages and explore the restaurant's information, menu, and booking options.*

**For the "Book a Table" page, you can use both the GET and POST methods. GET to access the page and POST to submit a reservation form for booking a table.**
