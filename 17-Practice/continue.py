#You are making a ticketing system.
#The price of a single ticket is $100.
#For children under 3 years of age, the ticket is free.

#Your program needs to take the ages of 5 passengers as input and output the total price for their tickets.

#Sample Input
#18
#24
#2
#5
#42

#Sample Output
#400
#There is one child under 3 among the passengers, so the total price of 5 tickets is $400.

total = 0
#your code goes here
x = 0
while x < 5:
    age = int(input()) 
    x+=1
    if age < 3:
        continue
    else:
        total = total + 100
    
    
print(total)