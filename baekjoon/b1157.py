# 백준 1157번
# 문제 : 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
# 입력 : 첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
# 출력 : 첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.

# 왜 런타임 에러가 뜰까...............

word = list(input().split())

new_string = ''
for i in word:
    new_string += i

# 대문자와 소문자를 구분하지 않으니 하나로 통일해주기위해 .upper() 메서드를 사용한다.
upper_string = new_string.upper()
new_dict = {}

for i in upper_string:
    if i in new_dict.keys():
        new_dict[i] += 1
    else:
        new_dict[i] = 1
        
max_key_list = []
max_value_list = []
for k, v in new_dict.items():
    max_key_list.append(k)
    max_value_list.append(v)

max_number = max(max_value_list)

count = max_value_list.count(max_number)
idx = max_value_list.pop(max_number)

if count == 1:
    print(max_key_list[idx])
else:
    print('?')
