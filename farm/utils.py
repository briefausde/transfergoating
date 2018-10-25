from random import choice, randint
from .models import *


HERDER_NAMES = ('John', 'Savage', 'Robert', 'Michael', 'Harry', 'Henry', 'Alex')
GOAT_NAMES = ('Acorn', 'Alvin', 'Asia', 'Audi', 'Bagel', 'Balou', 'Barclay', 'Barney', 'Beck', 'Bellatrix',
              'Bianca', 'Biloxi', 'Birdie', 'Biscuit', 'Blanca', 'Bobbafett', 'Bodie', 'Bono', 'Booboo',
              'Bootsie', 'Bordeaux', 'Brandy', 'Bren', 'Bronco', 'Bruin', 'Bubbles', 'Buffy', 'Burt', 'Butler',
              'Button', 'Calvin', 'Candy', 'Carter', 'Cece', 'Cessa', 'Chandler', 'Chaucer', 'Chevy', 'China',
              'Choochoo', 'Cisco', 'Claire', 'Cleopatra', 'Clooney', 'Coco(nut)', 'Connor', 'Cosmo', 'Crosby',
              'Cupcake', 'Daisy', 'Dallas', 'Daphne', 'Delilah', 'Diva', 'Doc', 'Domino', 'Donna', 'Donovan',
              'Dulus', 'Dutch', 'Ebony', 'Ed', 'Elton', 'Elwood', 'Ernie', 'Faith', 'Faya', 'Felix', 'Fig',
              'Fiona', 'Foxy', 'Fritz', 'Fuse', 'Giblet', 'Gibson', 'Gingi', 'Goofy', 'Graysen', 'Greystoke',
              'Guinness', 'Hershey', 'Holly', 'Honey', 'Huck Finn', 'Hudson', 'Hutch', 'Ike', 'Indira', 'Iris',
              'Ivory', 'Jade', 'Jasmine', 'Jasper', 'Jazzy', 'Jeeves', 'Jenna', 'Jenne', 'Joy', 'Kai', 'Kalua',
              'Kaly', 'Kassie', 'Kaya', 'Keanna', 'Keesha', 'Keiko', 'Kiefer', 'Kingston', 'Koby', 'Kona',
              'Laguna', 'Landon', 'Larissa', 'Lefty', 'Leia', 'Lexi', 'LilвЂ™bit', 'Lilypie', 'Linus', 'Logan',
              'Lola', 'Luca', 'Lucy', 'Luke', 'Madonna', 'Malble', 'Malibu', 'Margo', 'Marshmellow', 'Marti',
              'Max', 'Maya', 'Meadow', 'Mercedes', 'Merlot', 'Merry', 'Mia', 'Midnight', 'Midori', 'Mika', 'Milan',
              'Mira', 'Mischa', 'Mitzi', 'Moby', 'Mochi', 'Monet', 'Monkey', 'Mooshie', 'Mozart', 'Mr Big',
              'Muggles', 'Mulder', 'Mulligan', 'Murphy', 'Mylo', 'Nanda', 'Nate', 'Nell', 'Niana', 'Nico',
              'Noodle', 'Nugget', 'Olive', 'Onyx', 'Otis', 'Owen', 'Ozzie', 'Paddington', 'Paisley', 'Paris',
              'Parker', 'Paulie', 'Pazzo', 'Peanut', 'Pearl', 'Pepper', 'Persia', 'Pesci', 'Phoenix', 'Picasso',
              'Pinot', 'Pipsie', 'Pixie', 'Porche', 'Quattro', 'Ramona', 'Redford', 'Reece', 'Rico', 'Robin Hood',
              'Rocco', 'Rocky', 'Romeo', 'Roxie', 'Rufus', 'Rusty', 'Scotty', 'Scout', 'Shadow', 'Shaggy', 'Shane',
              'Shaq', 'Sheba', 'Silas', 'Skip', 'Skitty', 'Skyler', 'Smitty', 'Snooky', 'Snoopy', 'Sookie',
              'Spark', 'Sprite', 'Stitch', 'Strsky', 'Sugar', 'Summer', 'Sunny', 'Sushi', 'Sweetpea', 'Syrah',
              'Tallulah', 'Tango', 'Tank', 'Tanner', 'Tatertot', 'Theo', 'Tibbs', 'Timber', 'Tink', 'Toast',
              'Toffee', 'Tonka', 'Vegas', 'Wednesday', 'Wilbur', 'Willow', 'Winnie', 'Wolfie', 'Yoshiko', 'Zach',
              'Zara', 'Zeke', 'Zelda', 'Zeppelin', 'ZsaZsa')


def farm_init():
    """
    This function is called only when the farm is not created.
    And create farm, farmers, goats.
    """

    herder = Herder.objects.create(name='You', is_active=True)
    farm = Farm.objects.create(herder=herder)

    for name in GOAT_NAMES[randint(1, len(GOAT_NAMES))]:
        Goat.objects.create(name=name, herder=farm.herder)


def herder_create():
    herder = Herder.objects.create(name=choice(HERDER_NAMES))

    for _ in range(randint(1, len(GOAT_NAMES))):
        Goat.objects.create(name=choice(GOAT_NAMES), herder=herder)

    return herder
