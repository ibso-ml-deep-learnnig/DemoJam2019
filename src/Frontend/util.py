import os
import hashlib
import configparser as ConfigParser
from PIL import Image
from werkzeug.utils import secure_filename
from flask import session

def get_service_addr(SERVICE_ADDR):

    url = None

    url = os.environ.get(SERVICE_ADDR)
    if url == None:
       config = ConfigParser.ConfigParser()
       config.read('config.env')
       url = config.get('WHITE_LIST', SERVICE_ADDR)

    return url

def upload_image_with_md5_filename(file):

    img = Image.open(file)
    img = img.resize((1560, 1000), Image.ANTIALIAS)

    # Base Dir / temp path / images path
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#   Save the image to temp path, at first secure file name
    filename = secure_filename(file.filename)
    filename = session.get("user_id") + '-' + filename
    temp_abs_path = os.path.join(base_dir, "Frontend", "static", "asset", "temp", filename)
    img.save(temp_abs_path)

#   Generate md5 file name
    md5_obj = hashlib.md5()
    with open(temp_abs_path, 'rb') as file_obj:
        md5_obj.update(file_obj.read())
    digest = md5_obj.hexdigest()
    prefix = str(digest)
    suffix = filename.rsplit('.')[1]
    md5_filename = prefix + '.' + suffix

    md5_filename = secure_filename(md5_filename)
    images_abs_path = os.path.join(base_dir, "Frontend", "static", "asset", "images", md5_filename)

    return temp_abs_path, images_abs_path, md5_filename