from __future__ import print_function
import functools
import os
from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for

import grpc

# from genproto import easyshop_pb2
# from genproto import easyshop_pb2_grpc

bp = Blueprint("handlers", __name__, url_prefix="/handlers")

@bp.before_app_request
def load_logged_in_user():
    """If a user id is stored in the session, load the user object from
    the database into ``g.user``."""
    user_id = session.get("user_id")

    if user_id is None:
        g.user = None
    else:
        g.user = {
            "user_id": user_id,
            "user_name": session.get("user_name")
        }

@bp.route("/login", methods=("GET", "POST"))
def login():
  if request.method == "POST":
    user_id = request.form["user_id"]
    password = request.form["password"]

    error = None

    if not user_id:
      error = "User ID is required."
    elif not password:
      error = "Password is required."

    if error is None:
      # with grpc.insecure_channel('login:50052') as channel:
      #     stub = easyshop_pb2_grpc.AccountServiceStub(channel)
      #     response = stub.login(easyshop_pb2.LoginRequest(user_id=user_id, password=password))
      #
      session.clear()
      session["user_id"] = user_id
      session["user_name"] = 'Eric Wu'

      flash('Login successfully')

      return redirect(url_for("home"))

    flash(error)

  return render_template("page/login.html")

@bp.route("/register", methods=("GET", "POST"))
def register():
  if request.method == "POST":
    user_id = request.form["user_id"]
    user_name = request.form["user_name"]
    password = request.form["password"]
    password_confirm = request.form["password_confirm"]
    error = None
    # host=os.environ.get()
    # print (os.environ)

    if not user_id:
      error = "User ID is required."
    elif not user_name:
      error = "Username is required."
    elif not password:
      error = "Password is required."
    elif not password_confirm:
      error = "Password Confirm is required."
    elif (
      password != password_confirm
    ):
      error = "The password is not confirmed."


    if error is None:
      # the name is available, store it in the database and go to
      # the login page

      # with grpc.insecure_channel('register:50051') as channel:
      #     stub = easyshop_pb2_grpc.AccountServiceStub(channel)
      #     response = stub.register(easyshop_pb2.RegisterRequest(user_id=user_id, user_name=user_name, password=password, password_confirm=password_confirm))

      flash('Register successfully, please login')

      return redirect(url_for("handlers.login"))


    flash(error)

  return render_template("page/register.html")

@bp.route("/CreateAsset", methods=("GET", "POST"))
def createAsset():
  if request.method == "POST":
      return redirect(url_for("home"))

  return render_template("page/CreateAsset.html")


@bp.route("/logout", methods=("GET", "POST"))
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    flash('Logout successfully')
    return redirect(url_for("home"))