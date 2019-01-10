# Pandas

## DataFrame

by **dict**

```python
df1 = pd.DataFrame({
    'name': ['John Smith', 'Jane Doe', 'Joe Schmo'],
    'address': ['123 Main St.', '456 Maple Ave.', '789 Broadway'],
    'age': [34, 28, 51]
})
```

Note that the columns will **appear in alphabetical order** because dictionaries don't have any inherent order for columns.

```python
df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
  'Color': ['blue', 'green', 'red', 'black']
})
```

by **list**

column : `columns`

row: a list of lists

```python
df2 = pd.DataFrame([
    ['John Smith', '123 Main St.', 34],
    ['Jane Doe', '456 Maple Ave.', 28],
    ['Joe Schmo', '789 Broadway', 51]
    ],
    columns=['name', 'address', 'age'])
```

## CSV

- Online datasets (here's an example from [data.gov](https://catalog.data.gov/dataset?res_format=CSV)
- Export from Excel or Google Sheets
- Export from SQL

```python
column1,column2,column3
value1,value2,value3
```

```python
pd.read_csv('my-csv-file.csv')
df.to_csv('new-csv-file.csv')
```

`.read_csv()`

`.to_csv()`

