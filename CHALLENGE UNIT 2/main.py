class CricketPlayer:
    def play(self):
        print("The player is playing cricket.")

class Batsman(CricketPlayer):
    def play(self):
        print("The batsman is batting.")

class Bowler(CricketPlayer):
    def play(self):
        print("The bowler is bowling.")

# Create objects of Batsman and Bowler classes
batsman = Batsman()
bowler = Bowler()

# Call the play() method for each object
batsman.play()
bowler.play()