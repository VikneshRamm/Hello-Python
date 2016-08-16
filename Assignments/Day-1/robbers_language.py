def translate(str):
    new_str = ''
    vowels = ['a','e','i','o','u']
    str = str.lower()
    for c in str:
        if c not in vowels and c.isalpha():
            new_str += c + 'o' + c
        else:
            new_str += c
    return new_str

print 'The translated language is %s' %translate(raw_input('Enter the string\n'))
        
