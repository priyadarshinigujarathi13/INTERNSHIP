P-- MySQL Shell 9.7.0

-- Copyright (c) 2016, 2026, Oracle and/or its affiliates.
-- Oracle is a registered trademark of Oracle Corporation and/or its affiliates.
-- Other names may be trademarks of their respective owners.

-- Type '\help' or '\?' for help; '\quit' to exit.
--  MySQL  SQL > \sql
--  MySQL  SQL > \c root@localhost
-- Creating a session to 'root@localhost'
-- Please provide the password for 'root@localhost': ***********
-- MySQL Error 2003 (HY000): Can't connect to MySQL server on 'localhost:3306' (10061)
--  MySQL  SQL > \c darshini
-- Creating a session to 'priya@darshini'
-- Please provide the password for 'priya@darshini': **************
-- MySQL Error 1045 (28000): Access denied for user 'priya'@'Darshini' (using password: YES)
--  MySQL  SQL > \c root@localhost
-- Creating a session to 'root@localhost'
-- Please provide the password for 'root@localhost': **************
-- Save password for 'root@localhost'? [Y]es/[N]o/Ne[v]er (default No): show databases
-- Please pick an option out of [Y]es/[N]o/Ne[v]er (default No): Save payesord for 'root@localhost'? [Y]es/[N]o/Ne[v]er (default No): yes
-- Fetching global names for auto-completion... Press ^C to stop.
-- Your MySQL connection id is 13
-- Server version: 8.0.46 MySQL Community Server - GPL
-- No default schema selected; type \use <schema> to set one.
 show databases;
-- +--------------------+
-- | Database           |
-- +--------------------+
-- | information_schema |
-- | mysql              |
-- | performance_schema |
-- | sys                |
-- +--------------------+
-- 4 rows in set (0.0016 sec)
--  MySQL  localhost:3306 ssl  SQL > create database company;
-- Query OK, 1 row affected (0.0345 sec)
--  MySQL  localhost:3306 ssl  SQL > use company;
-- Default schema set to `company`.
-- Fetching global names, object names from `company` for auto-completion... Press ^C to stop.
 create table emloyee(e_id int primary ker,e_name varchar(20),salary decimal(20,30));
-- ERROR: 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'ker,e_name varchar(20),salary decimal(20,30))' at line 1
--  MySQL  localhost:3306 ssl  company  SQL > create table emloyee(e_id int primary ker,e_name varchar(20),salary bigint);
-- ERROR: 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'ker,e_name varchar(20),salary bigint)' at line 1
--  MySQL  localhost:3306 ssl  company  SQL > insert into employee values(1,'darsh',50000),(2,'priya',60000);
-- ERROR: 1146 (42S02): Table 'company.employee' doesn't exist
--  MySQL  localhost:3306 ssl  company  SQL > insert into emloyee values(1,'darsh',50000),(2,'priya',60000);
-- ERROR: 1146 (42S02): Table 'company.emloyee' doesn't exist
--  MySQL  localhost:3306 ssl  company  SQL > insert into emloyee values(1,'darsh',50000),(2,'priya',60000),(3,'jai',70000);
-- ERROR: 1146 (42S02): Table 'company.emloyee' doesn't exist
 create table employee(e_id int primary key,e_name varchar(20),salary bigint);
-- Query OK, 0 rows affected (0.0563 sec)
 insert into employee values(1,'darsh',50000),(2,'priya',60000),(3,'jai',70000);
-- Query OK, 3 rows affected (0.0448 sec)

-- Records: 3  Duplicates: 0  Warnings: 
 select * from employee;
-- +------+--------+--------+
-- | e_id | e_name | salary |
-- +------+--------+--------+
-- |    1 | darsh  |  50000 |
-- |    2 | priya  |  60000 |
-- |    3 | jai    |  70000 |
-- +------+--------+--------+
-- 3 rows in set (0.0006 sec)
 select count(*) as total_employees from employee;
-- +-----------------+
-- | total_employees |
-- +-----------------+
-- |               3 |
-- +-----------------+
-- 1 row in set (0.0031 sec)
 select avg(salary) as average_salary from employee;
-- +----------------+
-- | average_salary |
-- +----------------+
-- |     60000.0000 |
-- +----------------+
-- 1 row in set (0.0012 sec)
 select max(salary) as highest_salary,min(salary) as lowest_salary from employee;
-- +----------------+---------------+
-- | highest_salary | lowest_salary |
-- +----------------+---------------+
-- |          70000 |         50000 |
-- +----------------+---------------+
-- 1 row in set (0.0013 sec)
 select sum(salary) as total_salary from employee;
-- +--------------+
-- | total_salary |
-- +--------------+
-- |       180000 |
-- +--------------+
-- 1 row in set (0.0011 sec)
-- --  MySQL  localhost:3306 ssl  company  SQL >