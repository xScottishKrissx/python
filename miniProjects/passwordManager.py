from cryptography.fernet import Fernet

###Encryption
'''
# single use, remove once you've used it
def writeKey():
    key = Fernet.generate_key()
    with open("key.key", "wb") as keyFile:
        keyFile.write(key)
writeKey()
'''
def loadKey():
    #read/byte mode = reading in bytes
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

masterPassword = input("What is the master password? ")
#initialise encryption
fer = Fernet(key)


#function
def view():
    with open('passwords.txt', 'r') as f:
        for line in f.readlines():
            data = line.rstrip()
            # split - removes characters from a list
            user, userPassword = data.split('|')
            print("User: ", user, "-- Password:", fer.decrypt(userPassword.encode()).decode())


#function
def add():
    name = input("Account Name: ")
    password = input("Password: ")

    # with === auto close file when done with loop
    # open === open file but need to manually close the file
    # a === append mode (add something to end of file, create new if it doesn't exist)
    # w === mode write (will always overwrite file if it exists)
    # r === read mode (can't edit file)
    with open('passwords.txt', 'a') as f:
        f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")

while True:

    mode = input("Would you like to add a new pass or view existing(view, add,)? Q to quit. ").lower()
    if mode == "q":
        break

    if mode == "view":
        view()
    elif mode == "add":
        add()
    else:
        print("Invalid Mode")
        continue

