from typing import List

def inc_list(l: List[int]) -> List[int]: 
    return list(map(lambda n: n+1, l))

def main() -> None:
    res = inc_list([1,2,3])
    print(res)

main()
