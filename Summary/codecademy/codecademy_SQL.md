# SQL

**S**tructured **Q**uery **L**anguage

* Relational Database Management System

  https://www.codecademy.com/articles/what-is-rdbms-sql

## COMMANDS 

### ALTER TABLE

```sql
ALTER TABLE table_name 
ADD column_name datatype;
```

`ALTER TABLE` lets you add columns to a table in a database.

### AND

```sql
SELECT column_name(s)
FROM table_name
WHERE column_1 = value_1
  AND column_2 = value_2;
```

`AND` is an operator that combines two conditions. Both conditions must be true for the row to be included in the result set.

### AS

```sql
SELECT column_name AS 'Alias'
FROM table_name;
```

`AS` is a keyword in SQL that allows you to rename a column or table using an *alias*.

### AVG()

```sql
SELECT AVG(column_name)
FROM table_name;
```

`AVG()` is an aggregate function that returns the average value for a numeric column.

### BETWEEN

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name BETWEEN value_1 AND value_2;
```

The `BETWEEN` operator is used to filter the result set within a certain range. The values can be numbers, text or dates.

### CASE

```sql
SELECT column_name,
  CASE
    WHEN condition THEN 'Result_1'
    WHEN condition THEN 'Result_2'
    ELSE 'Result_3'
  END
FROM table_name;
```

`CASE` statements are used to create different outputs (usually in the `SELECT` statement). It is SQL's way of handling if-then logic.

### COUNT()

```sql
SELECT COUNT(column_name)
FROM table_name;
```

`COUNT()` is a function that takes the name of a column as an argument and counts the number of rows where the column is not `NULL`.

### CREATE TABLE

```sql
CREATE TABLE table_name (
  column_1 datatype, 
  column_2 datatype, 
  column_3 datatype
);
```

`CREATE TABLE` creates a new table in the database. It allows you to specify the name of the table and the name of each column in the table.

### DELETE

```sql
DELETE FROM table_name
WHERE some_column = some_value;
```

`DELETE` statements are used to remove rows from a table.

### GROUP BY

```sql
SELECT column_name, COUNT(*)
FROM table_name
GROUP BY column_name;
```

`GROUP BY` is a clause in SQL that is only used with aggregate functions. It is used in collaboration with the `SELECT` statement to arrange identical data into groups.

### HAVING

```sql
SELECT column_name, COUNT(*)
FROM table_name
GROUP BY column_name
HAVING COUNT(*) > value;
```

`HAVING` was added to SQL because the `WHERE` keyword could not be used with aggregate functions.

### INNER JOIN

```sql
SELECT column_name(s)
FROM table_1
JOIN table_2
  ON table_1.column_name = table_2.column_name;
```

An inner join will combine rows from different tables if the *join condition* is true.

### INSERT

```sql
INSERT INTO table_name (column_1, column_2, column_3) 
VALUES (value_1, 'value_2', value_3);
```

`INSERT` statements are used to add a new row to a table.

### IS NULL / IS NOT NULL

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name IS NULL;
```

`IS NULL` and `IS NOT NULL` are operators used with the `WHERE` clause to test for empty values.

### LIKE

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name LIKE pattern;
```

`LIKE` is a special operator used with the `WHERE` clause to search for a specific pattern in a column.

### LIMIT

```sql
SELECT column_name(s)
FROM table_name
LIMIT number;
```

`LIMIT` is a clause that lets you specify the maximum number of rows the result set will have.

### MAX()

```sql
SELECT MAX(column_name)
FROM table_name;
```

`MAX()` is a function that takes the name of a column as an argument and returns the largest value in that column.

### MIN()

```sql
SELECT MIN(column_name)
FROM table_name;
```

`MIN()` is a function that takes the name of a column as an argument and returns the smallest value in that column.

### OR

```sql
SELECT column_name
FROM table_name
WHERE column_name = value_1
   OR column_name = value_2;
```

`OR` is an operator that filters the result set to only include rows where either condition is true.

### ORDER BY

```sql
SELECT column_name
FROM table_name
ORDER BY column_name ASC | DESC;
```

`ORDER BY` is a clause that indicates you want to sort the result set by a particular column either alphabetically or numerically.

### OUTER JOIN

```sql
SELECT column_name(s)
FROM table_1
LEFT JOIN table_2
  ON table_1.column_name = table_2.column_name;
