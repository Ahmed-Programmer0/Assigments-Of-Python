# The List For Gettting Names(First Name, Last Name) With Two Methods
friends = ["Osama", "Ahmed", "Sayed", "Ali", "Mahamed"]

# The Two Methods For  First Name
print(friends[0])
print(friends[friends.index("Osama")])
# The Two Methods For  Last Name
print(friends[-1])
print(friends.pop(len(friends) - 1))