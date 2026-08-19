'''
Path parameters allow us to use a single API endpoint to handle multiple
dynamic routes.

Example — E-commerce website:

/products/1
/products/2
/products/3

Here, 1, 2, and 3 are dynamic values. We can use the same API to fetch
different products based on the product ID.

Key Points
Dynamic Routes: The route can change based on the value provided by the user.
Data Types: Path parameters can have data types such as int, str, etc.
Validation: We can validate the path parameter based on its expected data type and other conditions.
Example with User ID
/users/1
/users/2
/users/3

Here, the user ID determines which user we want to access. We don't need 
to create a separate route for every user. The same route handles all 
users dynamically.
'''

from fastapi import FastAPI
app = FastAPI()

# User Route
@app.get("/users/{user_id}")
def get_user(user_id):
    return{"user_id": user_id}

