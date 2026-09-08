class DormRoom:
    def __init__(self, room_number: str, dorm_assignment: str):
        # Public datafields for the class
        
        self.room_number = room_number
        self.dorm_assignment = dorm_assignment

        # Private datafields for the class

        self.__occupant_count = 0
        self.__occupants = []
        self.__bunk = {}

    def add_student(self, student_name: str, bed_type: str = "single"):
        """
        Receives parameters, changes private state in a safe manner
        """
        if student_name in self.__occupants:
            print(f"[{self.room_number}] {student_name} is already in this room.")
            return
            
        self.__occupants.append(student_name)
        self.__bunk[student_name] = bed_type
        self.__occupant_count += 1
        print(f"{self.room_number} --- Added {student_name} --- {bed_type}")
        
    def remove_student(self, student_name: str):
        """
        Remove student, updates private datafields
        """
        if student_name in self.__occupants:
            self.__occupants.remove(student_name)
            del self.__bunk[student_name]
            self.__occupant_count -= 1
            print(f"{self.room_number} --- Removed {student_name}.")
        else:
            print(f"{self.room_number} {student_name} not found in room.")

    def available_beds(self):
        """
        Reads/returns private state in also a safe manner
        """
        max_capacity = 6  
        available = max_capacity - self.__occupant_count
        return {
            "room": self.room_number,
            "dorm": self.dorm_assignment,
            "occupant_count": self.__occupant_count,
            "available_beds": max(0, available),
            "occupants": self.__occupants.copy(),
            "bunk_assignments": self.__bunk.copy()
        }


if __name__ == "__main__":  # Testing
    room1 = DormRoom("204", "Dorm 1")
    room2 = DormRoom("314", "Dorm 2")
    
    print("------------Before----------")
    print("Object 1:", room1.available_beds())
    print("Object 2:", room2.available_beds())
    print("---------------PERFORMING ACTION ON OBJECT 1-------------")
    room1.add_student("Alex", "lower bunk")
    room1.add_student("AnotherAlex", "upper bunk")

    print("----------AFTER------------")
    print("Object 1:", room1.available_beds())
    print("Object 2:", room2.available_beds())
