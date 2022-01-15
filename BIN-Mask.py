# Двоичная Маска
'''
Идея: любое количество подмножеств в множестве - это 2**n

Так происходит по двум причинам:
1) Это сумма всех 'C из n по k'
2) Любой элемент можно либо взять (True), либо не взять (False) >> подмножество можно представить, как двоичную маску
(в этом случае учитываются и пустые подмножества)

parentSet - {2, 3, 10}
childSets:
{} ========== [0, 0, 0]
{10} ======== [0, 0, 1]
{3} ========= [0, 1, 0]
{3, 10} ===== [0, 1, 1]
{2} ========= [1, 0, 0]
{2, 10} ===== [1, 0, 1]
{2, 3} ====== [1, 1, 0]
{2, 3, 10} == [1, 1, 1]
'''

def bin_mask(SET):
    dlin = len(SET)
    sets = []
    for i in range(2**dlin):
        # Создание двоичной (бинарной) маски
        var = bin(i)
        mask = var[2:]
        if len(mask) < dlin:
            for j in range(dlin - len(mask)):
                mask = '0' + mask
        mask = list(map(int, mask))

        # Соотнесение маски и множества
        no_mask = []
        for ind in range(dlin):
            if mask[ind] == 1:
                no_mask.append(SET[ind])
        sets.append(no_mask)
    return sets

print(bin_mask([1,2,3]))