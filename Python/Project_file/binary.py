#A python program to use mmap & performing various operations on a binary file.
#1. Display all the entries 
#2. Display the phone numbers
#3. Modify an entry
import pickle
import mmap
def load_phonebook():
    with open("phonebook.bin", "r+b") as file:
        mmapped_file = mmap.mmap(file.fileno(), 0)
        data = mmapped_file.read()
        phonebook = pickle.load(file)
        for idx, (name, phone) in enumerate(phonebook.items()):
            print(f"{name}: {phone}")
          
def load_numbers():
  with open("phonebook.bin", "rb") as file:
      phonebook = pickle.load(file)
      for phone in phonebook.items():
          print(f"+91{phone[1]}")

def modify_entry(name, new_phone):
    with open('phonebook.bin', "rb") as file:
        phonebook = pickle.load(file)
    if name in phonebook:
        phonebook[name] = new_phone
        with open("phonebook.bin", "wb") as file:
            pickle.dump(phonebook, file)
        print("Entry modified successfully")
    else:
        print("Name not found in phonebook")

while True:
  print("\nEnter your choice:")
  print("1. Display all the entries.")
  print("2. Display the phone numbers.")
  print("3. Modify an entries.")
  print("4. Exit")
  choice = int(input())
  if choice == 1:
    load_phonebook()
  elif choice == 2:
    load_numbers()
  elif choice == 3:
    print("Enter the name of the person whose phone number you want to modify:")
    name = input()
    print("Enter the new phone number:")
    new_phone = input()
    modify_entry(name, new_phone)
  elif choice == 4:
    break
  else:
    print("Invalid choice")
  