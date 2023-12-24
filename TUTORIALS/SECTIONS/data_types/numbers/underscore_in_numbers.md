### Raqamlarda pastki chiziqning qo'llanilishi
Katta raqamlarni yozayotganda, katta raqamlarni o'qishga qulay bo'lishi uchun pastki chiziqlardan foydalanib raqamlarni guruhlashingiz mumkin:

```python
dollar = 12_200
print(dollar)
# 12200
```

Agar pastgi chiziq bilan yozilgan raqamning turini tekshirib  ko'radigan bo'lsak quyidagicha natija olishimiz mumkin. Natija esa integer tur ekanini ko'rishimiz mumkin.
```python
print(type(dollar))
# <class 'int'>
```

Float turdagi raqam bilan ham o'xshash holatni kuzatishimiz mumkin. 

```python
dollar = 12_200.0
print(dollar)
# 12200.0
```

```python
print(type(dollar))
#<class 'float'>
```
