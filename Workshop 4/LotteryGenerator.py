import random
lotterynumbers=[]
quickpicks=int(input("how many quick picks"))
for i in range (0,quickpicks):
    gamenumbers=[]
    for number in range(6):
        gamenumbers.append(random.randint(0,45))
        gamenumbers.sort()
    lotterynumbers.append(gamenumbers)
strlottery="".join(lotterynumbers())
print (strlottery)
