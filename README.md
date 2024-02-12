**Portfolio Project 5**

# Highlights // The Highlights Journal

**What was the best part of your day?**

Possible features to implement that are not in the Moments walkthrough:

- Link to another user in a highlight
- Add a category/tag (#) to a highlight
- Add a location to a highlight
- A calendar view at the top of users profiles with links to the highlights
- Notifications
- Messages

## About

Highlights is a social media platform for people to share the best parts of their day based on the five minute journal. User are able to:
- Create an account
- Log in to their account
- Create, edit and delete a highlight (daily journal entry) including:
    - images 
    - tagging other users
    - category
    - location
- Follow other users so they can see their highlights as well as like and comment on them
- Filter highlights by:
    - users they follow
    - tags
    - category
    - date
    - location

## UX

### 1. Strategy

#### User Stories

- As a user I can create an account so I can enjoy the site
- As a user I can log in to my account
- As a user I can create a highlight
- As a user I can update one of my highlights
- As a user I can delete one of my highlights
- As a user I can see other users
- As a user I can view other users profiles
- As a user I can follow another user
- As a user I can un-follow a user
- As a user I can see a list of the top profiles
- As a user I can like/unlike another users highlight
- As a user I can comment on another users highlight
- As a user I can update a comment I have made on another users highlight
- As a user I can delete a comment I have made on another users highlight

### 2. Scope
### 3. Structure
### 4. Skeleton

#### Database
[Database edit](https://lucid.app/lucidchart/416f6b5f-1a8f-402b-9a48-252b729ca79d/edit?page=0_0&invitationId=inv_6dc8ebbb-1811-4e2d-98d4-dd97f1f2b8be#)
![Database schema](docs/database_schema.png)

To create a new app for a new model  
`python manage.py start app <appname>`  
Then add it to the `INTALLED_APPS` list in settings.py

To migrate the changes to the database  
`python manage.py makemigrations`  
`python manage.py migrate`

To create a superuser  
`python manage.py createsuperuser`

##### User
The user model contains information about the user and is part of the Django allauth library
- One-to-one relationship with the profile model's owner field
- ForeignKey relationship with the follower model's owner & followed fields
- ForeignKey relationship with the highlight model's owner & tagged_users fields
- ForeignKey relationship with the tagged_users model's highlight_owner & tagged_user fields
- ForeignKey relationship with the like model's owner field
- ForeignKey relationship with the comment model's owner field

##### Profile
The profile model contains the following information used in users profiles
- id
- owner (ForeignKey)
    - One to one relationship with the user model's id field
- created_on
- updated_on
- name
- bio
- image

##### Follower


##### highlight

##### Tagged Users

##### Like

##### Comment

#### Wireframes

![Landing page wireframe](/docs/landing-page-wireframe.png)
![signup wireframe](/docs/signup-wireframe.png)
![login wireframe](/docs/login-wireframe.png)
![feed wireframe](/docs/feed-wireframe.png)
![create highlight wireframe]()
![highlight wireframe](/docs/highlight-wireframe.png)
![profile wireframe](/docs/profile-wireframe.png)

### 5. Surface

![Color Palette](/docs/color-palette.png)

## Technologies Used

To create a requirements.txt file with all the dependencies  
`pip freeze > requirements.txt`

### Languages and Frameworks

- Python
- Django Rest Framework  
`pip install djangorestframework`

### Libraries & Tools

- [Cloudinary](https://cloudinary.com/) - Image storage
- [Pillow](https://pypi.org/project/pillow/) - Image processing

## Project Setup

1. Use the [Code Institute Template](https://github.com/Code-Institute-Org/gitpod-full-template) to create a new repository on GitHub.
2. Install Django Rest Framework with the following command
    - `pip3 install 'django<4'`
3. Initialize the project with the following command
    - `django-admin startproject drf_highlights .`
4. Install Django Cloudinary Storage for image storage with the following command
    - `pip install django-cloudinary-storage`
5. Install Pillow for image processing with the following command
    - `pip install Pillow`
6. Add `cloudinary` and `cloudinary_storage` to `INSTALLED_APPS` in settings.py with `django.contrib.staticfiles` between them
```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'cloudinary_storage', 
    'django.contrib.staticfiles',
    'cloudinary',
]
```
7. Create an env.py file in the base directory and add `import os` at the top, then add the cloudinary API Environment variable
```
import os

os.environ['CLOUDINARY_URL'] = '<Cloudinary API Environment variable>'
```
8. Back in settings.py 
    - add import os and env.py (if it it present)
    - set `CLOUDINARY_STORAGE` to the `CLOUDINARY_URL`
    - set `MEDIA_URL` so the settings knows where to put the image files
    - set the `DEFAULT_FILE_STORAGE` to `cloudinary_storage.storage.MediaCloudinaryStorage`
```
import os

if os.path.exists('env.py'):
    import env

CLOUDINARY_STORAGE = {
    'CLOUDINARY_URL': os.environ.get('CLOUDINARY_URL')
}
MEDIA_URL = '/media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'
```

## Deployment


## Validation

## Testing

## Bugs