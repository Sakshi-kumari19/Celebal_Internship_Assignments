-- Weather Observation Station 5 : Query the two cities in STATION with the shortest and longest CITY names, as well as their respective lengths
SELECT CITY, LENGTH(CITY) FROM STATION ORDER BY LENGTH(CITY),CITY LIMIT 1;
SELECT CITY, LENGTH(CITY) FROM STATION WHERE LENGTH(CITY)= (SELECT MAX(LENGTH(CITY)) FROM STATION) ORDER BY CITY LIMIT 1;
