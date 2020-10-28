INF = 10 ** 20

v, e = map(int, input().split())
dist_lst = [[INF] * v for _ in range(v)]
negative_cycle_flag = False
for _ in range(e):
  s, t, dist = map(int, input().split())
  dist_lst[s][t] = dist

for i in range(v):
  dist_lst[i][i] = 0

for k in range(v):
  for i in range(v):
    for j in range(v):
      if dist_lst[i][k] != INF and dist_lst[k][j] != INF:
        if dist_lst[i][j] > dist_lst[i][k] + dist_lst[k][j]:
          dist_lst[i][j] = dist_lst[i][k] + dist_lst[k][j]

#negative cycleあるかどうか(重みの合計値が負の閉路)
for v in range(v):
  if dist_lst[v][v] < 0:
    negative_cycle_flag = True