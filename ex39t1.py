# create a mapping of state to abbreviation ('OR', 'FL', etc.)
states = { # variable = dictionary
    'Noord-Holland': 'NH', # Key : Key value
    'Utrecht': 'UT',
    'Zuid-Holland': 'ZH',
    'Noord-Brabant': 'NB',
    'Limburg': 'LI',
}

# create a basic set of states and some cities in them
cities = { # variable = dictionary
    'UT': 'Utrecht', # Key : Key value
    'NH': 'Haarlem',
    'ZH': 'Den Haag'
}

# add some more cities
cities['LI'] = 'Maastricht' # Create new Key with Key Value inside 'cities' dictionary
cities['NB'] = '\'s-Hertogenbosch' # Create new Key with Key Value inside 'cities' dictionary

# print out some cities
print('-' * 10) # show 10 times the - sign ## ----------
print("De provincie Noord Holland heeft: ", cities['NH']) # Show message, variable [key: NY]
print("De provincie Noord-Brabant heeft: ", cities['NB']) # Show message, variable [key: OR]

# print some more states
print('-' * 10) # show 10 times the - sign ## ----------
print("De Noord-Hollandse provincie heeft als afkorting: ", states['Noord-Holland']) # Show message, variable [key: Michigan]
print("De afkorting voor Zuid-Holland is: ", states['Zuid-Holland']) # Show message, variable [key: Florida]

# do it by using the state then cities dict
print('-' * 10) # show 10 times the - sign ## ----------
# Show message, look-up 'Michigan Key in 'states' dict which returns MI, then 
# look-up 'MI' Key in 'cities' dict to show 'cities' Key value: 'Detroit' in message
print("Noord-Holland heeft: ", cities[states['Noord-Holland']]) 
print("Noord-Brabant heeft: ", cities[states['Noord-Brabant']]) 

# print every state abbreviation
print('-' * 10) # show 10 times the - sign ## ----------

for state, abbrev in list(states.items()): 
# New Loop to create list of items from dataset: 'states', a dictionary

# 'states' variable = a dictionary

# in = specify dataset being used. in = True if dataset contains data. False if not

# state, abbrev are new variables created at the start of the loop, and assigned 
# to the 'Key' and 'Key value' from 'states' dictionary dataset

    print(f"{state} is afgekort {abbrev}") # show variable 'state' with message 'abbrev'
   
# print every city in state
print('-' * 10) # show 10 times the - sign ## ----------
# loop create list from all 'states' dictionary items and re-assign 'Key' to 'abbrev' variable
# and 'Key value' to 'city' variable. Loop ends at the end of the list
for abbrev, city in list(states.items()):
    print(f"{abbrev} heeft {city}") # show message with variable
    
# now do both at the same time
print('-' * 10) # show 10 times the - sign ## ----------
for state, abbrev in list(states.items()):
    print(f"{state} is afgekort {abbrev}")
    print(f"en heeft als hoofdstad {cities[abbrev]}.")

print('-' * 10) # show 10 times the - sign ## ----------
# safely get a abbreviation by state that might not be there
state = states.get('Groningen') # variable = 'variable'.function('parameter')

# if-statement, outside a function
if not state: # if not 'variable' then:
    print("Sorry, geen Groningen.") # Show message
    
# get a city with a default value
city = cities.get('GR', 'Bestaat niet.') # variable = 'variable'.function('parameter', 'parameter')
print(f"De stad voor de provincie 'GR' is: {city}") # show message {variable} returns 'parameter'.
