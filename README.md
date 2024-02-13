**Portfolio Project 5**

# Highlights // Your Highlights Journal

**What was the best part of your day?**

Possible features to implement that are not in the Moments walkthrough:

- Link to another user in a highlight
- Add a category to a highlight
- Add a location to a highlight
- A calendar view at the top of users profiles with links to the highlights
- Feedback form for users to send to admin

## About

Highlights ia a social media platform designed to cultivate gratitude and positivity in everyday life. Inspired by the principles of the Five Minute Journal, our platform provides users with a space to share the highlights of their day and connect with others in a supportive online community.

Key Features:
- Highlight Sharing: Easily post and share the highlights of your day, complete with text descriptions, images, user tags and locations.
- Interactive Features: Engage with other users' highlights through likes, comments, and following other users.
- Search and Discovery: Explore highlights by keywords, categories, and user tags to find inspiration and connect with like-minded individuals.
- Calendar Integration: Visualize and track your daily highlights over time with a convenient calendar interface.

## UX

I followed the five planes of Website Design in the creation of this project.

### 1. Strategy

My strategy is to develop a social media platform designed to foster gratitude and enhance users perspective on life. Drawing inspiration from the principal of the five minute journal, the platform aims to provide a space where individuals can share their best highlights of their day. Grounded in scientific research on the benefits of gratitude, the platform aims to cultivate a positive online community.

Key features:
- Highlight sharing: Users can post the highlights of their day, promoting reflection and appreciation for positive moments.
- Interactive Features: To encourage engagement, user have the option to add categories, attach images, tag other users in their posts and add locations.
- Search Functionality: Users can search for highlights by tags, category, or location.
- User profiles: Users can view their profile and share their highlights with other users.
- Calendar display: Users can view their highlights on a calendar view.
- Follow and Un-follow: Users can follow and un-follow other users.

#### User Stories

Create an account & Login
- As a user I can view the landing page with information about the platform so I can learn more about it.
- As a user I can see the navbar on every page so I can easily navigate the site.
- As a logged out user I can see the login and sign up links in the navbar so I can navigate to them easily.
- As a new user I can create an account so I can log in and use the features.
- As a returning user I can log in to my account so I can enjoy the site.
- As a logged in user I can maintain my logged in status so I can keep using the site.
- As a logged in user I can see the add highlight, liked, profile and logout links in the navbar so I can easily navigate to them.

Creating Highlights
- As a user I can create a highlight so I can share my thoughts and feelings.
- As a user I can tag another user in my highlight so I can show my support for them.
- As a user I can add a tag to my highlight so I can categorize it.
- As a user I can add a location to my highlight so I can show where I was when I made that highlight.
- As a user I can add an image to my highlight so everyone can see it.
- As a user I can add a description to my highlight so there is more detail to read.
- As a user I can update one of my highlights so I can fix any mistakes I made.
- As a user I can delete one of my highlights so I can remove it from the site.

The Feed
- As a user I can see highlights ordered by the most recent so that each time I visit the site the content is fresh.
- As a user I can continue scrolling through the highlights without having to refresh the page or click next so that I can see more highlights.
- As a user I can see the posts of users that I follow so that I can see what they are up to.
- As a user I can see posts I have likes so that I can revisit the moments that I enjoyed.
- As a user I can search for for keywords so that I can to discover content I am interested in.
- As a user I can filter by category so I can see highlights that I am interested in.
- As a user I can filter by location so I can see highlights that are close to me.

Profile pages
- As a user I can add a profile avatar so I can show my picture.
- As a user I can add a bio so I can show my story.
- As a user I can add a name so I can show my name.
- As a user I can add a location so I can show my location.
- As a user I can edit my profile so I can update any information I need to.
- As a user I can change my password so I can protect my account.
- As a user I can view other users profiles so I can see their highlights and find out more about them.
- As a user I can see a list of the top profiles so I can see who is most active on the site.
- As a user I can see all the highlight from a user in their profile so I can see what they are up to.
- As a user I can see how many followers, following and posts users have in their profile so I can see how active they are.

Interactivity
- As a user I can like/unlike another users highlight so I can show my support for it.
- As a user I can comment on another users highlight so I can start a conversation.
- As a user I can update a comment I have made on another users highlight so I can fix any mistakes I made.
- As a user I can delete a comment I have made on another users highlight so I can remove it from the site.
- As a user I can follow another user so I can see their highlights in my feed.
- As a user I can un-follow a user so I no longer see their highlights in my feed.

General
- As a site owner I want the site to be fully responsive across all screen sizes so it can be used on any device.
- As a site owner I want the site to be easy to use so I can easily navigate and use it.
- As a site owner I want the site to be secure so I can use it safely and securely.
- As a site owner I want a 404 page so users know when they have tried to access a page that does not exist.
- As a user I want messages feedback messages to be shown when I create, update or delete a highlight or comment so that I can see if I am using the site correctly.

### 2. Scope

- Purpose: The purpose of the website is to provide a platform for users to share the highlight of their day, fostering gratitude and a positive outlook on life. The website aims to create a supportive online community where users can connect, inspire and uplift each other.
- Target Audience: The target audience includes individuals who are interested in personal development, mindfulness, and self-improvement. This may include a diverse range of demographics, including young adults, professionals, parents, and students, who share a common interest in cultivating gratitude and positivity.
- Core Functionality:
    - Highlight sharing: Users can easily post and share the highlights of their day, including text descriptions, images, locations, categories and other users.
    - Interactive features: The website enables users to engage with each others highlights through likes and comments, fostering a sense of community and connection.
    - Search and Discovery: Robust search functionality allows users to search for highlights by tags, category, or location.
    - User profiles: Users can view each others profiles and comment on individual highlights.
    - Calendar display: The user can view their highlights on a calendar view, providing a convenient and efficient way to keep track of their highlights over time.
    - Follow and Un-follow: Users are able to follow or un-follow other users to foster a more engaged and connected community.

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

##### Location

- id
- name
- latitude models.DecimalField(max_digits=9, decimal_places=6) 
- longitude

##### Like

##### Comment

#### Wireframes

![Landing page wireframe](/docs/landing-page-wireframe.png)
![signup wireframe](/docs/signup-wireframe.png)
![login wireframe](/docs/login-wireframe.png)
![feed wireframe](/docs/feed-wireframe.png)
![create highlight wireframe](/docs/add-a-highlight-woreframe.png)
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

A full list of the requirements and the versions used can be found in the requirements.txt file. To install them and run them on your own machine first setup a virtual environment with the command to create a venv...  
`python3 -m venv venv`  
Then this command to run the venv run the command  
`source venv/bin/activate`  
To stop running the environment simply type the command  
`deactivate`  
To install the requirements use the command, make sure your venv is activated  
`pip install -r requirements.txt`  

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