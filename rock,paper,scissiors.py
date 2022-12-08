import random
Computer_input=["Rock","Paper","Scissor"]

c_points,u_points=0,0

for i in range(1,6):
    print("Round",i,"started:")
    print("Select one of these:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissor")

    user_input=int(input("Your Choice:"))

    if user_input==1:
        user="Rock"
    elif user_input==2:
        user="Paper"
    elif user_input==3:
        user="Scissor"
    else:
        print("Invalid Input")
        break

    computer=random.choice(Computer_input)
    print("Computer:",computer)
 

    if user==computer:
        print("Computer points:",c_points)
        print("Your points:",u_points)

    elif (user=="Scissor") and (computer=="Paper"):
        u_points+=1
        print("Computer points:",c_points)
        print("Your points:",u_points)
        
    elif (user=="Paper") and (computer=="Scissor"):
        c_points+=1
        print("Computer points:",c_points)
        print("Your points:",u_points)

    elif (user=="Paper") and (computer=="Rock"):
        u_points+=1
        print("Computer points:",c_points)
        print("Your points:",u_points)

    elif (user=="Rock") and (computer=="Paper"):
        c_points+=1
        print("Computer points:",c_points)
        print("Your points:",u_points)

    elif (user=="Rock") and (computer=="Scissor"):
        u_points+=1
        print("Computer points:",c_points)
        print("Your points:",u_points)

    elif (user=="Scissor") and (computer=="Rock"):
        c_points+=1
        print("Computer points:",c_points)
        print("Your points:",u_points)
    else:
        break
    print()
    
if u_points>c_points:
    print("You Win!")
elif c_points>u_points:
    print("You Lose!")
else:
    print("Tie!")

    


        



        


