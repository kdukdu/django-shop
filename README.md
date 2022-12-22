# Shop - online store  

## Table of Contents
- [Introduction](#introduction)
- [Technology stack](#technology-stack)
- [Installation Guide](#installation-guide)
- [Injecting your own credentials](#injecting-your-own-credentials)
  * [Get your own Stripe keys.](#get-your-own-stripe-keys)
- [Run Guide](#run-guide)
- [Simulate payments to test Stripe integration](#simulate-payments-to-test-stripe-integration)


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
- Celery  
- Redis  
- Stripe API  
- SQLite3
- Bootstrap 5


## Installation Guide  
1. Clone git repository:
```  
git clone https://github.com/KirylDumanski/Shop.git  
``` 

2. Rename `.env.dist` to `.env` and [inject your own credentials](#injecting-your-own-credentials)
 

## Injecting your own credentials
### Get your own Stripe keys.
1. Head into [Stripe dashboard](https://dashboard.stripe.com/login?redirect=%2Ftest%2Fapikeys) and grab your API keys (public key and secret key).  
  
2. Copy API keys and paste them into ```.env```:  
```  
STRIPE_PUBLIC_KEY = "<YOUR_OWN_PUBLIC_KEY>"  
STRIPE_SECRET_KEY = "<YOUR_OWN_SECRET_KEY>"  
```  
3. Execute in terminal:
```
docker-compose up stripe-cli
```
4. Look in the logs for the message from stripe-cli where will be your own webhook secret code. Take that key and paste it into ``.env``:  
```
STRIPE_WEBHOOK_SECRET = "<whsec_YOUR_OWN_WEBHOOK_SECRET_KEY>"  
```
5. `Ctrl+C` to exit

## Run guide
1. Execute in terminal:
```
docker-compose up
```
This should start up the application at port 8000. The application can be accessed at http://localhost:8080

2. To create a superuser run the following command:
```
docker exec -it <container-id> python manage.py createsuperuser
```
Where <container_id> is shop-app container id


## Simulate payments to test Stripe integration

To simulate transactions without moving any money you can use special values in test mode.

>Use the card number: 4242 4242 4242 4242
> 
>Use any valid future date
> 
>Use any three-digit CVC
>  
>Use any value you like for other form fields
