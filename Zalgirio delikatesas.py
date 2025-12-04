import time
import random
import requests
import pandas as pd
from bs4 import BeautifulSoup,Comment

url = 'https://www.basketball-reference.com/international/euroleague/2026.html#team_stats_per_game'
response = requests.get(url)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
comments = soup.find_all(string=lambda text: isinstance(text, Comment))
table = None
for comment in comments:
    if 'id="team_stats_per_game"' in comment:
        comment_soup = BeautifulSoup(comment, "html.parser")
        table = comment_soup.find("table", {"id": "team_stats_per_game"})
        break
headers = [th.get_text(strip=True) for th in table.find_all("th")]
rows = table.find("tbody").find_all("tr")
rows_data = []
for row in rows:
    cells = [td.get_text(strip=True) for td in row.find_all("td")]
    rows_data.append(cells)

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

def gamemode():
    pass

def team_selection():
    teamchoice1=str(input("Įveskite namų komandą: "))
    teamchoice2=str(input("Įveskite kelio komandą: "))
    for i in range(team_amount):
        if teamchoice1 == rows_data[i][0][:3].lower():
            teamchoice1 = rows_data[i][0]
            t1_ix = i
        if teamchoice2 == rows_data[i][0][:3].lower():
            teamchoice2 = rows_data[i][0]
            t2_ix = i
    t1 = team(int(float(rows_data[t1_ix][10])*1000),int(float(rows_data[t1_ix][7])*1000),100,int((float(rows_data[t1_ix][14]))/(float(rows_data[t1_ix][14])+float(rows_data[t2_ix][15]))*1000),int(float(rows_data[t1_ix][13])*1000),int(float(rows_data[t1_ix][20])*10),200)
    t2 = team(int(float(rows_data[t2_ix][10])*1000),int(float(rows_data[t2_ix][7])*1000),100,int((float(rows_data[t2_ix][14]))/(float(rows_data[t2_ix][14])+float(rows_data[t1_ix][15]))*1000),int(float(rows_data[t2_ix][13])*1000),int(float(rows_data[t2_ix][20])*10),200)
    return teamchoice1, teamchoice2, t1, t2

otc=0
qrc=0
qrt=4
poss=20
team_amount=20
sleeptime = 0
game_in_action = True
teamchoice1, teamchoice2, t1, t2 = team_selection()
c1 = counters(0, 0, 0, 0, 0, 0) #after round13
c2 = counters(0, 0, 0, 0, 0, 0) #after round13
g1 = game_specific(0,[])
g2 = game_specific(0,[])

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
        print(f"{teamchoice1} - {teamchoice2}")
        print(f"{g1.tw} - {g2.tw}" + '\n')
        time.sleep(sleeptime * 10)
        if g1.tw == first_to:
            print(f"{teamchoice1} is the winner")
            break
        elif g2.tw == first_to:
            print(f"{teamchoice2} is the winner")
            break

if __name__ == "__main__":
    first_to = int(input("Reikalingas pergalių kiekis "))
    series(first_to)

if __name__ == "__main__":
    series(first_to)

