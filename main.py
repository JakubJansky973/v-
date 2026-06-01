import turtle
import time
from engine import GameEngine

def setup_screen():
    screen = turtle.Screen()
    screen.title("Tower Bloxx - Turtle Edition")
    screen.bgcolor("skyblue")
    screen.setup(width=600, height=800)
    screen.tracer(0)
    return screen
def main():
    screen = setup_screen()
    engine = GameEngine(screen)
    
    while not engine.konec_hry:
        engine.aktualizuj()
        screen.update()
        time.sleep(0.01)
    screen.mainloop()

main()

