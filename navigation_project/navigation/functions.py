# 길찾기 알고리즘을 기록해둔 공간입니다.

import sys
import heapq

input = sys.stdin.readline


def route_search(start_point, end_point, w):
    data = {}

    # data 딕셔너리 초기화
    def init(start_node, init_data):
        while init_data:
            next_node, distance = heapq.heappop(init_data)
            for _ in range(2):
                if start_node not in data:
                    data[start_node] = {next_node: distance}
                else:
                    data[start_node][next_node] = distance
                start_node, next_node = next_node, start_node  # 한번 초기화 할 때 양방향으로 초기화
        return start_node

    # 강의실, 복도, 화장실 노드
    # init 할때 양방향으로 초기화 되는 것을 고려하여 작성! 강의실이 같은 장소의 노드를 공유하더라도 공유하는 강의실만큼 노드 만들기 + 공유하는 강의실들도 노드에 거리 0 으로 초기화하기
    # 노드 분류 설정(개수증가하면 분류코드_1, _2...)
    # 엘리베이터 10,20,30... 비상계단 11 비상계단 12 직선계단 13
    ##1층
    n100 = init('n100', [['n13', 0]])
    n101_1 = init('n101_1', [['n101_2', 4.2], ['n12', 6.4]])
    n101_2 = init('n101_2', [['n195', 3.4]])
    n102 = init('n102', [['n103', 3.4], ['n195', 2.5]])
    n103 = init('n103', [['n104', 3.4]])
    n104 = init('n104', [['n105', 3.4]])
    n105 = init('n105', [['n106', 3.4]])
    n107 = init('n107', [['n195', 2.2], ['n108', 7.5]])
    n108 = init('n108', [['n109', 7.5]])
    n109 = init('n109', [['n110', 7.5], ['n1999', 4]])
    n11_2 = init('n14', [['n110', 3], ['n111', 4.5]])
    n198 = init('n198', [['n10', 1.3], ['n111', 4.7], ['n112', 2], ['n113', 2], ['n199', 4.7]])
    n112 = init('n112', [['n111', 4.2]])
    n113 = init('n113', [['n199', 4.2]])
    n197 = init('n197', [['n199', 14.5], ['n1999', 3.8], ['n11_1', 8]])
    n196 = init('n196', [['n12', 1.5], ['n13', 3.5], ['n11_1', 1.9]])

    ##2층
    init('n200', [['n299', 3.9], ['n212', 13]])
    init('n299', [['n298', 3]])
    init('n212', [['n211', 7.5], ['n20', 7]])
    init('n298', [['n20', 3.9], ['n299', 3.6]])
    init('n299', [['n20', 4.1], ['n21_2', 4.5]])
    init('n20', [['n211', 3.8]])
    init('n211', [['n210', 7.5]])
    init('n210', [['n209', 7.5]])
    init('n209', [['n208', 7.5], ['n2999', 4]])
    init('n208', [['n207', 7.5], ['n21_1', 0]])
    init('n207', [['n294', 2.5]])
    init('n294', [['n202', 2], ['n201', 7.5]])
    init('n202', [['n203', 4.3]])
    init('n203', [['n204', 3.5]])
    init('n204', [['n205', 3.5]])
    init('n205', [['n206', 3.5]])
    init('n201', [['n22', 4.5]])
    init('n22', [['n295', 13]])
    init('n295', [['n2999', 4.3], ['n296', 5]])
    init('n296', [['n23', 4], ['n21_2', 5]])

    ##3층
    n301 = init('n301', [['n302', 5], ['n398', 9.5]])
    n302 = init('n302', [['n303', 2], ['n3999', 3.5]])
    n303 = init('n303', [['n304', 3]])
    n304 = init('n304', [['n305', 2]])
    n305 = init('n305', [['n306', 4]])
    n306 = init('n306', [['n307', 4]])
    n307 = init('n307', [['n308', 3], ['n311', 3], ['n313', 7]])
    n308 = init('n308', [['n309', 3], ['n311', 0]])
    n309 = init('n309', [['n310', 3]])
    n311 = init('n311', [['n309', 3], ['n308', 0]])
    n312 = init('n312', [['n313', 3]])
    n313 = init('n313', [['n312', 8]])
    n314 = init('n314', [['n315', 6.5]])
    n315 = init('n315', [['n3999', 3.5], ['n316', 9]])
    n316 = init('n316', [['n317', 4.5]])
    n317 = init('n317', [['n397', 3], ['n318', 6], ['n320', 6]])
    n318 = init('n318', [['n320', 0], ['n319', 6]])
    n319 = init('n319', [['n309', 3]])
    n320 = init('n320', [['n318', 0], ['n319', 6]])
    n397 = init('n398', [['n398', 4]])
    n398 = init('n398', [['n399', 3]])
    n30 = init('n30', [['n397', 0]])
    n31_1 = init('n31_1', [['n306', 0]])
    n31_2 = init('n31_2', [['n316', 0]])
    n32 = init('n32', [['n306', 0]])
    n33 = init('n33', [['n399', 0]])

    # 이동수단 가중치 수식
    w_0 = w[0]  # 엘베 가중치
    w_1 = w[1]  # 비상계단 가중치
    w_2 = w[2]  # 소용돌이계단 가중치
    w_3 = w[3]  # 직선계단 가중치

    # 층 이동 노드 초기화 if 문 이용해서 층 이동에 따라 계단, 엘레베이터 정보 연결 시켜주기
    def connect_1_2():
        init('n10', [['n20', w_0]])
        init('n11_1', [['n21_1', w_1]])
        init('n11_2', [['n21_2', w_1]])
        init('n12', [['n22', w_2]])
        init('n13', [['n23', w_3]])

    def connect_1_3():
        init('n10', [['n30', w_0]])
        init('n11_1', [['n31_1', w_1]])
        init('n11_2', [['n31_2', w_1]])
        init('n12', [['n32', w_2]])
        init('n13', [['n33', w_3]])

    def connect_2_3():
        init('n30', [['n20', w_0]])
        init('n31_1', [['n21_1', w_1]])
        init('n31_2', [['n21_2', w_1]])
        init('n32', [['n22', w_2]])
        init('n33', [['n23', w_3]])

    if (start_point[1] == '1' and end_point[1] == '3') or (start_point[1] == '3' and end_point[1] == '1'):
        connect_1_3()
    elif (start_point[1] == '1' and end_point[1] == '2') or (start_point[1] == '2' and end_point[1] == '1'):
        connect_1_2()
    elif (start_point[1] == '2' and end_point[1] == '3') or (start_point[1] == '3' and end_point[1] == '2'):
        connect_2_3()

    def dijkstra(graph, start):
        distances = {node: float('inf') for node in graph}  # start로 부터의 거리 값을 저장하기 위함
        distances[start] = 0  # 시작 값은 0이어야 함
        queue = []
        heapq.heappush(queue, [distances[start], start])  # 시작 노드부터 탐색 시작 하기 위함.

        while queue:  # queue에 남아 있는 노드가 없으면 끝
            current_distance, current_destination = heapq.heappop(queue)  # 탐색 할 노드, 거리를 가져옴.

            if distances[current_destination] < current_distance:  # 기존에 있는 거리보다 길다면, 볼 필요도 없음
                continue

            for new_destination, new_distance in graph[current_destination].items():
                distance = current_distance + new_distance  # 해당 노드를 거쳐 갈 때 거리
                if distance < distances[new_destination]:  # 알고 있는 거리 보다 작으면 갱신
                    distances[new_destination] = distance

                    moving_result[new_destination] = current_destination  # 더 작은 거리로 갱신 될 때 바뀐 경로를 저장하기 위한 부모노드 변경

                    heapq.heappush(queue, [distance, new_destination])  # 다음 인접 거리를 계산 하기 위해 큐에 삽입

        return distances

    start, end = start_point, end_point  # 1층 출입구에서 3층화장실까지  # 이거 start_point, end_point 파라미터로 받는다
    moving_result = {}  # start 에서 end 까지의 최적경로 연결 상태
    route = []
    c = end
    print(dijkstra(data, start)[end])

    while c != start:
        route.append(c)
        c = moving_result[c]
    route.append(c)
    route.reverse()

    print(start + "에서" + end + "까지의 경로 =", end="")
    print(route)

    return route




