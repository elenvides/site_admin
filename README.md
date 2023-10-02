# Run with docker (local):

clone repo

add .env file (if you need)

run:

`docker-compose up -d --build`

swagger:

http://127.0.0.1:8009/docs/

admin part: 

http://127.0.0.1:8009/admin/

you should create superuser, and then modify new users, 
because only admin and manager can do more than "GET" with products.
