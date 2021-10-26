import sys
sys.path.append("../")
import uuid
from datetime import datetime, timedelta
from flask import jsonify, abort, request, Blueprint
from Selenium_code import Url_link_checker
from urllib.parse import unquote
from datetime import datetime, date, timedelta
from functools import wraps
from flask import Response
import json

REQUEST_API = Blueprint('request_api', __name__)


def get_blueprint():
    """Return the blueprint for the main app module"""
    return REQUEST_API

def docache(minutes=3, content_type='application/json; charset=utf-8'):
    """ Flask decorator that allow to set Expire and Cache headers. """
    def fwrap(f):
        @wraps(f)
        def wrapped_f(*args, **kwargs):
            r = f(*args, **kwargs)
            then = datetime.now() + timedelta(minutes=minutes)
            rsp = Response(r, content_type=content_type)
            rsp.headers.add('Expires', then.strftime("%a, %d %b %Y %H:%M:%S GMT"))
            rsp.headers.add('Cache-Control', 'public,max-age=%d' % int(60 * minutes))
            return rsp
        return wrapped_f
    return fwrap

@REQUEST_API.route('/request/<string:_url>', methods=['GET'])
@docache(minutes=3, content_type='application/json')
def get_record_by_id(_url):
    """
    @param _url: the url
    @return: 200:  a flask/response object \
    with application/json mimetype.
    """
    #print("**********************")
    url = "https://"+_url+"/"
    #print(url)
    collect_dict = Url_link_checker(url_link=str(url))
    return json.dumps(collect_dict)
