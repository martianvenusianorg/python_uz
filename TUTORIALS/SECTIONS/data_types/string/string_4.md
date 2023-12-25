### .isdigit() metodi
```python
str = 'abc'
str_isdisit = str.isdigit()
print(str_isdisit)
# False
```

```python
str = '123'
str_isdisit = str.isdigit()
print(str_isdisit)
# True
```

### .islower() metodi
```python
str = 'python'
str_islower = str.islower()
print(str_islower)
# True
```

```python
str = 'PYTHON'
str_islower = str.islower()
print(str_islower)
# False
```

```python
str = 'Python'
str_islower = str.islower()
print(str_islower)
# False
```

```python
str = 'pYTHON'
str_islower = str.islower()
print(str_islower)
# False
```

### .isupper() metodi

```python
str = 'python'
str_isupper = str.isupper()
print(str_isupper)
# False
```

```python
str = 'Python'
str_isupper = str.isupper()
print(str_isupper)
# False
```

```python
str = 'pYTHON'
str_isupper = str.isupper()
print(str_isupper)
# False
```

```python
str = 'PYTHON'
str_isupper = str.isupper()
print(str_isupper)
# True
```

### .isspace() metodi
```python
str = 'python'
str_isspace = str.isspace()
print(str_isspace)
# False
```

```python
str = ' python '
str_isspace = str.isspace()
print(str_isspace)
# False
```

```python
str = ' '
str_isspace = str.isspace()
print(str_isspace)
# True
```