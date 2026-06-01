import turtle

class UI:
    def __init__(self):
        self.text = turtle.Turtle()
        self.text.hideturtle()
        self.text.penup()
        self.text.color("black")
        
        self.skore_pen = turtle.Turtle()
        self.skore_pen.hideturtle()
        self.skore_pen.penup()
        self.skore_pen.color("black")
        self.skore_pen.goto(-280, 350)

        self.soubor_highscore = "highscore.txt"
        self.highscore = self.nacti_highscore()

    def nacti_highscore(self):
        try:
            soubor = open("highscore.txt", "r")
            nactene_skore = soubor.read()
            soubor.close()
            return int(nactene_skore)
        except:
            return 0
                
    def uloz_highscore(self, nove_skore):
        if nove_skore > self.highscore:
            self.highscore = nove_skore
            soubor = open("highscore.txt", "w")
            soubor.write(str(self.highscore))
            soubor.close()

    def zobraz_konec_hry(self):
        self.text.goto(0, 0)
        self.text.write("KONEC HRY", align="center", font=("Arial", 36, "bold"))

    def aktualizuj_skore(self, skore):
        self.skore_pen.clear()

        
        vypis = "Patra: " + str(skore) + " | Nejlepší: " + str(self.highscore)
            
        self.skore_pen.write(vypis, font=("Arial", 24))