import heapq
from datetime import datetime
from tabulate import tabulate

# Initiate
bids = []  
asks = []  
matches = []  


def _add_order(heap, price, quantity, timestamp):
    heapq.heappush(heap, (price, timestamp, quantity)) 


def add_bid(price, quantity):
    global matches  
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    matches = _match_order(price, quantity, is_bid=True, matches=matches)
    if quantity > 0:  
        _add_order(bids, -price, quantity, timestamp)

def add_ask(price, quantity):
    global matches  
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    matches = _match_order(price, quantity, is_bid=False, matches=matches)  
    if quantity > 0:  
        _add_order(asks, price, quantity, timestamp)  

def _match_order(price, quantity, is_bid, matches):
    target_heap = asks if is_bid else bids  

    for _ in range(len(target_heap)): 
        if quantity <= 0:  
            break

        target_price, target_timestamp, target_quantity = heapq.heappop(target_heap) 

        if (is_bid and -target_price <= price) or (not is_bid and target_price >= price):
            matched_quantity = min(quantity, target_quantity) 

            matches.append({
                "price": abs(target_price),  
                "quantity": matched_quantity,
                "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

            quantity -= matched_quantity

            if target_quantity > matched_quantity:
                heapq.heappush(target_heap, (target_price, target_timestamp, target_quantity - matched_quantity))
        else:
            heapq.heappush(target_heap, (target_price, target_timestamp, target_quantity))
            break 

    return matches

def get_order_book():
    bids_sorted = sorted([(-price, ts, qty) for price, ts, qty in bids], reverse=True)
    asks_sorted = sorted(asks)
    matches_sorted = sorted(matches, key=lambda x: (x["price"], x["timestamp"]))
    return {
        "bids": bids_sorted,
        "asks": asks_sorted,
        "matches": matches_sorted
    }


def display_order_book():
    order_book = get_order_book()

    bids_table = [(price, qty, ts) for price, ts, qty in order_book["bids"]]
    asks_table = [(price, qty, ts) for price, ts, qty in order_book["asks"]]
    matches_table = [(m["price"], m["quantity"], m["timestamp"]) for m in order_book["matches"]]

    print("\nOrder Book - Bids:")
    print(tabulate(bids_table, headers=["Price", "Quantity", "Timestamp"], tablefmt="grid"))

    print("\nOrder Book - Asks:")
    print(tabulate(asks_table, headers=["Price", "Quantity", "Timestamp"], tablefmt="grid"))

    print("\nOrder Book - Matches:")
    print(tabulate(matches_table, headers=["Price", "Quantity", "Timestamp"], tablefmt="grid"))


# Request
# Request pertama :
add_bid(5000, 5)
# Request kedua :
add_bid(5250, 2) 
# Request ketiga :
add_ask(2700, 3)
# Request keempat :
add_ask(5600, 3)
# Request kelima :
add_bid(1300, 2)
# Request keenam :
add_ask(5050, 1)

# print order book dan statistik
display_order_book()
