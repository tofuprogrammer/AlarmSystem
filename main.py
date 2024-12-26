dooropen = input("Is the door open")
buzzeron = "_"
while dooropen == "Yes":
    buzzeron = True
    print("The buzzer is on")
    dooropen = input("Is the door open")
while dooropen == "No":
    buzzeron = False
    print("The buzzer is off")
    dooropen = input("Is the door open")