import datetime

# Get today's date
date = datetime.datetime.now().date()

# Get the name of the day in short form with the first letter capitalized
day = date.strftime('%a')

# Determine the fare based on the day of the week
if day in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']:
    fare = 100
elif day == 'Sat':
    fare = 60
else:
    fare = 80

# Print the results
print("Date:", date)
print("Day:", day)
print("Fare:", fare)
