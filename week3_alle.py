

Til alle:

NEI TIL NORSKE BOKSTAVER!
plz?


i en for-loop har vi en teller, ergo du trenger ikke en til

``` python
#nei
s=0; k=1
for i in range(m):
	s+= 1./(2*k**2)
	k +=1


#JA
s=0
for k in range(1,m+1):
	s+= 1./(2*k**2)
```



Det er ikke nødvendig og skrive print rundt et kall på test-funksjoner

```python
#plz nei
print(test_...())

#JA
test_...()
```



En test funksjon tar ikke inn argumenter!



Når en lager en if, så trenger man ikke alltid else;


```python

#EKVIVALENT MED NESTE funksjon
def f(x):
	if sin(x) > 0:
		return sin(x)
	else:
		return 0


def f(x):
	if sin(x) > 0:
		return sin(x)
	return 0
```


