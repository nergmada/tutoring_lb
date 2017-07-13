def retrieveFromDatabase(id):
    db = open("students.csv", "r")
    for line in db:
        identifier, firstname, lastname, email, phone = line.split(',') 
        if identifier == id:
            return line.split(",")
    return None

def addToDatabase(firstname,lastname, email, phone):
    db = open("students.csv", "a")
    id = 1 
    while retrieveFromDatabase(str(id)) != None:
        id = id + 1
    db.write(str(id) + "," + firstname + "," + lastname + "," + email + "," + phone + "\n") 

addToDatabase("lewis", "burton", "lburton@alton.ac.uk", "01475287242")