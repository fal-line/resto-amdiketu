from query import getData
# import os
menuData =[]
result = []
inputID = ''
dic = {}
a = getData.menu(menuData)
inputID = input('Masukan ID:')
for i in a:
    # print(i)
    if inputID in str(i['id']):
        print(i['name'],i['price'])
    
    
# os.system('cls||clear')
# print('-- RESTO GAMING 2022 V.1 --')
# def halMasuk(inputID):
#     inputID=(input("Masukan ID:"))
#     masuk(inputID,result)
    

# def masuk(inputID,result):
#         if inputID in result:
#             os.system('cls||clear')
#             print('Berhasil masuk!')
#             print('GG gaming')
#         else:
#             os.system('cls||clear')
#             print('ID tidak terdaftar atau salah')
#             print('Silahkan coba lagi')
#             halMasuk(inputID)
            

    


# halMasuk(inputID)