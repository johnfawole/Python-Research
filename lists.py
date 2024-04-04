investors = ['John', 'Victor', 'Michael']

data = ['Joshua', '19', True]

emptylist = []

print ("Joshua" in emptylist)

print(investors[0])
print(investors[-2])

print(investors.index('Michael'))

print(investors[0:2])
print(investors[1:])
print(investors[-3:-1])

# fetches the length
print(len(data))

# shows how to insert
investors.insert(4, 'Joshua')
print(investors)

investors += ['Joseph']
print(investors)

investors.append('Abigael')
print(investors)

investors.extend(['Grace', 'Tope'])
print(investors)


