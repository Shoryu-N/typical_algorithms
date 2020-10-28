from heapq import heappush, heappop
INF = 10 ** 20

v, e, r = map(int, input().split())

edges_list = [[] for _ in range(v)]
dist_list = [INF for _ in range(v)]

for _ in range(e):
    s, t, dist = map(int, input().split())
    edges_list[s].append((t, dist))

dis_ver_list = []
heappush(dis_ver_list, (0, r))
dist_list[r] = 0
while dis_ver_list:
    dist, node = heappop(dis_ver_list)
    for to, cost in edges_list[node]:
        if dist_list[to] > cost + dist:
            dist_list[to] = cost + dist
            heappush(dis_ver_list, (cost+dist, to))

for dist in dist_list:
    if dist == INF:
        print("INF")
    else:
        print(dist)
        