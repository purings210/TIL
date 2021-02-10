# 백준 2562번
# 문제 : 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
#        예를 들어, 서로 다른 9개의 자연수
#        3, 29, 38, 12, 57, 74, 40, 85, 61
#        이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.
# 입력 : 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.
# 출력 : 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

# 한줄씩 숫자가 들어오므로 for문을 통해서 숫자입력을 받고 
# 이 숫자들을 순회하기 쉽도록 빈 리스트 선언 후 리스트에 계속해서 추가한다.
numbers = []
for i in range(9):
    N = int(input())
    numbers += [N]

max_value = 0
max_idx = 0
# 인덱스값과 값을 모두 활용하기 위해 enumerate를 사용한다.
for idx, item in enumerate(numbers):
    if item > max_value:
        max_value = item
        max_idx = idx

print(max_value)
# 인덱스의 경우 +1을 해줘야 위치에 맞는 숫자가 된다.
print(max_idx+1)