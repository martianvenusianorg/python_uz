### .split() metodi
```python
str = 'Bugun tong otdi. Va yana quyosh botdi!'
str_split = str.split('.')

print(str_split)
# ['Bugun tong otdi', ' Va yana quyosh botdi!']

print(type(str_split))
# <class 'list'>

print(len(str_split))
# 2

print(str_split[0])
# Bugun tong otdi

print(str_split[1])
#  Va yana quyosh botdi!
```

### .join() metodi
```python
folder1 = 'D:/folder1'
folder2 =  'folder2'
path = ''.join([folder1,'/',folder2,'/'])
print(path)
# D:/folder1/folder2/
```