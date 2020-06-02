CREATE TABLE Restrn(
	restrn_id int PRIMARY KEY,
	name varchar(25),
	counrtry_id int,
	personal_id int,
	menu_id int
);

CREATE TABLE Personal(
    id int PRIMARY KEY,
    name VARCHAR(30),
    posada VARCHAR(30),
    restrn_id int REFERENCES Restrn(restrn_id)
);

CREATE TABLE Country(
    country_id int PRIMARY KEY,
    name varchar(30)
);

CREATE TABLE Town(
    id int PRIMARY KEY,
    name varchar(40),
    counrty_id int REFERENCES Country(country_id)
);

CREATE TABLE RestrnCountry(
    Restrn_id int,
    Counrty_id int,
    FOREIGN KEY (Restrn_id) REFERENCES Restrn(restrn_id),
    FOREIGN KEY (Counrty_id) REFERENCES Counrty(country_id),
    UNIQUE (restrn_id, country_id)
);

CREATE TABLE Menu(
    menu_id int PRIMARY KEY,
    name VARCHAR(20),
    start date,
    finish date
);

CREATE TABLE RestrnMenu(
    Restrn_id int,
    Menu_id int,
    FOREIGN KEY (Restrn_id) REFERENCES Restrn(restrn_id),
    FOREIGN KEY (Menu_id) REFERENCES Menu(menu_id),
    UNIQUE (restrn_id, menu_id)
);

CREATE TABLE Soop(
    id int PRIMARY KEY,
    name VARCHAR(20),
    ingrid VARCHAR(100),
    menu_id int REFERENCES Menu(menu_id)
);