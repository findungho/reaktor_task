#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Module api.
# Description: Create routes for APIs testing.
# Author : Dung Ho
# Email: fin.dungho@gmail.com


from flask import (
    Blueprint,
    make_response,
    jsonify
)
from application.instances.functions import (
    data_jackets,
    data_shirts,
    data_accessories
)


# Create a Blueprint
api_test = Blueprint('api_test', __name__)


@api_test.route('/api/products/jackets')
def jackets_respone():

    return make_response(
        jsonify(data_jackets),
        200
    )


@api_test.route('/api/products/shirts')
def shirts_respone():

    return make_response(
        jsonify(data_shirts),
        200
    )


@api_test.route('/api/products/accessories')
def accessories_respone():

    return make_response(
        jsonify(data_accessories),
        200
    )
