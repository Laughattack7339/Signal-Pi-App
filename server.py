import pygame
from flask import Flask
pygame.mixer.init()
app = Flask(__name__)
@app.route('/play_doorbell')
def play_doorbell():
    pygame.mixer.Sound("doorbell.wav").play()
    return ('done')
app.run()