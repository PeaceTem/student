# this is the algorithm to rank a group of objects sample (4 objects)

objects = ['Akande', 'Olumide', 'Jonathan', 'Temiloluwa', 'Pamilerin', 'Olamide', 'Ayomide']


def rankalgo(collection: str):
    combinations = []
    while len(collection) > 1:
        unit_obj = collection.pop()
        for obj in collection:
            combination = [unit_obj, obj]
            combinations.append(combination)

    return combinations


print(rankalgo(objects))

print(len(rankalgo(objects)))

"""
    each combination will be taken from the list of combinations
    they will be rendered next to each other, shuffled for everyone
    the autoplay properties and cache system will be used to store the objects locally for an hour
    There would be buttons underneath the properties for selection of winners for each match
    they will be rendered like whatsapp status(design)
    switching between objects will be similar to whatsapp status' style
    while moving on the another set of objects' design will be similar to youtube shorts'
    each set will have a unique id
    but elements of each set will reference their respective ids in the catalogue
"""


