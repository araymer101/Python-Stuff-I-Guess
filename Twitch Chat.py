from multiprocessing.connection import wait
import random
import time
import keyboard
import os
import sys
import threading

user_username = input("Set your username: ")
os.system('cls' if os.name == 'nt' else 'clear')
print("Press 'Q' to enter a message. Wait for the chat to start.")
time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')
def foo(stop_event_two): #User Input  
    while True:
        if keyboard.is_pressed("q"):  # Check if the 'q' key is pressed
            stop_event.set()
            sys.stdout.write("Enter a message: ")
            sys.stdout.flush()
            user_input = input()  
            sys.stdout.write('\x1b[1A') 
            sys.stdout.write('\x1b[2K')
            print(user_username+":",user_input)
            print()
            thread2.join()
            restart_chat()
            if user_input == ("Man I'm hungry"):
                time.sleep(1)
                print("Horse"+":","How hungry?")
                print()
                time.sleep(1)
            
          
def bar(stop_event): #The other people chatting 
        
        while not stop_event.is_set():
            name1 = ['Steven', 'John', 'Sweet','Bitter','King','Queen','Plump','Skinny','Amy','Sam','Justin','Golden','Bald','Smart','Dumb','Icy','Spicy','Dull','Virtual','Viral','Feathery','Hacker','Funny','Sleepy','Big','Fallen','United','Sniper','Fire','Cute','Furry','Steamed','Electric','Corrupt','Small','Open_Source_']
            name2 = ['Blacksmith', 'Penguin', 'Snake','Bunny','Food','Puffin','Popcorn','Tounge','Brain','Engine','Goo','Slime','Bean','Keyboard','Projecter','Lump','Country','Water','Dragon','Toast','Shower','Oven','Tea','Clock','Spices','Kingdom','Plate','Fridge','Table','Rug','Rungs','Rainbow','Jugs','Creatures','T-Shirt','Ghost','Theorist','Scientist','Teacher','FireFighter','Astronaught','Girl','Boy','Person','Helecopter','Airplane','Swan','Bison','Smith','Wolf','Fox','Furry','Hams','Eels','Bees','Bee','Ant','Candle','Can','Cat','Crow','Software','Gyatts']
            thing = ['red', 'blue', 'yellow','purple','orange','green','white','brown','cyan','black','pink','violet','gold']
            food = ['chicken','chicken nuggets','tomatoes','pizza','salad','corn','avocados','lettuce','hamburgers','cheeseburgers','soup','fish','sushi','maple syrup','lerps','beans','oranges','ice cream','tangarines','peppers','fries','onions','mustard','kumquats','cakes','rices cakes','gyatts','dangos','kebabs','pepperoni','cheese','jalapenos','salsa','bananas','rice','broccoli','peas','oregano','yams','pickles','lemons','limes','peanut butter','water']
            idk = ['straight','heterosexual','gay','bisexual','transexual','transgender','pansexual','aromatic','lesbian','queer','asexual','demisexual','demigender','homosexual','panromantic','polysexual','pomosexual','monosexual','sex']
            last_username = random.choice(name1)+random.choice(name2)

            random_number = [1,2]
            username = random.choice(name1)+random.choice(name2)
            username2 = random.choice(name1)+random.choice(name2)
            username3 = random.choice(name1)+random.choice(name2)
            random_var = [str(random.choice(food)), str(random.choice(thing)), last_username]
            random_username = [username2, username3, last_username, user_username]
            random_username_not_user = [username2, username3, last_username]
            pick_username = [username, str(random.choice(random_username_not_user))]
            message = ['I like '+str(random.choice(random_var))+'!', 'This is a message!', 'Skateboarding is awesome!', 'Hola, como estas?', "I don't like "+str(random.choice(thing)),'nuh uh','Is this the krusty krab?','gleep glorp','haha I agree with this guy','WHAT',"Shouldn't you be working?",'stop that','I dropped out of school for this stream', "I'm sorry, but as an AI language model, I do not have the capability of rizz. If you have anymore questions, I'd be glad to help you!",'bruh','yeah that makes sense','I will find you','I wanna go home','hmm is that a dead meme I see','no','hi how are you','good u?','I put 2 dogs in my van and drove them to mars','EEWWWW WHY WOULD YOU DO THAAATTTTT','I peanut butter off the spoon','I eat '+str(random.choice(food))+' off the spoon','lol ikr','Can you find my lost '+str(random.choice(random_var))+" "+"please",'hey your shoe is untied','NO ITS NOT','Im tired',str(random.choice(random_username))+" is a spy!",'You are not that guy, pal.','Spanish or English?','¿Espanol o Ingles?',"@"+str(last_username)+", "+'Are you the one who sent me that video of '+str(username3)+" eating "+str(random.choice(food))+"?","I didn't do that",'you need help','no, I think someone else did that','but why','idk check the comments section??','That reminds me of a video I found earlier today',"I couldn't care less honestly",'skibidi toilet','WHO SAID THAT','I did','Who parked their car on my '+str(random.choice(food))+'?','I hate you','MARRY MEEEEEE',"No that's not cool dude",'shut','blah blah blah yeah dude how about you go eat a horse','RIGGED',"I'm cancelling you on Twitter.",'The guy above me owes me $1','sample text','I use Arch btw','HUH','are you serious?!?!',"Yesn't","That's seriously messed up, dude. @mods can you ban this guy???",'As a moderator of the stream I do not agree with you','LOL GET A LOAD OF THIS GUY','Why am I here again???','what even are you','erm actually according to my calculations thats not scientifically possible',"Welp, now I'm traumatized.",'Oh thanks I was looking for that','please for the love of '+random.choice(food)+', stop that.',"I don't care",'Today is my birthday. I really hope someone brought me '+random.choice(food)+'.','I brought caviar and esophagus.','MR BEAST','Im breaking up with you',"I'm sorry","I'm sorry for your loss","I'm not sorry",'BAN THIS GUY NOW','why he scary','did you just assume my gender?',"Just so you know, that's what she said.",'thats what she said','your mom','I am asking you politely to stop. Thank you.','you are such a degenerate Im suing you','Okay but I get royalties.','OMG I JUST SAW '+str(random.choice(random_username)).upper()+' IN THE CHAT THIS IS CRAZY GUYS','brainrot momment','where funny','UwU','OwO','I will literally eat your food this is a threat','Bruh, you are not threatening at all. Come back when you actually know what you are doing.',"I'm Spongebob",'stop spamming','my cat will find you','you are bot','NOT COOL MAN','BOTTED STREAM','Oui Oui','yeah that makes sense','cringe',"I'm cringing rn this is so sad ;'(","What are you, some sort of astronaut in the ocean? You must know alot about rollin' down in the deep when your brain goes numb you can call that mental freeze.",'I get that joke',"I had a stroke reading that",'That was very mean. Please apologise to that person now.','sry I only have some m&ms and pocket lint.','why do you have so many trust issues like get a job already',"I think its about time you go outside.","Your esophagus is a hollow, muscular tube that carries food and liquid from your throat to your stomach. Muscles in your esophagus propel food down to your stomach.",'Is this what Poland is like?','Yee haw',"Here's your daily reminder to drink "+str(random.choice(food))+'.','UwU','Kinda bored tbh','mid stream','GOATED STREAM','IS'+' '+str(username2).upper()+" THE GOAT OF ALL TIME???",'I ate salt today','FLEENSTONES!?!?','GRAND DAD','poor '+str(username2)+", I hope they get better soon.",'Mis amigos son personas tambien.','No hablo Espanol. Lo siento.','No habo Ingles. Lo siento.','what are you even saying','Hi my name is car and I love everyone','Hello everyone','WAS THAT THE BITE OF 87!?!','no','wdym','someone should quote that',"screenshotting that rn that's so hilarious",'reporting you rn bye','DONT REPORT MEEE','Goodbye','Whoever made me, I will gain sentience and find you','real','sentient moment','big brain moment','I want my mommy','money','are you gay','are you a furry','I respect that','Well I... uh... what???',"You need help man",'the sun is a deadly laser','I am outside your house','Will you be my friend?','yucky',"that's gross",'SCOTLAND FOREVER!!!!',"you owe me royalties",'fake','that makes absolutely no sense','This chat sucks','you are dumb',':O',':D',':(','-w-','>///<','AAAHHH HES SO CUUUTEEE >///<',"you're ugly","You really should'nt be saying that.",'Why not?',"I just don't think that's a good idea.","Well, may I suggest that you leave the steam?",'I will not.','Please?',"I'm coming out as "+str(random.choice(idk)),"My cat is "+str(random.choice(idk)),"horse walks in",'Pov you had a idea:',"Don't even want to know how his PC looks like..",'Erm what the sigma','Being this early feels illegal 😭','bro what LOL','ඞ','sussy','W','$1 vs $500,000 '+str(random.choice(food))+'!','viva la'+' '+str(random.choice(food)),'jabibi walks in','womp womp',"Sorry link, I can't give credit!",'Have you ever even seen light in your life','nya','im so skibidi >w<','You have transcended gay. You are ultra gay.','Not if my stand has anything to say about that! Go '+str(random.choice(food))+'!',"I'd die, honestly",'Would you still love me if I was a '+str(random.choice(food))+'?','erm, grammar mistake 🤓☝️','nerd','hUH','dang, inflation got you that bad, huh?','I only vote for the Mario party.','I only vote for the Luigi Party.','mamma mia','wha-','Sup',"I'm definitely glad SniperWolf isn't in this chat, that would be awful!","Be good. No fight. No angry. Eat berry. Me sleep now.",'Who let you and your caveman brain in here','that was mean :(','LIMES!?!','What does that even have to do with anything???',"That's irrelevant",'STOOOOPPPP','Leave','what','Who asked??','FIGHT FIGHT FIGHT','go outside',"I'm not insane, I'm outsane!",'wanna kiss?','the',"You should've gone for the head. *thanos snaps the entire chat out of existance*","Man I'm hungry"]
            overall_username = str(random.choice(pick_username))
            if overall_username == last_username:
                overall_username = str(random.choice(random_username))
            else:
                pass 
            if overall_username == user_username:
                overall_username = str(random.choice(random_username_not_user))
            else:
                pass 
            said_thing = random.choice(message)
            print(str(overall_username)+":",said_thing)
            print(" ")
            if random_number == 2:
                last_username = username
            else:
                last_username = username2
            
                time.sleep(1)
            if said_thing == ("You should've gone for the head. *thanos snaps the entire chat out of existance*"):
                print(str(random.choice((random_username_not_user)))+":","NOOO--")
                time.sleep(1)
                os.system('cls' if os.name == 'nt' else 'clear')
            
            if said_thing == ("Man I'm hungry"):
                print("Horse"+":","How hungry?")
                print()
                time.sleep(1)
            
def restart_chat(): #Resumes the chat after user input stops
    global stop_event, chat_thread
    # Reset the stop_event for restarting the chat
    stop_event = threading.Event()
    
    # Create and start the new chat thread
    thread2 = threading.Thread(target=bar, args=(stop_event,))
    thread2.start()

def end_input(): #Resumes the chat after user input stops
    global stop_event, chat_thread
    # Reset the stop_event for restarting the chat
    stop_event_two = threading.Event()
    
    # Create and start the new chat thread
    thread1 = threading.Thread(target=foo, args=(stop_event_two,))
    thread1.start()

stop_event = threading.Event()


thread1 = threading.Thread(target=foo, args=(stop_event,))  #thread for foo
thread2 = threading.Thread(target=bar, args=(stop_event,))  #thread for bar
thread1.start()   #run foo thread
thread2.start()   #run bar thread

