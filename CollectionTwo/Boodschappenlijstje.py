import time , webbrowser


boodschappenlijstje = dict()
vraag = ''
aantal = ''
meer = ''

def vraagtoevoeg(): 
    global vraag
    vraag = input("Welk item wilt u toevoegen aan de lijst? Invoer:")
    if vraag == str(vraag):
        vraagaantal()
    else:
        print ("Dit snappen wij niet!")
        vraagtoevoeg()

def vraagaantal(): 
    global aantal
    aantal = input("Hoeveel wilt u er van? Invoer:")
    try:
        aantal = int(aantal)
    except:
        print ("U kunt geen letter invullen, alleen cijfers!")
        vraagaantal()

    if aantal <1:
        print ("Getallen groter dan 0 graag!")
        vraagaantal()
    else:
        aantal = int(aantal)
        try: 
            boodschappenlijstje[vraag] += aantal
        except:
            boodschappenlijstje[vraag] = aantal

        nogmeer()
    
def nogmeer():
    global meer
    meer = input("Wilt u nog meer toevoegen? nee/ja | Invoer: ")
    if meer == "nee":   
        print ("Boodschappenlijstje:")
        print (boodschappenlijstje)
        print ("Bedankt voor het gebruiken van Milware!")
        print ("Royalistiq en wij namens team Milware wensen u een:")
        webbrowser.open("https://www.youtube.com/watch?v=7nbU6l9U__g")
        time.sleep(52)
        exit()
    elif meer == "ja":
        vraagtoevoeg()
        vraagaantal()
        nogmeer()
    else:
        print ("Dit snappen wij niet, probeer het opnieuw.")
        nogmeer()   
        
vraagtoevoeg()
