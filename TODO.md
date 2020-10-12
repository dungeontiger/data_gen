- then keys, categories

Date hierarchies
Indicate start date, end date and levels (year, month, half, quarter, week, etc)

seasonal trends
apply a factor based on date and some seasonal value

geography tables, generate places and locations easily
geography will be done like this
continent() returns a randome continent
country(continents) returns a random country, filtered by the list of continents
this allows for only countries in Europe for example or North and South America
state(countries) returns a random state filtered by the list of countries
city(countries/states) returns a random city filtered by country and states
this allows you to get the correct london or paris
maybe allow optionally to get code too

handle foreign keys, star schemas

implement and test seeds

add a trend start and end date
allow multiple trends, some start and end on different dates and referencing different date columns

proper tests for all the trend stuff

anolmolies use a valueexpression, if true, apply the change