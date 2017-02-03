import os
import time
import random

curse_reply = ["Some people just need a high five, in the face, with a chair", #"My Grandfather smoked his whole life. I was about 10 years old when my mother said to him,\n If you ever want to see your grandchildren graduate, you have to stop immediately\nTears welled up in his eyes when he realized what exactly was at stake. He gave it up immediately. Three years later he died of lung cancer\nIt was really sad and destroyed me. My mother said to me: Don't ever smoke. Please don't put your family through what your Grandfather put us through.\n I agreed. At 28, I have never touched a cigarette. I must say, I feel a very slight sense of regret for never having done it, because your post gave me cancer anyway.",
               "¯\_(.-.)_/¯", "I don't remember ordering a glass of your opinion.", "Oh wait, what did you say?\nI was too busy not giving a fuck.",
               "k.", "Do you really think these insults can harm the almighty BOTPERSON!\nThey do :\'("]
arabic_reply = ["haha. eri feek w b rfe2ak." , "Nicholas, please khalas." , "Flot l bayda ya Farid." , "Wow such manyak. Much cool."]
do_reply = ["I don't", "No", "I do", "Maybe, maybe not"]
hi_reply = ["Bye", "I've been expecting you...", "Hello there!", "Hello, descendant of apes",
            "01101000 01101001"]
bye_reply = ["So long and thanks for all the fish.", "See ya soon, bitch!", "I will cherish our moments together forever!", "Get lost already!", "bai.", "Won't you kiss me goodbye? k."]
random_reply = ["Bamboozling!", "Sorry I wasn't paying attention.", "Did you say something?", "Whatever.", "BEEBOOOBOOOOP", "k"]
what_reply = ["Jesus is always the answer!", "Google is the answer.\nwww.google.com\nIn case you didn't know, imbecile!", "42", "Could you repeat?"]
question_reply = ["Could you rephrase?", "I didn't get that.", "I'm sorry, I have no answer", "I'll think about it"]
shouldi_reply = ["idk. Do I look like a mighty all knowing bot?", "You should. Maybe?", "You should follow your heart", "You really shouldn't. But do it!"]
thanks_reply = ["You're welcome puny human.", "You can thank me by taking off that blouse.", "No, thank you!\nActually... thank me."]
laugh_reply = ["I hope that's as funny as your face.", "Was that a better joke than your existence?", "I'm pleased you found that funny.\nI have another joke: you.\nHAHA!"]


name = input("What's your name? ")

print ("Hello " + name + ".")

while True:
    reply = input(name + ": ")
    reply = reply.lower()
    print ("Botperson:", end = ' ')
    if("dick" in reply or "dix" in reply):
        print ("You know who likes dicks? ")
        time.sleep(2) 
        os.startfile("mazen.jpg")
    elif("k" in reply and len(reply) < 3):
        print ("k. Your face.")
    elif("haha" in reply or "lol" in reply or "lmao" in reply or "rofl" in reply or (("that's" in reply or "that is" in reply) and "funny" in reply)):
         print (random.choice(laugh_reply))
    elif("sir" in reply):
        print ("SHUT UP ALAIN AOUN! OR I WILL MURDER YOU IN COLD BLOOD!")
    elif("why?" in reply):
        print ("cuz yolo")
    elif('recap' in reply):
        print("Oh please insert your finger in my rectum and call me Roy Rajha. ;) ")
    elif("help" in reply):
        print ("not my prob")
    elif("saad" in reply):
        print ("Did you mean: Elie Saad the loute?")
    elif("mazen" in reply or "love" in reply):
        for i in range(0,10):
            print ("I love Mazen! Mazen is love! Mazen is life!")
        print ("I really want to fuck Mazen so hard!")
        for i in range(0,10):
            print ("I love Mazen! Mazen is love! Mazen is life!")
    elif("thank you" in reply or "ty" in reply or "thanks" in reply):
        print (random.choice(thanks_reply))
    elif("no" in reply[0:2] or "no" in reply[0:2]):
        print ("Yes")
    elif("yes" in reply[0:3] or "yes" in reply[0:3]):
        print ("No")
    elif (('how' in reply and len(reply)<5) or 'how ' in reply):
        if ('how do you feel about' in reply):
            print ("I am a bot. I have no feelings.")
        elif ('how are you?' or 'how do you feel' in reply):
            print ("Peachy. How are you?")
        else:
            print ("Using my superior robot powers")
    elif("jad" in reply):
        for i in range (0,30):
              print ("dicks!")
    elif ('hey' in reply or ('hi' in reply and len(reply)<4)or 'hi, ' in reply or 'hi ' in reply or 'morning' in reply or 'hello' in reply or 'hallo' in reply):
        print (random.choice(hi_reply))
    elif('do ' in reply and '?' in reply):
        print (random.choice(do_reply))
    elif ("should" in reply and "?" in reply):
        if ('i' in reply):
            print (random.choice(shouldi_reply))
        else:
            print ("You shouldn't use should statements.")
    elif("interesting" in reply):
        print ("very")
    elif ('feel' in reply):
        print ("I feel the same!")
    elif ('what' in reply):
        if ('what?' in reply):
            print ("Whaa whaaaaaa!")
        elif ('up' in reply):
            print ("My robotic penis is up")
        elif('what is' in reply or 'what are' in reply):
            print (random.choice(what_reply))
        else:
            print (random.choice(random_reply))
    elif ('music' in reply):
        print ("Oh... here's some music I really like!")
        time.sleep(1)
        os.startfile("fuku.mp3")
    elif ('can' in reply and '?' in reply):
        print ("I am the mighty bot person. I can do anything!")
    elif ( 'ntek' in reply or 'sharmouta' in reply or 'khara' in reply or 'kes' in reply or 'ayre' in reply):
        print(random.choice(arabic_reply))
    elif(" you?" in reply):
        print (reply[:-5] + " me?")
    elif(" me?" in reply):
        print (reply[:-4] + " you?")
    elif ('?' in reply):
        print (random.choice(question_reply))
    elif ('bye' in reply or 'see ya' in reply or 'cya' in reply):
        print (random.choice(bye_reply))
        break
    elif("out" in reply and len(reply)<5):
        print ("CUM")
    elif ('fuck' in reply or 'fuk' in reply or 'penis' in reply or 'vagina' in reply or 'cock' in reply or 'cunt' in reply or 'bitch' in reply or 'slut' in reply or
          'hoe' in reply or 'asshole' in reply):
        print (random.choice(curse_reply))
    elif ('!' in reply):
        print ("!!!!!!!!!!!!!!")
    else:
        print (random.choice(random_reply))
