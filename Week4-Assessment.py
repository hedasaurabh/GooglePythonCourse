
Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

Jamies_list.reverse()
final_list = []
for word in Drews_list:
    final_list.append(word)
for word in Jamies_list:
    final_list.append(word)

print (final_list)


def pline():
    print ("#######################################################################################################\n"
           "#######################################################################################################")

pline()

#The format_address function separates out parts of the address string into new strings: house_number and street_name,
#and returns: "house number X on street named Y". The format of the input string is: numeric house number, followed by
#the street name which may contain numbers, but never by themselves, and could be several words long. For example,
#"123 Main Street", "1001 1st Ave", or "55 North Center Drive". Fill in the gaps to complete this function.

def format_address(address_string):
    # Declare variables
    street_name = ""
    # Separate the address string into parts
    house_number = address_string.split()[0]
    street_name = address_string.split()[1:]
    # print(house_number)
    # print(street_name)
    # Traverse through the address parts
    # for __:
    # Determine if the address part is the
    # house number or part of the street name

    # Does anything else need to be done
    # before returning the result?

    # Return the formatted string
    return "house number {} on street named {}".format(house_number, ' '.join(street_name))


print(format_address("123 Main Street"))
# Should print: "house number 123 on street named Main Street"

print(format_address("1001 1st Ave"))
# Should print: "house number 1001 on street named 1st Ave"

print(format_address("55 North Center Drive"))
# Should print "house number 55 on street named North Center Drive"

pline()

#The highlight_word function changes the given word in a sentence to its upper-case version. For example, highlight_
# word("Have a nice day", "nice") returns "Have a NICE day". Can you write this function in just one line?

def highlight_word(sentence, word):
	return(sentence.replace(word,word.upper()))

print(highlight_word("Have a nice day", "nice"))
print(highlight_word("Shhh, don't be so loud!", "loud"))
print(highlight_word("Automating with Python is fun", "fun"))

pline()

#A professor with two assistants, Jamie and Drew, wants an attendance list of the students, in the order that they
# arrived in the classroom. Drew was the first one to note which students arrived, and then Jamie took over. After the
# class, they each entered their lists into the computer and emailed them to the professor, who needs to combine them
# into one, in the order of each student's arrival. Jamie emailed a follow-up, saying that her list is in reverse order.
# Complete the steps to combine them into one list as follows: the contents of Drew's list, followed by Jamie's list in
# reverse order, to get an accurate list of the students as they arrived.

def combine_lists(list1, list2):
    list1.reverse()
    final_list = []
    for word in list2:
        final_list.append(word)
    for word in list1:
        final_list.append(word)
    return (final_list)
    # Generate a new list containing the elements of list2
    # Followed by the elements of list1 in reverse order


Jamies_list = ["Alice", "Cindy", "Bobby", "Jan", "Peter"]
Drews_list = ["Mike", "Carol", "Greg", "Marcia"]

print(combine_lists(Jamies_list, Drews_list))

pline()
#Use a list comprehension to create a list of squared numbers (n*n). The function receives the variables start and end,
#and returns a list of squares of consecutive numbers between start and end inclusively. For example, squares(2, 3) should return [4, 9].

def squares(start, end):
	empty_list = []
	final_list = []
	while start <= end:
		empty_list.append(start)
		start +=1
	for i in empty_list:
		final_list.append(i*i)
	return final_list

print(squares(2, 3)) # Should be [4, 9]
print(squares(1, 5)) # Should be [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should be [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

pline()
#Complete the code to iterate through the keys and values of the car_prices dictionary, printing out some information
# about each one.

def car_listing(car_prices):
  result = ""
  for car,prices in car_prices.items():
    result += "{} costs {} dollars".format(car,prices) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))

pline()

#Taylor and Rory are hosting a party. They sent out invitations, and each one collected responses into dictionaries,
# with names of their friends and how many guests each friend is bringing. Each dictionary is a partial list, but Rory's
# list has more current information about the number of guests. Fill in the blanks to combine both dictionaries into
# one, with each friend listed only once, and the number of guests from Rory's dictionary taking precedence, if a name
# is included in both dictionaries. Then print the resulting dictionary.
def combine_guests(guests1, guests2):
  # Combine both dictionaries into one, with each key listed
  # only once, and the value from guests1 taking precedence
  final_list = {}
  final_list.update(guests2)
  final_list.update(guests1)
  #print(final_list)
  #for guest in guests2:
  #  if guest not in guests1:
    #  continue
    #else:
  #    final_list.update(guests2)
  #print(final_list)
  return final_list
Rorys_guests = { "Adam":2, "Brenda":3, "David":1, "Jose":3, "Charlotte":2, "Terry":1, "Robert":4}
Taylors_guests = { "David":4, "Nancy":1, "Robert":2, "Adam":1, "Samantha":3, "Chris":5}

print(combine_guests(Rorys_guests, Taylors_guests))

pline()

#Use a dictionary to count the frequency of letters in the input string. Only letters should be counted, not blank
# spaces, numbers, or punctuation. Upper case should be considered the same as lower case. For example,
# count_letters("This is a sentence.") should return {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}.

def count_letters(text):
  result = {}
  # Go through each letter in the text

  punctuations = '''!()-[]{};:'"\,<>./?+=@#$%^&*_~'''
  for x in text.lower():
    if x in punctuations:
      text = text.replace(x, "")
  text = text.replace(" ","")
  for letter in ''.join([i for i in text if not i.isdigit()]).lower():
    # Check if the letter needs to be counted or not
    if letter not in result:
      result[letter]=0
    # Add or increment the value in the dictionary
    result[letter]=result[letter]+1
  return result

print(count_letters("AaBbCc"))
# Should be {'a': 2, 'b': 2, 'c': 2}

print(count_letters("Math is fun! 2+2=4"))
# Should be {'m': 1, 'a': 1, 't': 1, 'h': 1, 'i': 1, 's': 1, 'f': 1, 'u': 1, 'n': 1}

print(count_letters("This is a sentence"))
# Should be {'t': 2, 'h': 1, 'i': 2, 's': 3, 'a': 1, 'e': 3, 'n': 2, 'c': 1}






