## Django-Rest-Project

* [Description](#description)
* [Technologies](#technologies)
* [Setup](#setup)

## Description
API that allows user to upload an image (PNG or JPG)
	
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


#### You are now ready to go (login and enjoy ;)):
### http://0.0.0.0:8000/


