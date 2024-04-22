# Election-Project

Goal of the project: Clearly state the project's objectives.

To create an election voting system and store demographic information. 

Significance of the project: Explain the project's meaningfulness and novelty
  This is applicable to similar voting systems. Large bits of information are needed to be tracked and analyzed. If-else statements are used to check voter eligibility and voter conditions. 

Installation and Instruction to use: Provide clear installation and usage instructions.
Download files and run into a code editor.

Structure of the code: Include a systematic code structure diagram and clear explanations.
  A virtual line of voters is placed in the queue.

Functionalities and Test Results: Present functionalities and testing results for verification.
# Output:
# election.display_voters()
# {'name': 'Jack', 'age': 56, 'party': 'Ice Cream', 'state_address': 'OH', 'id_number': '944'}
# {'name': 'Ryan', 'age': 32, 'party': 'Donut', 'state_address': 'CA', 'id_number': '992'}
# {'name': 'Daniel', 'age': 78, 'party': 'Ice Cream', 'state_address': 'OH', 'id_number': '301'}
# {'name': 'Jessica', 'age': 32, 'party': 'Donut', 'state_address': 'CA', 'id_number': '21'}
# {'name': 'Matthew', 'age': 18, 'party': 'Donut', 'state_address': 'OH', 'id_number': '517'}


# display_election_results()
# Election Results:
# - Age Range: 18-78
# - Average Age: 43.2
# - Votes by Party: {'Ice Cream': 2, 'Donut': 3}


Discussion and Conclusions: Discuss project issues, limitations, and the application of course learnings.
Issues: Lot of data to store, long lines of code, 
Not easy to look at and not too organized. Isn’t too user-friendly.

Limitations: Slow Runtime with larger amount of data. 

Application:
	Use of data structures and class hierarchy. In this project, we explored the uses of dictionaries to store various types of information. Conditions and loops are used in functions in classes that interact with each other. Queue data structure is implemented where you can register a person in a line for voting, and is removed(popped) once the process of voting is done with each person.
