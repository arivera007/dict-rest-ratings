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
        ratings[restaurant[0]] = int(restaurant[1])

    return ratings


def view_ratings():

    for item, rating in sorted(main_ratings.items()):
        print "%s is rated at %d." % (item, rating)


def add_rating():

    user_restaurant_name = raw_input("Please enter a restaurant name: ")
    user_restaurant_rating = int(raw_input("Please enter the restaurant score: "))
    main_ratings[user_restaurant_name] = user_restaurant_rating
    view_ratings()


def execute_user_choice(choice):
    while choice != "3":
        if choice == "1":
            view_ratings()
        elif choice == "2":
            add_rating()
        else:
            get_user_choice()
        break

main_ratings = {}

main_ratings = get_ratings_from_disk()


def get_user_choice():
    print "Would you like to: "
    print "1. see all ratings in alpha order"
    print "2. add a new restaurant"
    print "3. Quit"
    execute_user_choice(raw_input("Enter 1, 2, 3: "))

#get_user_choice()

# while user_input != "3":

#     if user_input == "1":
#         view_ratings()
#     elif user_input == "2":
#         add_rating()
#     else:
#         user_input = '3'

while True:
    print "Would you like to: "
    print "1. see all ratings in alpha order"
    print "2. add a new restaurant"
    print "3. Quit"
    choice = raw_input("Enter 1, 2, 3: ")
    if choice == "1":
        view_ratings()
    elif choice == "2":
        add_rating()
    else:
        # get_user_choice()
        break
