while 1:
  hundread = int(input('sadat (100): '))
  fifty = int(input('viisikymppiset (50): '))
  twenty = int(input('kaksikymppiset (20): '))
  ten = int(input('kympit (10): '))
  five = int(input('vitoset (5): '))
  two = int(input('kakkoset (2): '))
  one = int(input('eurot (1): '))
  fiftycent = int(input('fiftycent (0,50): '))
  twentycent = int(input('kakskytsenttiset (0,20): '))
  tencent = int(input('kymmensenttiset (0,10): '))
  fivecent = int(input('viisisenttiset (0,05): '))

  summa = hundread*10000+fifty*5000+twenty*2000+ten*1000+five*500+two*200+one*100+fiftycent*50+twentycent*20+tencent*10+fivecent*5
  print('')
  print((summa * 1.0)/100)
  oikeellisuus = raw_input('Menikö oikein? (K/e)')
  if ((oikeellisuus == "K") | (oikeellisuus == "k")):
    break
  print('')
