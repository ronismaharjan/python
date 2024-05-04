bill = 0

size = str(input(("what size pizza do you want? S,M,L? ")))
add_peperoni = str(input("Do you want pepperoni?y/n: "))
extra_cheese = str(input("Do you want extra cheese? "))


if(size =="s"):
    bill +=15
    if(add_peperoni == "y"):
        bill +=2


if(extra_cheese == "y"):
    bill += 1

elif(size == "m"):
    bill +=20
    if(add_peperoni == "y"):
        bill +=3


elif(size== "l"):
    bill +=25
    if(add_peperoni == "y"):
        bill +=3




else:
    print("There is an error, sorry try again.")

print("The total bill with "+ size +" size pizza " +" pepperoni " + add_peperoni + " and " + extra_cheese +" extra cheese is $" + str(bill) )