def greeting(name,dept):
    print ("Hello "+ name)
    print ("Department: "+ dept)

result = greeting("Saurabh","Comp")
print (result)

####################################################################################

def get_seconds(hours, minutes, seconds):
  return 3600*hours + 60*minutes + seconds

amount_a = get_seconds(2,30,0)
amount_b = get_seconds(0,45,15)
result = amount_a+amount_b
print (result)

####################################################################################

def convert_seconds(seconds):
    seconds=float(seconds)
    hours = seconds/3600
    minutes = seconds/60
    return (hours,minutes)

hours,seconds = convert_seconds(7100)
print (hours,seconds)

####################################################################################


def month_days(month, days):
    print (month +" has " + str(days) + " days.")

month_days("June",30)
month_days("July",31)

####################################################################################


# 1) Complete the function to return the result of the conversion
def convert_distance(miles):
	km = miles * 1.6  # approximately 1.6 km in 1 mile
	return km

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above
my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion
print("The distance in kilometers is " + str(my_trip_km))

# 4) Calculate the round-trip in kilometers by doubling the result,
#    and fill in the blank to print the result
print("The round-trip in kilometers is " + str(2*my_trip_km))

####################################################################################

# This function compares two numbers and returns them
# in increasing order.
def order_numbers(number1, number2):
	if number2 > number1:
		return number1, number2
	else:
		return number2, number1

# 1) Fill in the blanks so the print statement displays the result
#    of the function call
smaller,bigger = order_numbers(100, 99)
print(smaller, bigger)

####################################################################################


def lucky_number(name):
    number = len(name) * 9
    messages = "Hello " + name + ". Your lucky number is " + str(number)
    return messages


print(lucky_number("Kay"))
print(lucky_number("Cameron"))