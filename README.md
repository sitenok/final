Implementing a Service with RESTful APIs
===========================
Using RESTful APIs to provide a buyer-product service.
User may add a BUYER_NAME, a PRODUCT, make a PURCHASE and check PURCHASE HISTORY.
POST, GET, DELETE methods implemented with Python and saved in JSON format.



Environment
===========
Docker 20.10.16
Python 3.8.10


Usage
=====
The Dockerfile builds an image which will launch the RESTful APIs 

In terminal run the following **commands**:
-------------------------------------------

(check for any updates)
1. ``sudo apt-get update``

(install Docker Engine)

2. ``sudo apt-get install docker-ce docker-ce-cli containerd.io docker-compose-plugin``
  
3. ``docker build --file Dockerfile -t ANYTAG .``

4. ``docker run -d -p 8080:8080 ANYTAG:latest``


Add a new variable:
--------------------

5. ``curl -X POST “http://localhost:8080/numbers?new=(\any integer)”``


The following can be used with this RESTful API service:
-----------------------------------------------------------------

6. ``curl -X GET “http://localhost:8080/buyers”``

7. ``curl -X GET “http://localhost:8080/product”``

8. ``curl -X POST “http://localhost:8080/buyers?name=BUYER_NAME”``

9. ``curl -X POST “http://localhost:8080/products?name=PRODUCT_NAME”``

10. ``curl -X POST “http://localhost:8080/buyers?prod_name=PRODUCT_NAME”``

11. ``curl -X GET “http://localhost:8080/buyers/BUYER_NAME/purchased”``
