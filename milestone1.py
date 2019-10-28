list1=[]
dicks1={}

    
x=input("enter your choice---'a' for add, 'f' for find, 'l' for all movies, 'q' to quit \n " )
while(x!='q'):
    if(x=='a'):
        name=input("movie name? \n")
        year=input("movie year? \n")
        director=input("director \n")

        dicks1["name"]=name
        dicks1["year"]=year
        dicks1["director"]=director

        list1.append(dicks1)
        x=input("enter your choice---'a' for add, 'f' for find, 'l' for all movies, 'q' to quit \n " )
    elif(x=="l"):
        print(list1)
        x=input("enter your choice---'a' for add, 'f' for find, 'l' for all movies, 'q' to quit \n " )
    elif(x=='f'):
        y=input("enter abbrev")
        for movie in list1:
            if(y in movie["name"] or movie["year"] or movie["director"]):
                print(movie)
            else:
                print("no such movie")
        x=input("enter your choice---'a' for add, 'f' for find, 'l' for all movies, 'q' to quit \n " )
            