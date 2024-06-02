from random import randint as r
from random import choice as ch
import time as t
from helper import write, cl, qna

game_completed = 0
név = input('Add meg a játékosnevedet: ')
t.sleep(0.3)

#Program kezdete
def game_start(game_pt):
    pontszam_elso = 0
    pontszam_masodik = 0
    pontszam_harmadik = 0
    szazalek_elso_jateknal = 1
    szazalek_masodik_jateknal = 1
    szazalek_harmadik_jateknal = 1
    pontszam = 0
    
    while True:
        cl()
        t.sleep(1)
        begin2 = str(input(f'Üdvözlünk a menüben, {név}!\n\nKérdÉsVálasz - 1\nChessPuzzle - 2 \nLuckOrSkill - 3\n\nInfók / Készítők - 4\n--> '))
        
        if begin2 == '1':
            t.sleep(1)
            all, pontszam = QnA(game_pt=game_pt, already_gave_point=szazalek_elso_jateknal)
            
            if pontszam > pontszam_elso:
                pontszam_elso = pontszam
                
            if szazalek_elso_jateknal == 1:
                game_pt += all
                
            else:
                pass
            
            szazalek_elso_jateknal += 1
            
        elif begin2 == '2':
            t.sleep(1)
            all, pontszam = BasicChess(game_pt=game_pt, already_gave_point=szazalek_masodik_jateknal)
            
            if pontszam > pontszam_masodik:
                pontszam_masodik = pontszam
                
            if szazalek_masodik_jateknal == 1:
                game_pt += all
                
            else:
                pass
            
            szazalek_masodik_jateknal += 1
            
        elif begin2 == '3':
            t.sleep(1)
            all, pontszam = LuckOrKnowledge(game_pt=game_pt, already_gave_point=szazalek_harmadik_jateknal)

            if pontszam > pontszam_harmadik:
                pontszam_harmadik = pontszam
                
            if szazalek_harmadik_jateknal == 1:
                game_pt += all
                
            else:
                pass
            
            szazalek_harmadik_jateknal += 1
            
        elif begin2 == '4':
            t.sleep(1)
            cl()
            if pontszam == 0:
                test = credits(game_completed=game_pt,elso_jatek=0, masodik_jatek=0, harmadik_jatek = 0)
                
            elif pontszam > 0:
                test = credits(game_completed=game_pt,elso_jatek=pontszam_elso, masodik_jatek=pontszam_masodik, harmadik_jatek=pontszam_harmadik)
        else:
            cl()
            write('Kérjük, a felsorolt sorszámok közül írj be egyet!\n','red')
            t.sleep(0.2)
            game_start(game_pt=game_completed)

#KérdÉsVálasz
def QnA(game_pt: float, already_gave_point: int):
    life = 3
    pontszam = 0
    
    cl()
    write(f'Üdvözlünk, {név}!\n\n- Ebben a játékban kérdésekre kell válaszolnod, hogy továbbjuss.\n- Összesen {life} életed van.\nSok sikert!','white')
    t.sleep(1.5)
    cl()
    
    kerdes_szam = 1
    while kerdes_szam != 6:
        kerdes, valasz, rossz_valasz1, rossz_valasz2 = qna(kerdes_szam)
        
        elrejtes = r(1, 3)
        
        valasz1 = ""
        valasz2 = ""
        valasz3 = ""
        
        helyes_valasz = str(elrejtes)
        
        if elrejtes == 1:
            valasz1 += valasz
            valasz2 = ch([rossz_valasz1, rossz_valasz2])
            valasz3 = ch([x for x in [rossz_valasz1, rossz_valasz2] if x != valasz2])
            
        elif elrejtes == 2:
            valasz2 += valasz
            valasz1 = ch([rossz_valasz1, rossz_valasz2])
            valasz3 = ch([x for x in [rossz_valasz1, rossz_valasz2] if x != valasz1])
        
        elif elrejtes == 3:
            valasz3 += valasz
            valasz2 = ch([rossz_valasz1, rossz_valasz2])
            valasz1 = ch([x for x in [rossz_valasz1, rossz_valasz2] if x != valasz2])
            
        if life > 0:
            jatekos_valasz = input(f"{kerdes_szam}. Kérdés,\n{kerdes}1. {valasz1}2. {valasz2}3. {valasz3}--> ")

            if jatekos_valasz.strip() == helyes_valasz:
                print(f"Helyes válasz!\n{life} életed maradt!")
                pontszam = pontszam + 1
                
            elif jatekos_valasz.strip() != helyes_valasz:
                life = life - 1
                print(f"Nem jó válasz!\n{life} életed maradt!")
                
            t.sleep(1.5)
            cl()
            kerdes_szam += 1
        
        elif life == 0:
            write("Vesztettél! Nincsen több életed!","red")
            t.sleep(1)
            cl()
            kerdes_szam = 6
    
    if kerdes_szam == 6 and life > 0:
        print(f"Gratulálunk! Sikeresen teljesítetted az első játékot!\n\nPontszám: 5/{pontszam}")
        t.sleep(0.5)
        cl()
        if already_gave_point == 1:
            game_pt += 33.3
            return game_pt, pontszam
        
        elif already_gave_point != 1:
            return game_pt, pontszam
        
    else:
        write("Úgy látszik nem sikerült teljesítened a játékot, de majd máskor jobban sikerül!","red")
        t.sleep(0.5)
        cl()
        return game_pt, pontszam
    

