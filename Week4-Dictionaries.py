file_counts = {"PDF":23,"JPG":45}
print (type(file_counts))
print (file_counts["JPG"])

file_counts["py"]=55
print (file_counts)


del file_counts["py"]

print (file_counts)



toc = {"Introduction":1, "Chapter 1":4, "Chapter 2":11, "Chapter 3":25, "Chapter 4":30}
toc["Epilogue"]=39 # Epilogue starts on page 39
toc["Chapter 3"]=24 # Chapter 3 now starts on page 24
print(toc) # What are the current contents of the dictionary?
if "Chapter 5" in toc: # Is there a Chapter 5?
    print("True")
else:
    print("False")


def pline():
    print ("#######################################################################################################\n"
           "#######################################################################################################")

pline()

file_counts = {"PDF":23,"JPG":45,"Py":10,"PNG":5}

for extension in file_counts:    ### this will just print the values and not keys.
    print (extension)

for keys,value in file_counts.items():
    print ("Total files of {} are {}".format(keys,value))

pline()

print (file_counts.keys())

print (file_counts.values())

for i in file_counts.values():
    print (i)

pline()

cool_beasts = {"octopuses":"tentacles", "dolphins":"fins", "rhinos":"horns"}
for keys,values in cool_beasts.items():
    print("{} have {}".format(keys,values))

pline()

###Important
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] = result[letter] + 1
    return result

print (count_letters("aaa"))

pline()

##In Python, a dictionary can only hold a single value for a given key. To workaround this, our single value can be a
# list containing multiple values. Here we have a dictionary called "wardrobe" with items of clothing and their colors.
# Fill in the blanks to print a line for each item of clothing with each color, for example: "red shirt", "blue shirt", and so on.

wardrobe = {"shirt":["red","blue","white"], "jeans":["blue","black"]}
for key,value in wardrobe.items():
	for color in value:
		print("{} {}".format(color,key))


###Question 5
###The add_prices function returns the total price of all of the groceries in the dictionary. Fill in the blanks to
###complete this function.

def add_prices(basket):
	# Initialize the variable that will be used for the calculation
	total = 0
	# Iterate through the dictionary items
	for fruits,price in basket.items():
		# Add each price to the total calculation
		# Hint: how do you access the values of
		# dictionary items?
		total += price
	# Limit the return value to 2 decimal places
	return round(total, 2)

groceries = {"bananas": 1.56, "apples": 2.50, "oranges": 0.99, "bread": 4.59,
	"coffee": 6.99, "milk": 3.39, "eggs": 2.98, "cheese": 5.44}

print(add_prices(groceries)) # Should print 28.44