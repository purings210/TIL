# 백준 10818번
# 문제 : N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다. 둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
# 출력 : 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

N = int(input())
numbers = list(map(int, input().split()))

# 선택정렬을 사용해보자
# 선택정렬로 하면 시간초과가 난다....
# for i in range(N-1):
#     min_idx = i
#     for j in range(i+1, N):
#         if numbers[min_idx] > numbers[j]:
#             min_idx = j
#     numbers[min_idx], numbers[i] = numbers[i], numbers[min_idx]
#
# print(numbers[0], numbers[N-1])

print(min(numbers), max(numbers))