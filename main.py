#Title (title for the app)
#Label on GUI^

import club_confi
import time
import datetime

#gameplay mode (module):
#collecting the players feelings (hole by hole) along with score
#Short survey at the begining and end of the round to summarize mood
#(time of day, weather) as seprate data forms
#How much slaap, have you eaten, caffine intake
#Store data in app

#Data visualization (seperate module)
#graphs, scores, confidence leveles, mood

#implement automatic date for pre-round

player_data = open("playerdata.txt","a")
player_feedback = open("playerdata.txt","a")
course_info = open("course.txt","w")
#club_confi = open("clubconfidence.txt", "w")

#Club confidence level (seperate modele)
#irons, driver, wedges, short game, putting confidnece
#holds data for golfer to look back on and see what they need to imrpove
#see club_confi.py
'''
def club_conf():
    club1 = input("Driver: (1-10) ")
    #Slibers for all
    club2 = input("Woods, Hybrid and/or driving iron: (1-10) ")
    club3 = input("Irons: (1-10) ")
    club4 = input("Wedges: (1-10) ")
    club5 = input("Short game (chipping/pitching): (1-10) ")
    club6 = input("Putting (1-10) ")
    #we need a submit button at the end to save the position of the sliders
    #this function also needs to save the date this data was submitted and log in app
    club_confi.write(club1 + " \n")
'''

def pre_round():
    ques1 = input("What's your general mood today? ")
    #seletion box (very good, good, nuetral, bad, very bad)
    ques2 = input("How important is this round to you? (1 being not important at all and 10 being very important) ")
    #maybe a scroll bar or a slider for that one ^
    ques3 = input("How confident in your golf game are you right now? ")
    #selection box: veru confident, confident, nuetral, not confident, God help me)
    ques4 = input("What's your attitude going into the round? ")
    #write
    player_data.write(ques1 + " \n")
    player_data.write(ques2 + " \n")
    player_data.write(ques3 + " \n")
    player_data.write(ques4 + " \n")

def course():
    quest1 = input("Name of course: ")
    #usr input (label)
    quest2 = input("Time of day?(start of round) ")
    #Scroll menu?^
    quest3 = input("Describe the weather currently? ")
    #usr input or graphable data point
    quest4 = input("Course conditions/quality (1 being a mine field and 10 being Augusta National) ")
    #Scroll bar or slider
    #write
    course_info.write(quest1 + " \n")
    course_info.write(quest2 + " \n")
    course_info.write(quest3 + " \n")
    course_info.write(quest4 + " \n")

#gameplay mode (module):
#collecting the players feelings (hole by hole) along with score
#Short survey at the begining and end of the round to summarize mood
#(time of day, weather) as seprate data forms
#display hole number on GUI
#Store data in app

#Hole by hole gameplay:
def gameplay():
    label = input ("How do you feel after this hole? ")
    #Label^
    face1 = input ("Good")
    #Button
    face2 = input("Neutral")
    #Button
    face3 = input("Upset")
    score = input("score on hole (# of strokes): ")
    #drop scroll that ends at 12
    #writing:
    player_feedback.write(label + " \n")
    player_feedback.write(face1 + " \n")
    player_feedback.write(face2 + " \n")
    player_feedback.write(face3 + " \n")
    player_feedback.write(score + " \n")

#Gameplay mode:
gameplaymode = input("Select gameplay mode: (G or C) ")
if gameplaymode == "G":
    #Function calls
    pre_round()
    course()
    gameplay()
if gameplaymode == "C":
    #function call
    club_confi.club_conf()

#create for loop to run "gamplay()" either 9 or 18 times

#enable "end round" button that will stop the hole-by-hole questioning and save data

#Post round page:
#ask post round questions (general questions for data collection)
#page that shows your hole by hole questions as well as your pre/post round questions
