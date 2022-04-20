# Name: Wade Moulton
# Date: 10/11/2020
# Class: CS 4720
# Section: W01
# Instructor: Dr. Sarah North
# Assignment_4-Database


from db import do_command


# supplied function from lecture slides
def list_of_all_stores():
    return do_command("select * from store")


# supplied function from lecture slides
def list_of_all_films():
    return do_command("select * from film order by title")


# supplied function from lecture slides
def list_of_all_inventory():
    return do_command("select * from inventory")


# supplied function from lecture slides
def inventory_for_film(film_id):
    return do_command("select * from inventory where film_id = ?", [film_id])


# supplied function from lecture slides
def inventory_for_film_for_store(film_id, store_id):
    return do_command("select * from inventory where film_id = ? and store_id = ?" [film_id, store_id])


# supplied function from lecture slides
def count_rentals_for_film(film_id):
    invent = inventory_for_film(film_id)
    rentals = 0
    for inv in invent:
        rnt = do_command("select count(all) as cnt from rental where inventory_id = ?", [inv['inventory_id']])
        rentals += rnt[0]['cnt']
    return rentals


# api function to return all customers including addresses
# using left join in case there is no supplied address it will still list the customer
# ref: https://www.w3schools.com/sql/sql_join.asp
def list_of_all_customers():
    return do_command("SELECT customer.customer_id, customer.last_name, customer.first_name, address.address "
                      "FROM customer "
                      "LEFT JOIN address ON customer.address_id = address.address_id")


# api function to also return the number of rentals for a customer
# ref: https://www.w3schools.com/sql/sql_count_avg_sum.asp
def count_customer_rentals(customer_id):
    return do_command("SELECT COUNT(all) FROM rental WHERE customer_id = ?", [customer_id])
