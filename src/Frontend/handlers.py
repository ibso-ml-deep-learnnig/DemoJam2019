from __future__ import print_function
import functools
import os
import shutil
from flask import Blueprint
from flask import flash
from flask import g
from flask import redirect
from flask import render_template
from flask import request
from flask import session
from flask import url_for
import grpc

from genproto import account_pb2
from genproto import account_pb2_grpc
from genproto import createAsset_pb2
from genproto import createAsset_pb2_grpc
from genproto import db_pb2
from genproto import db_pb2_grpc

from logger import getJSONLogger
import util as util

# Server log
logger = getJSONLogger('frontend-server')

# Blue Print
bp = Blueprint("handlers", __name__, url_prefix="/handlers")

def login_required(view):
    """View decorator that redirects anonymous users to the login page."""
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for("handlers.login"))

        return view(**kwargs)

    return wrapped_view

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

    # Parameters
    user_id = request.form["user_id"]
    password = request.form["password"]

    error = None

    if not user_id:
      error = "User ID is required."
    elif not password:
      error = "Password is required."

    url = util.get_service_addr('ACCOUNT_SERVICE_ADDR')
    if url == '':
        error = 'The account service is not available now'

    if error is None:
      logger.info("Account Service Address: " + url)
      with grpc.insecure_channel(url) as channel:
          stub = account_pb2_grpc.AccountServiceStub(channel)
          response = stub.login(account_pb2.LoginRequest(user_id=user_id, password=password))
          if response.user_name == '':
              error = "User ID or Password is not correct"
          else:
              session.clear()
              session["user_id"] = user_id
              session["user_name"] = response.user_name

    if error is None:
        return redirect(url_for("handlers.explore"))
    else:
        flash(error)
        return redirect(url_for("handlers.login"))

  return render_template("page/login.html")

@bp.route("/register", methods=("GET", "POST"))
def register():
  if request.method == "POST":
    user_id = request.form["user_id"]
    user_name = request.form["user_name"]
    password = request.form["password"]
    password_confirm = request.form["password_confirm"]
    error = None

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
      # the account page

      # with grpc.insecure_channel('register:50051') as channel:
      #     stub = easyshop_pb2_grpc.AccountServiceStub(channel)
      #     response = stub.register(easyshop_pb2.RegisterRequest(user_id=user_id, user_name=user_name, password=password, password_confirm=password_confirm))

      flash('Register successfully, please account')

      return redirect(url_for("handlers.account"))


    flash(error)

  return render_template("page/register.html")


@bp.route("/CreateAsset", methods=("GET", "POST"))
@login_required
def createAsset():
  if request.method == "POST":

      error = None

      # url = util.get_service_addr('ASSET_CREATION_SERVICE_ADDR')
      # if url == '':
      #     error = 'The Asset Service is not available now'

      file = request.files["file"]
      if file:
          temp_path, images_path, filename = util.upload_image_with_md5_filename(file)
          logger.info("temp path: " + temp_path)
          logger.info("images path: " + images_path)
      else:
          error = 'No picture uploaded'

      newAsset = createAsset_pb2.assetInputs(
          asset_class = request.form["asset_class"],
          description = request.form["description"],
          picture = filename,
          company_code = request.form["company_code"],
          cost_center = request.form["cost_center"],
          acquisition_date = {'year': 2019, 'month': 8, 'day': 31},
          amount = float(request.form["amount"]),
          ul_year = int(request.form["useful_life_y"]),
          ul_period = int(request.form["useful_life_m"]),
          user_id = session["user_id"]
      )
          # 'asset_id': '<New>',
          # 'asset_class': request.form["asset_class"],
          # 'description': request.form["description"],
          # 'picture': filename,
          # 'company_code': request.form["company_code"],
          # 'asset_number': '9001',
          # 'asset_subno': '0000',
      #     'cost_center': request.form["cost_center"],
      #     'acquisition_date': {'year': 2019, 'month': 8, 'day': 31},
      #     'amount': float(request.form["amount"]),
      #     'ul_year': int(request.form["useful_life_y"]),
      #     'ul_period': int(request.form["useful_life_m"]),
      #     'user_id': session["user_id"]
      # }

      logger.info("request: " + str(newAsset))

      url = os.environ.get('ASSET_SERVICE_ADDR', 'localhost:50051')
      if error is None:
          logger.info("asset service address: " + url)

          with grpc.insecure_channel(url) as channel:
              stub = createAsset_pb2_grpc.s4apiStub(channel)
              newAssetResponse = stub.create(newAsset)
              if newAssetResponse.has_error is True:
                  error  = 'Has error'

              # stub = createAsset_pb2_grpc.s4apiStub(channel)
              # response = stub.create(createAsset_pb2.assetInputs(company_code='0001', asset_number='60001', description='testAsset'))
              #
              # logger.info("response from asset service api log: " +response.api_log)
              # logger.info("response from asset service db log: " +response.db_log)
              # logger.info("response from asset service error: " +response.error)

      if error is None:
          shutil.move(temp_path, images_path)
          flash('Your asset is complete!')
          return redirect(url_for("handlers.asset", id=newAssetResponse.db_log))
      else:
          flash(error)
          return redirect(url_for("handlers.createAsset"))

  return render_template("page/CreateAsset.html")


