from random import choice

startups = ["Google", "Facebook", "Dropbox", "SpaceX", "Uber", "Snapchat", "Twitter", "Stripe",
            "AirBnB", "Digital Ocean", "Github", "Tinder"]

demographies = ["Pets", "the elderly", "Robots", "noisy kids", "Cats", "Fruits",
                "Programming Languages", "Teachers", "Computer Scientists", "Janitors", "Film Producers",
                "Actors"]


for _ in xrange(10000):
    print choice(startups) + " for " + choice(demographies)
