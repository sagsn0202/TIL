# Pandas

## Create, Load, Select

### DataFrame

#### Dictionary

column names: keys

column: a list of values

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

#### List

column names: `columns`

row: a list of lists

```python
df2 = pd.DataFrame([
    ['John Smith', '123 Main St.', 34],
    ['Jane Doe', '456 Maple Ave.', 28],
    ['Joe Schmo', '789 Broadway', 51]
    ],
    columns=['name', 'address', 'age'])
```

### CSV

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

### Inspect a DataFrame

If it's a small DataFrame, you can display it by typing `print(df)`.

If it's a larger DataFrame, you can inspect a few items without having to look at the entire DataFrame.(`print(df.head())`)

`.head()` gives the first 5 rows of a DataFrame.

`.info()` gives some statistics for each column.

### Select Columns

 `customers['age']` or `customers.age`

When we select a single column, the result is called a *Series*.

`<class 'pandas.core.series.Series'>`

#### Multiple Columns

`new_df = orders[['last_name', 'email']]`

Make sure that you have a double set of brackets (`[[]]`)

`<class 'pandas.core.frame.DataFrame'>`

### Select Rows

`orders.iloc[2]`

When we select a single row, the result is a *Series*.

`<class 'pandas.core.series.Series'>`

#### Multiple Rows

`orders.iloc[3:7]`

`<class 'pandas.core.frame.DataFrame'>`

### with Logic

1. `df[df.MyColumnName == desired_column_value]`
2. `df[(df.age < 30) | (df.name == 'Martha Jones')]`

`|` means "or" and `&` means "and".

3. `df[df.name.isin(['Martha Jones', 'Rose Tyler', 'Amy Pond'])]`

### Setting Indices

|      | First Name | Last Name |
| ---- | ---------- | --------- |
| 0    | John       | Smith     |
| 4    | Jane       | Doe       |
| 7    | Joe        | Schmo     |

`df.reset_index()`

|      | index | First Name | Last Name |
| ---- | ----- | ---------- | --------- |
| 0    | 0     | John       | Smith     |
| 1    | 4     | Jane       | Doe       |
| 2    | 7     | Joe        | Schmo     |

the old indices have been moved into a new column called `'index'`. 

`df.reset_index(drop=True)`

|      | First Name | Last Name |
| ---- | ---------- | --------- |
| 0    | John       | Smith     |
| 1    | Jane       | Doe       |
| 2    | Joe        | Schmo     |

`df.reset_index(inplace=True, drop=True)`

If we use the keyword `inplace=True` we can just modify our existing DataFrame.

## Modify

### Adding a Column

Add a column to an existing DataFrame.

`df['Quantity'] = [100, 150, 50, 35]`

| Product ID | Product Description | Cost to Manufacture | Price | Quantity |
| ---------- | ------------------- | ------------------- | ----- | -------- |
| 1          | 3 inch screw        | 0.50                | 0.75  | 100      |
| 2          | 2 inch nail         | 0.10                | 0.25  | 150      |
| 3          | hammer              | 3.00                | 5.50  | 50       |
| 4          | screwdriver         | 2.50                | 3.00  | 35       |

`df['In Stock?'] = True`

| Product ID | Product Description | Cost to Manufacture | Price | In Stock? |
| ---------- | ------------------- | ------------------- | ----- | --------- |
| 1          | 3 inch screw        | 0.50                | 0.75  | True      |
| 2          | 2 inch nail         | 0.10                | 0.25  | True      |
| 3          | hammer              | 3.00                | 5.50  | True      |
| 4          | screwdriver         | 2.50                | 3.00  | True      |

`df['Sales Tax'] = df.Price * 0.075`

| Product ID | Product Description | Cost to Manufacture | Price | Sales Tax |
| ---------- | ------------------- | ------------------- | ----- | --------- |
| 1          | 3 inch screw        | 0.50                | 0.75  | 0.06      |
| 2          | 2 inch nail         | 0.10                | 0.25  | 0.02      |
| 3          | hammer              | 3.00                | 5.50  | 0.41      |
| 4          | screwdriver         | 2.50                | 3.00  | 0.22      |

### Column Operations

`.apply()`

```python
from string import upper

df['Name'] = df.Name.apply(upper)
```

| Name       | Email                |
| ---------- | -------------------- |
| JOHN SMITH | john.smith@gmail.com |
| JANE DOE   | jdoe@yahoo.com       |
| JOE SCHMO  | joeschmo@hotmail.com |

### Lambda Function

```python
mylambda = lambda x: (x * 2) + 3
print(mylambda(5))
```

```python
stringlambda = lambda x: x.lower()
print(stringlambda("Oh Hi Mark!"))
```

```python
mylambda = lambda x: x[0] + x[-1]
mylambda('Hello')
```

#### If statements

```python
lambda x: [OUTCOME IF TRUE] \
    if [CONDITIONAL] \
    else [OUTCOME IF FALSE]
```

```python
mylambda = lambda x: 'Welcome to BattleCity!' if x >= 13 else 'You must be over 13'
```

