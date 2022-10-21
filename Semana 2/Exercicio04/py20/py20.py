try:
    f = open('/home/guuga/code/SEII-GustavoBrunoOliveiraVasconcelos/Semana 2/Exercicio04/py20/teste.txt')
except Exception:
    print('Sorry. This file does not exist')

print('')
try:
    f = open('/home/guuga/code/SEII-GustavoBrunoOliveiraVasconcelos/Semana 2/Exercicio04/py20/teste.txt')
    var = bad_var
except FileNotFoundError:
    print('Sorry. This file does not exist')
except Exception:
    print('Sorry. Something went wrong')

print('')
try:
    f = open('/home/guuga/code/SEII-GustavoBrunoOliveiraVasconcelos/Semana 2/Exercicio04/py20/teste.txt')
    var = bad_var
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)

print('')
try:
    f = open('/home/guuga/code/SEII-GustavoBrunoOliveiraVasconcelos/Semana 2/Exercicio04/py20/teste.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()

print('')
try:
    f = open('/home/guuga/code/SEII-GustavoBrunoOliveiraVasconcelos/Semana 2/Exercicio04/py20/teste.txt')
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print(e)
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")

print('')
try:
    f = open('/home/guuga/code/SEII-GustavoBrunoOliveiraVasconcelos/Semana 2/Exercicio04/py20/corrompido.txt')
    if f.name == '/home/guuga/code/SEII-GustavoBrunoOliveiraVasconcelos/Semana 2/Exercicio04/py20/corrompido.txt':
        raise Exception
except FileNotFoundError as e:
    print(e)
except Exception as e:
    print('Error!')
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")
