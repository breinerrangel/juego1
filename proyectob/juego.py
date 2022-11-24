from random import randint
cantidad=int(input("cuntos veces quiere jugar : "))
maquina=0
x=randint(1,3)
conta=0
for i in range(cantidad):
    elija=int(input("ingre 1 para piedra /2 para papel /3 tijera : "))
    if  x==elija:
        print("empate ")
    elif elija==1 and x==3: 
        print("ganaste")  
        conta+=1
    elif elija==1 and x==2:
        print("perdiste")
        maquina+=1
    elif elija==2 and x==1:
        print(" ganaste")   
        conta+=1
    elif elija==2 and x==3:
        print("perdiste")     
        maquina+=1
    elif elija==3 and  x==1:
        print("perdiste")  
        maquina+=1  
    elif elija==3 and x==2:
        print("ganaste")   
        conta+=1
print(conta)   
print(maquina)      

print("")