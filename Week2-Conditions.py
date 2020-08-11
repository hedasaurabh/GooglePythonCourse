print(10>1)
print("cat"=="dog")
print(1!=2)
print(1 == "1")
#In Python uppercase letters are alphabetically sorted before lowercase letters.
print("cat" > "Cat")
print("cat" < "Cat")

print("Yellow" > "Cyan" and "Brown" > "Magenta")

print("Yellow" > "Cyan" or "Brown" > "Magenta")

print (not 42 =="Answer")
####################################################################################


def username_check(username):
    if len(username) < 6:
        print("Invalid username: Too Short")
    elif len(username) > 15:
        print("Invalid: Too Long")
    else:
        print ("Valid username")

username_check("Saurabh")

####################################################################################


#The is_positive function should return True if the number received is positive, otherwise it returns None. Can you fill in the gaps to make that happen?
def is_positive(number):
  if number >=1:
    return True
  return false

result=is_positive(10)
print (result)

####################################################################################

number=10
if number > 11:
  print(0)
elif number != 10:
  print(1)
elif number >= 20 or number < 12:
  print(2)
else:
  print(3)

#If a filesystem has a block size of 4096 bytes, this means that a file comprised of only one byte will still
# use 4096 bytes of storage. A file made up of 4097 bytes will use 4096*2=8192 bytes of storage.
# Knowing this, can you fill in the gaps in the calculate_storage function below, which calculates the total number of bytes
# needed to store a file of a given size?

####################################################################################

def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks are fully occupied
    full_blocks = block_size//filesize
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = full_blocks%block_size
    # Depending on whether there's a remainder or not, return
    # the total number of bytes required to allocate enough blocks
    # to store your data.
    if partial_block_remainder > 0:
        return filesize*block_size
    return ___

print(calculate_storage(1))    # Should be 4096
print(calculate_storage(4096)) # Should be 4096
print(calculate_storage(4097)) # Should be 8192
print(calculate_storage(6000)) # Should be 8192
