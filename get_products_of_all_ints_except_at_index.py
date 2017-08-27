"""
Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:

  [1, 7, 3, 4]

your function would return:

  [84, 12, 28, 21]

by calculating:

  [7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Also you can't use division... Bummer
"""
import time

def get_products_of_all_ints_except_at_index(list_of_ints):
    """
    Brute force for now

    This is O(N^N)... not super great... and makes a new list every time.
    """
    products = []
    for index in range(len(list_of_ints)):
        new_list = list(list_of_ints)
        new_list.pop(index)
        for count,val in enumerate(new_list):
            if count == 0:
                product = val
            else:
                product *= val
        products.append(product)
    return products

ints = [1,7,3,4]
start = time.time()
products = get_products_of_all_ints_except_at_index(ints)
stop = time.time()
print products
print " I should get [84, 12, 28, 21]"
print "Try 1 took ",(stop-start)



def get_products_of_all_ints_except_at_index1(list_of_ints):
    """
    Lets calculate as little as possible. I want to calculate the products before each integer and the products after each integer then multiply these together.

    """
# get each product before index 
    if len(list_of_ints) < 2:
        raise IndexError("calculating the product of numbers at other indecies requries at least two numbers")

    products = [None]*len(list_of_ints)
    product_so_far = 1
    for index in range(len(list_of_ints)):
        products[index] = product_so_far
        product_so_far *= list_of_ints[index]
    #return products
    product_so_far = 1
    index = len(list_of_ints) - 1
    while index >= 0:
        products[index] *= product_so_far
        product_so_far *= list_of_ints[index]
        index -= 1
    return products

start = time.time()
products = get_products_of_all_ints_except_at_index1(ints)
stop = time.time()
print "Round 2 gives"
print products
print "ints are"
print ints
print "Try 2 took ",(stop-start)

