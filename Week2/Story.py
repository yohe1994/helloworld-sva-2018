# let the user know what's going on
print ("Welcome to Yohe's MadLibs!")
print ("Please Answer the Questions Below to Play.")
pause1 = raw_input("-----------Press Enter to Continue-----------"+"\n")

what0 = raw_input("Choose a behavior below and enter the sequence number"+"\n"+"\n"+"1.Slaughter the pig and sheep"+"\n"+"2.Dance"+"\n"+"3.Streak"+"\n"+"4.Give a rap show"+"\n"+"5.Do a Pecha-Kucha"+"\n")
where0 = raw_input("Choose a place below and enter the sequence number"+"\n"+"\n"+"1.Inside a box"+"\n"+"2.In the women's toilet on the 80F of the Empire State Building"+"\n"+"3.In romantic Hawaiian seaside"+"\n"+"4.In the classroom"+"\n"+"5.In a stormy island"+"\n")
when0 = raw_input("Choose a time below and enter the sequence number"+"\n"+"\n"+"1.At midnight"+"\n"+"2.In doomsday"+"\n"+"3.In a stormy day"+"\n"+"4.5000 years ago"+"\n"+"5.Now"+"\n")
who0 = raw_input("Choose a person below and enter the sequence number"+"\n"+"\n"+"1.Holmes"+"\n"+"2.Superman"+"\n"+"3.Sheldon Lee Cooper"+"\n"+"4.Harry Porter"+"\n"+"5.Trump"+"\n")

when =["At midnight", "In doomsday", "In a stormy day", "5000 years ago", "Now"]
who = ["Holmes", "Superman", "Sheldon Lee Cooper", "Harry Porter", "Trump"]
where = ["inside a box", "in the women's toilet on the 80F of the Empire State Building", "in romantic Hawaiian seaside", "in the classroom", "in a stormy island"]
if when0 == "4":
	what = ["slaughtered the pig and sheep", "danced", "streaked", "gave a rap show", "did a Pecha-Kucha"]
elif when0 == "5":
	what = ["is slaughtering the pig and sheep", "is dancing", "is streaking", "is giving a rap show", "is doing a Pecha-Kucha"]
else:
	what = ["slaughters the pig and sheep", "dances", "streaks", "gives a rap show", "does a Pecha-Kucha"]

story0 = when[int(when0)-1] + ", " + who[int(who0)-1] + " " + what[int(what0)-1] + " " + where[int(where0)-1]+ "."
print ("Here is the sentence:"+"\n")
print (story0)
pause3 = raw_input("-----------Press Enter to Continue-----------"+"\n")
print ("Looks Funny or Just so so?")
print ("Try to Create Your Own Story")
print ("Have Fun."+"\n")
pause3 = raw_input("-----------Press Enter to Continue-----------")

# variables containing all of your story info
XXX = raw_input("What's your name? ")
NNN = raw_input("How will your parents usually call you? ")
VVV = raw_input("Which place do you like most? ")
AAA = raw_input("An interesting activity you have ever done: ")
BBB = raw_input("Which is the largest object in your home? ")
CCC = raw_input("Who is your favorite character? ")
DDD = raw_input("Which food or snack do you like most? ")

# this is the story. it is made up of strings and variables.
# the \ at the end of each line let's the computer know our string is a long one
# (a whole paragraph!) and we want to continue more code on the next line. 
# play close attention to the syntax!

story1 = "Hundreds years ago, in the center of Pacific, there is a secret island called " + AAA + ", everyone" +"\n"\
+"here needs to do " + AAA + " everyday. " + "\n" + "\n"\
+"One day morning, when " +XXX+ " was doing "+ AAA +" in front of lots of people. A person with" +"\n"\
+"a mask broke in and said, 'The world outside is destroyed, there is a monster called Sigoi that" +"\n"\
+"destroyed everywhere. I escaped and come here, but this place will be not safe soon. I know there" +"\n"\
+"is a place that we can survive'" +"\n" +"\n"\
+"'Stop! Whatever you would like to say, you need to do " + AAA+ " first!'"+XXX+" said to him." +"\n" +"\n"\
+"Mask man didn't tell anything and quickly did a "+AAA+" and said 'There isn't much time left," +"\n"\
"trust me and follow me.' Everyone looked at him like looking at a fool. Suddenly, a " +BBB+" fell to" + "\n"\
"the ground from the sky, the mask of mask man was blew away and everyone could see the face." +"\n"\
"It is " + CCC + "!" +"\n" +"\n"\
"'It is blown here by the typhoon made by Sigoi. There is a sentence in the bottom of this " + BBB + "," +"\n"\
"'Made in "+VVV+"'. "+VVV+" no longer exists. Can you trust me now? ' said "+ CCC +"."+"\n"+"\n"\
"Everyone looked face at each other and finally "+ XXX +" said, 'Ok, I trust you.' Then, they"+"\n"\
"followed him/her and finally came to a secret cave under the sea. Everyone entered in and "+ CCC +"\n"\
"closed the door and drained off water, then lighted the cave up and everyone discovered there are"+"\n"\
"tons of " + DDD +" here!"+"\n" +"\n"\
"'There were lots of food for use and we can stay here safely, because Sigoi cannot swim!' said " + CCC +"."+"\n" +"\n"\
"'Boom!' There is a loud noise outside suddenly." +"\n" +"\n"+"\n"\
"'"+NNN+", why are you still in the bed? Get up! You are late for Code Literacy!' "+"\n"

print ("\n")
print ("Plase Maximize Your Window, because the story might be a little bit long"+"\n")
pause3 = raw_input("-----------Press Enter to See the Story-----------"+"\n")
# finally we print the story
print (story1)
pause3 = raw_input("-----------Thx for Reading-----------")