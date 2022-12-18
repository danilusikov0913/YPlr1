# Используя замыкания функций, объявите внутреннюю функцию, которая принимает в
# качестве аргумента список целых чисел и удаляет из него все четные или нечетные
# значения в зависимости от значения параметра type . Если type равен «even», то
# удаляются четные значения, иначе – нечетные. По умолчанию type должно принимать
# значение «even». Вызовите внутреннюю функцию замыкания и отобразите на экране
# результат ее работы.
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':
    def delchis(list1):
        def delchetnechet(type='even'):
            if type == 'even':
                for x in range(len(list1)):
                    if x % 2 == 0:
                        list1.pop(list1.index(x))
                        print(list1)
            else:
                for x in range(len(list1)):
                    if x % 2 != 0:
                        list1.pop(list1.index(x))
                        print(list1)

        return delchetnechet


    f = delchis(list1=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14])
    f()
