class Patient:
  """ This is the superclass in the Hospital Management System, representing a normal patient. Its attributes include the name of the patient (in string) and the bill amount. Meanwhile, its methods include getting the name, setting the name, getting the bill amount, setting the bill amount, calculating the bill, and displaying the patient type (in this class, it's a Normal Patient)."""
  def __init__(self, name:str, bill_amount:float):
    self.__name = name
    self.__bill_amount = bill_amount
    
  def get_name(self):   # Obtains name
    return self.__name
    
  def set_name(self,name):   # Changes name
    self.__name = name
    
  def get_bill_amount(self):   # Obtains bill amount
    return self.__bill_amount
    
  def set_bill_amount(self,bill_amount):   # Sets bill amount
    self.__bill_amount = bill_amount

  def calculate_bill(self):   # Calculates bill (for a regular patient, no discounts)
    return self.__bill_amount

  def display_patient_type(self):   # Displays the type of patient (for this class, it's a regular patient)
    return "Regular Patient"

class SeniorPatient(Patient):
  """ This is a subclass, representing an specific type of patient, a senior patient. This inherited all the attributes and methods from super class Patient. And, it also overrides 2 methods. First is the display_patient_type() method, turning it from displaying "Regular Patient" to "Senior Citizen". Second is the calculate_bill() method, taking in the 20% discount during the calculations. """
  def calculate_bill(self):   # Overrides calculate_bill(self) method from superclass
    newbill = self.get_bill_amount() *0.8   # Multiplied by 0.8 to take in the 20% discount
    return newbill

  def display_patient_type(self):   # Overrides from Parent's method, now is "Senior Citizen" instead of "Regular Patient"
    return "Senior Citizen"

class PhilHealthPatient(Patient):
  """ Similar to the SeniorCitizen subclass, it inherits all attributes and methods from Patient with overriding of display_patient_type() (but this now displays "PhilHealth Member") and calculate_bill() (taking in the 15% discount) methods. """
  def calculate_bill(self):   # Overrides calculate_bill(self) method from superclass
    newbill = self.get_bill_amount() * 0.85   # Multiplied by 0.85 to take in the 15% discount
    return newbill

  def display_patient_type(self):   # Overrides from Parent's method, similar to the SeniorCitizen class' overriding 
    return "PhilHealth Member"

p1 = Patient("Juan Dela Cruz", 15000.00)
p2 = SeniorPatient("Maria Santos", 15000.00)
p3 = PhilHealthPatient("Pedro Reyes", 15000.00)

printinglist = [p1,p2,p3]

# Output
print("Hospital Billing System")
print("-----------------------")
for person in printinglist:   # Utilize loops to not make printing process clunky
  print(f"Patient Name: {person.get_name()}")
  print(f"Patient Type: {person.display_patient_type()}")
  print(f"Original Bill: ₱{person.get_bill_amount():,.2f}")
  print(f"Final Bill: ₱{person.calculate_bill():,.2f}")
  print()

  