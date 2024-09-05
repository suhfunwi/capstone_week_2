# sets
# you can modify sets, add values and whatnot but duplicates aren't allowed
# don't worry about the order, that's how sets make sure there are no duplicates
cats = set()
# the set function creates an empty set
cats.add('Lion')
cats.add('Tiger')
print(cats)
cats.add('Cheetah')
print(cats)

birds = {'owl', 'robin', 'swan'}
#  can also make a set like this
print(birds)
birds.add('robin')
# won't add duplicates
birds.add('cardinal')
birds.remove('owl')
print(birds)
# can still add and remove things from the set even
# if you tried to add a duplicate
for bird in birds:
    print(bird)
    # can also loop over sets

bird_list = ['owl', 'robin', 'swan', 'owl', 'robin', 'swan', 'owl', 'robin', 'swan']
bird_list_no_duplicates = list(set(bird_list))
print(bird_list_no_duplicates)
# an easy way to remove duplicates from a list is to turn it
# in to a set then turn it back in to a list.
# the order will be random again though

