# Shop - online store  

## Table of Contents
- [Introduction](#introduction)
- [Technology stack](#technology-stack)
- [Installation Guide](#installation-guide)
- [Injecting your own credentials](#injecting-your-own-credentials)
  * [Get your own Stripe keys.](#get-your-own-stripe-keys)
- [Run Guide](#run-guide)
- [Simulate payments to test Stripe integration](#simulate-payments-to-test-stripe-integration)
- [RESTful API](#restful-api)
  * [Structure](#structure)
  * [How to check?](#how-to-check)
  * [Create users and Tokens](#create-users-and-tokens)
  * [Testing](#testing)


## Introduction  
  
"Shop" is an application based on Python using the Django framework. It implements the following 
functionality:  

### Django admin panel
You can add, edit, remove products and categories. Also, you can get information about customer's orders.
Admin panel located at http://localhost:8000/admin

### Session based cart
Keeps track of the current relationship with the client and allows you to add and remove items from the cart.  

### Order processing and payment 
We can easily test this online-store with using Stripe API. You can use the Stripe API in test mode,
which doesn't affect your live data or interact with the banking networks.

### Running asynchronous tasks
With the help of Celery, my app can execute asynchronous tasks. Also, Celery requires a message broker
to process requests. For this purpose, I used Redis as is an in-memory data store.

### API
In a RESTful API endpoints (URLs) define the structure of the API and how end users access data from 
our application using the HTTP methods - GET, POST, PUT, PATCH, DELETE.


## Technology stack  
- Python 3.8  
- Django 4.1
- Django Rest Framework
- Djoser
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
1. Head into [Stripe dashboard](https://dashboard.stripe.com/login?redirect=%2Ftest%2Fapikeys) and 
grab your API keys (public key and secret key).  
  
2. Copy API keys and paste them into `.env`:  
```  
STRIPE_PUBLIC_KEY = "<YOUR_OWN_PUBLIC_KEY>"  
STRIPE_SECRET_KEY = "<YOUR_OWN_SECRET_KEY>"  
```  
3. Execute in terminal:
```
docker-compose up stripe-cli
```
4. Look in the logs for the message from stripe-cli where will be your own webhook secret code.
Take that key and paste it into `.env`:  
```
STRIPE_WEBHOOK_SECRET = "<whsec_YOUR_OWN_WEBHOOK_SECRET_KEY>"  
```
5. `Ctrl+C` to exit

## Run guide
1. Execute in terminal:
```
docker-compose up
```
This should start up the application at port 8000. The application can be accessed at http://localhost:8000

2. To provide initial data for Product and Category models run the following command:
```
docker exec -it <container_id> python manage.py loaddata subjects.json
```
Where `<container_id>` is shop-app container id
> In new terminal window exec `docker ps` to get the container id

3. To create a superuser run the following command:
```
docker exec -it <container_id> python manage.py createsuperuser
```
Where `<container_id>` is shop-app container id


## Simulate payments to test Stripe integration

To simulate success transactions without moving any money you can use special values in test mode.

>Use the card number: 4242 4242 4242 4242
> 
>Use any valid future date
> 
>Use any three-digit CVC
>  
>Use any value you like for other form fields


## RESTful API
### Structure
In our case, we have two resources, Product and Category. I also connected default Django Rest Framework authorization
and authorization by tokens using the Djoser library, so we will use the following URLs:

| Resources             | Endpoint             |     HTTP Method     | CRUD Method | Result                          |
|:----------------------|:---------------------|:-------------------:|:-----------:|:--------------------------------|
| **Product**           | api/v1/product/      |         GET         |    READ     | Get all products                |
|                       | api/v1/product/:id/  |         GET         |    READ     | Get one product                 |
|                       | api/v1/product/      |        POST         |   CREATE    | Create new product              |
|                       | api/v1/product/:id/  |     PUT / PATCH     |   UPDATE    | Update a product                |
|                       | api/v1/product/:id/  |       DELETE        |   DELETE    | Delete a product                |
| **Category**          | api/v1/category/     |         GET         |    READ     | Get all categories              |
|                       | api/v1/category/:id/ |         GET         |    READ     | Get one category                |
|                       | api/v1/category/     |        POST         |   CREATE    | Create new category             |
|                       | api/v1/category/:id/ |     PUT / PATCH     |   UPDATE    | Update a category               |
|                       | api/v1/category/:id/ |       DELETE        |   DELETE    | Delete a category               |
| **DRF Default Auth**  | api/v1/auth/login/   |         GET         |   CREATE    | Create initial session id in DB |
|                       | api/v1/auth/login/   |        POST         |   UPDATE    | Update session id               |
|                       | api/v1/auth/logout/  |         GET         |   UPDATE    | Update session id               |
| **Djoser URLs**       | auth/users/          |         GET         |    READ     | Get all users                   |
|                       | auth/users/:id/      |         GET         |    READ     | Get one user                    |
|                       | auth/users/          |        POST         |   CREATE    | Create new user                 |
| **Djoser Token Auth** | auth/token/login/    |        POST         |   CREATE    | Create user token               |
|                       | auth/token/logout/   |        POST         |   DELETE    | Delete user token from DB       |


### How to check?
We can test the API using [curl](https://curl.se/) or [httpie](https://pypi.org/project/httpie/),
or we can use [Postman](https://www.postman.com/). I use Postman.

### Create users and Tokens
#### Register
First we need to create a user, so we can log in. To register we should send POST request with the username, password 
and email to the following URL:
```
http://localhost:8000/auth/users/
```
We can do this using the Postman program. Select the POST request type and in the “Body” tab mark 
the “form-data” item and enter:

| KEY      | VALUE                   |
|:---------|:------------------------|
| username | User                    |
| password | Very1Difficult1Password |
| email    | user@gmail.com          |

We will receive the following response

    {
        "email": "user@gmail.com",
        "username": "User",
        "id": 3
    }

#### Get Token
To auth it is necessary to send POST request with the username and password to the following URL:
```
http://localhost:8000/auth/token/login/
```

Let's open a new tab in Postman, enter this URL, select the POST method, go to the "Body" tab, 
check "form-data" and enter:

| KEY      | VALUE                   |
|:---------|:------------------------|
| username | User                    |
| password | Very1Difficult1Password |


After sending the request, a response is returned to us in the form of a JSON string with an 
assigned token:

    {
        "auth_token": "0ea6de8839f49f1b74db976f9addc5fc6413c348"
    }

### Testing
Only authenticated users can use the API services, for that reason if we send GET-request
```
http://localhost:8000/api/v1/product/
```

we get:

    {
        "detail": "Authentication credentials were not provided."
    }

In order for the server to accept us as an authorized user, we need to add the following
in the Headers tab:

| KEY            | VALUE                                                             |
|:---------------|:------------------------------------------------------------------|
| Authorization  | Token 0ea6de8839f49f1b74db976f9addc5fc6413c348                    |

Now, when sending a request, we receive data. That is, by specifying the token issued to us in the 
GET request, we successfully pass the authentication procedure on the server and get access to 
confidential information.







