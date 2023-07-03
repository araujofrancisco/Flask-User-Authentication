from flask import Blueprint, render_template, request
from flask_login import login_required

from src import db
from src.accounts.models import User


users_bp = Blueprint("users", __name__)


# def get_users():
#     session = db.session()
#     users = session.query(User).all()
#     return users


# @users_bp.route("/users", methods=['GET','POST'])
# @login_required
# def home():
#     users = get_users()
    
#     if request.method == 'POST':
        
#         pass
#     return render_template("users/index.html", **locals())

@users_bp.route("/access", methods=['GET','POST'])
@login_required
def access():
    return render_template("users/access.html", **locals())
