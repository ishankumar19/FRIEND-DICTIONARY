"""
WAP to input your friend's name and their phone number and store them in the
dictionary as the key-value pair.Perform the following operation on the dictionary.
(a) Display the name and phone number of all your friends
(b) Add a new key-value pair in the dictionary and display the modified dictionary
(c) delete a particular friend from the dictionary.
(d) Modify the phone number of an existing friend
(e) Check if a friend is present in the dictonary or not
(f) Display the dictionary in sored order of names.
"""
n=int(input("How many friends:"))
fd={}
for i in range(n):
    print("Enter details of friend:",(i+1))
    name=input("Enter Name:")
    ph=int(input("Enter Phone Number:"))
    fd[name]=ph
    print("Friends dictionary is:",fd)
ch=0
while ch!=7:
    print("Menu")
    print("1. Display all friends:")
    print("2. Add new friend")
    print("3. Delete a friend:")
    print("4. Modify a Phone number:")
    print("5. Search a friend")
    print("6. Sort a names")
    print("7. Exit")
    ch=int(input("Enter your choice?"))
    if ch==1:
        print(fd)
    elif ch==2:
        print("Enter details of new friend:")
        name=input("Enter Name:")
        ph=int(input("Enter phone number:"))
        fd[name]=ph
    elif ch==3:
        nm=input("Friend Name to be deleted:")
        res=fd.pop(nm,-1)
        if res!=-1:
            print(res,"deleted")
        else:
            print("No such friend")
    elif ch==4:
        name=input("Friend Name:")
        ph=int(input("Changed Phone:"))
        fd[name]=ph
    elif ch==5:
        name=input("Friend Name:")
        if name in fd:
            print(name,"exist in the dictionary")
        else:
            print(name,"does not exist in the dictionary")
    elif ch==6:
        lst=sorted(fd)
        print("{",end=" ")
        for a in lst:
            print(a,":",fd[a],end=" ")
        print("}")
    elif ch==7:
        break
    else:
        print("valid choices are 1")
               
        
