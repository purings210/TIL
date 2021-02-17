# 백준 8958번
# 문제 : "OOXXOXXOOO"와 같은 OX퀴즈의 결과가 있다. O는 문제를 맞은 것이고, X는 문제를 틀린 것이다. 문제를 맞은 경우 그 문제의 점수는 그 문제까지 연속된 O의 개수가 된다. 예를 들어, 10번 문제의 점수는 3이 된다.
# "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
# OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.

# 입력 : 첫째 줄에 테스트 케이스의 개수가 주어진다. 각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다. 문자열은 O와 X만으로 이루어져 있다.
# 출력 : 각 테스트 케이스마다 점수를 출력한다.

T = int(input())

for test_case in range(1, T+1):
    # 입력되는 퀴즈결과
    sentence = input()

    # 점수 총합
    total = 0
    # 더할 점수
    key = 1
    # 연속 확인을 위한 변수
    link = False
    # 입력된 퀴즈결과를 하나씩 확인한다.
    for word in sentence:
        # 만약 퀴즈결과가 X라면
        if word == 'X':
            # 연속 확인은 False로 초기화
            link = False
            # 더할 점수도 1로 초기화
            key = 1

        # link == False일때
        if not link:
            # 들어온 퀴즈결과가 O이면
            if word == 'O':
                # 총합에 key를 더하고
                total += key
                # 다음번에 또 O가 들어오면 지금 key값보다 1큰값을 더해줘야하므로 key에 1을 더하고
                key += 1
                # 연속임을 나타내기위해 link를 True로 바꾼다.
                link = True
        # link == True일때, 즉 이전 퀴즈결과가 O였고, 이번에도 O라면
        else:
            # 현재 기준으로 key만큼 total에 합산해주고
            total += key
            # key를 또 1더해준다.
            key += 1

    print(total)