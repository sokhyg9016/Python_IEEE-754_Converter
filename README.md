# IEEE-754 Converter
| **작성일**       | **키워드**           |  **참고**|
| ------------- |:-------------:|:-------------:| 
| 2019.10.30     | `Python` `IEEE754` | `CSCI256` 'CSCI223' |

## Points
1. ```Python``` 를 이용하여 IEEE754 Converter를 만들어 보자. 
1. ```CSCI223``` 에서 ```C```로 작성한 코드를 ```Python```으로 변환해보자.

## Python Code
> Library & Modules
```python
import sys
from ctypes import *
```

> Structure & Union
```python
# Define user-defined union
class tBits(Union):
    _fields_ = [
        ("f", c_float),
        ("i", c_uint32),
    ]

# Define user-defined structure
class tParts(Structure):
    _fields_ = [
        ("sign", c_uint32),
        ("exponent", c_uint32),
        ("significand", c_uint32)
    ]
```

> Functions
```python
def main(): # 메인 함수
def Normalize(num): # 입력 값을 sign, exponent, significand 파트로 나눈다.
def MakeFloatBits(part): # 앞에서 나눈 값들을 bitwise 연산을 통해 변환 시킨다.
```

## Output
```console
Enter the number: 10
Integer Number: 10, Bits: 0x0000000a, Size: 28
Sign: 0, Exponent: 130, Significand: 0x00200000
By Software, Number:    10.000000, Bits: 0x41200000
By Hardware, Number:    10.000000, Bits: 0x41200000
```

