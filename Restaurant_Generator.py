import random

name = input("Enter Name: ")
question = "What on-campus resturant should I get lunch or dinner from?"
answer = ""
random_number = random.randint(1, 30)
#print(random_number)

if random_number == 1:
  answer = "Viva Los Tacos"
elif random_number == 2:
  answer = "Chick-fil-A "
elif random_number == 3:
  answer = "Pie Express Pizza"
elif random_number == 4:
  answer = "Prince of India"
elif random_number == 5:
  answer = "Oishii Bento"
elif random_number == 6:
  answer = "Hello Bistro"
elif random_number == 7:
  answer = "K-Town Korean Food"
elif random_number == 8:
  answer = "Roots Natural Kitchen "
elif random_number == 9:
  answer = "Piada Italian Street Food"
elif random_number == 11:
  answer = "CHiKN"
elif random_number == 12:
  answer = "The Eatery or The Perch"
elif random_number == 13:
    answer = "Primanti Brothers"
elif random_number == 14:
    answer = "Noodles and Company"
elif random_number == 15:
    answer = "The Porch at Schenley"
elif random_number == 16:
    answer = "Halal Pitt"
elif random_number == 17:
    answer = "Five Guys"
elif random_number == 18:
    answer = "Chick-n Grille"
elif random_number == 19:
    answer = "JJ Poke Bowl & Taiwanese Bubble Tea"
elif random_number == 20:
    answer = "芋见BAO"
elif random_number == 21:
    answer = "El Jefe's Taqueria"
elif random_number == 22:
    answer = "The Roost at Cathy"
elif random_number == 23:
    answer = "The Colombian Spot"
elif random_number == 24:
    answer = "Noodle House"
elif random_number == 25:
    answer = "McDonalds"
elif random_number == 26:
    answer = "Jimmy John's Sandwiches"
elif random_number == 27:
    answer = "Einstein's Bros"
elif random_number == 28:
    answer = "Divy Coffee and Buns"
elif random_number == 29:
    answer = "Chick'n Bubbly"
elif random_number == 30:
    answer = "Stack'd"
elif random_number == 31:
    answer = "Moes Southwest Grill"
else:
  answer = "Feast on dorm room snacks"

if name == "":
  print("Error! Please enter a name: ")
  name = input("Enter name: ")
else:
  print(name + " wants to know " + "\'" + question + "\'")
  print("Magic Restaurant Generator says: " + answer)
  print("Would you like to know what time " + answer + " closes on weekdays?")
  close_input = input("Yes or No: ")
  if close_input == 'Yes':
    hours = ""
    match answer:
        case "Viva Los Tacos":
            hours = "12 AM"
        case "Chick-fil-A":
            hours = "8 PM"
        case "Pie Express Pizza":
            hours = "11 PM"
        case "Prince of India":
            hours = "2:30 (lunch) and 9:30 (dinner)"
        case "Oishii Bento":
            hours = "9 PM"
        case "Hello Bistro":
            hours = "9 PM"
        case "K-Town Korean Food":
            hours = "8 PM"
        case "Roots Natural Kitchen":
            hours = "9:30 PM"
        case "Piada Italian Street Food":
            hours = "10 PM"
        case "CHiKN":
            hours = "10 PM"
        case "The Eatery of the Perch":
            hours = "12 AM and 10 PM"
        case "Primanti Brothers":
            hours = "12 AM"
        case "The Porch at Schenley":
            hours = "10 PM"
        case "Halal Pitt":
            hours = "10 PM"
        case "Five Guys":
            hours = "10 PM"
        case "Chick-n Grille":
            hours = "10 PM" 
        case "JJ Poke Bowl & Taiwanese Bubble Tea":
            hours = "8 PM"
        case "芋见BAO":
            hours = "9:30 PM"
        case "El Jefe's Taqueria":
            hours = "3 AM"
        case "The Roost at Cathy":
            hours = "7 PM"
        case "The Columbian Spot":
            hours = "9 PM "
        case "Noodle House":
            hours = "9:30 PM"
        case "McDonalds":
            hours = "Opens 24 hours"
        case "Jimmy John Sandwiches":
            hours = "10 PM"
        case "Einsteins Bros":
            hours = "4 PM"
        case "Divy Coffee and Buns":
            hours = "6 PM"
        case "Chick'n Bubbly":
            hours = "9 PM"
        case "Noodles and Company":
            hours = "10 PM"
        case "Stack'd":
            hours = "12 AM"
        case "Moes Southwest Grill":
            hours = "8 PM"
    print(answer + " closes at " + hours)
  elif close_input == "No":
      print("Ok! Goodbye!")
    
 
