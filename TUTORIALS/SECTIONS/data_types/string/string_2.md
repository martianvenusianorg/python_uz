### .find() metodi

```python
str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
str_i = str.find('a')
print(str_i)
# 0
```

```python
str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
str_i = str.find('s')
print(str_i)
# 18
```

```python
str = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
str_i = str.find('S')
print(str_i)
# 44
```

```python
str = 'abcd-abcd-abcd'
str_i = str.find('a',2)
print(str_i)
# 5
```

```python
str = 'abcd-abcd-abcd'
str_i = str.find('a',2,6)
print(str_i)
# 5
```

```python
str = 'abcd-abcd-abcd'
str_i = str.find('a',2,5)
print(str_i)
# -1
```

### .count() metodi

```python
str = 'abcd-abcd-abcd'
c = str.count('a')
print(c)
# 3
```

```python
str = 'abcd-abcd-abcd'
c = str.count('-')
print(c)
# 2
```
