from pathlib import Path
import time
import sys
import os

def fin_the_best(data,maximal_len,what):
    for iter in range(0,9):
        i=0
        poloczenie=[[] for _ in range(len(data))]
        for _ in range(1):
            while len(data)>i:
                j=0
                while len(data)>j and len(data)>i:
                    if data[i][0][len(data[i][0])-9+iter:len(data[i][0])] == data[j][0][0:9-iter] and i!=j:
                        poloczenie[i].append(j)
                    j+=1
                i+=1
            i=0
        poloczenie2=[0 for _ in range(len(data))]
        poloczenie02=[0 for _ in range(len(data))]
        
        for i in range(len(poloczenie)):
            for j in range(len(poloczenie[i])):
                poloczenie2[i]+=1
                poloczenie02[poloczenie[i][j]]+=1
        starting=set()
        starting = set(range(len(poloczenie)))
        used=set()
        for i in range(len(poloczenie)):
            if poloczenie2[i]>0:
                '''for k in range(len(poloczenie[i])):
                    j=poloczenie[i][k]
                    starting_true.discard(j)
                    ending.discard(i)'''
            if poloczenie2[i]==1 and poloczenie02[poloczenie[i][0]]==1:
                j=poloczenie[i][0]
                starting.discard(j)
                used.add(j)
        
            
        sum0=0
        taken=set()
        end=[]
        nowa={}
        sum0=0
        sum1=0
        sum2=0
        endings_of=dict()
        sum2=0
        for i in starting:
            endings_of[i]=poloczenie[i]
            pom=0
            if poloczenie2[i]==1 and poloczenie[i][0] not in taken and poloczenie02[poloczenie[i][0]]==1 :
                
                j=poloczenie[i][0]
                taken.add(j)
                if len(data[i][0])>=maximal_len:
                    what[0]=1
                    return data[i]
                dodanie_data(data,i,j,iter)

                endings_of[i]=poloczenie[j].copy()
                while poloczenie2[j]==1  and poloczenie[j][0] not in taken and poloczenie02[poloczenie[j][0]]==1:
                    j=poloczenie[j][0]
                    if len(data[i][0])>=maximal_len:
                        what[0]=1
                        return data[i]
                    dodanie_data(data,i,j,iter)
                    taken.add(j)
                    pom1=j
                    endings_of[i]=poloczenie[j].copy()
        
        starting.update(used-taken)
        for i in (used-taken):
            endings_of[i]=poloczenie[i].copy()
        for i in starting:
            if i not in taken:
                nowa[i]=[data[i],endings_of[i]]
        num=True
        i1=0
        sum0=0
        sum1=0
        sum2=0

        while num==True:
            i1+=1
            num=False
            for key, value in nowa.items():
                if key in value[1]:
                    value[1].remove(key)
                for val in value[1]:
                    if val not in list(nowa.keys()):
                        value[1].remove(val)
            
            i1+=1
            
            nowa_v1=sorted(nowa.items(),key=lambda x:x[1][0][2],reverse=True)
            for key, value in nowa_v1:
                
                num1=True
                
                if key in nowa:
                    while num1==True:
                        num1==False
                        pom1=[]
                        for i in range(len(value[1])):
                            if value[1][i] in nowa:
                                pom1.append(value[1][i])
                        pom=chosen1(nowa,pom1)
                        if pom==-1 or pom==key:
                            break
                        j=pom
                        if len(nowa[key][0][0])>=maximal_len:
                            break
                        dodanie_dict(nowa,key,j,iter)
                        if len(nowa[key][0][0])>=maximal_len:
                            what[0]=2
                            return nowa[key]
                        del nowa[j]
                        num1==True
                        num=True
                    
            
        for key1, _ in nowa_v1:   
            for key2, _ in nowa_v1:    
                if key1!=key2:
                    comparing_val_and_change(nowa,key1,key2,iter)

        data=[]
        sum0=0
        sum1=0
        sum2=0
        for key, value in nowa.items():
            data.append([value[0][0],value[0][1],value[0][2]])
            sum0+=len(value[0][0])
            sum1+=len(value[0][1])+1
            sum2+=value[0][2]
    what[0]=3
    return data

