# SHRIMP - AQUARIUM RELATIONSHIP ### ONE TO MANY RELATIONSHIP

# AQUARIUM ### HAS MANY SHRIMP
class Aquarium:
    
    def __init__(self, name:str, city:str):
        self.name = name
        self.city = city

    def __repr__(self):
        return f"Aquarium(name={self.name}, city={self.city})"
    

# SHRIMP ### BELONGS TO AN AQUARIUM
class Shrimp:

    def __init__(self, name:str):
        self.name = name

    def __repr__(self):
        return f"Shrimp(name={self.name})"



##############################
    


# DOCTOR - PATIENT RELATIONSHIP ### MANY TO MANY

# DOCTOR ### HAS MANY PATIENTS
class Doctor:

    def __init__(self, name:str, specialty:str):
        self.name = name
        self.specialty = specialty

    def __repr__(self):
        return f"Doctor(name={self.name}, specialty={self.specialty})"
    
    def patients(self):
        pass
    

# PATIENT ### HAS MANY DOCTORS
class Patient:

    def __init__(self, first_name:str, last_name:str):
        self.first_name = first_name
        self.last_name = last_name

    def __repr__(self):
        return f"Patient(first_name={self.first_name}, last_name={self.last_name})"
    
    def doctors(self):
        pass