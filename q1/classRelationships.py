# Note: I wrote my initial structure fully.
# Used online references to correctly implement and fix syntax errors. 
class Roommate:
    def __init__(self,name: str, assigned_chores: list = None):
        self.name = name
        self.assigned_chores = assigned_chores if assigned_chores is not None else []
        self.is_sleeping = False
        self.in_room = True

    def complain(self, complaint: str):
        print(f"{self.name} says: {complaint}")

    def do_chores(self):
        if self.assigned_chores:
            chore = self.assigned_chores.pop(0)
            print(f"{self.name} finished the: {chore}")
        else:
            print(f"{self.name} have no chores left.")

    def set_alarm(self, time_str: str):
        print(f"{self.name} sets an alarm for {time_str}.")

    def study(self):
        print(f"{self.name} studies in a quiet manner.")

class DormRoom:
    def __init__(self, room_number: str, dorm_assignment: str):
        self.room_number = room_number
        self.dorm_assignment = dorm_assignment
        self.__occupant_count = 0
        self.__occupants = []  
        self.__bunk = {}

    def add_student(self, student: Roommate, bed_type: str = "single"):
        # Check if the Object is already in list
        if student in self.__occupants:
            print(f"[{self.room_number}] {student.name} is already in this room.")
            return
            
        self.__occupants.append(student)  
        self.__bunk[student.name] = bed_type
        self.__occupant_count += 1
        print(f"{self.room_number} --- Added {student.name} --- {bed_type}")

    def available_beds(self):
        max_capacity = 6  
        available = max_capacity - self.__occupant_count
        return {
            "room": self.room_number,
            "dorm": self.dorm_assignment,
            "occupant_count": self.__occupant_count,
            "available_beds": max(0, available),
            "occupants": [s.name for s in self.__occupants],
            "bunk_assignments": self.__bunk.copy()
        }


if __name__ == "__main__":  # Testing
    room1 = DormRoom("204", "Dorm 1")
    room2 = DormRoom("314", "Dorm 2")

    alex = Roommate("Alex", ["Sweep floor", "Remove the maggots in the trash can"])
    another_alex = Roommate("AnotherAlex", ["Fix bed"])
    
    print("------------Before----------")
    print("Object 1:", room1.available_beds())
    print("Object 2:", room2.available_beds())
    print("---------------PERFORMING ACTION ON OBJECT 1-------------")
    room1.add_student(alex, "lower bunk")
    room1.add_student(another_alex, "upper bunk")

    print("----------AFTER------------")
    print("Object 1:", room1.available_beds())
    print("Object 2:", room2.available_beds())