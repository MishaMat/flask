# Testing person.py

---
##Method get_age
while testing found a mistake
`AssertionError: 19 != -19`.
So as we can see we shall fix our get_age method.
> changes: in return swaped current year and year of birth

###Correct ans:

```python
import datetime

def get_age(self):
    now = datetime.datetime.now()
    return now.year - self.yob 
```
---
##Method set_name
We found a mistake `self.name = self.name`.
>changes: simply delete self. in literal.
###Correct ans:

```python
def set_name(self, name):
    self.name = name
```
---
##Method set_address
Missclick :doubled '=' `self.address == address`.
>changes: delete '='.

###Correct ans:
```python
def set_address(self, address):
    self.address = address
```
---
##Method is_homeless
The problem is that `self.get_address is None` 
will not return True even if there is empty 
string in address.
>changes: ~~self.get_address is None~~ self.get_address == ''
###Correct ans:
```python
def is_homeless(self):
    '''
    returns True if address is not set, false in other case
    '''
    return self.address == ''
```
