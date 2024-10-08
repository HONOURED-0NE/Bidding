#Todo 1 : Ask for input

#todo 2 : Save the values into dictionary {Name:Price}
#todo 3 : Ask if theres any other person (loop)
def highest_bidder(bidding_dict):
    highest_bid = 0
    for bidder in bidding_dict:
        bid_amount = bids[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    
    print(f"The winner is {winner} with a bidding price of {highest_bid}")

bids = {}
continue_biding = True
while continue_biding:
    Name = input("Enter your name: \n")
    Price = int(input("Enter your bidding price: \n$"))
    bids[Name] = Price
    cont = input("Is there any other bidder with you?: (Y/N) \n").upper()
    if cont == "N":
        continue_biding = False
        highest_bidder(bidding_dict=bids)
    elif cont == "Y":
        print("\n"*50)

#Todo 4 : Compare the values in the dictionary


highest_bidder(bidding_dict=bids)
catalog = input("View full catalogue?(Y/N): \n").upper()
if catalog == "Y":
    print(bids)