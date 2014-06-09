from sys import argv

script, filename = argv

f= open(filename)

restaurants = {}

for line in f:
    l = line.rstrip()
    restaurant_name, rating = l.split(":")
    restaurants[restaurant_name] = rating


names = restaurants.keys()
names.sort()
print names

for name in names:
    print "Restaurant %r is rated at %r" % (name, restaurants[name])





