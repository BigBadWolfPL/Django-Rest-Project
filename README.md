## Django-Rest-Project

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
git clone https://github.com/BigBadWolfPL/Django-Rest-Project.git

```
2) Change location to project folder using command:
```
cd Django-Rest-Project
```

3) In location where docker-compose.yml is run command:

```
docker-compose up
```
4) With running docker container open second terminal window and paste this command (To create superuser):

```
docker-compose exec web python manage.py createsuperuser

```
* Enter your Username,
* Email (optional), 
* And Password.


#### You are now ready to go adress:
### http://0.0.0.0:8000/

##### Login as superuser and upload images

* Create some accounts (admin panel)
* You can change membership for each user in "Profiles" (admin panel) default membership = BASIC.
* Upload some images.
* See result on: (http://0.0.0.0:8000/   +   small_image_link), or just (CTRL + right mouse button on link in postman)


#### To see binary data you must generate token

##### Visit: http://0.0.0.0:8000/api-token-auth/
###### (IMPORTANT! In postman set: body/raw/JSON)
* Send username and password as POST request, example:


{
    "username":
        "Yourusername",
    "password":
        "yourpassword" 
}




You will get New token.

##### Visit: http://0.0.0.0:8000/binary/
###### (IMPORTANT! Set: Headers)
* Enter KEY: Authorization and VALUE: Token >token_you_received<
* Send that token as GET request, example:

* KEY: Authorization VALUE: Token dv284f7f96cd92345435fdg4352f33e13432d




Token expires afetr time set via uploading photo (default=300, max =30000 seconds)

