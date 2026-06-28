import pygame
from flask import Flask, request

#Turn on the speakers on the PI eg. let it know that were about to shove some sound in its mouth
pygame.mixer.init()

#Secret token that only PI knows
correct_token = "l725M284L"

#Establish a name for the app I think idrk what this does tbh
app = Flask(__name__)



def check_token(token):
    return token == correct_token


#Establish a route for our phone to go to and the PI to detect for example: our phone will go to webapp/play_doorbell and the PI will see that and be like "Holy Guacacamole he just went to that left.
#now i can finally get up and hit this big red button that says |DOORBELL|"
@app.route('/play_doorbell')

#He's kinda confused tho so he needs instructions to find the |DOORBELL| button so this is his map that tells him how to do it
def play_doorbell():
    #First tho hes gotta check if your even the right guy
    #Theres a pirate guy in his house and his name is args and he is the one that has the token and PI has to get it from him
    #Now that PI has the token he can check it to see if it is the right one
    if check_token(request.args.get("token")):
        #He used the map to find the |DOORBELL| button and then he presses it
        pygame.mixer.Sound("doorbell.wav").play()
        #Now that hes done he gets a glass of milk and sits down and tells me hes done pressing the cool shiny red |DOORBELL| button
        return ('Done', 200)
    else:
        return("PI checked it and its not the right token resumbit your token guess to args", 403)
    


@app.route('/forward')

def forward():
    if check_token(request.args.get("token")):
        print("forward")
        pygame.mixer.Sound("forward.wav").play()

        return ('Done', 200)
    else:
        return("PI checked it and its not the right token resumbit your token guess to args", 403)
    
@app.route('/backward')

def backward():
    if check_token(request.args.get("token")):
        print("backward")
        pygame.mixer.Sound("backward.wav").play()

        return ('Done', 200)
    else:
        return("PI checked it and its not the right token resumbit your token guess to args", 403)


@app.route('/left')

def left():
    if check_token(request.args.get("token")):
        print("left")
        pygame.mixer.Sound("left.wav").play()
        return ('Done', 200)
    else:
        return("PI checked it and its not the right token resumbit your token guess to args", 403)
    

@app.route('/right')

def right():
    if check_token(request.args.get("token")):
        print("right")
        pygame.mixer.Sound("right.wav").play()
        return ('Done', 200)
    else:
        return("PI checked it and its not the right token resumbit your token guess to args", 403)
    
@app.route('/stop')

def stop():
    if check_token(request.args.get("token")):
        print("stop")
        pygame.mixer.Sound("stop.wav").play()

        return ('Done', 200)
    else:
        return("PI checked it and its not the right token resumbit your token guess to args", 403)


#This is his house where he gets created
app.run(host='0.0.0.0',port=5000)


