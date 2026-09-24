class Roommate:
    def __init__(self, name: str, assigned_chores: list = None):
        self.name = name
        self.assigned_chores = assigned_chores if assigned_chores is not None else []
        self.is_sleeping = False
        self.in_room = True

    def complain(self, complaint: str):
        print(f"{self.name} says: {complaint}")

    def do_chores(self):
        if self.assigned_chores:
            chore = self.assigned_chores.pop(0)
            print(f"{self.name} finished: {chore}")
        else:
            print(f"{self.name} has no chores left.")

    def set_alarm(self, time_str: str):
        print(f"{self.name} set an alarm for {time_str}.")

    def study(self):
        print(f"{self.name} is studying quietly.")


class Furniture:
    def __init__(self, item_id: str, condition: str = "Good"):
        self.item_id = item_id
        self.condition = condition

    def inspect(self):
        print(f"Furniture Item: {self.item_id} | Condition: {self.condition}")


class Bed(Furniture):
    def __init__(self, item_id: str, bed_type: str = "single", condition: str = "Good"):
        super().__init__(item_id, condition)
        self.bed_type = bed_type
        self.assigned_student = None

    def assign_to_student(self, student: Roommate):
        self.assigned_student = student
        print(f"Assigned bed {self.item_id} ({self.bed_type}) to {student.name}.")


class DormRoom:
    def __init__(self, room_number: str, dorm_assignment: str):
        self.room_number = room_number
        self.dorm_assignment = dorm_assignment
        self.__occupant_count = 0
        self.__occupants = []  
        self.__beds = []        

    def add_bed(self, bed: Bed):
        self.__beds.append(bed)
        print(f"Room {self.room_number}: Added bed {bed.item_id} ({bed.bed_type})")

    def add_student(self, student: Roommate, bed: Bed):
        if student in self.__occupants:
            print(f"Room {self.room_number}: {student.name} is already in this room.")
            return

        if bed not in self.__beds:
            print(f"Room {self.room_number}: Bed {bed.item_id} is not in this room.")
            return
            
        self.__occupants.append(student)
        bed.assign_to_student(student)
        self.__occupant_count += 1
        print(f"Room {self.room_number}: Added {student.name} to {bed.bed_type}")

    def remove_student(self, student: Roommate):
        if student in self.__occupants:
            self.__occupants.remove(student)
            self.__occupant_count -= 1
            for bed in self.__beds:
                if bed.assigned_student == student:
                    bed.assigned_student = None
            print(f"Room {self.room_number}: Removed {student.name}.")
        else:
            print(f"Room {self.room_number}: {student.name} is not in this room.")

    def available_beds(self):
        max_capacity = 6
        available = max_capacity - self.__occupant_count
        return {
            "room": self.room_number,
            "dorm": self.dorm_assignment,
            "occupant_count": self.__occupant_count,
            "available_beds": max(0, available),
            "occupants": [s.name for s in self.__occupants],
            "beds": [f"{b.item_id} ({b.bed_type})" for b in self.__beds]
        }


if __name__ == "__main__":
    # Setup of Beds
    bed1 = Bed("Bed 1", bed_type="lower bunk", condition="New")
    bed2 = Bed("Bed 2", bed_type="upper bunk", condition="Good")

    bed1.inspect()  
    print(f"Bed Type: {bed1.bed_type}")

    # Setup of Students
    alex = Roommate("Alex", ["Sweep floor", "Remove maggots in the trash can"])
    another_alex = Roommate("AnotherAlex", ["Fix bed"])

    # Setup dorm room and assign the objects according to their bed and person
    room1 = DormRoom("204", "Dorm 1")

    room1.add_bed(bed1)
    room1.add_bed(bed2)

    room1.add_student(alex, bed1)
    room1.add_student(another_alex, bed2)

    # Print room info
    print("\nRoom Summary:")
    print(room1.available_beds())

    # Remove student and check independence
    print("\nRemoving Student:")
    room1.remove_student(alex)
    print(f"Is {alex.name} still available in system? Yes, remaining chores: {alex.assigned_chores}")