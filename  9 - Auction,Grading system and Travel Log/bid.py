bids = {}
should_continue = True

while should_continue:
    key = input("What is your name? ")
    value = int(input("Whats your bid?: $"))

    other_bids = input("Are there any other bidders? Type 'yes' or 'no'\n")

    if other_bids=="no":
        should_continue=False
        
    bids[key]=value

print(bids)

highest_bid = 0
highest_bidder = ''

for key in bids:
    if bids[key]>highest_bid:
        highest_bid=bids[key]
        highest_bidder=key

print(f"The highest bid is ${highest_bid}")
print(f"The winner is {highest_bidder}")