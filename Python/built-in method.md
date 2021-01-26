# 파이썬 내장함수

## `.sort()`와 `sorted()`의 차이점

- `.sort()`의 경우 기존의 list 값 자체를 정렬해서 바꾼다.

- `new_list = num_list.sort()`와 같이 코드를 작성하고 `print(new_list)`를 해보면 None이 출력된다.

- 즉 `.sort()`를 사용하게되면 원래있는 값을 바꾸는 것이지 리턴값은 없다.

  ```python
  num_list = [1, 3, 9, 2, 4]
  new_list = num_list.sort()
  
  print(new_list) #=> None이 출력된다.
  print(num_list) #=> [1, 2, 3, 4, 9]
  ```

  

- `sorted()`의 경우 기존의 list 값은 변환하지 않는다.

- `new_list = sorted(num_list)`와 같이 코드를 작성하고 `print(new_list)`를 해보면 정렬된 값이 출력된다.

  ```python
  num_list = [1, 3, 9, 2, 4]
  new_list = sorted(num_list)
  
  print(new_list) #=> [1, 2, 3, 4, 9] 오름차순으로 정렬되어 잘 출력된다.
  print(num_list) #=> [1, 3, 9, 2, 4] 원본 데이터는 변환되어있지 않다.
  ```

  

## `.append()`와 `.extend()`의 차이점

- `.append()`는 추가하는 값 그 자체를 가장 마지막에 추가한다.

- `.extend()`는 추가하는 iterable한 객체의 각 요소들을 추가한다.

  ```python
  number_list = [1, 2, 3, 4, 5]
  # number_list를 shallow copy한다.
  new_num_list = list(number_list)
  
  x = ['ping', 'pong']
  
  # append는 x그 자체를 원소로 가장 마지막에 추가한다.
  # 즉 x가 list이므로 list자체를 통째로 마지막에 추가한다.
  number_list.append(x)
  print(number_list) # => [1, 2, 3, 4, 5, ['ping', 'pong']]
  
  # extend는 iterable의 각 항목들을 넣는다.
  # x가 iterable한 객체이므로 각 요소들을 추가한다.
  new_num_list.extend(x)
  print(new_num_list) # => [1, 2, 3, 4, 5, 'ping', 'pong']
  
  # 조금 더 직관적으로 확인하려면 문자열을 넣어보면 확실하게 알수있다.
  y = 'tong'
  
  # append는 문자열이 통째로 요소로 추가된걸 볼 수 있지만
  number_list.append(y)
  print(number_list) # => [1, 2, 3, 4, 5, ['ping', 'pong'], 'tong']
  
  # extend는 iterable 객체의 각 요소를 추가하므로 t, o, n, g로 나눠서 추가된 걸 확인할 수 있다.
  new_num_list.extend(y)
  print(new_num_list) # => [1, 2, 3, 4, 5, 'ping', 'pong', 't', 'o', 'n', 'g']
  ```

  

## shallow copy와 deep copy

- 흔히 우리는 어떠한 변수에 값을 할당할 때 할당 연산자인 `=`을 사용한다.

- 변환 불가능한 객체(immutable)에 한해서는 아래와 같이 코드를 작성해도 서로의 값이 변하지않는다는 걸 알 수 있다.

  ```python
  abc = 'alpabet'
  print(abc) # => alpabet
  
  cba = abc
  cba = 'tebapla'
  print(abc) # => alpabet
  print(cba) # => tebapla
  ```

  

- 하지만 list와 같은 mutable객체는 위와같이 코드를 작성하게 되면 문제가 생긴다.

- 아래와 같이 `b[2] = 10`으로 b객체의 값을 바꿨는데 a의 값도 함께 바뀌는 걸 확인할 수 있다.

- 이는 mutable 객체의 특성상 `b = a`와 같이 코드를 작성하게되면 값을 복사하는것이 아닌 두 객체의 주소값이 같아지는 식으로 처리되기 때문이다.

  ```python
  a = [1, 2, [3, 4, 5]]
  b = a
  print(a) # => [1, 2, 3, 4, 5]
  print(b) # => [1, 2, 3, 4, 5]
  
  b[1] = 10
  print(a) # => [1, 10, [3, 4, 5]]
  print(b) # => [1, 10, [3, 4, 5]]
  ```



- 그렇기 때문에 mutable한 객체를 복사할때는 약간 다른 방식을 사용하여 복사를 해야한다.

  - shallow copy의 경우 아래와 같은 2가지 방법으로 진행할 수 있다.
  - `b = list(a)`와 같이 list로 형 변환을 해주며 주소값을 다르게 해주는 방법이 있고
  - `import copy`를 통해 copy 모듈을 불러와 `b = copy.copy(a)`와 같이 사용할 수 있다.

  ```python
  a = [1, 2, [3, 4, 5]]
  b = list(a)
  print(a) # => [1, 2, [3, 4, 5]]
  print(b) # => [1, 2, [3, 4, 5]]
  
  b[1] = 10
  print(a) # => [1, 2, [3, 4, 5]]
  print(b) # => [1, 10, [3, 4, 5]]
  ```

  ```python
  import copy
  
  a = [1, 2, [3, 4, 5]]
  b = copy.copy(a)
  print(a) # => [1, 2, [3, 4, 5]]
  print(b) # => [1, 2, [3, 4, 5]]
  
  b[1] = 10
  print(a) # => [1, 2, [3, 4, 5]]
  print(b) # => [1, 10, [3, 4, 5]]
  ```



- 1차원 list의 경우 위와같은 shallow copy로 복사가 가능하지만 2차원 list의 경우 list안의 list요소의 값이 제대로 복사되지 않아 deep copy를 사용해야 한다.

  ```python
  import copy
  
  a = [1, 2, [3, 4, 5]]
  b = copy.copy(a)
  print(a) # => [1, 2, [3, 4, 5]]
  print(b) # => [1, 2, [3, 4, 5]]
  
  b[1] = 10
  print(a) # => [1, 2, [3, 4, 5]]
  print(b) # => [1, 10, [3, 4, 5]]
  
  c = copy.copy(a)
  c[2].append(6)
  print(a) # => [1, 2, [3, 4, 5, 6]]   
  print(c) # => [1, 2, [3, 4, 5, 6]] 
  
  # 위에서 보는바와 같이 2차원 list의 경우 list안의 list값이 함께 바뀌는 걸 볼 수 있다.
  ```

  ```python
  import copy
  
  a = [1, 2, [3, 4, 5]]
  # 이렇게 deepcopy를 해주게되면 아래 출력값을 deepcopy한 d만 변환되게 출력할 수 있다!
  d = copy.deepcopy(a)
  d[2].append(6)
  print(a) # => [1, 2, [3, 4, 5]]   
  print(d) # => [1, 2, [3, 4, 5, 6]] 
  ```

  

