def vowel_check(c):
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    return c in vowels
c = raw_input('Enter a character\n')
print 'Is the character a vowel? ==> %s' %(vowel_check(c))
    
