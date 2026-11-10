"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. My object, my five fields, and why those:


# Your code below
name = input("Enter the customer's name: ")
email = input("Enter the customer's email: ")
city = input("Enter the customer's city: ")
country = input("Enter the customer's country: ")
product = input("Enter the product purchased: ")

customer = {
    "name": name,
    "email": email,
    "city": city,
    "country": country,
    "product": product
}

print("The customer's name is:", customer["name"])
print("The customer's email is:", customer["email"])
print("The customer's city is:", customer["city"])
print("The customer's country is:", customer["country"])
print("The product purchased is:", customer["product"])

customer["city"] = input("Enter the customer's new city: ")
print("The updated city is:", customer["city"])

customer_country = customer.pop("country")
print("The removed country is:", customer_country)

for field, value in customer.items():
    print(field, ":", value)
