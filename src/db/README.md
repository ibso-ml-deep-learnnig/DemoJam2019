

Build a mysql image   

    $ docker build -t db .
    

Run the image

    $ docker run -d -p 80051:80051 --name db -e MYSQL_ROOT_PASSWORD=helloworld01 db:latest --default-authentication-plugin=mysql_native_password
    

Start up a Admin tool

    $ docker run -d -p 8080:8080 --link db:db adminer:latest

