# Tuples
# Essentially a list that cannot be changed once created
city_state = [('Seattle', 'WA'), ('Portland', 'OR'), ('San Francisco', 'CA')]
print(len(city_state))

first_city_state = city_state[0]
print(first_city_state)

print(first_city_state[0])
print(first_city_state[1])
# tuple unpacking, allows you to access the individual values in a tuple
city, state = first_city_state
print(city, state)
# 'unpacks' the individual variables in the tuple

animals = ('lion', 'puma', 'tiger')
lion, puma, tiger, = animals
print(tiger)
# can unpack an unlimited amount of tuples, but make
# sure you have enough variables to unpack it into


def get_distance():
    miles = 1000
    km = miles * 1.6
    return miles, km
# returning two values makes it a tuple


distances = get_distance()
print(distances[0])
miles, km = get_distance()
print(km)
# can still unpack the tuple this way


# def get_random_cat_and_pattern():
#     return 'tiger', 'stripes'
# # return a tuple
#
# cat, pattern = get_random_cat_and_pattern()
# # unpack the tuple to get both values in separate variables
# # cat = tiger and pattern = stripes
# data = get_random_cat_and_pattern()
# try:
#     print(data[10])
# #     index 10 does not exist
# except:
#     print('oops, that does not exist.')
#     # instead of letting the program crash,
#     # it's sending an error message.

