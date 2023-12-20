'''
출입구에서 산봉우리로 가는 최단 경로를 구하는 문제
최단 경로 = 거쳐가는 간선 중 최댓값
다익스트라 : 매 순간마다 남아있는 가장 가까운 정점을 찾으면 거리를 확정할 수 있다.
    기존 다익스트라 d[next] = min(d[next], d[cur]+weight)
    이 문제 d[next] = min(d[next], max(d[cur], weight))
    여러개의 시작점을 가지는 다익스트라를 수행하자
산봉우리는 한번만 방문해야 한다. 
    1)산봉우리는 우선순위큐에 넣지 X => 다른 산봉우리 가는길 막기
    2)간선을 단방향으로
    탐색을 중단하면 안되나? 산봉우리가 여러개면 안찾고 탐색 끝나버릴 수 있음
'''

import heapq

MAX = float('inf')
d = [MAX] * 50005   #d[i] : i번 지점까지의 intensity
adj = [[] for _ in range(50005)]    # 간선(비용, 번호)
issummit = [False] * 50005  #issummit[i] : i번지점이 summit인지 여부

def solution(n, paths, gates, summits):
    for summit in summits:
        issummit[summit] = True
    for u, v, w in paths:
        adj[u].append((w,v))
        adj[v].append((w,u))
    heap = []
    for g in gates:
        d[g]=0
        heapq.heappush(heap, (d[g], g))
    
    while heap:
        cur = heapq.heappop(heap)   #cur = [현재까지비용, 현재 보는 정점의 인덱스]
        if d[cur[1]] != cur[0]: continue
        for next in adj[cur[1]]:    #next = [간선 비용, 간선이 연결하는 인덱스]
            if d[next[1]] <= max(d[cur[1]], next[0]): continue
            d[next[1]] = max(d[cur[1]], next[0])
            if not issummit[next[1]]:   #다른 산봉우리 못가게 next[1]이 산봉우리면 heapq에 안넣는다
                heapq.heappush(heap, (d[next[1]], next[1]))
    
    answer = summits[0]
    for summit in summits:
        if d[summit] < d[answer]:
            answer = summit
        elif d[summit] == d[answer] and summit < answer:
            answer = summit
            
    return [answer, d[answer]]
    
                