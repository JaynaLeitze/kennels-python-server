CUSTOMERS = [
    {
      "email": "duke@duke.com",
      "password": "12345",
      "name": "Duke Silver",
      "id": 1
    },
    {
      "email": "leslie@pawnee.gov",
      "password": "parks",
      "name": "Leslie Knope",
      "id": 2
    },
    {
      "email": "macklin@macklin.com",
      "password": "12345",
      "name": "Burt Macklin",
      "id": 3
    }
  ]

def get_all_customers():
    return CUSTOMERS

# Function with a single parameter
def get_single_customer(id):
    # Variable to hold the found customer, if it exists
    requested_customer = None

    # Iterate the CUSTOMERS list above. Very similar to the
    # for..of loops you used in JavaScript.
    for customer in CUSTOMERS:
        # Dictionaries in Python use [] notation to find a key
        # instead of the dot notation that JavaScript used.
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer