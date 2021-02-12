import itertools
x=["A","R"]

def racecar(commands):
    speed=1
    position=0
    for i in range(len(commands)):
        command=commands[i]
        if(command=="A"):
            position+=speed
            speed*=2
        if(command=="R"):
            if(speed<0):
                speed=1
            elif(speed>0):
                speed=-1
    return position

for commands in itertools.product(x, repeat=27):
    commands="".join(commands)
    commands="AAAAAAAAAAAA"+commands
    position=racecar(commands)
    if(position==5363):
        print(commands)