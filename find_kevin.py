# Reads the JSON files in the directory and constructs a graph.

# Dict of names has pointers to nodes for each actor.

import json
import sys
import os

# node class for actors
class Node(object):
	def __init__(self, name):
		self.name = name
		self.edges = []

	def addEdge(self, actor, film):
		self.edges.append((actor,film))


# function to load data from json files
def load_data(files):
	actordict = {}
	for filename in files:
		json_data=open("films/"+ filename).read()
		data = json.loads(json_data)
		filmname = data["film"]["name"]
		castlist = data['cast']

		# for each actor in the cast
		for c in range(0,len(castlist)):
			# if they have already been seen, get their node pointer
			if castlist[c]['name'] in actordict:
				actornode = actordict[castlist[c]['name']]

			# else create a new one
			else:
				actornode = Node(castlist[c]['name'])
				actordict[castlist[c]['name']] = actornode

			# for all the other actors, add an edge connecting them
			for a in range(c+1,len(castlist)):
					actornode.addEdge(castlist[a]['name'], filmname)

	return actordict

# function for computing dijsktra's algorithm on graph of actors
def find_kevin_bacon(actordict, name):
	# check for the man himself
	if name == "Kevin Bacon":
		return 2
	# check for unknown actor
	elif name not in actordict:
		return 0
	else:
		# create queue structure to hold actor node accessors and past path
  		queue = [(name, [(name, "start")])]
  		while queue:
  			(vertex, path) = queue.pop(0)
  			# iterate through the potential paths away from this actor, minus any already taken
  			for nextnode in set(actordict[vertex].edges) - set(path):
  				if nextnode[0] == "Kevin Bacon":
  					return path + [nextnode]
  				else:
  					queue.append((nextnode[0], path + [nextnode]))
  		# return error code for Kevin not connected
  		return 1

def pretty_print(path):
	print path[0][0],
	for p in path[1:]:
		print "-(" + p[1] + ")->" + p[0],


def main(arg):
	# -----
	# file directory to look in for film jsons, CHANGE THIS!!
	files = os.listdir("/Users/samantha/Documents/films/films/")
	# ----- 
	actordict = load_data(files)
	resp = find_kevin_bacon(actordict, arg)
	if resp == 0:
		print "I don't know this actor!"
	elif resp == 1:
		print "Kevin Bacon is not connected to this actor!"
	elif resp == 2:
		print "You gave me Kevin! Trickster"
	else:
		pretty_print(resp)

if __name__ == "__main__":
	for arg in sys.argv[1:]:
		main(arg)
		print ""

