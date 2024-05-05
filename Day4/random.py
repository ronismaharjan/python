import random from 
random_integer = random.randint(1, 4)


# for generating random decimal number we use random.random() we cannot put range in here its default give random decimal from 0.0000000 to 0.9999999. So by multiplying it by the number will give the range of the number but the multiplyed number will not be include.


# eg:
random_Decimal = random.random() #this will give random decimal from 0.000 to 0.99999

random_Decimal = random.random()*3 # this will give random number up to 2.999999999 
print(random_Decimal)