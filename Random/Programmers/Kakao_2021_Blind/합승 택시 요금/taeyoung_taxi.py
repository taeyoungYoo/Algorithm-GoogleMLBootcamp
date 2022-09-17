# Floyd warshall approach
def solution(n, s, a, b, fares):
    answer = INF = 987654321
    adj = [[INF] * (n+1) for _ in range(n+1)]
    for i in range(n+1):
        adj[i][i] = 0
    for x, y, z in fares:
        adj[x][y] = z
        adj[y][x] = z
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if adj[i][k] + adj[k][j] < adj[i][j]:
                    adj[i][j] = adj[i][k] + adj[k][j]
    for i in range(1, n+1):
        answer = min(answer, adj[s][i] + adj[i][a] + adj[i][b])
    return answer