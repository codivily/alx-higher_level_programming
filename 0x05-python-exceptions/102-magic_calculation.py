#!/usr/bin/python3
<<<<<<< HEAD
def magic_calcuation(a, b):
    pass
=======
def magic_calculation(a, b):
  result = 0
  for i in range(1, 3):
    try:
      if i > a:
        raise Exception('Too far')
      result += (a**b)/i 
    except:
       result = b + a 
       break;
  return result
>>>>>>> 0a4ec99725f6ff473fb8c3f612482b8c82cad974
