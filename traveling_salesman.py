INF = 10 ** 20

n = int(input())
dist = [[INF] * n for _ in range(n)]

#dp[s][v] 今まで訪れた頂点の集合がs 今いる頂点がvのときの最小コスト
#(1 << n)で初期化すると、n=5のとき2**5=32になる。つまり、indexは0~31(二進数で00000~11111)を差す。
dp = [[INF for _ in range(n)] for _ in range(1 << n)]

e = []
for i in range(n):
    x,y,z = map(int, input().split())
    e.append((x,y,z))
#下記実装でi==jのときは0が入る。 
for i in range(len(e)):
    for j in range(len(e)):
        dist1 = abs(e[i][0] - e[j][0]) + abs(e[i][1] - e[j][1]) + max(0, e[j][2] - e[i][2]) 
        
        dist[i][j] = dist1

#初期状態は0から一個移動したところからはじめる.
#dp[s]にすでに全頂点が入って、最後にvに0が入った時に終わりとしたいので。
for i in range(n):
    if i == 0: continue
    #dp[i<<i][i]: i桁目に1が立っている。そしてそのときiにいる。
    dp[1<<i][i] = dist[0][i]
    
for i in range(1 << n):
    for j in range(n):
        # ~ はnot。bitが立っていない時という意味合いになる。
        if ~i>>j&1: continue
        # jからkに向かう
        for k in range(n):
            #kがiに含まれていたら遷移してはいけない。
            if i>>k&1: continue
            #i|1<<kはiのk桁目に1を足すという意味になる。
            dp[i|1<<k][k] = min(dp[i|1<<k][k], dp[i][j]+dist[j][k])
#n = 5なら2**n-1のbitは11111。全部立っている状態で、最後に0に向かう時のコストが答えになる。
print(dp[2**n-1][0])
