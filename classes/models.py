# SHRIMP - AQUARIUM RELATIONSHIP ### ONE TO MANY RELATIONSHIP

# AQUARIUM ### HAS MANY SHRIMP
class Aquarium:

    # STEP 1: Create an all_aquariums class variable and add the append to the initializer
    all_aquariums = []
    
    def __init__(self, name:str, city:str):
        self.name = name
        self.city = city
        self.__class__.all_aquariums.append(self)

    def __repr__(self):
        return f"Aquarium(name={self.name}, city={self.city})"
    
    # STEP 3: create a method in the has many to get all the belongs tos
    def shrimp(self): # self IS THE AQUARIUM
        return [ shrimp for shrimp in Shrimp.all_shrimp if shrimp.aquarium == self ]


# SHRIMP ### BELONGS TO AN AQUARIUM
class Shrimp:

    # STEP 1: Create an all_shrimp class variable and add the append to the initializer
    all_shrimp = []

    def __init__(self, name:str, aquarium):
        self.name = name
        self.aquarium = aquarium # shrimp belongs to THIS aquarium
        self.__class__.all_shrimp.append(self)

    def __repr__(self):
        return f"Shrimp(name={self.name}, aquarium={self.aquarium.name})"
    
    # STEP 2: make a property GETTER and SETTER for aquarium so that the aquarium is always of the class Aquarium
    @property
    def aquarium(self): # GETTER
        return self._aquarium

    # self.aquarium = set_aquarium
    @aquarium.setter
    def aquarium(self, set_aquarium): # SETTER
        if isinstance(set_aquarium, Aquarium):
            self._aquarium = set_aquarium
        elif (set_aquarium == None):
            self._aquarium = None
        else:
            raise TypeError('aquarium must be an Aquarium!')



##############################
    


# DOCTOR - PATIENT RELATIONSHIP ### MANY TO MANY

# DOCTOR ### HAS MANY PATIENTS
class Doctor:

    all_doctors = []

    def __init__(self, name:str, specialty:str):
        self.name = name
        self.specialty = specialty
        self.__class__.all_doctors.append(self)

    def __repr__(self):
        return f"Doctor(name={self.name}, specialty={self.specialty})"
    
    def appointments(self):
        return [ appt for appt in Appointment.all_appointments if appt.doctor == self ]
    
    def patients(self):
        return [ appt.patient for appt in Appointment.all_appointments if appt.doctor == self ]
    

# PATIENT ### HAS MANY DOCTORS
class Patient:

    all_patients = []

    def __init__(self, first_name:str, last_name:str):
        self.first_name = first_name
        self.last_name = last_name
        self.__class__.all_patients.append(self)

    def __repr__(self):
        return f"Patient(first_name={self.first_name}, last_name={self.last_name})"
    
    def appointments(self):
        return [ appt for appt in Appointment.all_appointments if appt.patient == self ]
    
    def doctors(self):
        all_my_doctors = [ appt.doctor for appt in Appointment.all_appointments if appt.patient == self ]

        my_unique_doctors = set( all_my_doctors )

        return list( my_unique_doctors )
    
        # return list( set( [ appt.doctor for appt in Appointment.all_appointments if appt.patient == self ] ) )

class Appointment:

    all_appointments = []

    def __init__(self, doctor, patient, date):
        self.doctor = doctor
        self.patient = patient
        self.date = date
        self.__class__.all_appointments.append(self)

    @property
    def doctor(self):
        return self._doctor
    
    @doctor.setter
    def doctor(self, new_value):
        if isinstance(new_value, Doctor):
            self._doctor = new_value
        else:
            raise TypeError('doctor must be a real Doctor!')

    @property
    def patient(self):
        return self._patient
    
    @patient.setter
    def patient(self, new_value):
        if isinstance(new_value, Patient):
            self._patient = new_value
        else:
            raise TypeError('patient must be a Patient!')