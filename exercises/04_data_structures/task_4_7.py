# -*- coding: utf-8 -*-
'''
Задание 4.7

Преобразовать MAC-адрес mac в двоичную строку такого вида:
'101010101010101010111011101110111100110011001100'

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

mac = 'AAAA:BBBB:CCCC'

mac = mac.replace(':', '') 
mac = int(mac, 16)
mac = '{:0b}'.format(mac)
mac
или так:
mac = 'AAAA:BBBB:CCCC'
mac = mac.replace(':', '') 
mac = int(mac, 16)
bin(hex)[2:]