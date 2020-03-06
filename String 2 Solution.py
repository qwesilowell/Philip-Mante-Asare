def verbing(s):
  if len(s) < 3:
    return s
  else:
    if s[-3:] == "ing":
      answer = s + "ly"
    else:
      answer = s + "ing"
  return answer
        


def not_bad(s):
  if s.find("bad") > s.find("not"):
    start = s.find('not')
    end = s.find("bad") + 3
    return s.replace(s[start:end], "good")
  return s



def front_back(a, b):
  if len(a)%2 == 0:
    a_front = a[:len(a)/2]
    a_back =  a[len(a)/2:]
  else:
    a_front = a[:(len(a)/2)+ 1]
    a_back =  a[len(a)/2 + 1:]
    
  if len(b)%2 == 0:
    b_front = b[:len(b)/2]
    b_back =  b[len(b)/2:]
  else:
    b_front = b[:(len(b)/2) + 1]
    b_back =  b[len(b)/2 + 1:]
  

  return a_front + b_front + a_back + b_back



def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print ('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))




def main():
  print ('verbing'
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do'))

  print
  print ('not_bad'
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not"))

  print
  print ('front_back'
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut'))

main()
