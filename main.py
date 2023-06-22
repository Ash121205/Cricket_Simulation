import random

class Player:
    def __init__(self, name, bowling, batting, fielding, running, experience):
        self.name = name
        self.bowling = bowling
        self.batting = batting
        self.fielding = fielding
        self.running = running
        self.experience = experience

    def get_probability(self, event):
        if event == "bowling":
            return self.bowling
        elif event == "batting":
            return self.batting
        elif event == "fielding":
            return self.fielding
        elif event == "running":
            return self.running
        elif event == "experience":
            return self.experience
        else:
            raise ValueError("Invalid event")

class Team:
    def __init__(self, players):
        self.players = players

    def select_captain(self):
        return random.choice(self.players)

    def send_next_player_to_field(self):
        return random.choice(self.players)

    def choose_bowler_for_over(self):
        return random.choice(self.players)

    def decide_batting_order(self):
        return random.shuffle(self.players)

class Field:
    def __init__(self, field_size, fan_ratio, pitch_conditions, home_advantage):
        self.field_size = field_size
        self.fan_ratio = fan_ratio
        self.pitch_conditions = pitch_conditions
        self.home_advantage = home_advantage

    def get_probability(self, event):
        if event == "field_size":
            return self.field_size
        elif event == "fan_ratio":
            return self.fan_ratio
        elif event == "pitch_conditions":
            return self.pitch_conditions
        elif event == "home_advantage":
            return self.home_advantage
        else:
            raise ValueError("Invalid event")

class Umpire:
    def __init__(self, players, field):
        self.players = players
        self.field = field

    def chunk_probabilities(self):
        probabilities = {}
        for player in self.players:
            for event in ["bowling", "batting", "fielding", "running", "experience"]:
                probability = player.get_probability(event)
                if event not in probabilities:
                    probabilities[event] = []
                probabilities[event].append(probability)
        return probabilities

    def predict_outcome_of_ball(self):
        probabilities = self.chunk_probabilities()
        event = random.choice(list(probabilities.keys()))
        probability = random.choice(probabilities[event])
        if probability > 0.5:
            return "success"
        else:
            return "failure"

class Commentator:
    def __init__(self, umpire):
        self.umpire = umpire

    def provide_commentary_for_ball(self, ball_number, runs):

        commentary = " On ball {}.".format(ball_number)
        if runs == -1:
            commentary += "Oh! The batsman has been dismissed!"
        elif runs == 0:
            commentary += "The batsman has played a dot ball, {} runs".format(runs)
        elif runs == 1:
            commentary += "The batsman has played a single, {} run.".format(runs)
        elif runs < 4:
            commentary += "The batsman has scored {} runs.".format(runs)
        elif runs == 4:
            commentary += "The batsman has hit a boudary, {} runs.".format(runs)
        elif runs == 6:
            commentary += "The batsman has hit a six! {} runs.".format(runs)
        else:
            commentary += "That's an overthrow! {} runs.".format(runs)

        return commentary


players = [
        Player("MS Dhoni", 0.2, 0.8, 0.99, 0.8, 0.9),
        Player("Virat Kohli", 0.5, 0.9, 0.98, 0.9, 0.8),
        Player("Rohit Sharma", 0.4, 0.8, 0.97, 0.8, 0.7),
    ]
field = Field(100, 0.5, "good", 0.2)
umpire = Umpire(players, field)
commentator = Commentator(umpire)
runs_scored = 0
for ball_number in range(1, 7):
    runs = random.randint(-1, 6)
    if umpire.predict_outcome_of_ball() == False:
        runs_scored += 0
    else:
        runs_scored += runs
    comment = commentator.provide_commentary_for_ball(ball_number, runs)
    if comment.__contains__("dismissed"):
        runs_scored -= runs
    print(comment)
print("Total runs scored in the over:", runs_scored)