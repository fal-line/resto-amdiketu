from query import crewRaw
crewID =[]
result = []
inputID = ""
a = crewRaw.id(crewID)
for i in a:
    for x in i:
        result.append(x)
    
print('-- RESTO GAMING 2022 V.1 --')
def halMasuk(inputID):
    inputID=(input("Masukan ID:"))
    masuk(inputID,result)
    

def masuk(inputID,result):
        print(inputID)
        print(result)
        if inputID in result:
            print('GG gaming')
        else:
            print('ID tidak terdaftar atau salah')
            print('Silahkan coba lagi')
            halMasuk(inputID)
            

    


halMasuk(inputID)