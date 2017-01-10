# your code goes here
score_file = open("scores.txt")

ratings = {}

for line in score_file:
    line = line.rstrip()
    restaurant = line.split(':')
    restaurant_name = restaurant[0]
    restaurant_rating = int(restaurant[1])
    #ratings[restaurant_name] = ratings.get(restaurant_name, 0)
    ratings[restaurant_name] = restaurant_rating

for item, rating in sorted(ratings.items()):
    print "%s is rated at %d." % (item, rating)

# print ratings.items()
