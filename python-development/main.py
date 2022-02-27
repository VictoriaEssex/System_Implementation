class Patient: #Defining a class
    def __init__(self, name, address, phone): #constructor, a function to call to make an instance of a class
        self.name = name
        self.address = address
        self.phone = phone


        """Patient to request a prescription repeat and request an appointment""" 
        #Operations

    #create method, operation
    def request_repeat_prescription(self): 
        recpetionist_request_script(self)

    def request_appointment(self, receptionist): 
        receptionist.make_appointment(self) #taking in patient #passing the patient into the receptionist and visa versa
        # we are in the patient class, so self refers to the patient


class HealthcareProfessional: #camel case for class names
    def __init__(self, name, employee_number): #argument needs to be one word 
        self.name = name
        self.employee_number = employee_number
        
        """Conducts consultation: Operation"""
        
class Doctor(HealthcareProfessional):#create a subclass
    def __init__(self, name, employee_number):
        super().__init__(name, employee_number) #calling the instance of healthcare proffessional constructor
    """issue prescription"""

class Nurse(HealthcareProfessional): 
    def __init__(self, name, employee_number):
        super().__init__(name, employee_number)

class Prescription: 
    def __init__(self, type_of_drug, patient, doctor, quantity, dosage):
        self.type_of_drug = type_of_drug
        self.patient = patient
        self.doctor = doctor
        self.quantity = quantity
        self.dosage = dosage

    def request_prescription(self, receptionist):
        prescription = Prescription()
        self.request_prescription.add_prescription(prescription)
    

class Receptionist:
    def __init__(self, name, employee_number, appointment_schedule): #attributes and constructors #argument
        self.name = name
        self.employee_number = employee_number
        self.appointment_schedule = appointment_schedule

        '''Make an appointment or cancel an appointment'''


    def make_appointment(self, patient): 
        appointment = Appointment('Pyschological Therapy', 'Dr.Ruan', patient) 
        #taking patient from line 49 and using it as an argument
        #access the attribute
        self.appointment_schedule.add_appointment(appointment) #pass in the variable created on line 50

    def cancel_appointment(self, receptionist): 
        remove = Appointment.remove()
        receptionist.cancel_appointment()
           

class Appointment: 
    def __init__(self, type_of_appointment, staff, patient):
        self.type_of_appointment = type_of_appointment
        self.staff = staff
        self.patient = patient

    def __str__(self): 
      return f' Appointment staff: {staff.name} Patient: {patient.name}'

class AppointmentSchedule:
    def __init__(self):
        self.appointments = [] #empty list of appointments 
    
    def add_appointment(self, appointment):
        self.appointments.append(appointment) #adding an appointment to the list
    
    def cancel_appointment(self, patient): #cancel appointment according to patient name
            
        for a in self.appointments:  #For loop to access each appointment
          if a.patient.name == patient.name:
            self.appointments.remove(a) #make use of the remove method
            break #stop
        
    def __str__(self): 
      if not self.appointments: #If a list is empty, it returns false when using an if statement 
        return "There are no appointments"
      else: 
       return self.appointments.__str__()

    """Add appointment, cancel appointment, find next available time"""

#creating objects
appointment_schedule = AppointmentSchedule() #give the receptionist the appointment schedule

doctor = Doctor('Dr.Davidson', '1278749')
nurse = Nurse('Nurse.Shirley', '979162')
patient = Patient('Ruan van der Merwe', '1 Rose Street, Melrose Estate', '08326884016')
receptionist = Receptionist('Miss.Wentzel', '7798312', appointment_schedule)

print(f'Doctor: {doctor.name}') #it allows you to add to the string
print(f'Nurse: {nurse.name}')
print(f'Patient: {patient.name}')
print(f'Receptionist: {receptionist.name}')

#creating methods

patient.request_appointment(receptionist) #patient is requesting an appointment and we are taking in the recpetionist
print(receptionist.appointment_schedule)

#patient is requesting a repeat prescription from the doctor.

request_repeat_prescription = Prescription(type_of_drug='', patient='', doctor='', quantity='', dosage='')

doctor = Doctor('Dr.Davidson', '1278749')
patient = Patient('Ruan van der Merwe', '1 Rose Street, Melrose Estate', '08326884016')
type_of_drug = ('Zoloft')
quantity = ('1 repeat')
dosage = ('30mg Daily')

print(f'Doctor: {doctor.name}') #it allows you to add to the string
print(f'Patient: {patient.name}')
print(f'DrugType: {type_of_drug}')
print(f'Quantity: {quantity}')
print(f'Dosage: {dosage}')

#cancel exisiting appointment using remove item from list method

appointment_schedule.cancel_appointment(patient)
print(appointment_schedule)
  
