for x in range(5):
    print(x)

####################################################################################
####################################################################################

def square(n):
    return n*n

def sum_squares(x):
    sum = 0
    for n in range(x):
        sum += square(n)
    return sum

print(sum_squares(10)) # Should be 285

####################################################################################
####################################################################################
print ("XXXXXXXXXXXXXXXXX")

def factorial(n):
    result = 1
    for i in range(1,n):
        #result = result + i*result
         result += i * result

    return result

print(factorial(4)) # should return 24
print(factorial(5)) # should return 120

####################################################################################
####################################################################################
print ("XXXXXXXXXXXXXXXXX")

teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print ("Scheudle: " + home_team + " VS " + away_team)

####################################################################################
####################################################################################

for left in range(7):
    for right in range(left,7):
        print "["+str(left)+"|"+str(right)+"]",
    print 
