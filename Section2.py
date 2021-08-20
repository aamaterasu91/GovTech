#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 20 18:41:58 2021

@author: chiaweijie
"""
'''
I tried using the docker image for Postgres in my MAC but I encountered some environment issue. The error is
'ERROR: column rel.relhasoids does not exist LINE 8: pg_get_userbyid(rel.relowner) AS relowner, rel.relhasoids,... '
I was not able to rectify it and I can't run any query. However I am still able to extract the DDL statements from pgadmin.
There will be a 1) fact transaction and a 2) dimension car table. Both of these two tables will be linked by
ID, which is a unique identifier for a type of car. 
'''

CREATE TABLE public."DIM_CAR"
(
    "ID" integer,
    "Manufacturer" character varying(50),
    "ModelName" character varying(50),
    "SerialNumber" character varying(50),
    "WeightKG" character varying(10),
    "Price" character varying(10),
    PRIMARY KEY ("ID")
)
WITH (
    OIDS = FALSE
);

ALTER TABLE public."DIM_CAR"
    OWNER to postgres;
    
    
CREATE TABLE public."FACT_SALES_TXN"
(
    "CustomerName" character varying(100),
    "CustomerPhone" character varying(20),
    "SalesPerson" character varying(100),
    "ID" integer,
    "Timestamp" timestamp without time zone,
    PRIMARY KEY ("SalesPerson", "Timestamp")
)
WITH (
    OIDS = FALSE
);

ALTER TABLE public."FACT_SALES_TXN"
    OWNER to postgres;  
    
'''
SQL below is done using MySQL. I already have mySQL in my laptop so this is a workaround.
Syntax may be different for postgres but the logic is the same.
Assumption: 
1) If a customer buy 2 identical cars at one go, there will be two transactions.
2) There can be scenario where all the manufacturers have same sales quantity. So how to choose top 3 etc
'''    
    
##I want to know the list of our customers and their spending.  
select customername,sum(price) from FACT_SALES_TXN a
inner join DIM_CAR b 
on a.id=b.id
group by customername;

##I want to find out the top 3 car manufacturers that customers bought by sales (quantity) and the sales number for it in the current month.
select a.id as CarID,b.manufacturer,count(b.id) as count,b.price*count(b.id) as salesnumber
from FACT_SALES_TXN a
inner join DIM_CAR b 
on a.id=b.id 
where month(a.timestamp)=month(now())
group by a.id,b.manufacturer
order by count(b.id) desc
LIMIT 3;

##DDL for mySQL if needed
CREATE TABLE `DIM_CAR` (
  `ID` int NOT NULL,
  `Manufacturer` varchar(45) DEFAULT NULL,
  `ModelName` varchar(45) DEFAULT NULL,
  `SerialNumber` varchar(45) DEFAULT NULL,
  `WeightKG` varchar(45) DEFAULT NULL,
  `Price` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

CREATE TABLE `FACT_SALES_TXN` (
  `CustomerName` varchar(45) DEFAULT NULL,
  `CustomerPhone` varchar(45) DEFAULT NULL,
  `SalesPerson` varchar(45) NOT NULL,
  `ID` int DEFAULT NULL,
  `Timestamp` TIMESTAMP NOT NULL,
  PRIMARY KEY (`SalesPerson`,`Timestamp`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

