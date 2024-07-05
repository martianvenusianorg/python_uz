### `.sort()` funksiyasi yordamida listni tartiblash

```python
# numbers
ages = [27, 28, 18, 19]
print(ages)
# [27, 28, 18, 19]

ages.sort()
print(ages)
# [18, 19, 27, 28]

numbers = [27, 178.0, 80.0]
numbers.sort()
print(numbers)
# [27, 80.0, 178.0]
```

```python
# litters
names = ['akbar', 'akrom', 'huoyiddin', 'dilmurod']
print(names)
# ['akbar', 'akrom', 'huoyiddin', 'dilmurod']

names.sort()
print(names)
# ['akbar', 'akrom', 'dilmurod', 'huoyiddin']

names = ['akbar', 'Subxonberdiyev', 'Kamzayev',  'akrom']
print(names)
# ['akbar', 'Subxonberdiyes', 'Kamzayev', 'akrom']

names.sort()
print(names)
# ['Kamzayev', 'Subxonberdiyes', 'akbar', 'akrom']

```

```python
mixed = ['akrom', 27, 80.0, 178.0]
print(mixed)
# mixed.sort()
# TypeError: '<' not supported between instances of 'int' and 'str'
```

### `sorted()` funksiyasi yordamida listni tartiblash

```python
names = ['akrom', 'akbar', 'humoyiddin']

sorted_names = sorted(names)

print(names)
# ['akrom', 'akbar', 'humoyiddin']

print(sorted_names)
# ['akbar', 'akrom', 'humoyiddin']
```

### `.reverse()` funksiyasi yordamida listni teskari tartibda tartiblash

Listni teskari tartibda tartiblash uchun .reverse() funksyasidan foydalanamiz.

```python
ages = [27, 28, 18, 19]
print(ages)
# [27, 28, 18, 19]
ages.reverse()
print(ages)
# [19, 18, 28, 27]
```

```python
names = ['akbar', 'akrom', 'huoyiddin', 'dilmurod']
print(names)
# ['akbar', 'akrom', 'huoyiddin', 'dilmurod']
names.reverse()
print(names)
# ['dilmurod', 'huoyiddin', 'akrom', 'akbar']
```



### **Topshiriq:**

O'zingiz borishni istagan kamida beshta davlatning ro'yxatini yarating:

* Joy nomlarini ro'yxatga joylang va ular alifbo tartibda bo'lmasin.
* Roʻyxatni asl tartibda chop eting.
* Ro'yxatni haqiqiy tartibini saqlab qolgan holda sorted() dan foydalanib ro'yxatni alifbo tartibida chop eting.
* Qayta chop etish orqali ro‘yxatingiz asl tartibda ekanligini tekshiring.
* Asl ro'yxat tartibini o'zgartirmasdan ro'yxatingizni teskari alifbo tartibida chop etish uchun sorted() dan foydalaning.
* Qayta chop etish orqali ro‘yxatingiz asl tartibda ekanligini tekshiring.
* Ro'yxat tartibini o'zgartirish uchun reverse() dan foydalaning.
* Uning tartibi o'zgarganligini ko'rsatish uchun ro'yxatni chop eting.
* Roʻyxat tartibini yana oʻzgartirish uchun reverse() tugmasidan foydalaning.
* Roʻyxat asl tartibiga qaytganini koʻrish uchun ro'yxatni chop eting.
* Ro‘yxatni alifbo tartibida saqlash uchun sort() tugmasidan foydalaning.
* Ro'yxatning tartibi o'zgarganligni ko'rsatish uchun uni chop eting.
* Ro‘yxatni alifbo tartibida teskari tartibda saqlash uchun sort() tugmasidan foydalaning.
* Uning tartibi o'zgarganligini ko'rish uchun ro'yxatni chop eting.
