##### Author: Dung Ho
##### Email: fin.dungho@gmail.com
##### Phone number: +358 449865555


## Overview
_This is a simple web application which is used to fetch the products from the given APIs, and create the routes for display and APIs testing. The application was implemented by using Python Flask library._


## General
- The web application was implemented by using Python Flask library and RESTful protocol.
The application includes 3 product categories: jackets, shirts and accessories.


## Requirements
- Python 3.7 or above.
- Libraries: requirements.txt


## How to use
1. Install pipenv: 
	`pip install pipenv`

2. Install libraries:
    `pip install -r requirements.txt`

3. Run the application:
    `source venv/bin/activate`
    `flask run`

4. Testing:
    You can test in the FrontEnd part, or test by using Postman or cURL.
    + Front-End: navigate the URL on the web browser
        `http://127.0.0.1:5000/index`

    + Testing APIs:
        Example GET request:
		```
		curl --location --request GET 'http://127.0.0.1:5000/api/products/jackets'
		```
