import media
import page_genrator

# Six instances of the class Movie
deadpool = media.Movie(
    "Deadpool (2016)",
    "https://image.tmdb.org/t/p/w1280/30c5jO7YEXuF8KiWXLg9m28GWDA.jpg",
    "https://www.youtube.com/watch?v=9vN6DHB6bJc",
    "Deadpool tells the origin story of former Special Forces operative turned mercenary "
    "Wade Wilson, who after being subjected to a rogue experiment that leaves him with "
    "accelerated healing powers, adopts the alter ego Deadpool. Armed with his new abilities "
    "and a dark, twisted sense of humor, Deadpool hunts down the man who nearly destroyed his life.")

doctor_strange = media.Movie(
    "Doctor Strange (2016)",
    "https://image.tmdb.org/t/p/w1280/4PiiNGXj1KENTmCBHeN6Mskj2Fq.jpg",
    "https://youtu.be/9Golt91teTQ",
    "After his career is destroyed, a brilliant but arrogant surgeon gets a new "
    "lease on life when a sorcerer takes him under his wing and trains him to defend the world against evil.")

captain_amarica = media.Movie(
    "Captain America: Civil War (2016)",
    "https://image.tmdb.org/t/p/w1280/kSBXou5Ac7vEqKd97wotJumyJvU.jpg",
    "https://youtu.be/dKrVegVI0Us",
    "Following the events of Age of Ultron, the collective governments of the world pass an act designed to "
    "regulate all superhuman activity. This polarizes opinion amongst the Avengers, causing two factions to"
    "side with Iron Man or Captain America, which causes an epic battle between former allies.")

beast = media.Movie(
    "Fantastic Beasts and Where to Find Them (2016)",
    "https://image.tmdb.org/t/p/w1280/dXwbjYyZH1Se0IS3oVcPdvueLKd.jpg",
    "https://youtu.be/YdgQj7xcDJo",
    "In 1926, Newt Scamander arrives at the Magical Congress of the United States "
    "of America with a magically expanded briefcase, which houses a number of dangerous"
    " creatures and their habitats. When the creatures escape from the briefcase, it sends"
    " the American wizarding authorities after Newt, and threatens to strain even further the"
    "state of magical and non-magical relations.")

batman = media.Movie(
    "Batman v Superman: Dawn of Justice (2016)",
    "https://image.tmdb.org/t/p/w1280/cGOPbv9wA5gEejkUN892JrveARt.jpg",
    "https://youtu.be/IwfUnkBfdZ4",
    "Fearing the actions of a god-like Super Hero left unchecked, Gotham City’s own formidable,"
    " forceful vigilante takes on Metropolis’s most revered, modern-day savior, while the world"
    "wrestles with what sort of hero it really needs. And with Batman and Superman at war with "
    "one another, a new threat quickly arises, putting mankind in greater danger than it’s ever known before.")

split = media.Movie(
    "Split (2016)",
    "https://image.tmdb.org/t/p/w1280/rXMWOZiCt6eMX22jWuTOSdQ98bY.jpg",
    "https://youtu.be/KIpGKumxiGg",
    "Though Kevin has evidenced 23 personalities to his trusted psychiatrist, "
    "Dr. Fletcher, there remains one still submerged who is set to materialize "
    "and dominate all the others. Compelled to abduct three teenage girls led by "
    "the willful, observant Casey, Kevin reaches a war for survival among all of those "
    "contained within him — as well as everyone around him — as the walls between his compartments shatter apart.")

movies = [deadpool, doctor_strange, captain_amarica, beast, batman, split]

# Create and open the movie website .html file
page_genrator.open_movies_page(movies)
