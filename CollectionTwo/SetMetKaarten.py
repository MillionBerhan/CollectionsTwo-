import random,time

Jokers = {"joker", "joker"}

def deck():
        kleuren = ["harten", "klaveren", "schoppen", "ruiten"]
        speciaal = ["aas", "boer", "vrouw", "koning"]
        for x in range(4):
                for y in range(4):
                        Jokers.add(kleuren[x] + " " + speciaal[y])
                for i in range(1, 10):
                        Jokers.add(kleuren[x] + " " + str(i + 1))

def eigenkaarten():
        for i in range(1,8):
                print (f"kaart {i}: {Jokers.pop()}")


               
deck()
eigenkaarten() 
print(Jokers)
time.sleep(52)
