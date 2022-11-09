from db.query import crewRaw
import connectDB

connectDB.connect()
crewID =[]
result = []
inputID = ['19221493'] 
a = crewRaw.id(crewID)
for a in a:
    if a[0] == a[0]:
        result.append(a[0])
    
print('-- RESTO GAMING 2022 V.1 --')
def halMasuk(inputID):
    inputID = [input('Masukan ID :')]
    masuk(inputID,result)
    

def masuk(inputID,result):
    # print(inputID)
    # print(result)
    cek = set(inputID) & set(result)
    for cek in cek:
        print(cek)
        
        # if inputID == result:
        #     print('GG gaming')
        #     break
        # else:
        #     print('ID tidak terdaftar atau salah')
        #     print('Silahkan coba lagi')
        #     halMasuk(inputID)
            

    


masuk(inputID,result)