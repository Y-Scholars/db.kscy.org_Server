# -*- coding: utf-8 -*-
from flask_api import status
from flask_restful import Resource

from app.config import ENVIRONMENT, API_VERSION, APP_VERSION
from app.modules import yscholars


_URL = '/'


class Index(Resource):
    """
    @api {get} / Get API Information
    @apiName API Info
    @apiGroup Info

    @apiSuccess (200) {String} environment Environment
    @apiSuccess (200) {String} api API_VERSION
    @apiSuccess (200) {String} app APP_VERSION

    """
    @yscholars.API
    def get(self):
        _return = {
            'environment': ENVIRONMENT,
            'version': {
                'api': API_VERSION,
                'app': APP_VERSION
            }
        }

        return _return, status.HTTP_200_OK
