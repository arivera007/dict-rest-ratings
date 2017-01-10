# score_file = open("scores.txt")

# ratings = {}

# for line in score_file:
#     line = line.rstrip()
#     restaurant = line.split(':')
#     restaurant_name = restaurant[0]
#     restaurant_rating = int(restaurant[1])
#     #ratings[restaurant_name] = ratings.get(restaurant_name, 0)
#     ratings[restaurant_name] = restaurant_rating

# for item, rating in sorted(ratings.items()):
#     print "%s is rated at %d." % (item, rating)

# # print ratings.items()


def get_ratings_from_disk():

    score_file = open("scores.txt")

    ratings = {}

    for line in score_file:
        line = line.rstrip()
        restaurant = line.split(':')
        restaurant_name = restaurant[0]
        restaurant_rating = int(restaurant[1])
        #ratings[restaurant_name] = ratings.get(restaurant_name, 0)
        ratings[restaurant_name] = restaurant_rating

    return ratings


#def get_user_rating():
main_ratings = {}

user_restaurant_name = raw_input("Please enter a restaurant name: ")
user_restaurant_rating = int(raw_input("Please enter the restaurant score: "))
main_ratings = get_ratings_from_disk()
main_ratings[user_restaurant_name] = user_restaurant_rating

for item, rating in sorted(main_ratings.items()):
    print "%s is rated at %d." % (item, rating)
