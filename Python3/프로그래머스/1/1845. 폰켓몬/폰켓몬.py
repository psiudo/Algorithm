def solution(nums):
    # 전체 폰켓몬 수
    total_pokemon = len(nums)
    # 선택할 수 있는 최대 폰켓몬 수
    max_selectable = total_pokemon // 2
    # 폰켓몬 종류의 수
    unique_pokemon_types = len(set(nums))
    
    # 최대 선택할 수 있는 종류의 수는 max_selectable과 unique_pokemon_types 중 작은 값
    return min(max_selectable, unique_pokemon_types)
