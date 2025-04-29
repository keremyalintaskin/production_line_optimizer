def min_total_time(completion_time, transition_cost):
    n = len(completion_time)  
    m = len(completion_time[0])  

    dp = [[float('inf')] * m for _ in range(n)]

    for j in range(m):
        dp[0][j] = completion_time[0][j]

    for i in range(1, n):
        for j in range(m):
            for k in range(m):
                cost = dp[i-1][k] + transition_cost[k][j] + completion_time[i][j]
                if cost < dp[i][j]:
                    dp[i][j] = cost

    return min(dp[n-1])

print("Minimum toplam süre:", min_total_time(
    completion_time=[
        [5, 6, 8],
        [4, 7, 3],
        [6, 5, 4],
        [3, 6, 7]
    ],
    transition_cost=[
        [0, 2, 4],
        [2, 0, 1],
        [3, 2, 0]
    ]
))
