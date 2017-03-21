import random
lotterynumbers=[]
quickpicks=int(input("how many quick picks"))
for i in range (0,quickpicks):
    gamenumbers=[]
    for number in range(6):
        random_number=random.randint(1, 45)
        while random_number in gamenumbers:
            random_number=random.randint(1, 45)
        gamenumbers.append(random_number)
        gamenumbers.sort()
    lotterynumbers.append(gamenumbers)
print ('\n'.join(map(str, lotterynumbers)))
