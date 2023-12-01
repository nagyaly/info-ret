xs = '''
    And only herald to the gaudy spring
    Within thine own bud buriest thy content
    And tender churl makst waste in niggarding
    Pity the world or else this glutton be
    To eat the worlds due by the grave and thee
'''

xs = xs.split(" ")
print(len(xs))
#remove duplicates
xs = list(set(xs))
print(xs)
print(len(xs))