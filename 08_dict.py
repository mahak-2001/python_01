#it is unordered.
# it is mutable.
# it is indexed.
# cannot contain duplicate keys.
d={} #empty dictionary
marks={"harry": 85,
       "subham": 90,
       "rohan":23
    }
print(marks,type(marks))
print(marks["harry"])
print(marks.items())
print(marks.keys())
print(marks.values())
marks.update({"rohan":87,"mahak":100})
print(marks)
print(marks["harry"])#if key is not present so it returns error.

print(marks.get("harry"))
print(marks.get("harry1"))#if key is not present so it do not give error,it print none.

cart = {"item": "Book", "price": 500, "qty": 2}
cart.pop("price")   # Removes "price" and returns 500
print(cart)

cart.popitem()  # Removes and returns ("qty", 2)
print(cart)

cart.clear() # cart is now {}
print(cart)