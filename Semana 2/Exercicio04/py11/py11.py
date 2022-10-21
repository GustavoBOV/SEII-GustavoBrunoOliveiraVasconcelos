f = open('/home/guuga/code/SEII-GustavoBrunoOliveiraVasconcelos/Semana 2/Exercicio04/py11/teste.txt', 'r') #r is for read

print('')
print(f.name)
print(f.mode)

f.close()

print('')
with open('/home/guuga/code/SEII-GustavoBrunoOliveiraVasconcelos/Semana 2/Exercicio04/py11/teste.txt', 'r') as f:
    f_contents = f.read()
    print(f_contents)
    
print('')
with open('/home/guuga/code/SEII-GustavoBrunoOliveiraVasconcelos/Semana 2/Exercicio04/py11/teste.txt', 'r') as f:
    f_contents = f.readlines()
    print(f_contents)

print('')
with open('/home/guuga/code/SEII-GustavoBrunoOliveiraVasconcelos/Semana 2/Exercicio04/py11/teste.txt', 'r') as f:
    f_contents = f.readline()
    print(f_contents, end='') 
    f_contents = f.readline()
    print(f_contents, end='')

print('')
with open('/home/guuga/code/SEII-GustavoBrunoOliveiraVasconcelos/Semana 2/Exercicio04/py11/teste.txt', 'r') as f:
    for line in f:
        print(line, end='')

print('\n')
with open('/home/guuga/code/SEII-GustavoBrunoOliveiraVasconcelos/Semana 2/Exercicio04/py11/teste.txt', 'r') as f:
    f_contents = f.read(100) 
    print(f_contents, end='')
    f_contents = f.read(100) 
    print(f_contents, end='')

print('\n')
with open('/home/guuga/code/SEII-GustavoBrunoOliveiraVasconcelos/Semana 2/Exercicio04/py11/teste.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    while len(f_contents) > 0:
        print(f_contents, end='*')
        f_contents = f.read(size_to_read)
    
print('\n')
with open('/home/guuga/code/SEII-GustavoBrunoOliveiraVasconcelos/Semana 2/Exercicio04/py11/teste.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')
    f_contents = f.read(size_to_read)
    print(f_contents)
    print(f.tell())

print('\n')
with open('/home/guuga/code/SEII-GustavoBrunoOliveiraVasconcelos/Semana 2/Exercicio04/py11/teste.txt', 'r') as f:
    size_to_read = 10
    f_contents = f.read(size_to_read)
    print(f_contents, end='')
    f.seek(0) #recomeça do 0
    f_contents = f.read(size_to_read)
    print(f_contents)

print('\n')
with open('/home/guuga/code/SEII-GustavoBrunoOliveiraVasconcelos/Semana 2/Exercicio04/py11/teste.txt', 'w') as f: #w is for write
    f.write('test')
    f.seek(0)
    f.write('r')

print('\n')
with open('/home/guuga/code/SEII-GustavoBrunoOliveiraVasconcelos/Semana 2/Exercicio04/py11/teste.txt', 'r') as rf:
    with open('/home/guuga/code/SEII-GustavoBrunoOliveiraVasconcelos/Semana 2/Exercicio04/py11/teste.txt', 'w') as wf:
        for line in rf:
            wf.write(line)
