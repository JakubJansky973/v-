Hra se spouští souborem main.py

Nahoře na obrazovce se pohybuje kostka ze strany na stranu.

Stisknutím mezerníku hráč blok pustí.

Úkolem je trefit se novým blokem na předchozí postavené patro. S přibývajícími patry se postupně zvyšuje rychlost pohybu bloku.

Pokud blok spadne mimo věž (přesah je příliš velký), hra končí.

Hra si pamatuje highscore a ukládá si ho do textového souboru. Taky má mojí vlastní grafiku budov.

Cílem hry je postavit co nejvyšší věž


architektura

main.py - Spouštěcí soubor. Nastavuje velikost herního okna, načítá texturu budova.gif a obsahuje hlavní herní smyčku.

engine.py - Řídí herní logiku, eviduje postavené bloky (v seznamu self.polozene_bloky) a vyhodnocuje výpočty kolizí při dopadu. Zajišťuje posun kamery.

ui.py - Stará se o vykreslování textů na obrazovku (skóre, Game Over). Obsahuje metody pro čtení a zápis highscore do textového souboru.

bloky.py -
Bloky - Vytváří základní želvu, nastaví jí tvar Budova.gif a určuje její hitbox (60x40 pixelů).
Pohybujiciblok - Přidává logiku pro automatický pohyb ze strany na stranu a odrážení od okrajů obrazovky.


Využiti AI

Konzultoval jsem, jak správně rozdělit kód do více souborů a jak propojit Engine s UI.

Hledal jsem způsob, jak vyřešit kolize bez složitého fyzikálního enginu. AI mi poradila použít funkci abs() pro získání absolutní vzdálenosti středů obou kostek, aby hra věděla kdy kostka přepadne

V modulu turtle nelze jednoduše posouvat obrazovku nahoru. Ai mi poradilo že můžu celou budovu posunout o 40 bloků dolu jako to bývalo v retro hrách.

Pomoc s vysvětlením chyb, které jsem v projektu měl (nebylo jich málo).

Nechal jsem si poradit jak přidat vlastní texturu do hry. Modul turtle nepřijímá .jpg ale pouze .gif. 

A také jak ukládat highscore do textového souboru.

Projekt jsem dělal lokalně ve visual studiu i s většinou úprav, protože mi nedošlo že máme commitovat všechny změny. Takže jsou ukázany commity pouze u posledních pár změn.
