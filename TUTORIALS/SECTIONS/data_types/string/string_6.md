### f-strings

Bazan o'zgaruvchini biror bir gap yoki matnning ichida yozishimizga to'g'ri kelishi mumkin. Aytaylik, bizda first_name va last_name degan o'zgaruvchilarimiz bor va bu o'zgaruvchilardan foydalanib biror kishining to'liq ism sharifini ekranga chiqarmoqchi bo'lsak, buni quydagicha amalga oshirishimiz mumkin.

```python
first_name = 'alisher'
last_name = 'navoi'
full_name = f'Mir {first_name.title()} {last_name.title()}'
print(full_name)
# Mir Alisher Navoi
```

Shunday qilib, biror bir o'zgaruvchini satrn ichiga joylashtirmoqchi bo'lsak, unda satr uchun ochiladigan qo'shtirnoqning oldidan ***f** * harfini qo'llaymiz va satr ichida o'zgaruvchilarni qavsga olgan holda ishlatamiz. Shunda Python satrni o'qiyotganda o'zgaruvchini qiymatini bilan almashtirib satrni o'qiydi.  Va bu satr *f-stringlar* deb nomlanadi. Bu yerda *f* harfi *format*  degan manoni bildiradi. Bunga yana bir misolni quydagi misoldan ko'rib olishingiz mumkin.

```python
famous_person = "Alisher Navoi"
quote = '''Haq yo‘linda kim senga bir harf o‘qitmish ranj ila, Aylamak bo‘lmas ado, oning haqin yuz ganch ila.'''
message = f'{famous_person} once said, "{quote}"'
print(message)
# Alisher Navoi once said, "Haq yo‘linda kim senga bir harf o‘qitmish ranj ila, Aylamak bo‘lmas ado, oning haqin yuz ganch ila."
```

### .format

*F-string*lar Python 3.6 dan keyin ommaga taqdim etilgan. Ungacha formatlash *format()* ishlatilgan. Va uning ishlatilish usuli quydagichadir.

```python
first_name = 'alisher'
last_name = 'navoi'
full_name= 'Mir {} {}'.format(first_name.title(), last_name.title())
print(full_name)
# Mir Alisher Navoi
```
