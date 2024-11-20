import time
import random
list1=[]
list2=[]
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
zal = team(454,346,60,334,191,685,151)
pan = team(529,422,100,301,177,715,301)

zalx = team(1000,1000,100,1000,10,1000,1000)
panx = team(1000,1000,100,1000,10,1000,1000)

for i in range(qrt):
    for j in range(poss):
        if random.randint(1,10)<4:
            if random.randint(1,1000)>zal.trnv:
                if random.randint(1,1100-pan.d)<zal.o3:
                    tc1+=3
                    list1.append(3)
                if tc1>0:
                    if random.randint(1,1000)<zal.flp:
                        fc1+=1
                        if random.randint(1,1000)<zal.ftp:
                            tc1+=1
                            ftpc1+=1
                else:
                    if random.randint(1,1000)<zal.flp:
                        fc1+=1
                        for i in range(3):
                            if random.randint(1,1000)<zal.ftp:
                                tc1+=1
                                ftpc1+=1
            else:
                trnvc1+=1
                tvc1+=1
        if random.randint(1,10)<4:
            if random.randint(1,1000)>pan.trnv: 
                if random.randint(1,1100-zal.d)<pan.o3:
                    tc2+=3
                    list2.append(3)
                if tc2>0:
                    if random.randint(1,1000)<zal.flp:
                        fc2+=1
                        if random.randint(1,1000)<zal.ftp:
                            tc2+=1
                            ftpc2+=1
                else:
                    if random.randint(1,1000)<zal.flp:
                        fc2+=1
                        for i in range(3):
                            if random.randint(1,1000)<zal.ftp:
                                tc2+=1
                                ftpc2+=1
            else:
                trnvc2+=1
                tvc2+=1
        if tc1==0 and tvc1==0:
            if random.randint(1,1000)>zal.trnv:
                if random.randint(1,1100-pan.d)<zal.o2:
                    tc1+=2
                    list1.append(2)
                if tc1>0:
                    if random.randint(1,1000)<zal.flp:
                        fc1+=1
                        if random.randint(1,1000)<zal.ftp:
                            tc1+=1
                            ftpc1+=1
                else:
                    if random.randint(1,1000)<zal.flp:
                        fc1+=1
                        for i in range(2):
                            if random.randint(1,1000)<zal.ftp:
                                tc1+=1
                                ftpc1+=1
            else:
                trnvc1+=1
        if tc2==0 and tvc2==0:
            if random.randint(1,1000)>pan.trnv: 
                if random.randint(1,1100-zal.d)<pan.o2:
                    tc2+=2
                    list2.append(2)
                if tc2>0:
                    if random.randint(1,1000)<zal.flp:
                        fc2+=1
                        if random.randint(1,1000)<zal.ftp:
                            tc2+=1
                            ftpc2+=1
                else:
                    if random.randint(1,1000)<zal.flp:
                        fc2+=1
                        for i in range(2):
                            if random.randint(1,1000)<zal.ftp:
                                tc2+=1
                                ftpc2+=1
            else:
                trnvc2+=1
        if tc1 == 0 and tvc1==0 or tc2 == 0 and tvc2==0:
            if random.randint(1,1000)<zal.scp and tc1 == 0 and tvc1==0:
                if random.randint(1,1000)>zal.trnv:
                    if random.randint(1,1100-pan.d)<zal.o2:
                        tc1+=2
                        scpc1+=2
                        list1.append(2)
                else:
                    trnvc1+=1    
            if random.randint(1,1000)<pan.scp and tc2 == 0 and tvc2==0:
                if random.randint(1,1000)>pan.trnv:
                    if random.randint(1,1100-zal.d)<pan.o2:
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
        time.sleep(0.3)
    qrc+=1
    print(f"{sum(list1)} {sum(list2)} Q{qrc}")
    time.sleep(3)
