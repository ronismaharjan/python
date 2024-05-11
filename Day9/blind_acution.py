#Function to add dictionary to list 
def add_bidder(name, bid):
    bidders.append({
        "name":name, 
        "bid":bid,
    })

#Function to check the higgest bid
def higgest_bid(bidders_list):
    higgest_bidder ={}
    higgest_bidder["name"] =  bidders[0]["name"]
    higgest_bidder["bid"] =  bidders[0]["bid"]
    for index in range(0, len(bidders)):
        if(higgest_bidder["bid"] < bidders[index]["bid"]):
            higgest_bidder ={}
            higgest_bidder["name"] =  bidders[index]["name"]
            higgest_bidder["bid"] =  bidders[index]["bid"]
    print("The winner is " + higgest_bidder["name"] + ". The highest bid of " + "$" + str(higgest_bidder["bid"]))


#Main program
from art import logo
bidders = []
bid_ended = False
print(logo)
while not bid_ended:
    name = input("Whats your name: ")
    bid = int(input("Whats your bid? $"))
    add_bidder(name, bid)
    user_choice = input("Do you want to continue 'yes' or 'no'? ").lower()
    if user_choice == "no":
        bid_ended = True

higgest_bid(bidders)