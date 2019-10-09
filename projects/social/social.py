import random
import math

class User:
    def __init__(self, name):
        self.name = name

class SocialGraph:
    def __init__(self):
        self.lastID = 0
        self.users = {}
        self.friendships = {}

    def addFriendship(self, userID, friendID):
        """
        Creates a bi-directional friendship
        """
        if userID == friendID:
            print("WARNING: You cannot be friends with yourself")
        elif friendID in self.friendships[userID] or userID in self.friendships[friendID]:
            print("WARNING: Friendship already exists")
        else:
            self.friendships[userID].add(friendID)
            self.friendships[friendID].add(userID)

    def addUser(self, name):
        """
        Create a new user with a sequential integer ID
        """
        self.lastID += 1  # automatically increment the ID to assign the new user
        self.users[self.lastID] = User(name)
        self.friendships[self.lastID] = set()

    def populateGraph(self, numUsers, avgFriendships):
        """
        Takes a number of users and an average number of friendships
        as arguments

        Creates that number of users and a randomly distributed friendships
        between those users.

        The number of users must be greater than the average number of friendships.
        """
        # Reset graph
        self.lastID = 0
        self.users = {}
        self.friendships = {}
        
        # possibleFriendships = []
        totalFriendships = (avgFriendships * numUsers) // 2

        if numUsers <= avgFriendships:
            print("WARNING: number of users must be greater than average friendships.")
            return

        for i in range(1, numUsers + 1):
            self.addUser(f"TestUser{i}")
            # for j in range(i + 1, numUsers + 1):
            #     possibleFriendships.append((i, j))

        # random.shuffle(possibleFriendships)

        counter = 0
        while counter < totalFriendships:
            counter += 1
            # friendship = possibleFriendships.pop()
            friendship = (random.randint(1, numUsers), random.randint(1, numUsers))
            while friendship[0] == friendship[1] or int(friendship[1]) in self.friendships[friendship[0]]:
                friendship = (random.randint(1, numUsers), random.randint(1, numUsers))
            self.addFriendship(friendship[0], friendship[1])

    def getAllSocialPaths(self, userID):
        """
        Takes a user's userID as an argument

        Returns a dictionary containing every user in that user's
        extended network with the shortest friendship path between them.

        The key is the friend's ID and the value is the path.
        """
        visited = {}  # Note that this is a dictionary, not a set
        
        for user in self.users:
            target = int(user)
            queue = []
            cleared = set()
            queue.append([userID])
            paths = []
            
            while len(queue):
                current = queue.pop(0)
                cleared.add(current[-1])
                if current[-1] == target:
                    paths.append(current)
                for i in self.friendships[current[-1]]:
                    if i not in cleared:
                        queue.append(current + [i])
            
            if len(paths):
                min_path = paths[0]
                for i in paths:
                    if len(i) < len(min_path):
                        min_path = i
                visited[user] = min_path

        return visited


if __name__ == '__main__':
    sg = SocialGraph()
    sg.populateGraph(1000, 5)
    print(sg.friendships)
    connections = sg.getAllSocialPaths(1)
    print(connections)

