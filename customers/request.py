CUSTOMERS= [
    {
    "email": "dannymccracken13@yahoo.com",
    "password": "BarkBark",
    "name": "Danny McCracken",
    "id": 1
    },
    {
    "email": "jarrettrawlings@fake.com",
    "password": "LittleHunny",
    "name": "Jarrett Rawlings",
    "id": 2
    },
    {
    "email": "adriaanharsta@fake.com",
    "password": "ReggBahd",
    "name": "Adriaan Harsta",
    "id": 3
    },
    {
    "email": "bob@rightprice.net",
    "password": "thepriceiswrong",
    "name": "Bob Barker",
    "id": 4
    }
]

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

def get_all_customers():
    return CUSTOMERS

def create_customer(customer):
    # Get the id value of the last customer in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the customer dictionary
    customer["id"] = new_id

    # Add the customer dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer