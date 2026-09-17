# Class Relationships: Association and Multiplicity
## Previous Work
([Part I - Classes and Objects](https://github.com/amcoleto/9platinumcs3/blob/main/q1/classObjectUML.md))
([Part II - Class Attributes and Methods](https://github.com/amcoleto/9platinumcs3/blob/main/q1/classAttributesMethods.md))
## Existing Class
Class: DormRoom
Description: This class represents a dorm room in PSHS. It has the room number, number of occupants, name of the occupants, and the place where the occupant sleeps (single, upper bunk, or lower bunk). This class can also add students, remove students, and where the available beds are in a room.
## New Related Class
Class: Roommate
Description: This class represents a roommate in the dorm room. The class has the roommate's name, assigned chores, whether sleeping, and whether the roommate is inside the room. This class can also complain, do chores, set alarm, and study. 
## Association
Relationship: A DormRoom HAS-A Roommate
Explanation: A DormRoom can be associated with one or many Roommates, which represents the students living in that dorm room.
## Multiplicity
Multiplicity: 0..*
Explanation: A dorm room can have zero to six occupants. While a dorm room can be empty, partially full, or full, a roommate must belong to a room.
## UML Class Relationship Diagram
![Class Relationship Diagram](images/classRelationshipDiagram.png)
## Python Implementation
[View Python Source](classRelationships.py)
## Test Run
![Relationship Test Run](images/relationshipTestRun.png)
## Object Relationship Diagram
![Object Relationship Diagram](images/objectRelationshipDiagram.png)
## Analysis
### What is the association between your two classes?
### What multiplicity did you choose and why?
### How did you implement the relationship in Python?
### Why did you store an object reference instead of copying its data?
### If your relationship uses many, why is a list appropriate?