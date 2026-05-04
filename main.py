f=open("prob.txt")
data = f.read().split("\n")

i=0
while len(data)>i:
    if len(data[i])!=10:
        data.pop(i)
        i-=1
    i+=1
i=0
for iter in range(0,9):
    i=0
    poloczenie=[[] for _ in range(len(data))]
    for _ in range(1):
        while len(data)>i:
            j=0
            while len(data)>j and len(data)>i:
                if data[i][len(data[i])-9+iter:len(data[i])] == data[j][0:9-iter] and i!=j:
                    poloczenie[i].append(j)
                j+=1
            i+=1
        i=0
    poloczenie2=[0 for _ in range(len(data))]
    for i in range(len(poloczenie)):
        for j in range(len(poloczenie[i])):
            poloczenie2[i]+=1
    data1=[]
    all_rel=[0 for _ in range(len(poloczenie))]
    print("pol",poloczenie)
    print("pol1",poloczenie2)

    starting=set()
    starting = set(range(len(poloczenie)))
    temp=set()
    for i in range(len(poloczenie)):
        if poloczenie2[i]==1:
            for k in range(len(poloczenie[i])):
                j=poloczenie[i][k]
                starting.discard(j)
        elif poloczenie2[i]==2:
            for k in range(len(poloczenie[i])):
                j=poloczenie[i][k]
                temp.add(j)
    print(len(starting))
    print("all relewant")
    print(starting)
    sum=0
    taken=set()
    used=set()
    end=[]
    nowa={}
    for i in starting:
        pom=0
        if poloczenie2[i]!=0:
            
            j=poloczenie[i][0]
            taken.add(j)
            data[i]+=data[j][9-iter:len(data[j])]
            end=poloczenie[j]
            while poloczenie2[j]==1 and poloczenie[j][0] not in taken:
                j=poloczenie[j][0]
                data[i]+=data[j][9-iter:len(data[j])]
                taken.add(j)
                pom1=j
                end=poloczenie[j]
        sum+=len(data[i])
        print(i,data[i],"len",len(data[i]),end)
        nowa[i]=[data[i],end.copy()]
    print(sum)
    #print("taken",len(taken))
    print("nowa")
    for key, value in nowa.items():
        if key in value[1]:
            value[1].remove(key)
        
    i=0
    starting = starting-temp
    start=list(starting)[0]
    print(start)
    print(nowa[start][1])

    print("nowa")
    for key, value in nowa.items():
        print(key,value,len(value[0]))

    for i in range(7):
        for key, value in nowa.items():
            if key in value[1]:
                value[1].remove(key)
            for val in value[1]:
                if val not in list(nowa.keys()):
                    value[1].remove(val)

        for key, value in list(nowa.items()):
            if key in nowa:
                if len(value[1])==1  and value[1][0] in nowa:
                    print(key,value[1])
                    pom = value[1][0]
                    nowa[key][0]+=nowa[pom][0][9-iter:]
                    nowa[key][1]=nowa[pom][1]
                    del nowa[pom]
                    print(pom)
    print("nowa1")
    for key, value in nowa.items():
        print(key,value,len(value[0]))
    data=[]
    sum=0
    for key, value in nowa.items():
        data.append(value[0])
        sum+=len(value[0])
    print("iter",iter,"data",data)
    print("suma",sum)
while len(data)>1:
    data[0]+=data[1]
    data.pop(1)
sum=0
for i in data:
    sum+=len(i)
print("iter",iter,"data",data)
print("suma",sum)


