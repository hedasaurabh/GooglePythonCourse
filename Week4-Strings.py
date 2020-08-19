#Modify the first_and_last function so that it returns True if the first letter of the string is the same as the last letter of the string, False if theyre different.
# Remember that you can access characters using message[0] or message[-1].
# Be careful how you handle the empty string, which should return True since nothing is equal to nothing.

def first_and_last(message):
    x = len(message)
    if x == 0:
        return True
    if (message[0] == message[-1]):
        return True
    else:
       return False
print(first_and_last("else"))
print(first_and_last("tree"))
print(first_and_last(""))

#Substring
color = "Orange"
print (color[1:4])  #ran
print (color[:4])   #Oran
print (color[4:])   #ge

Fruit = "Pineapple"
print (Fruit[:4])
print (Fruit[4:])

message = "A kong string with a silly type"
new_message = message[0:2]+'l'+message[3:]
print (new_message)
print (color.index("g"))

#Using the index method, find out the position of "x" in "supercalifragilisticexpialidocious".
word = "supercalifragilisticexpialidocious"
print(word.index("x"))

#Email ID check

def email_check(email,old_domain,new_domain):
    if "@" + old_domain in email:
        index = email.index("@")
        new_email = email[:index] + "@" + new_domain
        return (new_email)
    return (email)

print (email_check("saurabh.heda13@abc.com","abc.com","xyz.com"))

#################################################################################################
print ("Mountains").upper()
print ("Mountains").lower()
print (" Mountains ").strip()


#################################################################################################
result = "Forest is Green"
print (result.isdigit())

#################################################################################################
#Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase received,
# in upper case.
# For example: "Universal Serial Bus" should return USB; local area network should return LAN.
def initials(phrase):
    words = phrase.split()
    print(words)
    result = ""
    for word in words:
        result += word[0]
    return result.upper()

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS

test = "Fill in the gaps in the initials function so that it returns the initials of the words contained in the phrase received"
print (test.count("in"))

#################################################################################################
#################################################################################################

#Modify the student_grade function using the format method, so that it returns the phrase "X received Y% on the exam".
# For example, student_grade("Reed", 80) should return "Reed received 80% on the exam".

def student_grade(name, grade):
	x = "{name} received {grade}% on the exam".format(name=name,grade=grade)
	return x
print(student_grade("Reed", 80))
print(student_grade("Paige", 92))
print(student_grade("Jesse", 85))


weather = "Rainfall"
print (weather[4:])