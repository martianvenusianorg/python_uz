### *Argumentlar va Parameterlar*

```python
def func(language):
    print(f'I love {language.title()}!')

language = "c++"
func(language)
>>> I love C++!
```

Yuqoridagi misolda *func* nomli funksiya yaratdik va biror bir qiymatni o'zida qabul qiladigan o'zgaruvchini ham funksiyaning qavslari orasida yaratib ketdik. Va biz bu funksiya chaqirganimizda bu o'zgaruvchi (*language*) orqali funksiyamizga qiymat uzatamiz. Va bu o'zgaruvchimiz yani *language* funksiyamizning **parametr**i deb aytiladi va bu parameter qabul qiladigan qiymatlar (yuqoridagi misolda 'python' yoki 'c++') argumentlar bo'ladi. Argument bu funksiya chaqirilganda unga uzatiladigan ma'lumotga aytiladi. Biz qachonki funksiyani chaqirib unga argumentni berganimizda funksiya bu argumentni qabul qiladi va o'zining parametriga o'zlashtiradi. Yuqoridagi misolimizda biz funksiyamizni (*func*) chaqirdik va unga *python* argumentni uzatdik va *func* funksiyasi argumentni qabul qilib uni *language* parametriga o'zlashtirib oldi. Yani *func* funksiyasining *language* parametrining qiymati *python* so'ziga ega bo'ldi.

*ESLATMA**: Ko'pchilik argument va parameterlarni bir birining o'rnini almashtirib atashadi. Agar funksiya yaratilayotganda o'zgaruvchini argument yoki funksiyani chaqirganda o'zgaruvchini parameter deb atashganini ko'rganingizda hayron qolmang!*

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

Funksiyani e'lon qilayotganimizda uning har bir parameteriga *default* qiymatlarni berish mumkin. Va funksiyaga murojat qilishda uning argumentlari berilmasa unda Python parameterning *default* qiymatidan foydalanadi. Shuning uchun agar funksiyani e'lon qilayotganda *defaul* parameter berib ketilsa funksiyaga murojat vaqtida funksiyaga argumentni uzatish shart bo'lmay qoladi va yuqorida aytilgani kabi Python *default* qiymatlardan foydalanadi. *Default* parameterlardan foydalanish funksiyani chaqirishni soddalashtiradi va funksiyada odatda foydalaniladigan argumentlarni alohida uzatishga xojat qoldirmaydi. Misol uchun uy hayvoni haqida ma'lumot beradigan *describe_pet()* funksiyasida  *anima_type* ga *"dog"* ni o'zlashtirish orqali default parameter sifatida belgilash mumkin. Chunki odatda biz  it(*dog*)ni uy hayvoni sifatida uyda saqlaymiz.

```
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')
```

Ko'rib turibsizki yuqoridagi misolda biz funksiyamizni chaqirganimizda argument o'rnida faqat itimizni ismi(pet_name='willie')ni  uzatdik va uning turini argument sifatida kiritishga hojat qolmadi. Chunki uning defaul parameter *animal_type* '*dog*' qiymatga ega. Natijamiz esa quydagicha bo'ladi:

```
I have a dog.
My dog's name is Willie.
```

E'tibor berish kerak bo'lgan narsa bu yearda funksiyaning parameterlarining tartibidir. Default qiymat sababli funksiyaning argumentida uy hayvoning turini kiritishning hojati yo'q. Bizda faqat uy hayvonining ismini kiritishimiz kerak bo'ladi holos. Python buni hali ham pozitsion argument sifatida biladi va funksiyaga faqatgina uy hayvonining ismi kiritiladigan bo'lsa unda bu argument funksiyaning birinchi parametriga mos keladi. Su sababdan birinchi funksiyaning birinchi parametri *pet_name*  deb belgilashimiz kerak bo'ladi. Bu funksiyadan foydalanishning eng sodda usuli funksiyani chaqirganda uning argumentiga faqat itning ismini ko'rsatishdir:

```
describe_pet('willie')
```

Ushbu funktsiya chaqiruvi oldingi misol bilan bir xil natijaga ega bo'ladi. Taqdim etilgan yagona argument "*willie*" dir, shuning uchun u ta'rifdagi birinchi parametr, *pet_name* bilan mos keladi. animal_type uchun argument berilmaganligi sababli, Python standart "*dog*" qiymatidan foydalanadi.

Itdan boshqa hayvonni tasvirlash uchun siz quyidagi kabi funktsiya chaqiruvidan foydalanishingiz mumkin:

```python
describe_pet(pet_name='harry', animal_type='hamster')
```

