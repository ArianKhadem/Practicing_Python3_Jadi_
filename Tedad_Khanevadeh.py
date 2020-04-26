'''
Created on ۲۰ فروردین ۱۳۹۹

@author: Mohammad
'''
Baradar=input('Lotfan tedad e baradaran khod ra ba adad e 3 va enter ra bezanid : ')
print('Hasel raa dar 5 zarb va adad e 20 ra be aan ezafe konid')
print('adad e be dast aamade raa dar 2 zarb konid')
print('hasel raa be tedad e khahar ha ezafe konid')
kol=input('Adad e hasele ra vared konid: ')
kol=int(kol)
adad=(kol+5)-75
baradar=adad//10
print('tedad e baradaran e shoma: ',+ baradar)
khahar=adad%10
print('tedad e khaharan e shoma :',+khahar)
khanevadeh=(adad//10)+(adad%10)+3
print('tedad aazaye khanevadeye shoma: ', + khanevadeh)