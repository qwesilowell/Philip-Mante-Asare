def donuts(count):
    if count < 9:
        return('number of donuts: {}' .format (count))
    else:
        return('number of donuts: many')
    
    print(donuts(5))
    
    

def both_ends(s):
    if len (s) < 2:
        print('')
    else:
        print(s[0:2] + s[-2:])

both_ends('Mallrk')




def fix_start(s):
    char = s[0]
    length = lens(s)
    s = s.replace(char, '*')
    s = char + s[1:]

    return s





def mix_up(a,b):
    new_a = b[:2]
    new_b = a[2:]

    return new_a + ' ' + new_b


def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = ' X '
    print   ('%s expected: %s' % (prefix, repr(got), repr(expected)))



def main():
    print(
    test(donuts(4), 'Number of donuts: 4'),
    test(donuts(9), 'Number of donuts: 9'),
    test(donuts(10), 'Number of donuts: many'),
    test(donuts(99), 'Number of donuts: many'))
    

    print ('both_ends')
    test(both_ends('spring'), 'spng')
    test(both_ends('Hello'), 'Helo')
    test(both_ends('a'), '')
    test(both_ends('xyz'), 'xyyz')


    print('fix_start')
    test(fix_start('babble'), 'ba**le')
    test(fix_start('aardvark'), 'a*rdv*rk')
    test(fix_start('google'), 'goo*le')
    test(fix_start('donut'), 'donut')


    print ('mix_up')
    test(mix_up('mix', 'pod'), 'pox mid')
    test(mix_up('dog', 'dinner'), 'dig donner')
    test(mix_up('gnash', 'sport'), 'spash gnort')
    test(mix_up('pezzy', 'firm'), 'fizzy perm')
    


if __name__ == '__main__':
        main()