animal_type uchun aniq argument berilganligi sababli, Python parametrning *default* (standart) qiymatini e'tiborsiz qoldiradi.

***ESLATMA:*** *Standart qiymatlardan foydalanganda standart qiymatga ega bo'lgan har qanday parametr standart qiymatlarga ega bo'lmagan barcha parametrlardan keyin ro'yxatga olinishi kerak. Bu Pythonga pozitsion argumentlarni to'g'ri talqin qilishni davom ettirish imkonini beradi.*

### Funksiyaning chaqirishda turli yo'llar

*Positional* argument, *keyword* va *default argument*larni birgalikda ishlatish mumkin bo'lganligi sababli  funksiyani chaqirishda ham bir qancha variantlarni qo'llash mumkin. *Default* parameterga ega quydagi funksiyani ko'rib chiqaylik:

```python
def describe_pet(pet_name, animal_type='dog'):
```

Yuqoridagi funksiyada ko'rinib turibdiki *pet_name* uchun har doim argumentlarni kiritish talab qilinadi va qiymat *positional* va *keyword* formatlarda berilishi mumkin. Agar *animal_type* *dog* bo'ladigan bo'lsa *animal_type* uchun qiymat kiritishning hojati yo'q chunki uning qiymati *default* parameter bilan berilgan. Agar *animal_type* *dog* bo'lmaydigan bo'lsa unda uning qiymati funksiya chaqirilayotga vaqtda majburiy kiritilish talab etiladi. Bu yo *positional* yoki *keyword* formatlarda berilishi mumkin.

Quydagi hamma funksiya chaqiruvlari bu funksiya uchun ishlaydi:

```python
   # A dog named Willie.
   describe_pet('willie')
   describe_pet(pet_name='willie')
```

```python
   # A hamster named Harry.
   describe_pet('harry', 'hamster')
   describe_pet(pet_name='harry', animal_type='hamster')
   describe_pet(animal_type='hamster', pet_name='harry')
```

Yuqoridagi barcha funksiya chaqiruvlari bir xil natija beradi.

*ESLATMA: Funksiyani qaysi uslubda chaqirishingizning ahamiyati yo'q. Muhimi sizning funksiyangiz siz kutgan natijani bersa bo'ldi. Shunchaki o'zingiz tushinishingiz oson bo'lgan uslubni tanlang.*

### Argument kiritishda xatolarni oldini olish

### TOPSHIRIQ:

**Topshiriq 3:**  make_shirt() degan funksiya yarating. Bu funksiyangiz *size* va *message* degan parameterlarga ega bo'lsin. Funksiyangizning tanasida kiyimning o'lchami(*size*)ni va kiyim ustiga yoziladigan xabar(*message*)ni chop (print) qilsin.

* Funksiyangizni pozitsion argument(*positional arguments*)lardan foydalanib chaqiring.
* Funksiyangizni kalit so'z argument(*keyword arguments*)lardan foydalanib chaqiring.

**Topshiriq 4:** make_shirt() funksiyangizga o'zgartirish kiriting.

* Parameter *size*ning turi (*type*) *string* bo'lsin. Yani funksiyani chaqirganingizda *size* uchun argumentlarni X, XL, XXL kabi kirita oladigan bo'lsin.
* Parameter *size*ning turi (*type*) *integer* bo'lsin. Yani funksiyani chaqirganingizda *size* uchun argumentlarni 35, 40, 45 kabi kirita oladigan bo'lsin.
* Funksiyangizni pozitsion argument(*positional arguments*)lardan foydalanib chaqiring.
* Funksiyangizni kalit so'z argument(*keyword arguments*)lardan foydalanib chaqiring.

**Topshiriq 5:**  Topshiriq 4dagi make_shirt() funksiyangizga o'zgartirish kiriting.

* Parameterlarga *default* parameterlarni belgilang. Misol uchun *size* parameter uchun XL yoki 40 ni *default* paramter sifatida belgilang. *message* parameter uchun "*I love Python*" xabarini *default* qiymat sifatiga bering.
* Parameter *size*ning turi (*type*) *string* bo'lsin. Yani funksiyani chaqirganingizda *size* uchun argumentlarni X, XL, XXL kabi kirita oladigan bo'lsin.
* Parameter *size*ning turi (*type*) *integer* bo'lsin. Yani funksiyani chaqirganingizda *size* uchun argumentlarni 35, 40, 45 kabi kirita oladigan bo'lsin.
* Funksiyangizni pozitsion argument(*positional arguments*)lardan foydalanib chaqiring.
* Funksiyangizni kalit so'z argument(*keyword arguments*)lardan foydalanib chaqiring.
