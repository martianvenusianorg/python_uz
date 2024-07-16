Bu bo'limda biz dictionary haqida o'rganamiz.

Dictionaryga qisqacha misol:
Aytaylik biz biror bir avto mashina haqidagi ma'lumotlarni biror bir o'zgaruvchida saqlamoqchimiz. Avto mashinamiz quydagi ma'lumotlarga ega: Rusumi, rangi va ishlab chiqarilgan yili. Bu ma'lumotlarni o'zida saqlovchi dictionaryni quydagicha ifodalash mumkin:

```python
car = {'model':'bmw', 'color':'black', 'year':'2020'}
```

type() funksyasi yordamida o'zgaruvchimizning dictionary turli o'zgaruvchi ekanligiga ishonch hosil qilishimiz mumkin:

```python
car = {'model':'bmw', 'color':'black', 'year':'2020'}
print(type(car))
# <class 'dict'>
```

Yuqorida yaratgan dictionarymizni print() funksiyasi yordamizda chop qilib ko'rishimiz mumkin:

```python
car = {'model':'bmw', 'color':'black', 'year':'2020'}
print(car)
# {'model': 'bmw', 'color': 'black', 'year': '2020'}
```

Dictionary tanasi gajak qavslar bilan yasaladi.

Dictionary bitta *item* (bitta *key* va bitta *value*)dan iborat bo'lishi mumkin.

```python
car = {'model':'bmw'}
# {'model': 'bmw'}
```

Eng sodda dictionary o'zida hech qanday item saqlamasligi mumkin. Yani bo'sh bo'lishi ham mumkin. Rostdan dictionary turdagi o'zgaruvchi ekanligini type() funksyasi yordamida tekshirib ko'rishimiz mumkin.

```python
car = {}
print(car)
print(type(car))
# {}
# <class 'dict'>
```

**Items - Dictinaryning itemlari**

Dictonary *item*lari virgullar (,) bilan ajratiladi. Dictionaryda istaganingizcha itemlarni joylashtirishingiz mumkin. Dictionaryning har bir itemi *key-value* (kalit-qiymat) juftliklaridan iboratdir.  Kalit va qiymatlar o'zaro ikki nuqta (:) bilan ajratiladi. Yuqoridagi misolimizda *model*, *color*, *year* kalitlardir (*key*lardir) va *bwm*, *black*, *2020* lar qiymatlardir (*value*lardir).

**Keys - Dictionaryning kalitlari**

Har bir kalit o'ziga tegishli qiymat bilan uzviy bog'liq bo'ladi. Har bir kalit yordamida unga tegishli bo'lgan qiymatga murojaat qilish mumkin.

**Values - Dictionaryning qiymatlari**

Dictionary qiymatlari *integer*, *float*, *string*, *list* xatto *dictionary* kabi turli ma'lumot turlaridan iborat bo'lishi mumkin. Aniqroq aytadigan bo'lsak Python dasturlash tilida yaratish mumkin bo'lgan istalgan obyekt dictionaryning qiymatlari bo'lishi mumkin.

****Eslatma:** Python 3.7 dan boshlab dictionary yaratilgan vaqtidagi o'z itemlar tartibini saqlab qoladi. Yangi qo'shilgan itemlar ham qo'shilgan navbatiga qarab tartiblanadi.
**

**Kalit yordamida qiymatga murojaat qilish**

key yordamida uning valuesiga murojaat qilish uchun avvalo dictionary nomini yozamiz va to'rt burchak qavslar ichida *key*ni beramiz. Bu bizga valueni beradi. Bu quydagicha amalga oshiriladi:

```python
car = {'model':'bmw', 'color':'black', 'year':'2020'}
print(car['color'])
# black
```

Yuqoridagi misolda kalit *color* yordamida uning qiymati *black* ni chop qildik.

**Yangi item qo'shish**

Dictionary bu dinamik tuzilishga ega bo'lib, siz istgan vaqtingizda yangi item qo'shishingiz mumkin. Buning uchun dictinaryning nomidan keyin to'r burchak qavs ichida yangi kalitni kiritib unga yangi qiymatni o'zlashtiramiz.

```python
car = {'model':'bmw', 'color':'black', 'year':'2020'}
print(car)
# {'model': 'bmw', 'color': 'black', 'year': '2020'}
car['x_position'] = 10
car['y_position'] = 40
print(car)
# {'model': 'bmw', 'color': 'black', 'year': '2020', 'x_position': 10, 'y_position': 40}
```

Bo'sh dictionaryga item qo'shish ham yuqoridagi singari amalga oshiriladi

```python
car = {}
car['model'] = 'bmw'
car['color'] = 'black'
car['year'] = '2020'
car['x_position'] = 10
car['y_position'] = 40
print(car)
# {'model': 'bmw', 'color': 'black', 'year': '2020', 'x_position': 10, 'y_position': 40}
```
