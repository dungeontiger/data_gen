# data_gen
A tool to generate data for use in testing, demos and machine learning training.


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
