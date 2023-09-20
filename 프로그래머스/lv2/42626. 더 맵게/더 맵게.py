#scoville지수에서 가장 작은 수와 그 다음 작은 수를 주어진 공식을 이용해 값을 구하고 그 값을 다시 배열에 넣어 새로운 배열을 이용한다. 새로운 scoville지수를 만들때마다 count 해주고, 만약 새로 만든 스코빌지수가 k이상이 된다면 count 값을 반환한다.
import heapq

def solution(scoville, K):
    # 초기 음식 리스트를 힙으로 변환해주는 heapify함수
    heapq.heapify(scoville)
    
    count = 0
    
    while scoville[0] < K:
        if len(scoville) < 2:
            # 모든 음식을 섞어도 K 이상으로 만들 수 없는 경우 -1 반환
            return -1
        
        # 가장 맵지 않은 음식-> heapq의 heappop을 이용하면 알아서 가장 작은 노드를 빼준다.
        first_scoville = heapq.heappop(scoville)
        #두 번째로 맵지 않은 음식
        second_scoville = heapq.heappop(scoville)
        # 두 음식의 스코빌을 섞어 만든 스코빌 지수
        mixed_scoville = first_scoville + (second_scoville * 2)
        
        # 섞은 음식을 다시 힙에 추가해주고, 추가했으면 카운트 업해준다. 그리고 다시 반복
        heapq.heappush(scoville, mixed_scoville)
        count += 1
    
    return count
