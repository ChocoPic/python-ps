'''DP 문제
* 테이블의정의
    dp[alp_max][j]: 알고력 alp_max 이상, 코딩력 j 달성에 필요한 시간
    dp[i][cop_max]: 알고력 j, 코딩력 cop_max 이상 달성에 필요한 시간
    다른 dp[i][j]들: 그대로. 알고력 i, 코딩력 j 달성에 필요한 시간
    => 테이블의 크기 alp_max x cop_max (최대 150x150)
* 점화식
    dp[min(alp_max, i+alp_rwd)][min(cop_max, j+cop_rwd)]
    = min(dp[i][j]+cost, 
        dp[min(alp_max, i+alp_rwd)][min(cop_max, j+cop_rwd)]) 
* 초기값(+채우는순서)
    dp[alp][cop] = 0
'''

def solution(alp, cop, problems):
    # 0 <= alp_req, cop_req <= 150
    ALP = 151
    COP = 151
    
    # 모든 문제를 풀기 위해 필요한 최대 알고력과 코딩력을 찾습니다.
    max_alp = max(p[0] for p in problems)   #문제 중 가장 높은 alp_req
    max_cop = max(p[1] for p in problems)   #문제 중 가장 높은 cop_req
    
    # 초기 알고력, 코딩력은 최대 알고력, 코딩력을 넘으면 안됨
    alp = min(alp, max_alp)
    cop = min(cop, max_cop)
    
    # dp 배열을 큰 값으로 초기화합니다.
    dp = [[float('inf')]*(COP) for _ in range(ALP)]
    
    # 시작 지점(현재 알고력과 코딩력 & 소요시간)
    dp[alp][cop] = 0 
        
    # dp 배열을 채웁니다.
    for a in range(alp, ALP):
        for c in range(cop, COP):    
            # 선택지1) 알고리즘 공부 or 이전 계산값 유지 로 세팅
            if a+1 <= max_alp:
                dp[a+1][c] = min(dp[a][c] + 1, dp[a+1][c])
                
            # 선택지2) 코딩 공부 or 이전 계산값 유지 가 더 적게 걸리면 교체
            if c+1 <= max_cop:
                dp[a][c+1] = min(dp[a][c] + 1, dp[a][c+1])
                
            # 선택지3) 문제풀이 or 이전 계산값 유지 가 더 적게 걸리면 교체
            for alp_req, cop_req, alp_rwd, cop_rwd, cost in problems:
                if a >= alp_req and c >= cop_req:   #해당 문제를 풀 수 있으면
                    new_a = min(a+alp_rwd, max_alp) #최대 알고력을 넘어가면 최대치로 보정
                    new_c = min(c+cop_rwd, max_cop) #최대 코딩력을 넘어가면 최대치로 보정
                    dp[new_a][new_c] = min(dp[a][c]+cost, dp[new_a][new_c])
    
    return dp[max_alp][max_cop]