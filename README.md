# Django-Rest-Project

* [Description](#description)
* [Technologies](#technologies)
* [Setup](#setup)

## Description
API that allows user to upload an image and ...

##### There are three bultin account tiers: Basic, Premium and Enterprise:

#### Users that have "Basic" plan after uploading an image get: 
* a link to a thumbnail that's 200px in height

#### Users that have "Premium" plan get:
* a link to a thumbnail that's 200px in height
* a link to a thumbnail that's 400px in height
* a link to the originally uploaded image

#### Users that have "Enterprise" plan get
* a link to a thumbnail that's 200px in height
* a link to a thumbnail that's 400px in height
* a link to the originally uploaded image
* ability to fetch a link to the (binary) image that expires after a number of seconds (user can specify any number between 300 and 30000) (Not fully done yet)

Skiped the registration part (users are created via the admin panel).


	
## Technologies
Project is created with:
* Django 4.1.6
* djangorestframework 3.14.0
* django-imagekit 4.1.0


## Setup
To run project:

1) Clone this repository

```
git clone https://github.com/BigBadWolfPL/Django-Rest-Project.git &&
cd Django-Rest-Project &&
python -m venv env_rest &&
source env_rest/bin/activate &&
pip install -r requirements.txt &&
python manage.py makemigrations &&
python manage.py migrate &&
python manage.py createsuperuser &&
python manage.py runserver

```

* Enter your Username,
* Email (optional), 
* And Password.

2) Change location to project folder using command:
```

```

3) Create virtual environment using command:
```

```

4) Activate virtual environment by using command (Unix or MacOS):
```

```

or (Windows):
```
source env_rest\Scripts\activate
```


5) Install all packages from requirements.txt:

```


```
6) Create superuser:

```
python manage.py makemigrations &&
python manage.py migrate &&
python manage.py createsuperuser &&
python manage.py runserver

```

* Enter your Username,
* Email (optional), 
* And Password.

6) Run server:

```
python manage.py runserver

```

## LOGIN:
### If you using browser go directly to: http://0.0.0.0:8000/
* Login as a superuser you created
* Create some accounts (admin panel)
* You can change membership for each user in "Profiles" (admin panel) default membership = BASIC.
* Upload some images.
* See result on: (http://0.0.0.0:8000/   +   small_image_link), or just (CTRL + right mouse button on link in postman)

### If you use postman go to: http://0.0.0.0:8000/api-auth/login/
* send GET request to recive token
* in HEADERS create 

(KEY: X-CSRFToken VALUE: >TokenYouRecived<

* in BODY/form-data create

(KEY: username VALUE: yourusername)

(KEY: password VALUE: yourpassword)
* send POST request

If You login successfully you will be redirected to the adress: accounts/profile/ (that does not exist)
* you can now visit http://0.0.0.0:8000/


## To see binary data you must generate expiring token

### Visit: http://0.0.0.0:8000/api-token-auth/

#### IMPORTANT! In postman set: body/raw/JSON
* Send username and password as POST request, example:


{
    "username":
        "Yourusername",
    "password":
        "yourpassword" 
}




You will recive New Token.

### Visit: http://0.0.0.0:8000/binary/

### IMPORTANT! In Headers:
* Create (KEY: Authorization  VALUE: Token >token_you_received<)
* Send that token as GET request, example:

* KEY: Authorization VALUE: Token dv284f7f96cd92345435fdg4352f33e13432d




Token expires afetr time set via uploading photo (default=300, max =30000 seconds)

