# Madlibs python program

# string concatination (aka how to put strings together)
# suppose you want to create a string that says "subscribe to Pewdiepie"
# youtuber = "Pewdiepie" # some string variable

# a few ways to do this
# print("Subscribe To " + youtuber);
# print("Subscribe To {}".format(youtuber));
# print(f"Subscribe To {youtuber}");

adj = input("Adjective: ")
verb1 = input("Verb: ")
verb2 = input("Verb: ")
friends_name = input("Friends name: ")

madlib = f"APUSH is so {adj}! It makes me want to {verb1} because it's too much work and isn't even intellectually stimulating. I honestly might {verb2} every time I have that class with {friends_name} because it's so boring!"

print(madlib);