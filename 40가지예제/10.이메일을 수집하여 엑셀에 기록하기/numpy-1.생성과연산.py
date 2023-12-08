#넘파이 패키지 임포트¶
#배열을 사용하기 위해서는 우선 다음과 같이 넘파이 패키지를 임포트한다. 넘파이는 np라는 이름으로 임포트하는 것이 관례이다.

#https://laboputer.github.io/machine-learning/2020/04/25/numpy-quickstart/

import numpy as np

#1차원 배열 만들기¶
#array

#넘파이의 array 함수에 리스트를 넣으면 ndarray 클래스 객체 즉, 배열로 변환해 준다. 따라서 1 차원 배열을 만드는 방법은 다음과 같다.
ar = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(ar)
print(type(ar))

# numpy.ndarray의 대표적인 속성값들은 다음과 같습니다.
#
# ndarray.shape : 배열의 각 축(axis)의 크기
# ndarray.ndim : 축의 개수(Dimension)
# ndarray.dtype : 각 요소(Element)의 타입
# ndarray.itemsize : 각 요소(Element)의 타입의 bytes 크기
# ndarray.size : 전체 요소(Element)의 개수

print(ar.shape)
# (3, 5)
print(ar.ndim)
# 2
print(ar.dtype)
# int64
print(ar.itemsize)
# 8
print(ar.size)
# 15
print(type(ar))
# <class 'numpy.ndarray'>

#1) 파이썬의 리스트를 사용하는 방법
list1 = [1,2,3,4]
a = np.array(list1)
print(a)
print(a.shape)

b = np.array([[1,2,3],[4,5,6]])
print(b)
print(b.shape)
print(b[0,0])

### 2) Numpy에서 제공하는 함수를 사용하는 방법
#### zeros(): 배열에 모두 0을 집어 넣음

aa = np.zeros((2,2))
print(aa)
type(aa)

#### ones(): 배열에 모두 1을 집어 넣음
aa = np.ones((2,3))
print(aa)

### 3)full(): 배열에 사용자가 지정한 값을 넣음
aa=np.full((2,3), 10)
print(aa)

### 4) eye(): 대각선으로는 1이고 나머지는 0인 2차원 배열을 생성
aa=np.eye(3)
print(aa)

#### 5) reshape(): 다차원으로 변형하는 함수
aa=np.array(range(20)).reshape((5,4)) #range(n): 0~n-1까지의 숫자를 생성하는 함수
print(aa)

#https://ooyoung.tistory.com/141

#벡터화 연산
#배열 객체는 배열의 각 원소에 대한 반복 연산을 하나의 명령어로 처리하는 벡터화 연산(vectorized operation)을 지원한다. 예를 들어 다음처럼 여러개의 데이터를 모두 2배 해야 하는 경우를 생각하자.

#1. 벡터화 연산
#1-1. 벡터
#벡터의 개념을 찾아보면 여러 가지 의미가 나온다. 그중 파이썬에서 사용하는 벡터의 개념을 이해하기로는, 한 가지 타입의 여러 개의 원소를 변수에 저장한 배열을 의미

#1-2. 벡터화 연산
#벡터화 연산은 벡터의 같은 인덱스에 위치한 원소들끼리 연산을 수행하는 기능이다
#반복문을 사용하지 않고도 반복해서 연산이 가능한 것이 특징이다.
# Numpy의 벡터화연산 기능을 사용하지 않는다면 for문과 같은 반복문을 구성해서 연산을 해야 같은 인덱스의 원소들끼리 연산을 수행할 수 있다.
array1 = np.arange(5)
print(array1)
print(array1 + array1)

#2-2. 2차원 ndarray 간 연산
array2 = np.arange(6).reshape(2, 3)
print(array2)
print(array2 + array2)

#2-3. 2차원 ndarray 배열간 사칙연산
print(array2 - array2)
print(array2 * array2)
print(array2 / array2)


#3. 배열과 스칼라의 연산
# 스칼라를 배열의 모든 원소에 대입해서 연산을 하기 때문이다. 아래에서 1차원, 2차원 배열 연산의 예를 들어본다.

array1 = np.arange(5)
print(array1)
#[0 1 2 3 4]