print("")
print(f"End of Regulation score: {sum(list1)} - {sum(list2)}  Second chance points: {scpc1} - {scpc2}  Turnovers: {trnvc1} - {trnvc2}")
print(f"Foul points {ftpc1} - {ftpc2}")
print("")
while sum(list1) == sum(list2):
    for i in range(poss//2):
        if random.randint(1,10)<4:
            if random.randint(1,1000)>zal.trnv:
                if random.randint(1,1100-pan.d)<zal.o3:
                    tc1+=3
                    list1.append(3)
                if tc1>0:
                    if random.randint(1,1000)<zal.flp:
                        fc1+=1
                        if random.randint(1,1000)<zal.ftp:
                            tc1+=1
                            ftpc1+=1
                else:
                    if random.randint(1,1000)<zal.flp:
                        fc1+=1
                        for i in range(3):
                            if random.randint(1,1000)<zal.ftp:
                                tc1+=1
                                ftpc1+=1
            else:
                trnvc1+=1
                tvc1+=1
        if random.randint(1,10)<4:
            if random.randint(1,1000)>pan.trnv: 
                if random.randint(1,1100-zal.d)<pan.o3:
                    tc2+=3
                    list2.append(3)
                if tc2>0:
                    if random.randint(1,1000)<zal.flp:
                        fc2+=1
                        if random.randint(1,1000)<zal.ftp:
                            tc2+=1
                            ftpc2+=1
                else:
                    if random.randint(1,1000)<zal.flp:
                        fc2+=1
                        for i in range(3):
                            if random.randint(1,1000)<zal.ftp:
                                tc2+=1
                                ftpc2+=1
            else:
                trnvc2+=1
                tvc2+=1
        if tc1==0 and tvc1==0:
            if random.randint(1,1000)>zal.trnv:
                if random.randint(1,1100-pan.d)<zal.o2:
                    tc1+=2
                    list1.append(2)
                if tc1>0:
                    if random.randint(1,1000)<zal.flp:
                        fc1+=1
                        if random.randint(1,1000)<zal.ftp:
                            tc1+=1
                            ftpc1+=1
                else:
                    if random.randint(1,1000)<zal.flp:
                        fc1+=1
                        for i in range(2):
                            if random.randint(1,1000)<zal.ftp:
                                tc1+=1
                                ftpc1+=1
            else:
                trnvc1+=1
        if tc2==0 and tvc2==0:
            if random.randint(1,1000)>pan.trnv: 
                if random.randint(1,1100-zal.d)<pan.o2:
                    tc2+=2
                    list2.append(2)
                if tc2>0:
                    if random.randint(1,1000)<zal.flp:
                        fc2+=1
                        if random.randint(1,1000)<zal.ftp:
                            tc2+=1
                            ftpc2+=1
                else:
                    if random.randint(1,1000)<zal.flp:
                        fc2+=1
                        for i in range(2):
                            if random.randint(1,1000)<zal.ftp:
                                tc2+=1
                                ftpc2+=1
            else:
                trnvc2+=1
                tvc2+=1
        if tc1 == 0 and tvc1==0 or tc2 == 0 and tvc2==0:
            if random.randint(1,1000)<zal.scp and tc1 == 0:
                if random.randint(1,1000)>zal.trnv:
                    if random.randint(1,1100-pan.d)<zal.o2:
                        tc1+=2
                        scpc1+=2
                        list1.append(2)
                else:
                    trnvc1+=1    
            if random.randint(1,1000)<pan.scp and tc2 == 0:
                if random.randint(1,1000)>pan.trnv:
                    if random.randint(1,1100-zal.d)<pan.o2:
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
        time.sleep(0.3)
    qrc+=1
    otc+=1
    print(f"{sum(list1)} {sum(list2)} OT{otc}")
    time.sleep(3)

if qrc>4:
    print("")
    print(f"Final score: {sum(list1)} - {sum(list2)}  Second chance points: {scpc1} - {scpc2}")
    print(f"Foul points {ftpc1} - {ftpc2}  Turnovers: {trnvc1} - {trnvc2}")
    print("")