#2. játék
def BasicChess(game_pt: float, already_gave_point: int):
    score = 0
    chess_puzzle = []
    cl()
    t.sleep(1)
    write(f'Üdvözlünk a második játékunkban! Tudsz valamennyire sakkozni, ugye? Ebben a játékban sakkfeladványokat kell megoldanod. Igyekezz minél többet megoldani! Sok szerencsét!','white')
    write('\nJelzések:\nBábu: FEHÉR (jelzés nagy betűvel) /fekete (jelzés kis betűvel) \nKirály: K/k\nKirálynő: Q/q\nBástya: R/r\nHuszár: N/n\nFutó: B/b\nGyalog: P/p\nfehér gyalogból királynő lesz pl: a8=Q','white')
    t.sleep(1.5)
    cl()

    for sus in range(1):
        x = r(1,4)
        chess_puzzle.append(x)


    if chess_puzzle[0] == 4:
            # Function to create an 8x8 chessboard
        def create_chessboard():
        # Create an 8x8 chessboard with empty slots
            return [[" " for _ in range(8)] for _ in range(8)]

        # Function to print the chessboard
        def print_chessboard(board):
            # Print column headers
            print("  A B C D E F G H")
            for i, row in enumerate(board):
                # Print row number
                print(f"{8 - i} " + " ".join(row) + f" {8 - i}")
            # Print column headers again
            print("  A B C D E F G H")

        # Function to update a slot on the chessboard
        def update_chessboard(board, position, value):
            # Convert the position (like 'E2') into board coordinates
            columns = "ABCDEFGH"
            col = columns.index(position[0].upper())
            row = 8 - int(position[1])
            # Update the slot with the given value
            board[row][col] = value

        # Example usage
        chessboard = create_chessboard()
        #print_chessboard(chessboard)

        # Update some positions
        update_chessboard(chessboard, 'A8', 'r')  
        update_chessboard(chessboard, 'E8', 'k')  
        update_chessboard(chessboard, 'F8', 'b')
        update_chessboard(chessboard, 'B7', 'p')
        update_chessboard(chessboard, 'C7', 'p')
        update_chessboard(chessboard, 'E7', 'n')
        update_chessboard(chessboard, 'F7', 'N')
        update_chessboard(chessboard, 'H7', 'p')
        update_chessboard(chessboard, 'A6', 'p')
        update_chessboard(chessboard, 'D6', 'p')
        update_chessboard(chessboard, 'G6', 'p')
        update_chessboard(chessboard, 'E5', 'p')
        update_chessboard(chessboard, 'H5', 'b')
        update_chessboard(chessboard, 'C4', 'B')
        update_chessboard(chessboard, 'E4', 'N')
        update_chessboard(chessboard, 'C3', 'R')
        update_chessboard(chessboard, 'F3', 'P')
        update_chessboard(chessboard, 'A2', 'P')
        update_chessboard(chessboard, 'B2', 'P')
        update_chessboard(chessboard, 'G2', 'P')
        update_chessboard(chessboard, 'H2', 'P')
        update_chessboard(chessboard, 'F1', 'n')
        update_chessboard(chessboard, 'G1', 'K')
        print_chessboard(chessboard)
        #feladvány
        write('\nFekete a(z) Nf8 lépést tette meg. Nyerd meg a játékot 1 lépésből!','white')
        move = input('\nLépés > ')
        if move == 'Nf6' or move == 'NF6':
            score += 1
            t.sleep(1)
            write(f'Helyes megoldás, teljesítetted ezt a játékot is! Pontszám: 1/{score}','yellow')
            cl()
            if already_gave_point == 1:
                game_pt+= 33.3
                return game_pt, score
            
            elif already_gave_point != 1:
                return game_pt, score

        else:
            t.sleep(1)
            write('Helytelen megoldás. Sajnos nem sikerült megoldanod ezt a feladványt, de később biztosan sikerülni fog!','red')
            cl()
            return game_pt, score



    elif chess_puzzle[0] == 3:
            # Function to create an 8x8 chessboard
        def create_chessboard():
        # Create an 8x8 chessboard with empty slots
            return [[" " for _ in range(8)] for _ in range(8)]

        # Function to print the chessboard
        def print_chessboard(board):
            # Print column headers
            print("  A B C D E F G H")
            for i, row in enumerate(board):
                # Print row number
                print(f"{8 - i} " + " ".join(row) + f" {8 - i}")
            # Print column headers again
            print("  A B C D E F G H")

        # Function to update a slot on the chessboard
        def update_chessboard(board, position, value):
            # Convert the position (like 'E2') into board coordinates
            columns = "ABCDEFGH"
            col = columns.index(position[0].upper())
            row = 8 - int(position[1])
            # Update the slot with the given value
            board[row][col] = value

        # Example usage
        chessboard = create_chessboard()
        #print_chessboard(chessboard)

        # Update some positions
        update_chessboard(chessboard, 'A8', 'r')
        update_chessboard(chessboard, 'B8', 'n')
        update_chessboard(chessboard, 'C8', 'b')
        update_chessboard(chessboard, 'D8', 'q')
        update_chessboard(chessboard, 'E8', 'k')
        update_chessboard(chessboard, 'F8', 'b')
        update_chessboard(chessboard, 'G8', 'n')
        update_chessboard(chessboard, 'H8', 'r')
        update_chessboard(chessboard, 'B7', 'p')
        update_chessboard(chessboard, 'C7', 'p')
        update_chessboard(chessboard, 'D7', 'p')
        update_chessboard(chessboard, 'E7', 'p')
        update_chessboard(chessboard, 'G7', 'p')
        update_chessboard(chessboard, 'A6', 'p')
        update_chessboard(chessboard, 'F5', 'p')
        update_chessboard(chessboard, 'G4', 'Q')
        update_chessboard(chessboard, 'C3', 'N')
        update_chessboard(chessboard, 'E3', 'P')
        update_chessboard(chessboard, 'A2', 'P')
        update_chessboard(chessboard, 'B2', 'P')
        update_chessboard(chessboard, 'C2', 'P')
        update_chessboard(chessboard, 'D2', 'P')
        update_chessboard(chessboard, 'F2', 'P')
        update_chessboard(chessboard, 'H2', 'P')
        update_chessboard(chessboard, 'A1', 'R')
        update_chessboard(chessboard, 'C1', 'B')
        update_chessboard(chessboard, 'E1', 'K')
        update_chessboard(chessboard, 'F1', 'B')
        update_chessboard(chessboard, 'G1', 'N')
        update_chessboard(chessboard, 'H1', 'R')
        print_chessboard(chessboard)
        #feladvány
        write('\nFekete egy lépésből elvesztette a játékot. Mutasd meg neki, mekkora hibát követett el a(z) f5 lépéssel!','white')
        move = input('\nLépés > ')
        if move == 'QG6' or move == 'Qg6':
            score += 1
            t.sleep(1)
            write(f'Helyes megoldás, teljesítetted ezt a játékot is! Pontszám: 1/{score}','yellow')
            cl()
            if already_gave_point == 1:
                game_pt+= 33.3
                return game_pt, score
            
            elif already_gave_point != 1:
                return game_pt, score

        else:
            t.sleep(1)
            write('Helytelen megoldás. Sajnos nem sikerült megoldanod ezt a feladványt, de később biztosan sikerülni fog!','red')
            cl()
            return game_pt, score



    elif chess_puzzle[0] == 2:
            # Function to create an 8x8 chessboard
        def create_chessboard():
        # Create an 8x8 chessboard with empty slots
            return [[" " for _ in range(8)] for _ in range(8)]

        # Function to print the chessboard
        def print_chessboard(board):
            # Print column headers
            print("  A B C D E F G H")
            for i, row in enumerate(board):
                # Print row number
                print(f"{8 - i} " + " ".join(row) + f" {8 - i}")
            # Print column headers again
            print("  A B C D E F G H")

        # Function to update a slot on the chessboard
        def update_chessboard(board, position, value):
            # Convert the position (like 'E2') into board coordinates
            columns = "ABCDEFGH"
            col = columns.index(position[0].upper())
            row = 8 - int(position[1])
            # Update the slot with the given value
            board[row][col] = value

        # Example usage
        chessboard = create_chessboard()
        #print_chessboard(chessboard)

        # Update some positions
        update_chessboard(chessboard, 'D7', 'P')
        update_chessboard(chessboard, 'H7', 'k')
        update_chessboard(chessboard, 'H5', 'K')
        update_chessboard(chessboard, 'D4', 'Q')
        print_chessboard(chessboard)
        #feladvány
        write('\nFehér lép, adj mattot az ellenségednek 2 lépésben!','white')
        move = input('\nLépés > ')
        if move == 'Qa7' or move == 'QA7':
            print('Helyes lépés!')
            t.sleep(1)
            cl()
            update_chessboard(chessboard, 'D7', 'P')
            update_chessboard(chessboard, 'G8', 'k')
            update_chessboard(chessboard, 'H5', 'K')
            update_chessboard(chessboard, 'A7', 'Q')
            update_chessboard(chessboard, 'D4', ' ')
            update_chessboard(chessboard, 'H7', ' ')
            print_chessboard(chessboard)
            move = input('\nLépés > ')
            if move == 'D8=Q' or move == 'd8=Q':
                t.sleep(1)
                score += 1
                write(f'Helyes megoldás, teljesítetted ezt a játékot is! Pontszám: 1/{score}','yellow')
                if already_gave_point == 1:
                    game_pt+= 33.3
                    return game_pt, score
            
                elif already_gave_point != 1:
                    return game_pt, score
            
            else:
                write('Helytelen megoldás. Sajnos nem sikerült megoldanod ezt a feladványt, de később biztosan sikerülni fog!','red')
                return game_pt, score

        else:
            write('Helytelen megoldás. Sajnos nem sikerült megoldanod ezt a feladványt, de később biztosan sikerülni fog!','red')
            return game_pt, score




    elif chess_puzzle[0] == 1:
            # Function to create an 8x8 chessboard
        def create_chessboard():
        # Create an 8x8 chessboard with empty slots
            return [[" " for _ in range(8)] for _ in range(8)]

        # Function to print the chessboard
        def print_chessboard(board):
            # Print column headers
            print("  A B C D E F G H")
            for i, row in enumerate(board):
                # Print row number
                print(f"{8 - i} " + " ".join(row) + f" {8 - i}")
            # Print column headers again
            print("  A B C D E F G H")

        # Function to update a slot on the chessboard
        def update_chessboard(board, position, value):
            # Convert the position (like 'E2') into board coordinates
            columns = "ABCDEFGH"
            col = columns.index(position[0].upper())
            row = 8 - int(position[1])
            # Update the slot with the given value
            board[row][col] = value

        # Example usage
        chessboard = create_chessboard()
        #print_chessboard(chessboard)

        # Update some positions
        update_chessboard(chessboard, 'C8', 'q')
        update_chessboard(chessboard, 'F8', 'k')
        update_chessboard(chessboard, 'A4', 'P')
        update_chessboard(chessboard, 'D4', 'Q')
        print_chessboard(chessboard)
        #feladvány
        write('\nFehér lép...','white')
        move = input('\nLépés > ')
        if move == 'Qh8' or move == 'QH8':
            print('Helyes megoldás!')
            cl()
            t.sleep(1)
            update_chessboard(chessboard, 'F8', ' ')
            update_chessboard(chessboard, 'E7', 'k')
            update_chessboard(chessboard, 'H8', 'Q')
            print_chessboard(chessboard)
            move = input('\nLépés > ')
            if move == 'Qc8' or move == 'QC8':
                t.sleep(1)
                score += 1
                write(f'Helyes megoldás, teljesítetted ezt a játékot is! Pontszám: 1/{score}','yellow')
                if already_gave_point == 1:
                    game_pt+= 33.3
                    return game_pt, score
            
                elif already_gave_point != 1:
                    return game_pt, score
                
                else:
                    write('Helytelen megoldás. Sajnos nem sikerült megoldanod ezt a feladványt, de később biztosan sikerülni fog!','red')
                    return game_pt, score

        else:
            write('Helytelen megoldás. Sajnos nem sikerült megoldanod ezt a feladványt, de később biztosan sikerülni fog!','red')
            return game_pt, score
        

