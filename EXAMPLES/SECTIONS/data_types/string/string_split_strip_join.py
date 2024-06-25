name = 'Bugun tong otdi. Yana quyosh botdi.'

ajrat = name.split('.')
print(ajrat)

join_str = ''.join([ajrat[1].strip(), '. ', ajrat[0],'.'])
print(join_str)