```

An outer join will combine rows from different tables even if the join condition is not met. Every row in the *left* table is returned in the result set, and if the join condition is not met, then `NULL` values are used to fill in the columns from the *right* table.

### ROUND()

```sql
SELECT ROUND(column_name, integer)
FROM table_name;
```

`ROUND()` is a function that takes a column name and an integer as an argument. It rounds the values in the column to the number of decimal places specified by the integer.

### SELECT

```sql
SELECT column_name 
FROM table_name;
```

`SELECT` statements are used to fetch data from a database. Every query will begin with SELECT.

### SELECT DISTINCT

```sql
SELECT DISTINCT column_name
FROM table_name;
```

`SELECT DISTINCT` specifies that the statement is going to be a query that returns unique values in the specified column(s).

### SUM

```sql
SELECT SUM(column_name)
FROM table_name;
```

`SUM()` is a function that takes the name of a column as an argument and returns the sum of all the values in that column.

### UPDATE

```sql
UPDATE table_name
SET some_column = some_value
WHERE some_column = some_value;
```

`UPDATE` statements allow you to edit rows in a table.

### WHERE

```sql
SELECT column_name(s)
FROM table_name
WHERE column_name operator value;
```

`WHERE` is a clause that indicates you want to filter the result set to include only rows where the following *condition* is true.

### WITH

```sql
WITH temporary_name AS (
   SELECT *
   FROM table_name)
SELECT *
FROM temporary_name
WHERE column_name operator value;
```

`WITH` clause lets you store the result of a query in a temporary table using an alias. You can also define multiple temporary tables using a comma and with one instance of the `WITH` keyword.

The `WITH` clause is also known as common table expression (CTE) and subquery factoring.

## Manipulation

### Relation Databases

* A *relational database* is a database that organizes information into one or more tables. Here, the relational database contains one table. 

Some of the most common data types are:

- `INTEGER`, a positive or negative whole number
- `TEXT`, a text string
- `DATE`, the date formatted as YYYY-MM-DD for the year, month, and day
- `REAL`, a decimal value

### Statements

Statements always end in a semicolon `;`.

1. `CREATE TABLE` is a *clause*. By convention, clauses are written in capital letters. Clauses can also be referred to as commands.
2. `table_name` refers to the name of the table that the command is applied to.
3. `(column_1 data_type, column_2 data_type, column_3 data_type)` is a *parameter*. A parameter is a list of columns, data types, or values that are passed to a clause as an argument.

### Create

database scheme: 구조와 제약 조건

```sql
CREATE TABLE celebs (
   id INTEGER, 
   name TEXT, 
   age INTEGER
);
```

- `id` is the first column in the table. It stores values of data type `INTEGER`
- `name` is the second column in the table. It stores values of data type `TEXT`
- `age` is the third column in the table. It stores values of data type `INTEGER`

### Insert

The `INSERT` statement inserts a new row into a table.

```sql
INSERT INTO celebs (id, name, age) 
VALUES (1, 'Justin Bieber', 22);
```

### Select

`SELECT` statements are used to fetch data from a database.

`SELECT` statements always return a new table called the *result set*.

```sql
SELECT * FROM celebs;
```

```sql
SELECT name FROM celebs;
```

```sql
SELECT COUNT(*) FROM users;
SELECT AVG(<col>) FROM <table_name>;
SELECT SUM(<col>) FROM <table_name>;
SELECT MIN(<col>) FROM <table_name>;
SELECT MAX(<col>) FROM <table_name>;
```

### Alter

The `ALTER TABLE` statement adds a **new column** to a table. 

```sql
ALTER TABLE celebs 
ADD COLUMN twitter_handle TEXT;

ALTER TABLE table_name
ADD COLUMN column_name DATA_TYPE;
```

```sql
AlTER TABLE user RENAME TO users;
```

### Update

The `UPDATE` statement edits a row in a table.

```sql
UPDATE celebs 
SET twitter_handle = '@taylorswift13' 
WHERE id = 4;
```

### Delete

The `DELETE FROM` statement deletes one or more rows from a table.

```sql
DELETE FROM celebs 
WHERE twitter_handle IS NULL;
```

### Constraints

*Constraints* be used to tell the database to reject inserted data that does not adhere to a certain restriction.

```sql
CREATE TABLE celebs (
   id INTEGER PRIMARY KEY, 
   name TEXT UNIQUE,
   date_of_birth TEXT NOT NULL,
   date_of_death TEXT DEFAULT 'Not Applicable'
);
```

1. `PRIMARY KEY` columns can be used to uniquely identify the row. 

   Attempts to insert a row with an identical value to a row already in the table will result in a *constraint violation* which will not allow you to insert the new row.

2. `UNIQUE` columns have a different value for every row. 

   This is similar to `PRIMARY KEY` except a table can have many different `UNIQUE` columns.

3. `NOT NULL` columns must have a value. 

   Attempts to insert a row without a value for a `NOT NULL` column will result in a constraint violation and the new row will not be inserted.

4. `DEFAULT` columns take an additional argument that will be the assumed value for an inserted row if the new row does not specify a value for that column.

### Summary

- `CREATE TABLE` creates a new table.
- `INSERT INTO` adds a new row to a table.
- `SELECT` queries data from a table.
- `ALTER TABLE` changes an existing table.
- `UPDATE` edits a row in a table.
- `DELETE FROM` deletes rows from a table.

## Queries

### As

```sql
SELECT column AS 'Nickname' 
FROM table_name;
```

### Distinct

`DISTINCT` is used to return unique values in the output. 

```sql
SELECT DISTINCT genre 
FROM movies;
```

### Where

```sql
SELECT *
FROM movies
WHERE imdb_rating > 8;
```

### Like(Pattern)

```sql
SELECT * FROM <table_name>
WHERE <col> LIKE '<pattern>'
```

| 시작 | 예시    | 설명                    |
| ---- | ------- | ----------------------- |
| `%`  | `2%`    | 2로 시작하는 값         |
|      | `%2`    | 2로 끝나는 값           |
|      | `%2%`   | 2가 들어가는 값         |
| `_`  | `_2`    | 두번째 글자가 2인 값    |
|      | `1___`  | 1로 시작하며 4자리      |
|      | `2_%_%` | 2로 시작하며 최소 3자리 |

### Null

- `IS NULL`
- `IS NOT NULL`

```sql
SELECT name
FROM movies 
WHERE imdb_rating IS NOT NULL;
```

### Between

```sql
SELECT *
FROM movies
WHERE name BETWEEN 'A' AND 'J';
```

```sql
SELECT *
FROM movies
WHERE year BETWEEN 1990 AND 1999;
```

### And

```sql
SELECT * 
FROM movies
WHERE year BETWEEN 1990 AND 1999
   AND genre = 'romance';
