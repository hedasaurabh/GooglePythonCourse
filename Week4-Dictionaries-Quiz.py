###The email_list function receives a dictionary, which contains domain names as keys, and a list of users as values.
# Fill in the blanks to generate a list that contains complete email addresses (e.g. diana.prince@gmail.com).

def email_list(domains):
	emails = []
	for key,users in domains.items():
	  for user in users:
	    emails.append(user+"@"+key)
	return(emails)

print(email_list({"gmail.com": ["clark.kent", "diana.prince", "peter.parker"], "yahoo.com": ["barbara.gordon", "jean.grey"], "hotmail.com": ["bruce.wayne"]}))


groups_per_user = {"local": ["admin", "userA"], "public":  ["admin", "userB"],"administrator": ["admin"] }

print (type (groups_per_user.values()))

i = groups_per_user.values()

print (i[1:])

if "admin" in i[0]:
    print ("true")


###The dict.update method updates one dictionary with the items coming from the other dictionary, so that existing entries
###are replaced and new entries are added. What is the content of the dictionary “wardrobe“ at the end of the following code?

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)

print (wardrobe)