from query import crewRaw
import os
crewID =[]
result = []
inputID = ""
a = crewRaw.id(crewID)
for i in a:
    for x in i:
        result.append(x)
    
os.system('cls||clear')
print('-- RESTO GAMING 2022 V.1 --')
def halMasuk(inputID):
    inputID=(input("Masukan ID:"))
    masuk(inputID,result)
    

def masuk(inputID,result):
        if inputID in result:
            os.system('cls||clear')
            print('Berhasil masuk!')
            print('GG gaming')
        else:
            os.system('cls||clear')
            print('ID tidak terdaftar atau salah')
            print('Silahkan coba lagi')
            halMasuk(inputID)
            

    


halMasuk(inputID)