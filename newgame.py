#!/usr/bin/python3

#use this temp as base for idea if applicable

#8 ball idea
#could spit out ideas, answers, questions, topics based off number entered?(1-10 or so)

#A Guess of characters based off discriptions with answerru?
#
#1-10 characters (cartoon, movie, etc.) notable like aang or Shazam dont know which character type, maybe both?
#Give description of character wiht multipe choice. (put like this incase you cant figure out a code)
#3 chances before a fail? Try a hint section maybe?
#Figure out how to randomize(questions, answers) if not too difficult
#ideas stop here/notes

#game below
message = print("Welcome to the Game, Determine the Character based off description")
print()
def questions():
    def questionsOne():
        global right, wrong, questionNumber
round=0
print("Who is known to be so scared yet so brave?")

while round <=2 :
    
    ans = input(" \n A Johnny Test. B Little Jimmy. C Johnny Bravo D Courage. [A/B/C/D]? : ")
    if ans == 'D' or ans == 'd' or ans == 'Courage' or ans == 'courage' :
         print("Correct nj!")
         break
    else: 
         print("Nah, you got it wrong")
         round +=1
         
print("Who has the power of so many in so little?") 
while round <=2 :
 
   ans = input(" \n A Johnny Test. B Dexter. C Ben10. [A/B/C]? : ")
   if ans == 'C' or ans == 'c' or ans == 'Ben10' or ans == 'ben10' :
         print("Well shuckkks!")
         break
   else: 
         print("ohhh ya almost had it")
         round +=1

print("Who received a scar during one of their fights?")
while round <=2 :
    ans = input(" \n A Beast Boy. B Tom. C Zuko. [A/B/C]? : ")
    if ans == 'C' or ans == 'c' or ans == 'Zuko' or ans == 'zuko' :
          print("Welll illl beeee!")
          break
    else:
          print("ya gotta be quicker then that")
          round +=1

print("Which group has the know it all scammer?")
while round <=2 :
    ans = input(" \n A KidsNextDoor. B Ed,Edd,Eddy. C Teen Titans. [A/B/C]? : ")
    if ans == 'B' or ans == 'b' or ans == 'Ed,Edd,Eddy' or ans == 'ed,edd,eddy' :
          print("Your on a rootin tootin roll!")
          break
    else:
          print("You get it by now, lol answer wrong kekw")
          round +=1


















