#A python program to create phonebook with name and phonenumbers
import os
import pickle
def main():
  print("Enter The Number of names you want to add:")
  n=int(input())
  phonebook={}
  for i in range(n):
    print("Enter the name:")
    name=input()
    print("Enter the phone number:")
    phone=input()
    phonebook[name]=phone
  phonebook = loadbinfile(phonebook)
  makebinfile(phonebook)


  
def makebinfile(phonebook):
  with open("phonebook.bin","wb") as file:
    pickle.dump(phonebook, file)

def loadbinfile(phonebook):
 with open("phonebook.bin","rb") as file:
   while True:
     try:
       phonebook.update(pickle.load(file))
     except EOFError:
       break
 return phonebook


main()