@bp.route("/explore", methods=("GET", "POST"))
@login_required
def explore():

    assets = [
        {
            'asset_id': 'add_new_asset',
            'asset_class': '',
            'description': 'Add New ...',
            'picture':  '../static/asset/add-new.jpg',
            'company_code': 'A001',
            'asset_number': '<New Asset>',
            'asset_subno': '',
            'cost_center': '',
            'acquisition_date': '',
            'amount': '',
            'ul_year': '',
            'ul_period': '',
            'user_id': '',
            'create_date': '',
            'create_time':''
        }
    ]
    url = os.environ.get('DB_SERVER_SERVICE_ADDR', 'localhost:8001')
    with grpc.insecure_channel(url) as channel:
        stub = db_pb2_grpc.DBServiceStub(channel)
        assetList = stub.selectAssetAll(db_pb2.ListAssetsRequest(user_id=session["user_id"]))

        for asset in assetList.asset:
            assets.append(asset)

    # assets = [
    #     {
    #         'id': 'add_new_asset',
    #         'number': '<New Asset>',
    #         'description': 'Add New...',
    #         'picture': '../static/asset/add-new.jpg'
    #     },
    #     {
    #         'id': '1',
    #         'number': 'a0001',
    #         'description': 'air plants',
    #         'picture': '../static/asset/a0001.jpg'
    #     },
    #     {
    #         'id': '2',
    #         'number': 'a0002',
    #         'description': 'Vintage Camera Lens',
    #         'picture': '../static/asset/a0002.jpg'
    #     }
    # ]
    return render_template("page/list.html", assets=assets)

@bp.route("/asset/<string:id>", methods=("GET", "POST"))
@login_required
def asset(id):
    logger.info("request method:" + request.method)
    logger.info("request param:" + id)
    if request.method == "GET":
        # asset = {
        #         'id': '1',
        #         'number': 'a0001',
        #         'description': 'air plants',
        #         'picture': '../../static/asset/images/a0001.jpg'
        #     }

        asset = None

        url = os.environ.get('ASSET_SERVICE_ADDR', 'localhost:50051')
        with grpc.insecure_channel(url) as channel:
            stub = createAsset_pb2_grpc.s4apiStub(channel)
            asset = stub.display(createAsset_pb2.AssetId(asset_id=id))

        if asset is None:
            flash('No Asset Found!')

        return render_template("page/asset.html", asset=asset)

@bp.route("/logout", methods=("GET", "POST"))
def logout():
    """Clear the current session, including the stored user id."""
    session.clear()
    return redirect(url_for("home"))