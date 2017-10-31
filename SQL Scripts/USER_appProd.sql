
CREATE USER 'appProd'@'tiagoawsmysql.cteqiyblhicy.us-east-2.rds.amazonaws.com' IDENTIFIED BY 'appProd2017';

grant SELECT, INSERT, UPDATE, DELETE ON Vehicles.CARS TO appProd;

grant SELECT, INSERT, UPDATE, DELETE ON Vehicles.MOTORCYCLE TO appProd;