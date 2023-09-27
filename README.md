<h1 align="center">Website for a photographer on Flask</h1>

---
![img.png](readme.png)
# [Link to working site](https://morenko-wedding.ru)
___
### Description of the site
___
Portfolio website for a photographer, there is a main page with photographs,
a page with different portfolios, a contacts page with a feedback form and 
a map to indicate the office, as well as an abou page, with an interesting performance of skills.

The site design is based on
[template Rex](https://themeforest.net/item/rex-clean-minimal-portfolio-html5-template/25023918),

Backend site is implemented in python 3.10, using the
[Flask framework](https://flask.palletsprojects.com/en/2.3.x/)

Еhe site was launched on a vps server ubuntu, with the help -
[Gunicorn server](https://gunicorn.org),
[Nginx](https://nginx.org).

Since the database in the application is not complicated, I used 
[MySQL](https://www.mysql.com).


## How to start

---
1. Download the repository to your device:
```
git clone https://github.com/Ser-Alex/flask-app.git flask-app
```
2. Create a virtual environment and activate it:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
3. Installing libraries from a file requirements:
```
pip install -r requirements.txt
```
4. Сreate a .env file in the project root and fill it in according to .env.template
* I used Yandex because it was convenient for me, you can edit the config file and use Google or something else.
* Also, the map on the contacts page is implemented using Yandex, for it to work you need to insert your key for Yandex maps in the template.
5. Create a user:
```
flask user create [login] [password] [email]
```
6. After completing all the steps we can launch our application:
```
flask run
```
7. Congratulations, your site has been launched locally, now follow the link from the terminal to the home page, 
now it is empty, but adding ```localhost:5000/admin ```to the link will take you to the admin panel, where you will need to log in, 
enter the user data that you created earlier, after successful authorization you will need to fill out the 
site models according to the instructions.

## Results

After completing the steps, your site is almost ready for use and uploading to the server, but there are little 
things that you need to complete yourself, in the basic template you need to fill out the meta description and 
title, as well as links to social networks, fill in the YandexMap key, and also configure the email correctly 
notification, and your portfolio website for a photographer will be ready.
___


### Feedback
- ser.alex.serb@gmail.com