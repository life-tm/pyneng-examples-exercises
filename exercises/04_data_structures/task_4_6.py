# -*- coding: utf-8 -*-
'''
Задание 4.6

Обработать строку ospf_route и вывести информацию на стандартный поток вывода в виде:
Protocol:              OSPF
Prefix:                10.0.24.0/24
AD/Metric:             110/41
Next-Hop:              10.0.13.3
Last update:           3d18h
Outbound Interface:    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

'''

ospf_route = 'O        10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

ospf_route = ospf_route.split()
ospf_route.insert(0,"Protocol")
ospf_route.insert(1,"OSPF")
ospf_route.pop(2)
ospf_route.insert(2,"AD/Metric")
ospf_route.insert(3,"Next-Hop")
ospf_route.insert(4,"Last update")
ospf_route.insert(5,"Outbound Interface")
ospf_route.pop(-4)
ospf_route.insert(3,"Prefix")