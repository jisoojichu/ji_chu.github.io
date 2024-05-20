def solution(nums):
    # 폰켓몬 종류 개수 계산
    count = len(set(nums))
    
    # N/2 마리를 선택하는 경우의 수 계산
    n = len(nums)
    ways = n // 2
    
    # 폰켓몬 종류별 최대 개수 계산
    max_freq = min(count, ways)
    
    return max_freq