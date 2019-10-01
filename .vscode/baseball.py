
import re, sys, os
# Code below was obtained and modified from the "Command-Line Expressions" section of the Python class wiki
if len(sys.argv) < 2:
    sys.exit(f"Usage: {sys.argv[0]} filename")

filename = sys.argv[1]

if not os.path.exists(filename):
    sys.exit(f"Error: File '{sys.argv[1]}' not found")

# Code below was obtained and modified from the "Python" section of the Regular Expressions class wiki
name_regex = re.compile(r"\b([A-Z][A-Za-z]+ [A-Z][A-Za-z]+)\b")
atbats_regex = re.compile(r"\bbatted (\d+)\b")
hits_regex = re.compile(r"\b(\d+) hits\b")
runs_regex = re.compile(r"\b(\d+) runs\b")

def namer(test):
    #.search() function found on https://docs.python.org/3/howto/regex.html
	match = name_regex.match(test)
	if match is not None:
		return match.group(1)
	else:
		return False

def atbat(test):
    #.search() function found on https://docs.python.org/3/howto/regex.html
	match = atbats_regex.search(test)
	if match is not None:
		return match.group(1)
	else:
		return False

def hitscalc(test):
    #.search() function found on https://docs.python.org/3/howto/regex.html
	match = hits_regex.search(test)
	if match is not None:
		return match.group(1)
	else:
		return False

def runscalc(test):
    #.search() function found on https://docs.python.org/3/howto/regex.html
	match = runs_regex.search(test)
	if match is not None:
		return match.group(1)
	else:
		return False

class Player:
    def __init__(self, name, atbats, hits):
        self.name = name
        self.atbats = atbats
        self.hits = hits
    def addBats(self, num):
        self.atbats = self.atbats + num
    def addHits(self, num):
        self.hits = self.hits + num
    def getBA(self):
        if self.atbats==0:
            return 0.000
        else:
            return self.hits/self.atbats

def batavg(player):
    return player.getBA()

players = {}
# with clause code below found and modified from "File I/O" section of Python class wiki
with open(filename) as f:
    for line in f:
        stringtxt = line.strip()
        if (namer(stringtxt)!=False):
            name = namer(stringtxt)
            atbats = int(atbat(stringtxt))
            hits = int(hitscalc(stringtxt))
            runs = int(runscalc(stringtxt))
            if name in players:
                players[name].addBats(atbats)
                players[name].addHits(hits)
            else:
                player = Player(name, atbats, hits)
                players[name] = player 


# Code for moving dictionary values to list from https://stackoverflow.com/questions/1679384/converting-dictionary-to-list
# .values() function found on https://www.geeksforgeeks.org/iterate-over-a-dictionary-in-python/
sortedPlayers = []
for player in players.values():
    sortedPlayers.append(player)

# key and reverse variables understood from https://www.programiz.com/python-programming/methods/list/sort
sortedPlayers.sort(key=batavg, reverse=True)

# round() function found on https://www.w3schools.com/python/ref_func_round.asp
# format() funcation found on https://stackoverflow.com/questions/15619096/add-zeros-to-a-float-after-the-decimal-point-in-python
for player in sortedPlayers:
    print(f"{player.name}: {format(round(player.getBA(), 3), '.3f')}")