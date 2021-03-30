#0329세션 72쪽
Likelion = {"이화여대 멋사 대표님": "현숙", "멋사 창립자" : "두희", "파이썬 세션 튜터" : "세은", "야옹" : "마루"}
for key, value in Likelion.items():
    print("다음은 누구에 대한 설명일까요?")
    print(key)
    print("1. 현숙 2. 세은 3. 두희 4. 마루")
    ans = input()
    if ans == value:
        print("정답입니다!")
    else:
        print("오답입니다!") 