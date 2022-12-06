
# Project Title

## Price comparison Application

This application allow users to search for a product and presents the user with results(product picture and price) it fetches from different platforms that sells the particular product.

This application helps shoppers or prospective shoppers(users) to find relevant deals and compare prices accross a variety of major retailers or vendor of a product.


### Project layout

#### The project will include the following areas;
#####  1. Project Design
#####  2. Frontend Development
#####  3. Backend Development
#####  4. Backend Development

### Tools used 

#### The following tools/programming languages will be used in the each areas, respectively;
####  1. Project Design
        figma  etc
####  2. Frontend Development
        HTML   CSS   BootStrap   JavaScript
####  3. Backend Development
         Python3 Django
####  4. version control
        Github

## Project Files Structure

           REPO
            ├── README.md
            ├── .gitignore => list of files that will not be pushed to github.
            ├── venv => virtual environment folder, use for activate a virtual or controlled environment.
            ├── requirements.txt => The dependencies we need to install with `pip3 install -r requirements.txt`
            └── Django project => Main Project folder, contains all project codes, boiler plates and folders.
                ├──App =>look
                │   ├── __init__.py
                │   ├──migration => Sub_folder to store database migrations
                │   ├── static
                │   │   ├── css
                │   │   ├── img
                │   │   └── js
                │   │
                │   ├── templates
                │   │   ├── errors
                │   │   ├── forms
                │   │   ├── layouts
                │   │   └── pages
                │   │
                │   ├── admin.py
                │   ├── apps.py
                │   ├── form.py => form to models 
                │   ├── models.py
                │   ├── tests.py
                │   ├── urls.py
                │   └── views.py
                │
                ├── django_project => Folder contains code to setup project
                │   ├── __init__.py
                │   ├── asgi.py
                │   ├── settings.py
                │   ├── urls.py
                │   └── wsgi.py
                │
                ├──.env
                └──manage.py
                           

## django Installation Steps :-
       1. Install Python 3.10 Or Higher. (download and install globally)
### open the folder contain the project, in your VScode terminal(or cmd)
       2. Install all dependencies cmd -python -m pip install –-user -r requirements.txt.
### cd into the project directory
       3. Finally run cmd - python manage.py runserver.
        N:B we are using Django version 4.1.3.




## How it works

There are two categories of users that are allowed on the application

- Unauthenticated User : User without a registered account on the application (roaming Visitor) 
- Authenticated User : User with a registered account on the application

These users have different priviledges as stated below.

#### Unauthenticated users

These users has free access to the application's landing page, view basic information and documentation. 

They can interact with the documentation like click "read more" and be redirected to page or section to read more, they can also browse through available products but not interact with them. 

To interact with products and view more details they will have to register using the sign-up button/link provided on the page.

#### Authenticated users
These are registered or authenticated users they have full access to the application. They can comment under product/price that is displayed in response to there search and available products on the page. These comments are loaded from the database on the page the user interacts with everytime he or she login to use the application service(s).

When and If an authenticated user found a product with their prefered price, he/she have a link below the product of interest that redirects he/she to vendor's platform to complete his/her order.

They can also share the product they found on the page or result of their search with other people on social media or via email.



##  Project Stages

The project is carried out in 4 progressive stages as stated below with their respective product;

### Stage 1
| Design sketch | 
| :------------- |
| Data schema |
| Mood board |

### Stage 2
| loading...| 
| :------------- |
| loading...|
| loading...|

### Stage 3
| loading...| 
| :------------- |
| loading...|
| loading...|

### Stage 4
| loading...| 
| :------------- |
| loading...|
| loading...|


## Appendix

Any additional information goes here


## Authors

- [@bintghazall](https://www.github.com/bintghazall)

## Project Contributors 

- [@aliu691](https://www.github.com/aliu691)
- [@bintghazall](https://www.github.com/bintghazall)
- [@Oyindamolajames](https://www.github.com/Oyindamolajames)
- [@Joshua-oneshioagbe](https://www.github.com/Joshua-oneshioagbe)
- [@Affy-art](https://www.github.com/Affy-art)
- [@Amakaugwuanyi](https://www.github.com/Amakaugwuanyi)
- [@IamNaeto](https://www.github.com/IamNaeto)
- [@Fejiro-J](https://www.github.com/Fejiro-J)
- [@Mercyozioma](https://www.github.com/Mercyozioma)
- [@Ayoolajamiu](https://www.github.com/Ayoolajamiu)
- [@NnadozieAmara](https://www.github.com/NnadozieAmara)
- [@CynthiaKings](https://www.github.com/CynthiaKings)
- [@Yemioladd](https://www.github.com/Yemioladd)
- [@Gudnuel](https://www.github.com/Gudnuel)
- [@Only1SP](https://github.com/orgs/zuri-training/people/Only1SP)


## Badges

Add badges from somewhere like: [shields.io](https://shields.io/)

[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](https://choosealicense.com/licenses/mit/)
[![GPLv3 License](https://img.shields.io/badge/License-GPL%20v3-yellow.svg)](https://opensource.org/licenses/)
[![AGPL License](https://img.shields.io/badge/license-AGPL-blue.svg)](http://www.gnu.org/licenses/agpl-3.0)

## Color Reference

| Color             | Hex                                                                |
| ----------------- | ------------------------------------------------------------------ |
| Example Color | ![#0a192f](https://via.placeholder.com/10/0a192f?text=+) #0a192f |
| Example Color | ![#f8f8f8](https://via.placeholder.com/10/f8f8f8?text=+) #f8f8f8 |
| Example Color | ![#00b48a](https://via.placeholder.com/10/00b48a?text=+) #00b48a |
| Example Color | ![#00d1a0](https://via.placeholder.com/10/00b48a?text=+) #00d1a0 |

