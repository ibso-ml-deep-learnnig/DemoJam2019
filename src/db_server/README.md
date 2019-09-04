

Build a db_server image

    $ docker build -t db_server .
    

Run the image

    $ docker run -d -p 80051:80051 --link db:db db_server:latest
    

Start up a Admin tool

    $ docker run -d -p 8080:8080 --link db:db adminer:latest