```

### Or

```sql
SELECT *
FROM movies
WHERE year > 2014
   OR genre = 'action';
```

### Order by

```sql
SELECT * FROM users ORDER BY age, last_name ASC LIMIT 10;
```

`ASC`: 오름차순

`DESC`: 내림차순

### Limit

```sql
SELECT <col> FROM <table_name>
LIMIT <num>
```

### Case

It is SQL's way of handling [if-then](https://en.wikipedia.org/wiki/Conditional_(computer_programming)) logic.

```sql
SELECT name,
 CASE
  WHEN imdb_rating > 8 THEN 'Fantastic'
  WHEN imdb_rating > 6 THEN 'Poorly Received'
  ELSE 'Avoid at All Costs'
 END AS 'Review'
FROM movies;
```

```sql
SELECT , CASE WHEN THEN END AS 
```

### Summary

- `SELECT` is the clause we use every time we want to query information from a database.
- `AS` renames a column or table.
- `DISTINCT` return unique values.
- `WHERE` is a popular command that lets you filter the results of the query based on conditions that you specify.
- `LIKE` and `BETWEEN` are special operators.
- `AND` and `OR` combines multiple conditions.
- `ORDER BY` sorts the result.
- `LIMIT` specifies the maximum number of rows that the query will return.
- `CASE` creates different outputs.

## Aggregate

### Count

how many rows are in a table 

```sql
SELECT COUNT(*)
FROM table_name;
```

### Sum

 add all values in a particular column 

```sql
SELECT SUM(downloads)
FROM fake_apps;
```

### Max / Min

the highest and lowest values in a column, respectively

```sql
SELECT MIN(downloads)
FROM fake_apps;
```

### Average

calculate the average value of a particular column

```sql
SELECT AVG(downloads)
FROM fake_apps;
```

### Round

`ROUND()` function takes two arguments inside the parenthesis:

1. a column name
2. an integer

```sql
SELECT name, ROUND(price, 0)
FROM fake_apps;
```

```sql
SELECT ROUND(AVG(price), 2)
FROM fake_apps;
```

### Group by

`GROUP BY` is a clause in SQL that is used with aggregate functions. It is used in collaboration with the `SELECT` statement to arrange identical data into *groups*.

The `GROUP BY` statement comes after any `WHERE` statements, but before `ORDER BY` or `LIMIT`.

```sql
SELECT price, COUNT(*) 
FROM fake_apps
WHERE downloads > 20000
GROUP BY price;
```

```sql
SELECT year,
   AVG(imdb_rating)
FROM movies
GROUP BY year
ORDER BY year;
```

- `1` is the first column selected
- `2` is the second column selected
- `3` is the third column selected

```sql
SELECT category, price, AVG(downloads)
FROM fake_apps
GROUP BY 1, 2;
```

### Having

we want to *filter groups*. This is where `HAVING` comes in.

all types of `WHERE` clauses you learned about thus far can be used with `HAVING`.

```sql
SELECT year, genre, COUNT(name)
FROM movies
GROUP BY 1, 2
HAVING COUNT(name) > 10;
```

### Summary

- `COUNT()`: count the number of rows
- `SUM()`: the sum of the values in a column
- `MAX()`/`MIN()`: the largest/smallest value
- `AVG()`: the average of the values in a column
- `ROUND()`: round the values in the column

- `GROUP BY` is a clause used with aggregate functions to combine data from one or more columns.
- `HAVING` limit the results of a query based on an aggregate property.