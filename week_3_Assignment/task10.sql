-- Average Population : Query the average population for all cities in CITY, rounded down to the nearest integer.
SELECT COUNTRY.CONTINENT, FLOOR(AVG(CITY.POPULATION)) 
FROM 
COUNTRY JOIN CITY 
ON 
CITY.COUNTRYCODE = COUNTRY.CODE 
GROUP BY 
COUNTRY.CONTINENT ;
