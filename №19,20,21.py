'''
P1 -  позиция, при попадании в которую, игрок побеждает своим первым ходом
(хотя бы одним, он же не дебил  - сливать)
P2 -  позиция, при попадании в которую, игроку потребуется ровно два хода, чтоб победить
(но у него всегда будет хотя бы один ход, ведущий к победе => ведущий в 'V1')
V1 - позиция, из которой любой ход игрока будет вести к его проигрышу =>
(все ходы будут вести в 'P1')
V2 - позиция, из которой любой ход игрока будет вести к его проигрышу, но за два хода =>
(все ходы будут вести в 'P2')
'''

'''
ПРИМЕР:

1) Петя - первый игрок, Ваня - второй игрок.
2) Есть две кучи, победа наступает в момент, когда сумма камней в двух кучах >= 47
3) в первой куче - 10 камней, во второй - S камней
4) 1 <= S <= 36
5) за один ход можно:
либо - (+1, +2),
либо - (+2, +1),
либо - (None, *2),
либо - (*2, None)

# №19 #
    Известно, что Ваня выиграл своим первым ходом после неудачного первого хода Пети. Укажите минимальное значение S,
когда такая ситуация возможна.

# №20 #
    Найдите максимальное S, при котором у Пети есть выигрышная стратегия, причём одновременно выполняются два условия:
— Петя не может выиграть за один ход;
— Петя может выиграть своим вторым ходом независимо от того, как будет ходить Ваня.

# №21 #
    Найдите минимальное значение S, при котором одновременно выполняются два условия:
— у Вани есть выигрышная стратегия, позволяющая ему выиграть первым или вторым ходом при любой игре Пети;
— у Вани нет стратегии, которая позволит ему гарантированно выиграть первым ходом.
'''

# https://docs.google.com/spreadsheets/d/1ygwQlcqpPnWLApP3NFZbvRQfQdatGFHBce-Qs8iVcrc/edit#gid=0 - пример эксель


from functools import lru_cache

def moves(begin):
    a, b = begin
    # print((a + 1, b + 2), (a + 2, b + 1), (a*2, b), (a, b*2))
    return (a + 1, b + 2), (a + 2, b + 1), (a*2, b), (a, b*2)

@lru_cache(None)
def game(start):
    if (sum(start)>=47):
        return 'END'
    if any(game(x)=='END' for x in moves(start)):
        return 'P1'
    if all((game(x)=='P1') for x in moves(start)):  # поставив вместо all - any, мы выбираем для Пети, самый лоховской ход (для №19)
        return 'V1'
    if any((game(x)=='V1') for x in moves(start)):
        return 'P2'
    if all((game(x)=='P2' or game(x)=='P1') for x in moves(start)):
        return 'V2'


for i in range(1, 38):
    s = (10, i)
    print(s, game(s))

# Советы:
# 1) всегда проверять moves(), отдельно от game() на открытых данных (чтоб не закрабить из-за невнивательности)

