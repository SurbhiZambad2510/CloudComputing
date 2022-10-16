This files contains example of terminal commands used to create the containers and run it


docker build -t my_db .


docker build -t my_dba .


docker run --name mydb -itd -p5432:5432 -d my_db 

docker network create mynetwork

docker run --name mydb --network mynetwork  -itd -p5432:5432 -d my_db 

docker run --name mydba --network mynetwork  -p 8081:80 -d my_dba

docker build -t my_django . 

docker run -it -p8000:8000 -v $(pwd)/app:/app my_django /bin/bash

django-admin startproject app

python manage.py runserver 0.0.0.0:8000

