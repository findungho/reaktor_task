#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Module views.
# Description: Create routes for HTML views.
# Author : Dung Ho
# Email: fin.dungho@gmail.com


from flask import render_template, Blueprint
from application.instances.functions import (
    custome_pagination,
    data_jackets,
    data_shirts,
    data_accessories
)


# Create a Blueprint
html_view = Blueprint('html_view', __name__)


@html_view.route("/")
@html_view.route("/index")
@html_view.route("/home")
def index():
    return render_template("index.html", index=True)


@html_view.route('/products/jackets')
def jackets(product="Jackets"):
    """
    """
    pagination, pagination_items = custome_pagination(
        data_jackets
    )

    return render_template(
        'products.html',
        items=pagination_items,
        pagination=pagination,
        product=product,
        jackets=True
    )


@html_view.route('/products/shirts')
def shirts(product="Shirts"):
    """
    """
    pagination, pagination_items = custome_pagination(
        data_shirts
    )

    return render_template(
        'products.html',
        items=pagination_items,
        pagination=pagination,
        product=product,
        shirts=True
    )


@html_view.route('/products/accessories')
def accessories(product="Accessories"):
    """
    """
    pagination, pagination_items = custome_pagination(
        data_accessories
    )

    return render_template(
        'products.html',
        items=pagination_items,
        pagination=pagination,
        product=product,
        accessories=True
    )
