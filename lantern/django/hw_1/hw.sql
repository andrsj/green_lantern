CREATE TABLE Restaurant(
	id int PRIMARY KEY,
	name varchar(25),
	counrtry_id int,
	personal_id int,
	menu_id int
);

CREATE TABLE Personal(
    id int PRIMARY KEY,
    name VARCHAR(30),
    posada VARCHAR(30),
    restaurant_id int REFERENCES Restaurant(id)
);

CREATE TABLE Country(
    id int PRIMARY KEY,
    name varchar(30)
);

CREATE TABLE Town(
    id int PRIMARY KEY,
    name varchar(40),
    counrty_id int REFERENCES Country(id)
);

CREATE TABLE RestaurantCountry(
    restaurant_id int,
    country_id int,
    FOREIGN KEY (restaurant_id) REFERENCES Restaurant(id),
    FOREIGN KEY (country_id) REFERENCES Country(id),
    UNIQUE (restaurant_id, country_id)
);

CREATE TABLE Menu(
    id int PRIMARY KEY,
    name VARCHAR(20),
    start date,
    finish date
);

CREATE TABLE RestaurantMenu(
    restaurant_id int,
    menu_id int,
    FOREIGN KEY (restaurant_id) REFERENCES Restaurant(id),
    FOREIGN KEY (menu_id) REFERENCES Menu(id),
    UNIQUE (restaurant_id, menu_id)
);

CREATE TABLE Soop(
    id int PRIMARY KEY,
    name VARCHAR(20),
    ingredient VARCHAR(100),
    menu_id int REFERENCES Menu(id)
);