**Portfolio Project 5**

# Highlights // The Highlights Journal

**What was the best part of your day?**

Possible features to implement that are not in the Moments walkthrough:

- Link to another user in a post
- Add a category/tag (#) to a post
- Add a location to a post
- A calendar view at the top of users profiles with links to the posts
- Notifications
- Messages


## User Stories

## Database

![Database schema](docs/database_schema.png)

To create a new app for a new model  
`python manage.py start app <appname>`  
Then add it to the `INTALLED_APPS` list in settings.py

To migrate the changes to the database  
`python manage.py makemigrations`  
`python manage.py migrate`

To create a superuser  
`python manage.py createsuperuser`

### User
The user model contains information about the user and is part of the Django allauth library
- One-to-one relationship with the profile model's owner field
- ForeignKey relationship with the follower model's owner & followed fields
- ForeignKey relationship with the post model's owner & tagged_users fields
- ForeignKey relationship with the tagged_users model's post_owner & tagged_user fields
- ForeignKey relationship with the like model's owner field
- ForeignKey relationship with the comment model's owner field

### Profile
The profile model contains the following information used in users profiles
- id
- owner (ForeignKey)
    - One to one relationship with the user model's id field
- created_on
- updated_on
- name
- bio
- image

### Follower


### Post

### Tagged Users

### Like

### Comment


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