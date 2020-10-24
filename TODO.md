Before release:
- multiple trends
- random module references
- math module reference
- date hierarchy
    - add all the pieces
    - add a prefix
- geography hierarchy
- product hierarchy
- error reporting
- documentation
- examples
- proper unit tests
- fix lint issues
- build system on github

- difference between adding to a value and setting a value?

geography tables, generate places and locations easily
geography will be done like this
continent() returns a randome continent
country(continents) returns a random country, filtered by the list of continents
this allows for only countries in Europe for example or North and South America
state(countries) returns a random state filtered by the list of countries
city(countries/states) returns a random city filtered by country and states
this allows you to get the correct london or paris
maybe allow optionally to get code too

implement and test seeds

add a trend start and end date
allow multiple trends, some start and end on different dates and referencing different date columns

proper tests for all the trend stuff

need some asserts in the dataset test cases

better way to import all the names of the random module so I don't miss any, also math functions I suppose too

add more names so they are plenty of combinations, include european and asian names / characters
