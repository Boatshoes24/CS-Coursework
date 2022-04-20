# Name: Wade Moulton
# Date: 10/11/2020
# Class: CS 4720
# Section: W01
# Instructor: Dr. Sarah North
# Assignment_4-Database


import db_access

# original supplied code
films = db_access.list_of_all_films()
stores = db_access.list_of_all_stores()

# call db_access api to supply list of customers
customers = db_access.list_of_all_customers()

# original supplied template code
# template = "{:>5}  {:30}{:>15} {:>15}"
# row = template.format("ID", "Title", "In Inventory", "Rentals")

# creating my own template for row formatting
template = "{:>5}  {:<12}{:<12} {:<40} {:<15}"


def report_all_customers():

    # print header row
    print(template.format("ID", "Last Name", "First Name", "Address", ""))

    # add divider between header and data
    print("-" * 100)

    # iterate through each customer entry and assign needed values to variables
    # after variable assignment create row from global template to format text
    for customer in customers:
        customer_id = customer['customer_id']
        last_name = customer['last_name']
        first_name = customer['first_name']
        address = customer['address']
        print(template.format(customer_id, last_name, first_name, address, ""))


def report_all_customers_and_rentals():

    # print header row
    print(template.format("ID", "Last Name", "First Name", "Address", "Rentals"))

    # add divider between header and data
    print("-" * 100)

    # iterate through each customer entry and assign needed values to variables
    # after variable assignment create row from global template to format text
    # on this variation we additionally add the rental amounts
    for customer in customers:
        customer_id = customer['customer_id']
        last_name = customer['last_name']
        first_name = customer['first_name']
        address = customer['address']
        # gather rental value from dict containing 'count(all)' as key
        rentals = db_access.count_customer_rentals(customer_id)
        num_rentals = rentals[0]['count(all)']
        print(template.format(customer_id, last_name, first_name, address, num_rentals))


# creating main method to separate reports into functions
def main():
    # call all customers function
    report_all_customers()
    # adding in a little divider to make it easier to differentiate between the two reports
    print("-"*100)
    print("*"*100)
    print("-"*100)
    # call all customers and rentals function
    report_all_customers_and_rentals()


if __name__ == '__main__':
    main()
