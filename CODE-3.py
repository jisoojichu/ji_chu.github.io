def solution(arr):
    result = []
    prev_num = arr[0]
    result.append(prev_num)
    
    for num in arr[1:]:
        if num!= prev_num:
            result.append(num)
            prev_num = num
            
    return result

이 코드는 배열 내의 연속된 중복 값을 제거하는 함수를 구현하는 것입니다.

solution() 함수에서는 입력으로 받은 배열 arr을 순회하며 중복되는 값들을 제거합니다.
첫 번째 값은 무조건 리스트에 추가되며, 이후 값들부터는 이전 값(prev_num)과 비교하여 다르면 리스트에 추가하고 이전 값으로 설정합니다.
이렇게 하면 결과적으로 중복되는 값들이 모두 제거된 배열이 만들어집니다.
예를 들어, solution([1, 2, 3, 2, 4]) 함수가 호출되면 반환값은 [1, 2, 3, 4]가 됩니다. 왜냐하면 [2, 3, 2, 4] 중 2와 3만이 이전 값과 다르기 때문입니다. 이 알고리즘은 매우 효율적이며 시간 복잡도는 O(n)입니다.
