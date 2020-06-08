
#This dictionary is used fo turn the random number into the card name.
from random import*
dict_1 = {
2 : "Two",
3 : "Three",
4 : "Four",
5 : "Five",
6 : "Six",
7 : "Seven",
8 : "Eight",
9 : "Nine",
10 : "Ten",
11 : "Jack",
12 : "Queen",
13 : "King",
1 : "Ace"
}

#This dictionary is used to turn the card name into its values.
dict_2 = {
"Two" : 2,
"Three" : 3,
"Four" : 4,
"Five" : 5,
"Six" : 6,
"Seven" : 7,
"Eight" : 8,
"Nine" : 9,
"Ten" : 10,
"Jack" : 10,
"Queen": 10,
"King" : 10,
"Ace" : 1
}

#This method will explain the rules of Black Jack to the user and then ask them if they want to play it. If they do, it will return a true so it will run the rest of the program. If false, it will print "thats too bad" and end the program.
def welcome():
  print "Welcome to Luke's Blackjack game!\n"
  print "_______________________________________________________"
  print "You and the dealer will be dealt 2 cards each, and you can see your cards and one of the dealer's. Now, you can choose to either hit or stand. If you hit, you get another card. If your cards add up to over 21, then you lose the game. If you stand, the dealer turns over his other card and has to hit till he adds to 17. If the dealer's cards add up to over 21, he loses the game. If you are both under 21, the person with the higher cards wins. This will be a first to 5 game. \n"
  question1 = "Hello"
  count = 0
  while count != 1:
    question1 = raw_input ("Would you like to play? ")
    if question1.upper() == "NO":
      print "That's too Bad"
      count = 1
      return False
    if question1.upper() == "YES":
      print "\nGreat \n"
      count = 1
      return True

# This method will generate 4 cards, two for the user and the other two for the dealer. Then, it tells the user his two card and one of the dealers cards.
def dealing():
  usercard1 = randint(1,13)
  usercard2 = randint(1,13)
  dealercard1 = randint(1,13)
  dealercard2 = randint(1,13)
  name1 = (dict_1[usercard1])
  value1 = (dict_2[name1])
  name2 = (dict_1[usercard2])
  value2 = (dict_2[name2])
  name3 = (dict_1[dealercard1])
  value3 = (dict_2[name3])
  name4 = (dict_1[dealercard2])
  value4 = (dict_2[name4])
  if value1 == 1:
    ace_question = int(raw_input("You drew an Ace would you like to make it a 1 or an 11? "))
    value1 = ace_question
  if value2 == 1:
    ace_question = int(raw_input("You drew an Ace would you like to make it a 1 or an 11? "))
    value2 = ace_question
  if value3 == 1:
    value3 = 11
  if value4 == 1:
    value4 = 11
    if value4 + value3 > 21:
      value4 = 1

  print "You have been dealt a %s " % (dict_1[usercard1]) + "and a %s " % (dict_1[usercard2]) + "for a total of " + str(value1 + value2)
  print "\nAnd the dealer is showing a %s and the other card is face down." %(dict_1[dealercard1])
  if value3 == 11:
    print "The dealer made the Ace worth 11.\n"
  return [value1, value2, value3, value4, name4]

#This method allows the user to either hit or stand. If you hit, the game generates a new card fot he user and adds it to the user value. THis can be repeated till the user busts or stand. If the player stand, it will take the user avlue and move on the the next par to of the program.
def user_play(list):
  playervalue = list[0] + list[1]
  dealervalue = list[2] + list[3]
  count = 0
  playerbusted = 0
  while count != 1:
    question = raw_input ("\nWould you like to hit or stand? ")
    if question.upper() == "HIT":
      newcard = randint(1,13)
      newname = (dict_1[newcard])
      newvalue = (dict_2[newname])
      if newvalue == 1:
        ace_question = int(raw_input("You drew an Ace would you like to make it a 1 or an 11? "))
        newvalue = ace_question
      playervalue = playervalue + newvalue
      print "\nYou were given a %s " % (dict_1[newcard]) + "for a total of " + str(playervalue) + "\n"
      if playervalue > 21:
        print "You Butsed!!!"
        count = 1
        playerbusted = 1
    if question.upper() == "STAND":
      count = 1
  return [playervalue, dealervalue, playerbusted, list[4]]

#After the player stands, the dealer will get a new card if the sum is less than 17 by generating a new card. This is repeated till the dealer has a hand over 16. If the dealer busts,that is send to the next method.  If the number does not pass 21, then it will return the values and move on to compare.  
def dealer_play(list):
  playervalue = list[0]
  dealervalue = list[1]
  over21 = 0
  dealerbust = 0
  if list[2] == 0:
    print "\nThe dealer flipped over the other card which was a " + list[3] + " for a total of " + str(list[1]) + "\n"
    while dealervalue < 17:
      newdealercard = randint(1,13)
      newndealername = (dict_1[newdealercard])
      newvalue = (dict_2[newndealername])
      if newvalue == 1:
        newvalue = 11
        if newvalue + list[1] > 21:
          newvalue = 1
        print "The dealer got an Ace and selected the value of " + str(newvalue) + "\n"
      dealervalue = dealervalue + newvalue
      print "The dealer drew a " + newndealername + " for a total of " + str(dealervalue) + "\n"
      if dealervalue > 21:
        over21 = 1
        dealerbust = 1
        print "Dealer Busted\n"

  return [playervalue, dealervalue, list[2] , dealerbust]


#This method checks the values of the user and dealer as long as both of them did not bust. If the dealer has a greater number, then the dealer wins and the same for the user. If the user and dealer tie, then it is a push.
def compare(list):
  if list[2] == 1:
    print "\nBetter luck next time. \n"
    winner = 0
  elif list[3] == 1:
    print "\nYou were lucky!\n"
    winner = 1
  elif list[1] > list[0]:
    print "\nThe dealer wins\n"
    winner = 0
  elif list[1] < list[0]:
    print "\nYou win\n"
    winner = 1
  elif list[1] == list[0]:
    print "\nIt's a push\n"
    winner = 2
  return winner

#This part of the program has the whole game in one method. And makes it a best of 5 game. If will make the variable either a 0 for the user and a 1 for the dealer and will add points respectivly."
def play_game():
  dealerscore = 0
  userscore = 0
  score = 0
  if welcome():
    gamenumber = 1
    while score != 5:
      print "Game number " + str(gamenumber) + "\n"
      gamenumber = gamenumber + 1
      winner = compare(dealer_play(user_play(dealing())))
      if winner == 0:
        dealerscore = dealerscore + 1
        score = dealerscore
      if winner == 1:
        userscore = userscore + 1
        score = userscore
      print "The dealer has " + str(dealerscore) + " points, and you have " + str(userscore) + " points. \n"
      print"\n______________________________________________________\n"
    if dealerscore == 5:
      print "The dealer won :( "
    if userscore == 5:
      print "You Win :) "

#This is the main code that calls play game.
play_game()