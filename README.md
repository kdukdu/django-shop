# Shop - online store
## Introduction

"Shop" is an application based on Python using the Django framework. It implements the following
functionality:

- **Django admin panel** - _where you can add, edit, remove products and categories_
- **Session based cart** -  _which keeps track of the current relationship with the client and allows you to
  add and remove items from the cart_
- **Order processing**
- **Filter products by a category**

## Technology stack
- Python 3.8
- Django 4.1
- SQLite3
- Bootstrap 5


## Installation Guide
**1. Clone git repository:**
```
git clone
```  
**2. Install a Virtual Environment**

**3. Install the dependencies**
```
pip install -r requirements.txt
```
**4. Make and apply migrations**
```
python manage.py makemigrations
python manage.py migrate
```
**5. Create superuser**
```
python manage.py createsuperuser
```
**6. Run server**
```
python manage.py runserver
```
