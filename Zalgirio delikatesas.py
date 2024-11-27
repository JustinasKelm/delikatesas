import time
import random
list1=[]
list2=[]
list3=[]
list4=[]
tvc1=0
tvc2=0
tc1=0
tc2=0
otc=0
scpc1=0
scpc2=0
trnvc1=0
trnvc2=0
qrc=0
qrt=4
poss=20
ftpc1=0
ftpc2=0
fc1=0
fc2=0

class team:
    def __init__(self, o2, o3, d, scp, trnv, ftp, flp):
        self.o2=o2
        self.o3=o3
        self.d=d
        self.scp=scp
        self.trnv=trnv
        self.ftp=ftp
        self.flp=flp

teamchoice1=str(input("Įveskite pirmąją komandą: "))
if teamchoice1 == "ZAL":t1 = team(504,314,62,151,145,692,288) #r10
elif teamchoice1 == "PAN":t1 = team(593,414,132,126,139,704,213) #r10
elif teamchoice1 == "BAS":t1 = team(501,307,120,162,133,812,213) #r10
elif teamchoice1 == "PAR":t1 = team(518,373,188,132,139,776,258) #r10
teamchoice2=str(input("Įveskite antrąją komandą: "))
if teamchoice2 == "ZAL":t2 = team(504,314,62,151,145,685,288)
elif teamchoice2 == "PAN":t2 = team(593,414,132,126,139,704,213)
elif teamchoice2 == "BAS":t2 = team(501,307,120,162,133,812,213)
elif teamchoice2 == "PAR":t2 = team(518,373,188,132,139,776,258) 

print()
print(teamchoice1,teamchoice2)
for i in range(qrt):
    for j in range(poss):
        if random.randint(1,10)<4:
            if random.randint(1,1000)>t1.trnv:
                if random.randint(1,1100-t2.d)<t1.o3:
                    tc1+=3
                    list1.append(3)
                if tc1>0:
                    if random.randint(1,1000)<t2.flp:
                        fc1+=1
                        if random.randint(1,1000)<t1.ftp:
                            tc1+=1
                            list1.append(1)
                            ftpc1+=1
                else:
                    if random.randint(1,1000)<t2.flp:
                        fc1+=1
                        if fc1>4:
                            for i in range(3):
                                if random.randint(1,1000)<t1.ftp:
                                    tc1+=1
                                    list1.append(1)
                                    ftpc1+=1
            else:
                trnvc1+=1
                tvc1+=1
        if random.randint(1,10)<4:
            if random.randint(1,1000)>t2.trnv: 
                if random.randint(1,1100-t1.d)<t2.o3:
                    tc2+=3
                    list2.append(3)
                if tc2>0:
                    if random.randint(1,1000)<t1.flp:
                        fc2+=1
                        if random.randint(1,1000)<t2.ftp:
                            tc2+=1
                            list2.append(1)
                            ftpc2+=1
                else:
                    if random.randint(1,1000)<t1.flp:
                        fc2+=1
                        if fc2>4:
                            for i in range(3):
                                if random.randint(1,1000)<t2.ftp:
                                    tc2+=1
                                    list2.append(1)
                                    ftpc2+=1
            else:
                trnvc2+=1
                tvc2+=1
        if tc1==0 and tvc1==0:
            if random.randint(1,1000)>t1.trnv:
                if random.randint(1,1100-t2.d)<t1.o2:
                    tc1+=2
                    list1.append(2)
                if tc1>0:
                    if random.randint(1,1000)<t2.flp:
                        fc1+=1
                        if random.randint(1,1000)<t1.ftp:
                            tc1+=1
                            list1.append(1)
                            ftpc1+=1
                else:
                    if random.randint(1,1000)<t2.flp:
                        fc1+=1
                        if fc1>4:
                            for i in range(2):
                                if random.randint(1,1000)<t1.ftp:
                                    tc1+=1
                                    list1.append(1)
                                    ftpc1+=1
            else:
                trnvc1+=1
        if tc2==0 and tvc2==0:
            if random.randint(1,1000)>t2.trnv: 
                if random.randint(1,1100-t1.d)<t2.o2:
                    tc2+=2
                    list2.append(2)
                if tc2>0:
                    if random.randint(1,1000)<t1.flp:
                        fc2+=1
                        if random.randint(1,1000)<t2.ftp:
                            tc2+=1
                            list2.append(1)
                            ftpc2+=1
                else:
                    if random.randint(1,1000)<t1.flp:
                        fc2+=1
                        if fc2>4:
                            for i in range(2):
                                if random.randint(1,1000)<t2.ftp:
                                    tc2+=1
                                    list2.append(1)
                                    ftpc2+=1
            else:
                trnvc2+=1
        if tc1 == 0 and tvc1==0 or tc2 == 0 and tvc2==0:
            if random.randint(1,1000)<t1.scp and tc1 == 0 and tvc1==0:
                if random.randint(1,1000)>t1.trnv:
                    if random.randint(1,1100-t2.d)<t1.o2:
                        tc1+=2
                        scpc1+=2
                        list1.append(2)
                else:
                    trnvc1+=1    
            if random.randint(1,1000)<t2.scp and tc2 == 0 and tvc2==0:
                if random.randint(1,1000)>t2.trnv:
                    if random.randint(1,1100-t1.d)<t2.o2:
                        tc2+=2
                        scpc2+=2
                        list2.append(2)
                else:
                    trnvc2+=1
        print(tc1,tc2)
        list3.append(tc1)
        list4.append(tc2)
        tc1=0
        tc2=0
        tvc1=0
        tvc2=0
        fc1=0
        fc2=0
        time.sleep(0.3)
    qrc+=1
    print(f"{sum(list1)} {sum(list2)} Q{qrc}")
    time.sleep(3)
