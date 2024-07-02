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