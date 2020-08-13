

CREATE TABLE person
(
    id integer primary key,
name varchar (255),
family varchar (255)
); 




CREATE TABLE car
(
    id integer primary key,
personid integer,
cartype varchar (255),
color varchar (255)
); 




CREATE TABLE house
(
    id integer primary key,
personid integer,
price numeric (15,5),
rooms integer,
inches numeric (15,5)
); 


