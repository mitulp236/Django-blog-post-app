# Django-blog-post-app
A simple micro blog app who gives to post 200 character blog post. 


1> Clone the repository

```
git clone https://github.com/mitul-gateway/Django-blog-post-app.git
```

2> Create virtualenv

```
virtualenv -p python3.8 venv_myblog

source Django-blog-post-app-env/Scripts/activate
```

3> Install dependencies

```
pip install -r requirements.txt
```

5> Run migrations

```
python manage.py makemigrations
python manage.py migrate
```

6> Run the project

```
python manage.py runserver
```
<br/>

**Routes For API ** 

1> For API login | HTTP-POST 

```
http://127.0.0.1:8000/rest-auth/login/
```
2> For Signup | HTTP-POST

```
http://127.0.0.1:8000/rest-auth/registration/
```
3> For retrive all blog post | HTTP-GET

```
http://127.0.0.1:8000/api/blogs/
```
4> For retrive authenticated user's blog post | HTTP-GET

```
http://127.0.0.1:8000/rest-auth/myblogs/
```
5> For create new post | HTTP-POST

```
http://127.0.0.1:8000/rest-auth/create/
```
