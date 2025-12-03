import time
import random
otc=0
qrc=0
qrt=4
poss=20
sleeptime = 0
game_in_action = True

def getting_a_foul(team,point_amount):
    if team == 1:
        if c1.tc > 0:
            point_amount = 1
        if random.randint(1, 1000) < t2.flp//(point_amount*2):
            c1.fc += 1
            for i in range(point_amount):
                if random.randint(1, 1000) < t1.ftp:
                    c1.tc += 1
                    g1.list.append(1)
                    c1.ftpc += 1
    else:
        if c2.tc > 0:
            point_amount = 1
        if random.randint(1, 1000) < t1.flp//(point_amount*2):
            c2.fc += 1
            for i in range(point_amount):
                if random.randint(1, 1000) < t2.ftp:
                    c2.tc += 1
                    g2.list.append(1)
                    c2.ftpc += 1

def possesion():
    if random.randint(1, 10) < 4:
        if random.randint(1, 1000) > t1.trnv:
            if random.randint(1, 1100 - t2.d) < t1.o3:
                c1.tc += 3
                g1.list.append(3)
            getting_a_foul(1,3)
        else:
            c1.trnvc += 1
            c1.tvc += 1
    if random.randint(1, 10) < 4:
        if random.randint(1, 1000) > t2.trnv:
            if random.randint(1, 1100 - t1.d) < t2.o3:
                c2.tc += 3
                g2.list.append(3)
            getting_a_foul(2,3)
        else:
            c2.trnvc += 1
            c2.tvc += 1
    if c1.tc == 0 and c1.tvc == 0:
        if random.randint(1, 1000) > t1.trnv:
            if random.randint(1, 1100 - t2.d) < t1.o2:
                c1.tc += 2
                g1.list.append(2)
            getting_a_foul(1,2)
        else:
            c1.trnvc += 1
    if c2.tc == 0 and c2.tvc == 0:
        if random.randint(1, 1000) > t2.trnv:
            if random.randint(1, 1100 - t1.d) < t2.o2:
                c2.tc += 2
                g2.list.append(2)
            getting_a_foul(2,2)
        else:
            c2.trnvc += 1
    if c1.tc == 0 and c1.tvc == 0 or c2.tc == 0 and c2.tvc == 0:
        if random.randint(1, 1000) < t1.scp and c1.tc == 0 and c1.tvc == 0:
            if random.randint(1, 1000) > t1.trnv:
                if random.randint(1, 1100 - t2.d) < t1.o2:
                    c1.tc += 2
                    c1.scpc += 2
                    g1.list.append(2)
            else:
                c1.trnvc += 1
        if random.randint(1, 1000) < t2.scp and c2.tc == 0 and c2.tvc == 0:
            if random.randint(1, 1000) > t2.trnv:
                if random.randint(1, 1100 - t1.d) < t2.o2:
                    c2.tc += 2
                    c2.scpc += 2
                    g2.list.append(2)
            else:
                c2.trnvc += 1
    print(c1.tc, c2.tc)
    c1.tc = 0
    c2.tc = 0
    c1.tvc = 0
    c2.tvc = 0
    time.sleep(sleeptime)

class game_specific:
    def __init__(self,tw,list):
        self.tw = tw
        self.list = list
class team:
    def __init__(self, o2, o3, d, scp, ftp, trnv, flp):
        self.o2=o2
        self.o3=o3
        self.d=d
        self.scp=scp
        self.trnv=trnv
        self.ftp=ftp
        self.flp=flp
class counters:
    def __init__(self,tc,fc,ftpc,trnvc,tvc,scpc):
        self.tc=tc
        self.fc=fc
        self.ftpc=ftpc
        self.trnvc=trnvc
        self.tvc=tvc
        self.scpc=scpc

first_to = int(input("Reikalingas pergalių kiekis "))
teamchoice1=str(input("Įveskite namų komandą: "))
c1 = counters(0, 0, 0, 0, 0, 0) #after round13
g1 = game_specific(0,[])
if teamchoice1 == "AND":t1 = team(554,355,103,314,781,131,293)
elif teamchoice1 == "ASM":t1 = team(573,328,52, 292,781,99,360)
elif teamchoice1 == "CZM":t1 = team(552,374,50,372,731,142,374)
elif teamchoice1 == "DUB":t1 = team(552,325,100,316,819,120,393)
elif teamchoice1 == "EAM":t1 = team(534,382,85,318,818,113,287)
elif teamchoice1 == "BAR":t1 = team(530,392,90,355,763,123,282)
elif teamchoice1 == "BAY":t1 = team(541,316,80,304,789,128,262)
elif teamchoice1 == "FEN":t1 = team(509,361,43,316,791,132,303)
elif teamchoice1 == "HTA":t1 = team(591,406,74,292,854,120,284)
elif teamchoice1 == "BAS":t1 = team(615,332,100,289,762,134,297)
elif teamchoice1 == "LDC":t1 = team(491,308,99,335,789,135,328)
elif teamchoice1 == "MTA":t1 = team(524,348,125,339,784,118,349)
elif teamchoice1 == "OLY":t1 = team(569,340,62,359,788,131,400)
elif teamchoice1 == "PAN":t1 = team(574,340,80,344,768,105,333)
elif teamchoice1 == "PAR":t1 = team(501,350,74,393,768,149,326)
elif teamchoice1 == "PAT":t1 = team(537,348,105,301,799,114,270)
elif teamchoice1 == "RMA":t1 = team(558,333,69,336,795,132,362)
elif teamchoice1 == "VBA":t1 = team(545,371,62,351,725,135,289)
elif teamchoice1 == "VRB":t1 = team(581,366,77,312,771,150,277)
elif teamchoice1 == "ZAL":t1 = team(539,410,59,326,747,119,318)

