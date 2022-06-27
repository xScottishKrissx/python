def schoolAgeCalculator(age, name):
    if age < 18:
        print("In Secondary School or Out of work!", name, "is", age )
    elif age == 16:
        print("Definitly in Secondary school")
    else:
        print("Solid chance", name, "is out of work lol")
    
schoolAgeCalculator(15, "chris")