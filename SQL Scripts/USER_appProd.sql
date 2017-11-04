
CREATE USER 'pythonTest'@'rdstiagoaws.cteqiyblhicy.us-east-2.rds.amazonaws.com' IDENTIFIED BY 'pythonTest2017';

grant SELECT, INSERT, UPDATE, DELETE ON Vehicles.CARS TO pythonTest;

grant SELECT, INSERT, UPDATE, DELETE ON Vehicles.MOTORCYCLE TO pythonTest;


commit;