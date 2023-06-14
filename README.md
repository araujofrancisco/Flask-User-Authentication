# Flask Basic User Authentication 

User authentication is important for protecting sensitive information and resources from unauthorized access. In this tutorial, you will learn how to set up basic user authentication – that is password-based authentication – in your Flask application.

Blog Tutorial: https://ashutoshkrris.hashnode.dev/how-to-set-up-basic-user-authentication-in-a-flask-app

Project Demo: https://youtu.be/XxSESg89xEI

### Instructions to run from code

```
git clone https://github.com/ashutoshkrris/Flask-User-Authentication

cd Flask-User-Authentication
python3 -m venv env
. env/bin/activate
pip install -r requirements.txt
source .env

flask db init
flask db migrate
flask db upgrade

python manage.py run
```
