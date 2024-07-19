from module import run_game

INTRO = '''РАССЧИТАЙ И ПОБЕДИ!
Загрузка...

Твоя цель — за 5 ходов набрать такое количество очков урона противнику,
которое попадет в диапазон +– 10 от значения здоровья противника.

Значение здоровья противника генерируется случайным образом
в диапазоне от 80 до 120 очков.

В твоём распоряжении три вида атак:
lite — урон от 2 до 5 очков;
mid — урон от 15 до 25 очков;
hard — урон от 30 до 40 очков.
ВПЕРЁД К ПОБЕДЕ!!!
HE-HE-HE-HA
'''

def main():
    print(INTRO)
    replay = True
    while replay:
        replay = run_game()

if __name__ == '__main__':
    main()