#3.játék
def LuckOrKnowledge(game_pt: float, already_gave_point: int):
    scorepoint = 0
    rng1 = r(1,3)
    rng2 = r(1,6)
    rng3 = r(1,8)
    cl()
    write('Szia, üdvözlünk az utolsó játékunkban! Itt kiderül, mennyire is vagy szerencsés... vagyis mennyire vagy jó valószínüségszámításban. Ez a feladat több körből áll, és mindegyikre helyesen kell válaszolnod! Ha egyet is elrontasz, a játék véget ér. Sok sikert!\nÜgyelj arra, hogy SORSZÁMOT írsz be!','white')
    t.sleep(1)
    cl()
    lvl_1 = int(input('Válassz!\n1 - Alma\n2 - Barack\n3 - Kiwi\n>> '))
    if lvl_1 == rng1:
        write('Helyes megoldás!','white')
        scorepoint+=1
        cl()
        lvl_2 = int(input('Dobsz egy dobókockával, hányast dobtál vele? !\n1 - 1\n2 - 2\n3 - 3\n4 - 4\n5 - 5\n6 - 6\n>> '))
        if lvl_2 == rng2:
            write('Helyes megoldás!','white')
            scorepoint+=1
            cl()
            lvl_3 = int(input('Melyik számra gondoltam?\n1 - 6\n 2 - 28\n3 - 42\n 4 - 69\n5 - 56\n6 - 94\n7 - 1/4\n8 - 72\n>> '))
            if lvl_3 == rng3:
                write('Helyes megoldás!','white')
                scorepoint+=1
                cl()
                lvl_4 = int(input('3 ajtó van, egyik mögött egy Ferrari van, a többi mögött semmi. Egyik üres ajtó kinyílik. Mekkora esélyed van, hogy a jó ajtót választod?\n1 - 33%\n2 - 50%\n3 - 66%\n>> '))
                if lvl_4 == 3:
                    write('Helyes megoldás!','white')
                    scorepoint+=1
                    cl()
                    write('Gratulálok, teljesítetted az utolsó játékunkat is!','yellow')

                    if already_gave_point == 1:
                        game_pt+= 33.3
                        return game_pt, scorepoint
            
                    elif already_gave_point != 1:
                        return game_pt, scorepoint
                else:
                    write('Sajnos most nem volt szerencséd, de ne csüggedj, legközelebb sikerülni fog!','red')
                    return game_pt, scorepoint
            else:
                write('Sajnos most nem volt szerencséd, de ne csüggedj, legközelebb sikerülni fog!','red')
                return game_pt, scorepoint 
        else:
            write('Sajnos most nem volt szerencséd, de ne csüggedj, legközelebb sikerülni fog!','red')
            return game_pt, scorepoint
    else:
        write('Sajnos most nem volt szerencséd, de ne csüggedj, legközelebb sikerülni fog!','red')
        return game_pt, scorepoint
        
#credits
def credits(game_completed, elso_jatek, masodik_jatek, harmadik_jatek):
    print(f'Infók:\nEnnyire sikerült teljesítened a játékot: {round(game_completed)}%\nJátékos Neved: {név}\nKérdÉsVálasz:\t  - Pontszám: 5/{elso_jatek}\nBasicChess: \t Pontszám: 1/{masodik_jatek}\nLuckOrSkill: \t Pontszám: 4/{harmadik_jatek}\n\nKészítők:\n\tBodolai Richárd - Játékok programozása\n\tBagosi Bence - Játék promóciós weboldalának készítése')
    back = str(input('\nNyomj ENTER a menübe való visszatéréshez.\n--> '))
    
    while back != "":
        back = str(input('Nyomj ENTER a menübe való visszatéréshez.\n--> '))
        
    else:
        cl()
        t.sleep(0.5)
        return None

if __name__ == "__main__":
    game_start(game_pt=game_completed)
