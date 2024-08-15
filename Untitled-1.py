from art import *
import random
from IPython.display import clear_output
tprint("High & Lower Game")


# Dictionary of famous stars with their number of followers (in millions)
famous_stars = {
    "Tom Cruise": 9,
    "Scarlett Johansson": 12,
    "Dwayne Johnson": 350,
    "Leonardo DiCaprio": 54,
    "Emma Watson": 65,
    "Will Smith": 62,
    "Jennifer Lawrence": 24,
    "Chris Hemsworth": 56,
    "Robert Downey Jr.": 50,
    "Angelina Jolie": 13
}

# Dictionary of famous players with their number of followers (in millions)
famous_players = {
    "Cristiano Ronaldo": 500,
    "Lionel Messi": 420,
    "LeBron James": 150,
    "Roger Federer": 10,
    "Virat Kohli": 250,
    "Serena Williams": 15,
    "Neymar Jr.": 200,
    "Rafael Nadal": 12,
    "Tiger Woods": 5,
    "Michael Jordan": 25
}

# Dictionary of famous business persons with their number of followers (in millions)
famous_business_persons = {
    "Elon Musk": 130,
    "Jeff Bezos": 4,
    "Bill Gates": 75,
    "Mark Zuckerberg": 10,
    "Warren Buffett": 1.5,
    "Richard Branson": 12,
    "Jack Ma": 2,
    "Tim Cook": 12,
    "Sundar Pichai": 1.2,
    "Satya Nadella": 1
}

# Dictionary of famous places with their number of followers (in millions)
famous_places = {
    "Eiffel Tower": 8,
    "Great Wall of China": 3,
    "Taj Mahal": 4,
    "Statue of Liberty": 2,
    "Machu Picchu": 1,
    "Colosseum": 1.5,
    "Pyramids of Giza": 1.8,
    "Grand Canyon": 1.2,
    "Sydney Opera House": 2.5,
    "Mount Fuji": 0.5
}

# Dictionary of famous companies with their number of followers (in millions)
famous_companies = {
    "Apple": 50,
    "Microsoft": 15,
    "Amazon": 30,
    "Google": 70,
    "Facebook": 40,
    "Tesla": 25,
    "Alibaba": 10,
    "Berkshire Hathaway": 1,
    "Visa": 5,
    "Johnson & Johnson": 4
}

# Dictionary of famous singers with their number of followers (in millions)
famous_singers = {
    "Ariana Grande": 240,
    "Justin Bieber": 220,
    "Taylor Swift": 230,
    "Katy Perry": 110,
    "Rihanna": 150,
    "Beyoncé": 200,
    "Billie Eilish": 100,
    "Selena Gomez": 210,
    "Ed Sheeran": 140,
    "Shawn Mendes": 70
}

all_item_list = [famous_stars,famous_business_persons,famous_companies,famous_places,famous_players,famous_singers]
all_item_list_str = ["famous star","famous business person","famous companie ","famous place ","famous player ","famous singer "]


def randomly_chosen():
    randomly_chosen_list = random.randint(0,len(all_item_list)-1) 
    random_chosen_person_place = random.choice(list(all_item_list[randomly_chosen_list]))
    return  all_item_list_str[randomly_chosen_list],random_chosen_person_place , all_item_list[randomly_chosen_list][random_chosen_person_place]
    

def chosen_2_famous_things():
    first_random_chosen = randomly_chosen()
    second_random_chosen = randomly_chosen()
    
    wrong_input = True
    while wrong_input:
        global user_answer
        user_answer = input(f"Choose who do you think have high followers? The {first_random_chosen[0]} {first_random_chosen[1]} or {second_random_chosen[0]} {second_random_chosen[1]}? Type A or B for the answer: " ).lower()
        if user_answer in ["a","b"]:
            wrong_input = False
        else:
            print("Game Right Input")
            wrong_input = True
            
    comparing = compareing_the_highest_followers(first_number=first_random_chosen[2],second_number=second_random_chosen[2])
    
    if user_answer == comparing:
        print("Right Answer")
        print(f"The {first_random_chosen[1]} has {first_random_chosen[2]} Millions followers and the {second_random_chosen[1]} has {second_random_chosen[2]} Million followes")
        return 1
    else:
        print("You loose")
        print(f"The {first_random_chosen[1]} has {first_random_chosen[2]} Million followers and the {second_random_chosen[1]} has {second_random_chosen[2]} Million followes")
        return 0
            
    

        
    
def compareing_the_highest_followers(first_number, second_number):
    if first_number > second_number:
        return "a"
    else:
        return "b"
        
        
def play_again():
    play_again_input = input("To play again press 'y' or press any key to exit: ").lower()
    if play_again_input == "y":
        return True
    else:
        print("Thanks for playing")
        False
        
game_running = True
game_point = 0
while game_running:
    game_backend = chosen_2_famous_things()
    if game_backend == 1:
        game_point += 1
    else:
        print(f"Your Total point is {game_point}")
        game_running = play_again()