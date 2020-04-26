enter=input('lotfan yeki az kalamat e zir ra ENTEKHAB konid va enter bezanid: ')
print('----------------------------------------------------------------')
print('A - Ab- Ali - Hami - Mehra - Parham - khodkar - Mohammad')
enter=input('----------------------------------------------------------------')
enter=input('1. tedad e horof e kalame ra da 5 ZARB konid- ENTER PLS')
print('----------------------------------------------------------------')
enter=input('2. sepas adad e 3 raa be aan EZAFEH konid- ENTER PLS')
print('----------------------------------------------------------------')
enter=input('3. adad e hasel raa dar 2 ZARB konid- ENTER PLS')
print('----------------------------------------------------------------')
enter=input('4. yek adad e delkhah az 1-9 be aan EZAFEH konid- ENTER PLS')
print('----------------------------------------------------------------')
adad=int(input('Lotfan adad e nahaei ra vared konid: '))
adad=adad-6
kalameh=(adad//10)
kalameh=int(kalameh)
ezafeh=int(adad%10)
print('shoma adad e',+ezafeh,'raa dar aakhar ezafeh karde eid.')
if kalameh == 1:
    print('Kalameye entekhabi shoma A boode ast.')
elif kalameh == 2:
    print('Kalameye entekhabi shoma Ab boode ast.')
elif kalameh == 3:
        print('Kalameye entekhabi shoma Ali boode ast.')
elif 4 == kalameh:
        print('Kalameye entekhabi shoma Hami boode ast.')
elif 5 == kalameh:
        print('Kalameye entekhabi shoma Mehra boode ast.')
elif 6 == kalameh:
        print('Kalameye entekhabi shoma Parham boode ast.')
elif 7 == kalameh:
        print('Kalameye entekhabi shoma Khodkar boode ast.')
elif 8 == kalameh:
        print('Kalameye entekhabi shoma Mohammad boode ast.')
else:
        print('Kalameye entekhabi shoma az list e dade shode naboodeh!!')
'''
Created on ۲۱ فروردین ۱۳۹۹

@author: Mohammad
'''
