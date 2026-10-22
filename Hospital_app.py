def register_patient (name, age):
  message = "Patient " + name + ", aged " + str(age) + ", registered successfully."
  return message
  
print (register_patient("Lisa", 50))
