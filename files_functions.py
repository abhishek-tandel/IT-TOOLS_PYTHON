file1 = open('myfile.txt', 'w')
file1.write('hello\n')
file1.writelines('''This is my 1st PP program hello byee''')
file1.close()
file1 = open('myfile.txt', 'r+')
print 'output of Read function is'
print file1.read()

file1.seek(0)

print 'output of Readline function is '
print file1.readline()

file1.seek(0)

print 'output of Read(9)function is '
print file1.read(9)

file1.seek(0)
print 'output of Readline(9)function is '
print file1.readline(9)

file1.seek(0)
print 'output of Readlines function is '
print file1.readlines()
file1.close()