def comparing_val_and_change(nowa,key1,key2,iter):
    pom_val=nowa[key1][0][2]-2
    pom=pom_val
    pom1=0
    for i in range(len(nowa[key1][0][0]),10-iter,-1):
        
        if pom<=1:
            return
        if pom1==0:
            pom1 = nowa[key1][0][1][pom]
        pom1-=1
        if pom_val-pom>=nowa[key2][0][2]:
            break
        if nowa[key1][0][0][i-9+iter:i] == nowa[key2][0][0][:9-iter]:
            pom_str=nowa[key1][0][0][:i-9+iter]+nowa[key2][0][0]
            pom_str1=nowa[key1][0][0][i-9:]
            nowa[key1][0][0]=pom_str
            nowa[key2][0][0]=pom_str1

            pom_tab=nowa[key1][0][1][0:pom]+nowa[key2][0][1]
            nowa[key2][0][1]=nowa[key1][0][1][pom:]
            nowa[key1][0][1]=pom_tab

            nowa[key1][0][2]=pom+nowa[key2][0][2]
            nowa[key2][0][2]=pom_val-pom+2
            break
        
        if pom1==0:
            pom-=1
    return








def dodanie_data(data,i,j,iter):
    data[i][0]+=data[j][0][9-iter:len(data[j][0])]
    data[i][1].append(iter+1)
    data[i][1].extend(data[j][1])
    data[i][2]+=data[j][2]
    return

def dodanie_dict(nowa,key,pom,iter):
    nowa[key][0][0]+=nowa[pom][0][0][9-iter:]
    nowa[key][0][1].append(iter+1)
    nowa[key][0][1].extend(nowa[pom][0][1])
    nowa[key][0][2]+=nowa[pom][0][2]


    nowa[key][1]=nowa[pom][1]
    return
def chosen1(nowa,pom):
    if pom == []:
        return -1
    i=0
    pom1=[]
    for i in range(len(pom)):
        pom1.append([pom[i],len(nowa[pom[i]][0][1])])


    max_value = max(pom1, key=lambda x: x[1])[1]

    if sum(1 for x in pom1 if x[1] == max_value) == 1:
        maximal = max(pom1, key=lambda x: x[1])
        return maximal[0]
    else:
        return -1




def wypisz(nowa,i):
    sum0=0
    sum1=0
    sum2=0
    for key, value in nowa.items():
        sum0+=len(value[0][0])
        sum1+=len(value[0][1])+1
        sum2+=value[0][2]

if (len(sys.argv)!=2):
    print("give only name of a file or name of folders of files")
    exit(1)
current_folder = Path.cwd()
folder = Path(os.path.join(current_folder,sys.argv[1]))

if folder.is_file():
    folders=[folder]
else:
    folders=folder.glob("*")
i=0


for file_path in folders:  
    
    start = time.perf_counter()
    if file_path.is_file():  
        print("file name",file_path.name)     
        file_name = file_path.name.split(".")[1] 
        plus = file_name.split("+")
        minus = file_name.split("-")
        try:
            maximal_len=int(plus[0])
            opt=int(plus[0])
        except Exception as e:
            i+=1   
        try:
            maximal_len=int(minus[0])+9
            opt=int(minus[0])-int(minus[1])
        except Exception as e:
            i+=1 

    f=open(file_path)
    data_pom = f.read().split("\n")
    data=[]
    j=0
    for i in data_pom:
        if len(i)==10:
            data.append([i,[],1])
            j+=1

    what=[0]
    data_fin=fin_the_best(data,maximal_len,what)
    nowa=dict()
    if what[0]==1:
        nowa[0]=[data_fin]

    elif what[0]==2:
        nowa[0]=[data_fin[0]]
    else:
        for i in range(len(data_fin)):
            nowa[i]=[data_fin[i]]
    
    sum0=0
    list_of_items=sorted(nowa.items(),key=lambda x: len(x[1][0][0]),reverse=True)
    sum_len=0
    sum_num=0
    used_num=0
    val=""
    for i in range(len(list_of_items)):
        if sum_len+len(list_of_items[i][1][0][0])>maximal_len-10:
            val+=list_of_items[i][1][0][0][0:10]
            sum_num+=1
            used_num=maximal_len-sum_len-10
            sum_len+=10
            j=0
            k=0
            pom_pom=0
            while used_num>0 and k<len(list_of_items[i][1][0][1]):
                sum_len+=1
                j+=1
                val+=list_of_items[i][1][0][0][j+9]
                if pom_pom==0:
                    sum_num+=1
                    pom_pom=list_of_items[i][1][0][1][k]
                    k+=1
                pom_pom-=1
                used_num-=1
            break
        sum_len+=len(list_of_items[i][1][0][0])
        sum_num+=list_of_items[i][1][0][2]
        val+=list_of_items[i][1][0][0]
    print("ciag =",val)
    print("Wartosc funkcji celu =",sum_num,end="\t")
    print("dlugosc =",sum_len,end="\t")
    print("odleglosc od optimum =",opt-sum_num,end="\t")
    
    end = time.perf_counter()

    print("Czas:", end - start, "sekundy")
