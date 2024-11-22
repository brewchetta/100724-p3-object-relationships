# One to Many #
from classes.models import Shrimp, Aquarium

# Many to Many #
from classes.models import Doctor, Patient, Appointment

# SEED DATA GOES BELOW
# seed data is temporary testing data we add in a development environment

zoolander = Aquarium(name="Derrick Zoolanders Aquarium for Shrimp Who Cant Read or Eat Other Shrimp Very Good", city="Atlantis")
boston = Aquarium(name="Boston Aquarium", city="Boston")
pyonyang = Aquarium(name="Pyonyang Aquarium", city="Pyonyang")

herb = Shrimp(name="Herb", aquarium=zoolander)
shellvis = Shrimp(name="Shellvis", aquarium=zoolander)
small_fry = Shrimp(name="Small Fry", aquarium=boston)
prawn_connery = Shrimp(name="Prawn Connery", aquarium=boston)
mugatu = Shrimp(name="Mugatu", aquarium=pyonyang)
kim_prawn_shrimp = Shrimp(name="Kim Prawn Shrimp", aquarium=pyonyang)

doctor1 = Doctor(name="Strange", specialty="Surgery or the future or whatever")

patient0 = Patient(first_name="Patient", last_name="Zero")
patient1 = Patient(first_name="Dog", last_name="the Bounty Hunter")

appt1 = Appointment(doctor=doctor1, patient=patient1, date="January 1st 1970")
appt2 = Appointment(doctor=doctor1, patient=patient0, date="September 11th")
appt3 = Appointment(doctor=doctor1, patient=patient1, date="April 27th")