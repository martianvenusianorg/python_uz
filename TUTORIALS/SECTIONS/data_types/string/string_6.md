### f'{}'

```python
first_name = 'alisher'
last_name = 'navoi'
full_name = f'Mir {first_name.title()} {last_name.title()}'
print(full_name)
# Mir Alisher Navoi
```

```python
famous_person = "Alisher Navoi"
quote = '''Haq yo‘linda kim senga bir harf o‘qitmish ranj ila, Aylamak bo‘lmas ado, oning haqin yuz ganch ila.'''
message = f'{famous_person} once said, "{quote}"'
print(message)
# Alisher Navoi once said, "Haq yo‘linda kim senga bir harf o‘qitmish ranj ila, Aylamak bo‘lmas ado, oning haqin yuz ganch ila."
```

### .format

```python
first_name = 'alisher'
last_name = 'navoi'
full_name= 'Mir {} {}'.format(first_name.title(), last_name.title())
print(full_name)
# Mir Alisher Navoi
```
