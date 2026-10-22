def register_patient (name, age):
  message = "Patient " + name + ", aged " + str(age) + ", registered successfully."
  return message
  
print (register_patient("John Doe", 30))
