class Person:
    '''
    A class representing a person in a social network.
    Attributes:
        name (str): The name of the person.
        friends (list): A list of friends (Person objects).
    Methods:
        add_friend(friend): Adds a friend to the person's friend list.
   '''
    def __init__(self, name):
        self.name = name
        self.friends = []

    def add_friend(self, friend):
        if friend not in self.friends:
            self.friends.append(friend)


class SocialNetwork:
    '''
    A class representing a social network.
    Attributes:
        people (dict): A dictionary mapping names to Person objects.
    Methods:
        add_person(name): Adds a new person to the network.
        add_friendship(person1_name, person2_name): Creates a friendship between two people.
        print_network(): Prints the names of all people and their friends.
    '''
    def __init__(self):
        self.people = {}

    def add_person(self, name):
        if name not in self.people:
            self.people[name] = Person(name)

    def add_friendship(self, person1_name, person2_name):
        if person1_name in self.people and person2_name in self.people:
            person1 = self.people[person1_name]
            person2 = self.people[person2_name]

            person1.add_friend(person2)
            person2.add_friend(person1)
        else:
            if person1_name not in self.people:
                print(f"Friendship could not be created, {person1_name} not found.")
            else:
                print(f"Friendship could not be created, {person2_name} not found.")

    def print_network(self):
        for person_name, person_obj in self.people.items():
            friendship_names = [p.name for p in person_obj.friends]

            friendships = ", ".join(friendship_names)
            print(f"{person_name} is friends with: {friendships}")

network = SocialNetwork()

# adding people to the network
network.add_person("Jacob")
network.add_person("Tyler") 
network.add_person("Daniel")
network.add_person("Eric")
network.add_person("Morgan")
network.add_person("Riley")

# adding friendships to the network
network.add_friendship("Jacob", "Tyler")
network.add_friendship("Jacob", "Daniel")
network.add_friendship("Tyler", "Eric")
network.add_friendship("Daniel", "Morgan")
network.add_friendship("Eric", "Riley")
network.add_friendship("Morgan", "Riley")
network.add_friendship("Daniel", "Riley")
network.add_friendship("Jacob", "Eric")

# adding friendships for people not in the network
network.add_friendship("Tyler", "Nathan") 
network.add_friendship("Casey", "Eric")
network.add_friendship("Brendan", "Michael")

# printing the network after all changes
network.print_network()

'''
DESIGN MEMO
'''