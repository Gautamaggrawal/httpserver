# [HTTP SERVER]

***Without any Framework***
---

# Overview

A Http Server in Python that is used to host 5 REST APIs (CREATE, UPDATE, VIEW, DELETE, LIST)

# Requirements

* Python (2.7)
* BaseHTTPServer (Python 2) / http.server (Python 3)

# Usage:

Let's take a look at a quick example of Http sever using CURL 

Starting Server...

    python httpserver.py

PUT example using curl:
    
    curl -X PUT http://localhost:8080/api/put/1 -d 'string1' -H "Content-Type: application/json 

GET using curl:
    
    curl -X GET http://localhost:8080/api/get/1 -H "Content-Type: application/json

LIST using curl:
    
    curl -X GET http://localhost:8080/api/list/ -H "Content-Type: application/json

DELETE using curl:
    
    curl -X DELETE http://localhost:8080/api/delete/1 -H "Content-Type: application/json



[security-mail]: mailto:gautamaggrawalsd@yahoo.in