teamchoice2=str(input("Įveskite kelio komandą: "))
c2 = counters(0, 0, 0, 0, 0, 0) #after round 13
g2 = game_specific(0,[])
if teamchoice2 == "AND":t2 = team(554,355,103,314,781,131,293)
elif teamchoice2 == "ASM":t2 = team(573,328,52, 292,781,99,360)
elif teamchoice2 == "CZM":t2 = team(552,374,50,372,731,142,374)
elif teamchoice2 == "DUB":t2 = team(552,325,100,316,819,120,393)
elif teamchoice2 == "EAM":t2 = team(534,382,85,318,818,113,287)
elif teamchoice2 == "BAR":t2 = team(530,392,90,355,763,123,282)
elif teamchoice2 == "BAY":t2 = team(541,316,80,304,789,128,262)
elif teamchoice2 == "FEN":t2 = team(509,361,43,316,791,132,303)
elif teamchoice2 == "HTA":t2 = team(591,406,74,292,854,120,284)
elif teamchoice2 == "BAS":t2 = team(615,332,100,289,762,134,297)
elif teamchoice2 == "LDC":t2 = team(491,308,99,335,789,135,328)
elif teamchoice2 == "MTA":t2 = team(524,348,125,339,784,118,349)
elif teamchoice2 == "OLY":t2 = team(569,340,62,359,788,131,400)
elif teamchoice2 == "PAN":t2 = team(574,340,80,344,768,105,333)
elif teamchoice2 == "PAR":t2 = team(501,350,74,393,768,149,326)
elif teamchoice2 == "PAT":t2 = team(537,348,105,301,799,114,270)
elif teamchoice2 == "RMA":t2 = team(558,333,69,336,795,132,362)
elif teamchoice2 == "VBA":t2 = team(545,371,62,351,725,135,289)
elif teamchoice2 == "VRB":t2 = team(581,366,77,312,771,150,277)
elif teamchoice2 == "ZAL":t2 = team(539,410,59,326,747,119,318)

print('\n' + teamchoice1,teamchoice2)

def game(otc,qrt,qrc,poss,sleeptime,game_in_action):
    for i in range(qrt):
        for j in range(poss):
            possesion()
        qrc+=1
        print(f"{sum(g1.list)} {sum(g2.list)} Q{qrc}")
        time.sleep(sleeptime * 10)
    print('\n' + f"End of Regulation score: {teamchoice1} {sum(g1.list)} - {sum(g2.list)} {teamchoice2}  Second chance points: {c1.scpc} - {c2.scpc}  Turnovers: {c1.trnvc} - {c2.trnvc} Foul points {c1.ftpc} - {c2.ftpc}" + '\n')
    while game_in_action == True:
        if sum(g1.list) == sum(g2.list):
            for i in range(poss // 2):
                possesion()
            qrc += 1
            otc += 1
            print(f"{sum(g1.list)} {sum(g2.list)} OT{otc}")
            time.sleep(sleeptime * 10)
        elif sum(g1.list)>sum(g2.list):
            g1.tw+=1
            game_in_action = False
        else:
            g2.tw+=1
            game_in_action = False
        if qrc > 4 and game_in_action == False:
            print('\n' + f"Final score: {teamchoice1} {sum(g1.list)} - {sum(g2.list)} {teamchoice2}  Second chance points: {c1.scpc} - {c2.scpc} Foul points {c1.ftpc} - {c2.ftpc}  Turnovers: {c1.trnvc} - {c2.trnvc}" + '\n')
            if otc>3:
                time.sleep(100)
    g1.list=[]
    g2.list=[]
    c1.scpc=0
    c2.scpc=0
    c1.ftpc=0
    c2.ftpc=0
    c1.trnvc=0
    c2.trnvc=0

def series(first_to):
    for i in range(first_to*2-1):
        game(otc,qrt,qrc,poss,sleeptime,game_in_action)
        print(f"{teamchoice1} {teamchoice2}")
        print(f"{g1.tw} - {g2.tw}" + '\n')
        time.sleep(sleeptime * 10)
        if g1.tw == first_to:
            print(f"{teamchoice1} is the winner")
            break
        elif g2.tw == first_to:
            print(f"{teamchoice2} is the winner")
            break

if __name__ == "__main__":
    series(first_to)