def w_updater(test):
    user_pick = [0, 0, 0, 0]
    after = [0, 0, 0, 0]
    w = [0, 0, 0, 0]

    # 현재 데이터상 사용자 선호도를 user_pick에 업데아트 하는 과정
    for object in test:
        route = object.route
        if route == 'elevator':
            user_pick[0] += 1
        elif route == 'emergency_stair':
            user_pick[1] += 1
        elif route == 'whirlpool_stair':
            user_pick[2] += 1
        else:
            user_pick[3] += 1 # 직선형 계단
    print(user_pick)
    
    # 이번에는 가중치 값을 변경하면서 결과 관찰.
    # 사용자가 가장 선호하는 특정 이동수단이 선택된 횟수와 계산상 결과에서 특정 이동수던이 선택된 횟수가 같을 때까지 계속 프로구램을 돌려 가중치를 업데이트한다.
    # 가중치는 기본적으로 1 단위로 올린다. 여기서 가중치를 1단위로 올린다는 것은 결국 간선비용의 증가를 의미하며, 이는 해당 경로가 선택되는 경우를 최대한 억제하는 결과를 가져온다.

    while True:
        if user_pick[user_pick.index(max(user_pick))] <= after[user_pick.index(max(user_pick))]:
            print(w)
            return w
        else:
            for i in range(len(w)):
                if i == user_pick.index(max(user_pick)):
                    continue
                else:
                    w[i] += 1

        after = [0, 0, 0, 0]

        for object in test:
            after_route = route_search(object.start_point, object.end_point, w)
            for i in range(len(after_route) - 1):
                if (len(after_route[i]) == 3) and (len(after_route[i + 1]) == 3):
                    if after_route[i][2] == '0':  # 엘리베이터
                        after[0] += 1
                    elif after_route[i][2] == '2':  # 송용돌이 계단
                        after[2] += 1
                    elif after_route[i][3] == '2':  # 직선형 계단
                        after[3] += 1
                elif (len(after_route[i]) == 5 and '_' in after_route[i]) and (len(after_route[i+1]) == 5 and '_' in after_route[i+1]):
                    after[1] += 1
                    
                    