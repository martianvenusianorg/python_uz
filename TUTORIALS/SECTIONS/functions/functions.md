## Funksiyalar

Funksiya bu ma'lum bir vazifani bajaruvchi va o'z nomiga ega bo'lgan maxsus blokka olingan kodga aytiladi. Funksiya yordamida dasturda tez-tez takrorlanuvchi bir xil vazifani bajaruvchi kodlarni qayta-qayta yozishning oldini olish mumkin. Yani biror vazifani bajaruvchi kod yozishga to'g'ri kelganda shu vazifani bajaruvchi funksiyani chaqirish kifoya. Buning uchun dasturning biror qismida funksiya yaratiladi va shu funksiyaga ihtiyoj tug'ilganda uni chaqirib bajarilishi kerak bo'lgan vazifa unga yuklanadi. Shunda Python funksyaning ichidagi kodni ishga tushiradi. Funksya kodingizni yozishda, o'qishda, test qilib ko'rishda va tuzatish kiritishda sizga ancha qulayliklar yaratadi.

### Funksiyani yaratish

Python dasturlash tilida funksiya `def` maxsus so'zi yordamida ifodalanadi. _def_ maxsus so'zi funksiya yaratilayotganligini ifodalaydi va _def_ dan so'ng `funksiyaning nomi` beriladi. Funksiyaning nomidan so'ng `()`(qavs) ochib yopiladi va `:`(ikki nuqta) qo'yish orqali funksiyani ifodalash yakunlanadi. Ikki nuqtadan keyingi kodning blok qismi funksiyaning `tana`si hisoblanadi va qachonki funksiyaga murojat qilinganda funksiya tanasi ishga tushadi. Funksiya yaratilish davomida qavslar bo'sh bolishi mumkin (quyidagi 1-misol kabi), yoki funksiyaning qavslari o'z ichiga biror bilan ma'lumotni ham olishi mumkin (quyidagi 2-misol kabi). Bu haqida keyingi qismlarda to'liqroq ma'lumot beriladi.

```python
def func():
    language = 'python'
    print(f'I love {language.title()}!')
```

```python
def func(language):
    print(f'I love {language.title()}!')
```

### Funksiyaga murojaat qilish

Yaratilgan funksiyaga muroajaat shu funksiyaning nomi va qavslarni yozish orqali amalga oshiriladi. Qachonki siz bu funksiyadan foydalanishni istaganingizda bu funksiyani chaqirasiz va Python bu funksiyaning tanasini ishga tushiradi.

```python
func()
>>> I love PYTHON!
```

Yuqorida funksiyani chaqirdik va chaqirilgan funksiya o'z tanasini ishga tushirish orqali _\'I love Python!\'_ degan matnni chop etdi.

Qavslar orasida ma'lumot qabul qiluvchi funksiyaga esa quydagicha murojaat qilinadi.

```python
language = "python"
func(language)
>>> I love PYTHON!
```

Funksiya qavslari orasidagi _language_ o'zgaruvchisi orqali qiymat qabul qilda va shu qiymatni o'z tanasida qayta ishlab _\'I love PYTHON!.\'_ deb chop qildi. _\'language'_ o'zgaruvchisiga biror bir qiymatni berish orqali istagan boshqa so'zni funksiyaga uzatishimiz va shu so'zni fuksiya yordamida chop qilishimiz mumkin.

```python
language = "c++"
func(language)
>>> I love C++!
```

### *Argumentlar va Parameterlar*

Yuqoridagi misolda *func* nomli funksiya yaratdik va biror bir qiymatni o'zida qabul qiladigan o'zgaruvchini ham funksiyaning qavslari orasida yaratib ketdik. Va biz bu funksiya chaqirganimizda bu o'zgaruvchi (*language*) orqali funksiyamizga qiymat uzatamiz. Va bu o'zgaruvchimiz yani *language* funksiyamizning **parametr**i deb aytiladi va bu parameter qabul qiladigan qiymatlar (yuqoridagi misolda 'python' yoki 'c++') argumentlar bo'ladi. Argument bu funksiya chaqirilganda unga uzatiladigan ma'lumotga aytiladi. Biz qachonki funksiyani chaqirib unga argumentni berganimizda funksiya bu argumentni qabul qiladi va o'zining parametriga o'zlashtiradi. Yuqoridagi misolimizda biz funksiyamizni (*func*) chaqirdik va unga *python* argumentni uzatdik va *func* funksiyasi argumentni qabul qilib uni *language* parametriga o'zlashtirib oldi. Yani *func* funksiyasining *language* parametrining qiymati *python* so'ziga ega bo'ldi.

*ESLATMA**: Ko'pchilik argument va parameterlarni bir birining o'rnini almashtirib atashadi. Agar funksiya yaratilayotganda o'zgaruvchini argument yoki funksiyani chaqirganda o'zgaruvchini parameter deb atashganini ko'rganingizda hayron qolmang!*

### *docstring*

```python
def func():
    """Bu funksiya shunchaki oddiy textni chop qiladi"""
    print("I love PYTHON")
```

Yuqoridagi misolda funksiyaning tanasi bir qator matn bilan boshlanmoqda. Bu matn *docstring* deb nomlanadi va bu matn funksiya nima ish bajarishi haqida ma'lumot beradi. *Docstring*lar uch juft qo'shtirnoqlar orasiga olingan bo'lishi kerak. Python hujjatlashni yaratganda aynan shu *docstring*larni qidiradi.

### Topshiriq

**Topshiriq-1:** *display_message()* degan funksiya yarating va bu funksiyangiz siz python dasturlash tilini o'rganayotganingiz haqida xabar chiqarsin. Funksiyani ishga tushiring va funksiyangiz to'g'ri ishlayotganiga ishonch hosil qiling.

**Topshiriq-2:** *favorite_language()* degan funksiya yarating va u o'zida *language_name* degan parameterni qabul qilsin. Funksiyangiz 'Mening sevimli kitobim PYTHON' yoki 'Mening sevimli kitobim C++' kabi xabarlarni chiqarsin. Funksiyangizni chaqiring va to'g'ri ishlayotganiga ishonch hosil qiling. Funksiyani chaqirganingizda 'python' yoki 'c++' kabi argumentlarni funksiyaga berishni unutmang.
