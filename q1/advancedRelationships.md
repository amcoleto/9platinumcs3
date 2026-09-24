# Advanced Class Relationships
## Previous Activities
[classAttrib](https://github.com/amcoleto/9platinumcs3/blob/main/q1/classAttributesMethods.md)
[classRel](https://github.com/amcoleto/9platinumcs3/blob/main/q1/classRelationships.md)
## Existing System Description:
The system exhibits properties and actions in a designated dorm room ('DormRoom'), and having an ownership on a student occupant ('Roommate'). 'Roommate' exhibits individual students' data like their name, what 'Roommate' can do include chores assigned, studying, setting alarms, and complaining. Meanwhile, the dorm room 'DormRoom' class has an ownership on 'Roommate'. 'DormRoom' has its room number, dorm assignments, and occupant count. It can do adding or removing 'Roommate' objects, tracking bunk bed aassignments as well as bed capacity in a room.

## Inheritance Relationship
Parent: Furniture
Child: Bed
Explanation: A bed is a specific type of furniture in a dorm. In a dorm room, overall furniture will share properties like 'condition' and 'ID', but introduce properties like assigned students and the bed type; therefore, 'Furniture' inherits 'Bed'.

## Inheritance UML
![Inheritance](Images/inheritanceUMLDiagram.png)
## Composition/Aggregation
Relationship: Aggregation 
Explanation: 'DormRoom' is like a container for 'Roommate' or residents, as well as 'Bed'. Additionally, they will still exist even if they are unassigned or 'DormRoom' is destroyed.
## Advanced UML Diagram
![Advanced UML](Images/advancedClassDiagram.png)
## Python Implementation
[Source Code](advancedRelationships.py)
## Test Run
![Test](Images/advancedTestRun.png)
## Object Diagram
![Objects](images/advancedObjectDiagram.png)

## Reflection
Answers:
