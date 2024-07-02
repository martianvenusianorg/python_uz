import os
import platform
if platform.system() == 'Darwin':
    os.system('clear')
if platform.system() == 'Windows':
    os.system('cls')
    
names = ['akbar', 'akrom', 'humoyiddin', 'dilmurod', 'elmurod']
message = 'Salom {}! Seni kechgi ovqatga taklif qilaman.'

for name in names:
    print(message.format(name.title()))


not_coming = 'humoyiddin'
index_not_coming = names.index(not_coming)

print(f'\nKechgi ovqatga kelolmaydigan mehmon: {not_coming.title()}. Uning index raqami: {index_not_coming}')

new_guest = 'Suhrob'
print(f'Yangi taklif qilingan mehmonning ismi: {new_guest.title()}.\n')

names.remove(names[index_not_coming])
names.insert(index_not_coming, new_guest.lower())
for name in names:
    print(message.format(name.title()))
