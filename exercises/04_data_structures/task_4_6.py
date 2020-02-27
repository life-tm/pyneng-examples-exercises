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
ospf_route=ospf_route.split()
o2=ospf_route[2].strip('[]')
o4=ospf_route[4].strip(',')
o5=ospf_route[5].strip(',') 
ospf_route.insert(2,o2)
ospf_route.pop(0)
ospf_route.pop(2)
ospf_route.pop(2)
ospf_route.pop(2)
ospf_route.pop(2)
ospf_route.insert(2,o4)
ospf_route.insert(3,o5)
ospf_route=' '.join(ospf_route)
ospf_route = ospf_route.split()
ospf_route.insert(0,"OSPF")

print ("Protocol:              " + ospf_route[0]  
  + "\nPrefix:                " + ospf_route[1]  
  + "\nAD/Metric:             " + ospf_route[2]  
  + "\nNext-Hop:              " + ospf_route[3]  
  + "\nLast update:           " + ospf_route[4]  
  + "\nOutbound Interface:    " + ospf_route[5]  
)   