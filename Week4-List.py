x = ['we','are','now','cooking']
print (x)

print (x[1:3])
print (x[:2])
print (x[1:])

######Using the "split" string method from the preceding lesson, complete the get_word function to return the {n}th word
# from a passed sentence. For example, get_word("This is a lesson about lists", 4) should return "lesson", which is the
# 4th word in this sentence. Hint: remember that list indexes start at 0, not 1.

def get_word(sentence, n):
	# Only proceed if n is positive
	if n > 0:
		words = sentence.split()
		# Only proceed if n is not more than the number of words
		if n <= len(words):
			return(words[n-1])
	return("")


print(get_word("This is a lesson about lists", 4)) # Should print: lesson
print(get_word("This is a lesson about lists", -4)) # Nothing
print(get_word("Now we are cooking!", 1)) # Should print: Now
print(get_word("Now we are cooking!", 5)) # Nothing


fruits = ["Apple","Banana","Melon"]
fruits.append("Chikoo")
print (fruits)

fruits.insert(0,"Orange")
print (fruits)

fruits.remove("Melon")
print (fruits)

fruits.pop(2)
print (fruits)

fruits[0] = "Strawberry"
print (fruits)


####The skip_elements function returns a list containing every other element from an input list, starting with the first
# element. Complete this function to do that, using the for loop to iterate through the input list.


def skip_elements(elements):
    #return (elements[::2])   ##### Easiet way
	# Initialize variables
	new_list = []
	i = 0

	# Iterate through the list
	for element in elements:
		# Does this element belong in the resulting list?
		#print(j)
		if i % 2 == 0:
			# Add this element to the resulting list
			new_list.append(element)
		# Increment i
		i = i + 1

	return new_list



print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']
print(skip_elements([])) # Should be []


##Let's use tuples to store information about a file: its name, its type and its size in bytes. Fill in the gaps in this ' \
##code to return the size in kilobytes (a kilobyte is 1024 bytes) up to 2 decimal places.

def file_size(file_info):
	name,type,size= file_info
	return("{:.2f}".format(size / 1024))



print(file_size(('Class Assignment', 'docx', 17875))) # Should print 17.46
print(file_size(('Notes', 'txt', 496))) # Should print 0.48
print(file_size(('Program', 'py', 1239))) # Should print 1.21

animals = ["Lion","Monkey","Dolphin","Zebra"]
chars = 0
for animal in animals:
    chars += len(animal)
print ("#############\n"+ "Total Charcters:{}, Average Length:{}".format(chars,chars/len(animals)))

def linef():
    print "\n###########################################################################################################\n"

linef()

def skip_elements(elements):
	new_list = []
	# code goes here
	for index,element in enumerate(elements):
		if index % 2 == 0:
			new_list.append(element)
	return new_list

print(skip_elements(["a", "b", "c", "d", "e", "f", "g"])) # Should be ['a', 'c', 'e', 'g']
print(skip_elements(['Orange', 'Pineapple', 'Strawberry', 'Kiwi', 'Peach'])) # Should be ['Orange', 'Strawberry', 'Peach']


linef()


def result_email(people):
    result = []
    for name,email in enumerate(people):
        result.append("{} <{}>".format(name,email))
    return result

print (result_email(["Saurabh","saurabh.heda13@gmail.com"]))
#print (result_email(["Saurabh","saurabh.heda13@gmail.com"]))


linef()

mutliples = []
for x in range (1,11):
    mutliples.append(x*7)
print (mutliples)

linef()

mutliples=[x*7 for x in range (1,11)]
print (mutliples)

linef()

#The odd_numbers function returns a list of odd numbers between 1 and n, inclusively. Fill in the blanks in the function,
#using list comprehension. Hint: remember that list and range counters start at 0 and end at the limit minus 1.

def odd_numbers(n):
	return [x for x in range (1,n+1) if x % 2 !=0]

print(odd_numbers(5))  # Should print [1, 3, 5]
print(odd_numbers(10)) # Should print [1, 3, 5, 7, 9]
print(odd_numbers(11)) # Should print [1, 3, 5, 7, 9, 11]
print(odd_numbers(1))  # Should print [1]
print(odd_numbers(-1)) # Should print []

filenames = ["sample.hpp","sample"]

for filename in filenames:
    if filename.endswith("hpp"):
        x = filename.replace("hpp","c")
        print (x)

linef()

text = "hello how are you"

words = text.split()
say = []
for word in words:
    x = word[1:]+word[0]+"ay"
    say.append(x)
print (say)

linef()
