create table Vehicles.CARS (Identification varchar(100) not null, Model varchar(100), Automaker varchar(100), Year int);

ALTER TABLE Vehicles.CARS ADD CONSTRAINT PK_CARS PRIMARY KEY (Identification);


create table Vehicles.MOTORCYCLE (Identification varchar(100) not null, Model varchar(100), Automaker varchar(100), Year int);

ALTER TABLE Vehicles.MOTORCYCLE ADD CONSTRAINT PK_MOTORCYCLE PRIMARY KEY (Identification);
