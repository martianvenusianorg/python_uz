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

message = 'Salom {}! Kechgi ovqatga yangi mehmonlarni taklif qimoqchiman. Yangi mehmonlar ro\'yxati: {}'

three_guests = ['yusuf', 'hasan', 'husan']
print()
for name in names:
    print(message.format(name.title(), three_guests))

names.insert(0, three_guests[0])
names.insert(len(names)//2, three_guests[1])
names.insert(-1, three_guests[2])
print("\nMehmonlarning yangi ro'yxati:")
for name in names:
    print(f'\t{name.title()}')