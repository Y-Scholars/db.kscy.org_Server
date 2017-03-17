# -*- coding: utf-8 -*-
from flask import request
from flask_api import status
from flask_restful import Resource

from app import token_auth
from app.modules import yscholars
from app.models.user_token_model import token_expire_with_token

_URL = '/logout'


class Logout(Resource):
    """
    @api {post} /logout Logout
    @apiName Logout
    @apiGroup Auth

    @apiHeader {String} Authorization Access token.
    @apiHeaderExample {json} Header-Example:
      {
        "Authorization": "304924"
      }

    """
    @yscholars.API
    @token_auth.login_required
    def post(self):
        token = request.headers['Authorization'].split()[1]
        token_expire_with_token(token)

        return None, status.HTTP_200_OK
