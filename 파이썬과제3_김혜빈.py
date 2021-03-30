#0329세션 74쪽
class animation():
    def __init__(character, name, age, gender):
        character.name = name
        character.age = age
        character.gender = gender
    def __str__(character):
        return '{}는 {}세이고, {}입니다.'.format(character.name, character.age, character.gender)

shinchan = animation('짱구', 5, '남자')
doraemon = animation('도라에몽', 14, '남자')
conan = animation('코난', 8, '남자')
shochola = animation('쇼콜라', 15, '여자')
amu = animation('아무', 12, '여자')
kayoung = animation('가영', 16, '여자')

Character = [shinchan, doraemon, conan, shochola, amu, kayoung]

for x in Character:
    print(x)