print("")
print(f"End of Regulation score: {teamchoice1} {sum(list1)} - {sum(list2)} {teamchoice2}  Second chance points: {scpc1} - {scpc2}")
print(f"Foul points {ftpc1} - {ftpc2}  Turnovers: {trnvc1} - {trnvc2}")
print("")
print(f"{sum(list3[0:19])} - {sum(list4[0:19])} Q1")
print(f"{sum(list3[20:39])} - {sum(list4[20:39])} Q2")
print(f"{sum(list3[40:59])} - {sum(list4[40:59])} Q3")
print(f"{sum(list3[60:79])} - {sum(list4[60:79])} Q4")
print("")
while sum(list1) == sum(list2):
    for i in range(poss//2):
        if random.randint(1,10)<4:
            if random.randint(1,1000)>t1.trnv:
                if random.randint(1,1100-t2.d)<t1.o3:
                    tc1+=3
                    list1.append(3)
                if tc1>0:
                    if random.randint(1,1000)<t2.flp:
                        fc1+=1
                        if random.randint(1,1000)<t1.ftp:
                            tc1+=1
                            list1.append(1)
                            ftpc1+=1
                else:
                    if random.randint(1,1000)<t2.flp:
                        fc1+=1
                        if fc1>4:
                            for i in range(3):
                                if random.randint(1,1000)<t1.ftp:
                                    tc1+=1
                                    list1.append(1)
                                    ftpc1+=1
            else:
                trnvc1+=1
                tvc1+=1
        if random.randint(1,10)<4:
            if random.randint(1,1000)>t2.trnv: 
                if random.randint(1,1100-t1.d)<t2.o3:
                    tc2+=3
                    list2.append(3)
                if tc2>0:
                    if random.randint(1,1000)<t1.flp:
                        fc2+=1
                        if random.randint(1,1000)<t2.ftp:
                            tc2+=1
                            list2.append(1)
                            ftpc2+=1
                else:
                    if random.randint(1,1000)<t1.flp:
                        fc2+=1
                        if fc2>4:
                            for i in range(3):
                                if random.randint(1,1000)<t2.ftp:
                                    tc2+=1
                                    list2.append(1)
                                    ftpc2+=1
            else:
                trnvc2+=1
                tvc2+=1
        if tc1==0 and tvc1==0:
            if random.randint(1,1000)>t1.trnv:
                if random.randint(1,1100-t2.d)<t1.o2:
                    tc1+=2
                    list1.append(2)
                if tc1>0:
                    if random.randint(1,1000)<t2.flp:
                        fc1+=1
                        if random.randint(1,1000)<t1.ftp:
                            tc1+=1
                            list1.append(1)
                            ftpc1+=1
                else:
                    if random.randint(1,1000)<t2.flp:
                        fc1+=1
                        if fc1>4:
                            for i in range(2):
                                if random.randint(1,1000)<t1.ftp:
                                    tc1+=1
                                    list1.append(1)
                                    ftpc1+=1
            else:
                trnvc1+=1
        if tc2==0 and tvc2==0:
            if random.randint(1,1000)>t2.trnv: 
                if random.randint(1,1100-t1.d)<t2.o2:
                    tc2+=2
                    list2.append(2)
                if tc2>0:
                    if random.randint(1,1000)<t1.flp:
                        fc2+=1
                        if random.randint(1,1000)<t2.ftp:
                            tc2+=1
                            list2.append(1)
                            ftpc2+=1
                else:
                    if random.randint(1,1000)<t1.flp:
                        fc2+=1
                        if fc2>4:
                            for i in range(2):
                                if random.randint(1,1000)<t2.ftp:
                                    tc2+=1
                                    list2.append(1)
                                    ftpc2+=1
            else:
                trnvc2+=1
                tvc2+=1
        if tc1 == 0 and tvc1==0 or tc2 == 0 and tvc2==0:
            if random.randint(1,1000)<t1.scp and tc1 == 0:
                if random.randint(1,1000)>t1.trnv:
                    if random.randint(1,1100-t2.d)<t1.o2:
                        tc1+=2
                        scpc1+=2
                        list1.append(2)
                else:
                    trnvc1+=1    
            if random.randint(1,1000)<t2.scp and tc2 == 0:
                if random.randint(1,1000)>t2.trnv:
                    if random.randint(1,1100-t1.d)<t2.o2:
                        tc2+=2
                        scpc2+=2
                        list2.append(2)
                else:
                    trnvc2+=1
        print(tc1,tc2)
        tc1=0
        tc2=0
        tvc1=0
        tvc2=0
        fc1=0
        fc2==0
        time.sleep(0.3)
    qrc+=1
    otc+=1
    print(f"{sum(list1)} {sum(list2)} OT{otc}")
    time.sleep(3)
if qrc>4:
    print("")
    print(f"Final score: {teamchoice1} {sum(list1)} - {sum(list2)} {teamchoice2}  Second chance points: {scpc1} - {scpc2}")
    print(f"Foul points {ftpc1} - {ftpc2}  Turnovers: {trnvc1} - {trnvc2}")
    print("")
