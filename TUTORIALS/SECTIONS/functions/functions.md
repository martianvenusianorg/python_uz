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

### *Funksiyaga ko'p marta murojaat*

Funksiyaga istaganingizcha murajaat qilishingiz mumkin. Aytaylik siz matn chop qiladigan funksiya yaratdingiz. Va bu funksiyani ketma ket 3 marta chaqiramiz. Va har safar funksiyani chaqirganimizda funksiyamizning tanasi ishga tushadi va 'I love PYTHON' matnini ketma ket 3 marta chop qiladi.

```python
def func():
    print('I love PYTHON!')
func()
func()
func()
```

```
I love PYTHON!
I love PYTHON!
I love PYTHON!
```

Funksiyani istagan vaqtda murojaat qilish ko'plab qulayliklarni beradi. Siz funksiyani kodning biror qismida yaratib qo'yasiz. Faqa qachonki bu funksiyaga ihtiyoj sezsangiz uni chaqirasiz va Python funksiyaning tana qismidagi kod blokni ishga tushiradi.

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


### Argumentlarni funksiyaga uzatish

Funksiyani bir necha parameterlar bilan birga yarish mumkin va huddi shu kabi funksiyani chaqirganingizda ham bir necha argumentlarni uzatishingiz mumkin. Funksiyaga parameterlarni bir necha yo'llar bilan uzatish mumkin. Parameterlarning yaratilgan tartibi shakli bilan bir xil tartibda, yani *positional arguments* yo'li bilan yoki *keyword arguments*, yani har bir argumentni o'zgaruvchiga uning qiymatini o'zlashtirish orqali amalga oshiriladi. O'zgaruvchilar list yoki dictionary kabi turli o'zgaruvchilardan iborat bo'lishi mumkin. Keling, bularning har birini o'z navbatida ko'rib chiqaylik.

### **Pozitsion argumentlar (Positional Arguments)**

Funksiya chaqirilganda funksiyaning argumentlari funksiya yaratilgandagi parameterlarining tartibiga most tushishi kerak. Shu tarzda parameter va argumentlarning mos kelishi *positional arguments* deb ataladi.

Buning qanday ishlashini ko'rish uchun uy hayvonlari haqida ma'lumot chiqaradigan funksiyani ko'rib chiqamiz. Bu funksiyamiz har bir uy havonining ismini va u qanaqa hayvon ekanligi haqida ma'lumotni chop qilsin.

```python
def describe_pet(animal_type, pet_name):
	"""Display information about pet."""
	print(f"\nI have a {animal_type}.")
	print(f"My {animal_type}'s name is {pet_name.title()}.")

def describe_pet('hamster', 'harry')
```

Yuqorida ko'rib turganingizdek yaratgan funksiyamiz *animal_type*, *pet_name* parameterlari bilan yaratildi. Biz bu funksiyamizni chaqirganimizda *animal_type*, *pet_name* parameterlar tartibiga most ravishda argumentlarni berdik (*'hamster'*, *'harry'*). Funksiyaning tanasida bu ikki parameter uy hayvonimiz haqidagi ma'lumotlarni chiqarishda ishlatildi. Natija quydagicha bo'ladi:

```
I have a hamster.
My hamster's name is Harry.
```

Funksiyangizda pozitsion argumentlardan istaganingizcha foydalanishingiz mumkin. Funksiyangizni chaqirganingizda berilgan argumentlarning tartibiga qarab Python bu argumentlarni funksiyaning parameterlariga mos o'zlashtiradi.

#### Pozitsion argumentlarda tartib juda muhim

Pozitsion argumentlardan foydalanganda chaqirilgan funksiyaning argumentlarini funksiyaning parameterlariga mos ravishda bermasangiz siz kutmagan natija yoki xatolik ro'y berishi mumkin. Keling quydagicha funksiya yaratib unga murojaat qilaylik

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('harry', 'hamster')
```

Ko'rib turibsizki yuqoridagi misolda *animal_type*, *pet_name* parameterlarga ega funksiya yaratdek. Lekin funksiyani chaqirishda parameter *animal_type* o'rnida argumentimizni '*harry*' va parameter  *pet_name* o'rnida argumentimizni '*hamster*' deb uzatdik. Yani uy hayvonining turi o'rniga ismni va ismining o'rniga uni turini uzatdik. Va natijamiz quydagicha bo'ldi:

```
I have a harry.
My harry's name is Hamster.
```

Agar siz shunaqa g'alati natijaga duch kelsangiz unda argumentlaringizning tartibi funksiyangizning parameterlariga mos kelish kelmasligini yana bir bor tekshirib ko'ring.

### Kalit so'zli argumentlar (Keyword Arguments)

*Keyword Arguments* shaklda argumentlarni uzatish funksiya chaqirganda argumentlarning tartibi funksiya yaratilgandagi parameterlarning tartigibi mos kelishi talab etilmaydi. Faqat bunda funksiyaga uzatilayotgan argument o'ziga mos bo'lgan parameter nomi bilan bir xil o'zgaruvchiga o'zlashtirilgan holda uzatiladi. Shu tarzda argumentlarning tartibi parameterlarning tartibiga mos kelmasa ham uzatilayotgan argument funksiyaga tug'ri tartibda uzatiladi. Keling buni quydagi misolda ko'rib chiqamiz. Oldin *describe_pet()* nomi funksiya yarataylik. U *animal_type*, *pet_name* parameterlarga ega bo'lsin. 

```python
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")
```

Bu funksiyani chaqirishda argumentlarni (animal_type='hamster', pet_name='harry') funksiya yaratilgan vaqtdagi parameterlar tartibiga mos ravishda beramiz. 

```python
describe_pet(animal_type='hamster', pet_name='harry')
```

```
I have a hamster.
My hamster's name is Harry.
```

Funksiyamizni ikkinchi marta chaqirganimizda argumentlarni (pet_name='harry', animal_type='hamster') funksiya yaratilgan vaqtdagi parameterlar tartibiga teskari ravishda beramiz. 

```python
describe_pet(pet_name='harry', animal_type='hamster)
```

```
I have a hamster.
My hamster's name is Harry.
```

Faqat ikki holatda ham argumentlarni uzatishda funksiya parameterlariga mos ismli o'zgaruvchilarga o'zlashtirgan holda uzatdik. Ikki holatda ham funksiyamiz bir hil natijani berganini ko'rishimiz mumkin.

***ESLATMA:** Kalit so'zli argumentlar (Keyword Arguments)dan foydalanib funksiyaga murojaat qilganda, funktsiya yaratishdagi parametrlarning aniq nomlaridan foydalanganingiz kerak bo'ladi.*

### Standart qiymatlar (Default Values)
