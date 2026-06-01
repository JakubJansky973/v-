from bloky import MovingBlock
from ui import UI

class GameEngine:
    def __init__(self, screen):
        self.screen = screen
        self.sirka = 600
        self.vyska = 800
        self.polozene_bloky = []
        self.aktualni_blok = MovingBlock(0, 250, 4)
        self.je_padajici = False
        self.konec_hry = False
        self.ui = UI()
        self.ui.aktualizuj_skore(0)
        self.screen.listen()
        self.screen.onkeypress(self.pust_blok, "space")
    def pust_blok(self):
        if not self.je_padajici and not self.konec_hry:
            self.je_padajici = True
    def aktualizuj(self):
        
        if not self.je_padajici:
            self.aktualni_blok.pohybzestranynastranu(self.sirka)
        else:
            stare_y = self.aktualni_blok.shape.ycor()
            nove_y = stare_y - 10
            self.aktualni_blok.shape.sety(nove_y)

            if len(self.polozene_bloky) == 0:
                cilove_y = -300

            else:
                posledni_blok = self.polozene_bloky[-1]
                cilove_y = posledni_blok.shape.ycor() + 30

            if nove_y <= cilove_y:
                self.aktualni_blok.shape.sety(cilove_y)
                

                trefa = True
                if len(self.polozene_bloky) > 0:
                    aktualni_x = self.aktualni_blok.shape.xcor()
                    posledni_x = self.polozene_bloky[-1].shape.xcor()
                    rozdil_x = abs(aktualni_x - posledni_x)
                    if rozdil_x > 80:
                        trefa = False
                if trefa:
                    self.je_padajici = False
                    self.polozene_bloky.append(self.aktualni_blok)
                    self.ui.aktualizuj_skore(len(self.polozene_bloky))

                    if self.aktualni_blok.shape.ycor() > 100:
                        for blok in self.polozene_bloky:
                            nove_y_bloku = blok.shape.ycor() - 30
                            blok.shape.sety(nove_y_bloku)



                    nova_rychlost = 4 + (len(self.polozene_bloky) * 0.3)
                    self.aktualni_blok = MovingBlock(0, 250, nova_rychlost)
                else:
                    self.konec_hry = True
                    self.ui.uloz_highscore(len(self.polozene_bloky))
                    self.ui.zobraz_konec_hry()