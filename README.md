Web-Services
======================
A web services used by [akshayon.net](http://akshayon.net) like twitter tweets, mail-handler and blogs listing.This project is developed using [Django Rest-Framework](http://www.django-rest-framework.org/), also known as `DRF`.

## Dependencies
1. Python 3.7+

2. `pip` , a python package manager

3. `virtualenv` installed
    
    ```bash
        # To install `virtualenv`
        $ pip install virtualenv
    ```

## Instructions
1. First create a `virtual` environment and also install some dependencies, follow these commands

    ```bash
        $ virtualenv venv
        $ source venv/bin/activate
        $ pip install -r requirements.txt
    ```

2. To run the app

    ```bash
        $ cd webservices
        $ python manage.py runserver
    ```
