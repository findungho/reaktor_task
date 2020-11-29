#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Module function.
# Description: Fetching products data and check the availabilities.
# Author : Dung Ho
# Email: fin.dungho@gmail.com


import re
import requests
import asyncio
import requests_async
from operator import iconcat
from functools import reduce, partial
from collections import defaultdict
from application.instances.variables import base_uri, headers
from flask_paginate import Pagination, get_page_args


def custome_pagination(data):
    """
    Function returns a custome pagination and pagination items
    which is display 10 items per page.

    :param data: the input stream data.

    :return: pagination and pagination_items.
    """
    page, per_page, offset = get_page_args(
        page_parameter='page',
        per_page_parameter='per_page'
    )

    pagination_items = data[offset: offset + per_page]

    pagination = Pagination(
        page=page,
        per_page=per_page,
        total=len(data),
        css_framework='bootstrap4',
    )

    return pagination, pagination_items


def check_availability(acc, item):
    """
    This function is used as an argument for reduce function.

    :param acc: accummulater as a dictionary.
    :param item: the given item used to check availability.

    :return a dictionary
    """
    pattern = ">(.*?)<"
    try:
        if item['id']:
            availability = re.search(pattern, item['DATAPAYLOAD'])
            acc[item['id']] = availability.group(1)

    except TypeError:
        pass

    return acc


def extract_item(item, availabilities):
    """
    Re-structure data from the given item.

    :param item: the given item that used to extract information.
    :availabilities: optional argument.

    :return a dictionary of a single product.
    """
    return {
        'id': item['id'],
        'name': item['name'],
        'color': item['color'],
        'price': item['price'],
        'manufacturer': item['manufacturer'],
        'availability': availabilities.get(item['id'].upper())
    }


def fetch_products(base_uri, product_name):
    """
    Fetching the products from the given APIs that based on the
    product name.

    :param base_uri: the base URI used to fetching.
    :param product_name: the type of product

    :return: a list of products.
    """
    async def get_availabilities(urls):
        """
        Async function returns a dictionary of the product's availibilities.

        :param urls: the given list of URLs.

        :return a dictionary of the availabilites
        """
        tasks = []
        for url in urls:
            task = asyncio.create_task(requests_async.get(url))
            tasks.append(task)

        responses = await asyncio.gather(*tasks)

        response_json = [response.json()['response'] for response in responses]

        total_availabilities = reduce(iconcat, response_json, [])

        availabilities = reduce(
            check_availability,
            total_availabilities,
            defaultdict(list)
        )

        return availabilities

    # Fetching product data
    data_products = requests.get(
        f'{base_uri}/products/{product_name}',
        headers=headers
    ).json()

    # List of manufacturers
    manufacturers = set(item['manufacturer'] for item in data_products)

    # List of product availabilities URLs
    urls = [f'{base_uri}/availability/{i}' for i in manufacturers]

    # The total availabilities of all products that based on the manufacturers.
    products_availabilities = asyncio.run(get_availabilities(urls))

    # Adding optional argument for using 'map' function
    extract_completed_item = partial(
        extract_item,
        availabilities=products_availabilities
    )

    # Sorted data by item's name
    sorted_data = sorted(data_products, key=lambda x: x['name'])

    return list(map(extract_completed_item, sorted_data))


data_jackets = fetch_products(base_uri, 'jackets')
data_shirts = fetch_products(base_uri, 'shirts')
data_accessories = fetch_products(base_uri, 'accessories')
