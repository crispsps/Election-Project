import random

class Voter:
    def __init__(self, name, age, party, state, id_number):
        self.name = name
        self.age = age
        self.party = party
        self.state = state
        self.id_number = id_number

    def vote(self, election):
        voter_data = {
            "name": self.name,
            "age": self.age,
            "party": self.party,
            "state_address": self.state,
            "id_number": self.id_number,
        }
        election.add_voter(voter_data)


class Election:
    def __init__(self):
        self.voters = []

    def add_voter(self, voter_data):
        self.voters.append(voter_data)

    def display_voters(self):
        for i in self.voters:
            print(i)
       
def display_election_results(election):
    # Calculate age range
    youngest_voter = min(voter["age"] for voter in election.voters)
    oldest_voter = max(voter["age"] for voter in election.voters)
    age_range = f"{youngest_voter}-{oldest_voter}"

    # Calculate average age
    total_age = sum(voter["age"] for voter in election.voters)
    average_age = total_age / len(election.voters)

    # Count votes for each party
    party_votes = {}
    for voter in election.voters:
        party = voter["party"]
        if party not in party_votes:
            party_votes[party] = 0
        party_votes[party] += 1
    # Display results
    print("Election Results:")
    print(f"- Age Range: {age_range}")
    print(f"- Average Age: {average_age}")
    print(f"- Votes by Party: {party_votes}")
       
voter_names = ["Jack", "Jane", "Bob", "Alice", "Tom", "Mary", "David", "Sarah", "Michael", "Jessica", "Chris", "Amanda", "Matthew", "Elizabeth", "Joshua", "Emily", "Andrew", "Olivia", "Daniel", "Lily", "James", "Isabella", "Joseph", "Ava", "William", "Mia", "Ryan", "Charlotte", "Nicholas", "Abigail"]
voter_ages = [random.randint(16, 80) for _ in range(30)]
voter_parties = ["Donut", "Ice Cream"]
voter_states = ["CA", "TX", "FL", "NY", "PA", "IL", "OH", "MI", "NC", "GA"]

voters = []

for i in range(5):
    name = random.choice(voter_names)
    age = voter_ages[i]
    party = random.choice(voter_parties)
    state = random.choice(voter_states)
    id_number = str(random.randint(000, 999))
    voter = Voter(name, age, party, state, id_number)

    # Check if voter is at least 18 years old
    if age >= 18:
        voter = Voter(name, age, party, state, id_number)
        voters.append(voter)
    else:
        print(f"{name} is not eligible to vote because they are under 18 years old.")
# Example usage:
#added voters to election
election = Election()

while voters:
    v = voters.pop(0)  # dequeue the first voter
    v.vote(election)  # voter votes
# print("Election results:", election.voters)
election.display_voters()
display_election_results(election) #changed from election

# Output:
# {'name': 'Jack', 'age': 56, 'party': 'Ice Cream', 'state_address': 'OH', 'id_number': '944'}
# {'name': 'Ryan', 'age': 32, 'party': 'Donut', 'state_address': 'CA', 'id_number': '992'}
# {'name': 'Daniel', 'age': 78, 'party': 'Ice Cream', 'state_address': 'OH', 'id_number': '301'}
# {'name': 'Jessica', 'age': 32, 'party': 'Donut', 'state_address': 'CA', 'id_number': '21'}
# {'name': 'Matthew', 'age': 18, 'party': 'Donut', 'state_address': 'OH', 'id_number': '517'}
# Election Results:
# - Age Range: 18-78
# - Average Age: 43.2
# - Votes by Party: {'Ice Cream': 2, 'Donut': 3}
