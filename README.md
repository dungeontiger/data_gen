# data_gen
A tool to generate data for use in testing, demos and machine learning training.

# This is an early work in progress

valueExpression can be any python expression.
You have access to all methods of the random module
You also have the following predefined functions:
    column(name) gets the value of the named column for the current row
    the order matters, columns can only reference columns defined before it
    that means there is no dependency analysis, its very simple


There are various types of columns
- measures
- dates
- categories
- identifiers (keys)

Dates are treated as YYYY-MM-DD for simplicity, which is the ISO format anyway

Can repeat rows per sequential date to simulation multiple orders on the same day for example.

Rows on the table are really a row limit.  If another column, like a sequential date says its done
generation stops.

categories are going to be complicated....

Trends are applied to valueExpression columns
They need to reference a seqential date column since this is a trend over time

trends
Apply an accumulation amount based on a date column
- trends are applied each day, so if they are given montly or yearly they are broken down to days
- its an approximation so monthly amounts divided by 30 days and yearly 365 days
- quarterly is divided by (365/4)
- multiple trends can be specified, if they are they are additive "daily, monthly, etc"
- trends are expressed as a factor like a percentage.  if the daily trend is 0.1, values will increase by 10% each day
- trends are expressed as strings since they are themselves expressions to allow for randomness
- the expressions are evaluated each day
- so if the daily trend is between 0.1 and 0.2, a new trend value is calculated each day
- the trend is per day, so it will not be applied to multiple rows for the same day

best practise is to generate your dimension tables first, then use a foreign key
for example, generate a bunch of random geography places first,
then reference them with a choice from your fact table

geography is built in.
You can ask for a list of continents, you can ask for a random one or not and you can stipulate unique or not
When all you ask for unquie, using all unique values is a stop condition
This helps to create a dimension table

You can specifiy the values for columns.  By default each row will choice a random value from this list.
However, if you want to use all these values, use random:False and you will be given each value in order.  It will stop when out of values.  This is a good way to make a dimension table.

Sequential integers can be created by setting startInt and endInt.  Once endInt is reached generation will stop, unless loop is set to true.  In this case it will go back to the beginning.
You can use this to create string keys by also setting the prefix.

You can generate random people's names by setting 'personName' to first, last or full

get_value gets a value from a column, you have to specifiy the column's name.  If you do not specify the table name, it defaults to the same table.  This makes it easy to get the current value from a another column in the same table.

If you specify a table name, it will look for the column in that table and get its last value.

You can also specify random_value = True to get a random value.  This is useful when creating foreign keys.

People's names are only from the US right now.  Most common ones.
By default you will get a mix of female and male first names.  You can ask for one or the other by specifying sex='M' or sex='F'  The default is sex='B'.  Not dealing with other or non-binary at this point.
No guarantee that the names are unique, but that happens in real life too.

Values are determined from the expression
Then a trend is applied (if applicable)
Then anomalies are applied in the order of definition
anomalies SET the value, so if you want to update the current value, use 'get_value() + 100'
Both condition and value of an anomaly are expressions that are evaluated

date multi columns allow you to create a dimension table
    "name": "dateMultiColumn",
    "dateMultiColumn": {
Name is required but not used (*)
List columns you have, choices are:
- year
- month
- day
- date
- quarter 1 - 4 (uses calendar year)
- half 1 - 2 (uses calendar year)
- dayOfWeek (1-7, 1 is Monday)