### Applying a Lambda to a Column

| Name       | Email                |
| ---------- | -------------------- |
| JOHN SMITH | john.smith@gmail.com |
| Jane Doe   | jdoe@yahoo.com       |
| joe schmo  | joeschmo@hotmail.com |

`df['Email Provider'] = df.Email.apply(lambda x: x.split('@')[-1])`

| Name       | Email                | Email Provider |
| ---------- | -------------------- | -------------- |
| JOHN SMITH | john.smith@gmail.com | gmail.com      |
| Jane Doe   | jdoe@yahoo.com       | yahoo.com      |
| joe schmo  | joeschmo@hotmail.com | hotmail.com    |

### Applying a Lambda to a Row

If we use `apply` with the argument `axis=1`, the input to our lambda function will be an entire row. To access particular values of the row, we use the syntax `row.column_name` or `row[‘column_name’]`.

If `Is taxed?` is `Yes`, multiply `Price` by 1.075 (for 7.5% sales tax).

If `Is taxed?` is `No`,  `Price`without multiplying it.

```python
df['Price with Tax'] = df.apply(lambda row:
     row['Price'] * 1.075
     if row['Is taxed?'] == 'Yes'
     else row['Price'],
     axis=1
)
```

**axis=1**

### Renaming Columns

```python
df = pd.DataFrame({
    'name': ['John', 'Jane', 'Sue', 'Fred'],
    'age': [23, 29, 21, 18]
})
df.columns = ['First Name', 'Age']
```

```python
df = pd.DataFrame({
    'name': ['John', 'Jane', 'Sue', 'Fred'],
    'age': [23, 29, 21, 18]
})
df.rename(columns={
    'name': 'First Name',
    'age': 'Age'},
    inplace=True)
```

 Why `.rename`is preferable to `.columns`:

- You can rename just one column
- You can be specific about which column names are getting changed

If you misspell one of the original column names, it just won't change anything.

## Aggregate

### Column Statistics

`df.column_name.command()`

| Command   | Description                       |
| --------- | --------------------------------- |
| `mean`    | Average of all values in column   |
| `std`     | Standard deviation                |
| `median`  | Median                            |
| `max`     | Maximum value in column           |
| `min`     | Minimum value in column           |
| `count`   | Number of values in column        |
| `nunique` | Number of unique values in column |
| `unique`  | List of unique values in column   |

### Aggregate Functions

#### Groupby

`df.groupby('column1').column2.measurement()`

- `column1` is the column that we want to group by (`'student'` in our example)
- `column2` is the column that we want to perform a measurement on (`grade` in our example)
- `measurement` is the measurement function we want to apply (`mean` in our example)

`<class 'pandas.core.series.Series'>`

##### More than One Column

`df.groupby(['Location', 'Day of Week'])['Total Sales'].mean().reset_index()`

#### Reset Index(DataFrame)

`df.groupby('column1').column2.measurement().reset_index()`

* `reset_index()` will transform our Series into a DataFrame and move the indices into their own column

`df = df.rename(columns={"id": "count"})`

`<class 'pandas.core.frame.DataFrame'>`

#### Lambda

the input to our lambda function will always be a list of values

```python
# np.percentile can calculate any percentile over an array of values
high_earners = df.groupby('category').wage.apply(lambda x: np.percentile(x, 75)).reset_index()
```

### Pivot Tables

Reorganizing a table in this way is called **pivoting**. The new table is called a **pivot table**.

```python
df.pivot(columns='ColumnToPivot',
         index='ColumnToBeRows',
         values='ColumnToBeValues')
```

| Location     | Date       | Day of Week | Total Sales |
| ------------ | ---------- | ----------- | ----------- |
| West Village | February 1 | W           | 400         |
| West Village | February 2 | Th          | 450         |
| Chelsea      | February 1 | W           | 375         |
| Chelsea      | February 2 | Th          | 390         |

```python
# First use the groupby statement:
unpivoted = df.groupby(['Location', 'Day of Week'])['Total Sales'].mean().reset_index()
```

| Location     | Day of Week | Total Sales |
| ------------ | ----------- | ----------- |
| Chelsea      | M           | 300         |
| Chelsea      | Tu          | 310         |
| Chelsea      | W           | 320         |
| Chelsea      | Th          | 290         |
| ...          |             |             |
| West Village | Th          | 400         |
| West Village | F           | 390         |
| West Village | Sa          | 250         |
| ...          |             |             |

```python
# Now pivot the table
pivoted = unpivoted.pivot(
    columns='Day of Week',
    index='Location',
    values='Total Sales')
```

| Location     | M    | Tu   | W    | Th   | F    | Sa   | Su   |
| ------------ | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| Chelsea      | 400  | 390  | 250  | 275  | 300  | 150  | 175  |
| West Village | 300  | 310  | 350  | 400  | 390  | 250  | 200  |
| ...          |      |      |      |      |      |      |      |

```python
pivoted = unpivoted.pivot(
    columns='Day of Week',
    index='Location',
    values='Total Sales').reset_index()
```

