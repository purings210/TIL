# 백준 2438번
# 문제 : 첫째 줄에는 별 1개, 둘째 줄에는 별 2개, N번째 줄에는 별 N개를 찍는 문제 
# 입력 : 첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
# 출력 : 첫째 줄부터 N번째 줄까지 차례대로 별을 출력한다.

# 들어온 숫자를 list의 요소로 추가하면서 int로 형변환을 시켜준다.
N = list(map(int, input().split()))

# range함수를 통해 반복횟수를 정한다.(곱셈을 활용하여 *을 print하기위해 1부터 N[0]+1까지로 range의 범위를 정한다.)
for i in range(1, N[0]+1):
    print('*' * i) 