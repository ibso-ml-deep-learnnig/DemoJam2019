

Build a db_server image

    $ docker build -t hme000/hme1:db_server .
    

Run the image

    $ docker run -d -p 8001:8001 --link db:db hme000/hme1:db_server
    

Start up a Admin tool

    $ docker run -d -p 8080:8080 --link db:db adminer:latest

