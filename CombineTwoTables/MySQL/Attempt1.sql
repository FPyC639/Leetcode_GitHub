Select firstName, lastName, city, state
From Person 
Left Join Address
ON Person.personId = Address.personID;