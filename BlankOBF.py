import os
os.system("cls" if os.name=="nt" else "clear")
while True:
    try:
        filename=input("\033[93mEnter filename:\033[00m ")
        for i in filename:
            if i in r"""#%&{}\<>*?/$"':@+|=`""":
                print("\033[91mInvalid filename!\033[00m\n")
                invalid=True
                break
            else:
                invalid=False
        if invalid:
            continue
        if filename=="":
            print("\033[91mInvalid filename\033[00m\n")
            continue
        if not "." in filename:
            print("\033[91mInclude file extention also!\033[00m\n")
            continue
        if not filename.endswith('.py'):
            print('\033[91mOnly ".py" files are supported!\033[00m\n')
            continue
        if os.path.basename(filename).lower()==(os.path.basename(__file__)).lower():
            print("\033[91mYou can't do that!\033[00m\n")
            continue
        with open(filename) as e:
            code=e.read()
            if code=="":
                print('\033[91mFile is empty!\033[00m\n')
                continue
            break
    except Exception:
        print('\033[91mFile does not exist!\033[00m\n')
os.system("cls" if os.name=="nt" else "clear")
while True:
    try:
        n=int(input("\033[93mEnter the level of obfuscation (1 - 30):\033[00m "))
        if n<1:
            print("\033[91mLevel cannot be less than 1!\033[00m\n")
        elif n>30:
            print("\033[91mLevel cannot be more than 30!\033[00m\n")
        else:
            break
    except Exception:
        print('\033[91mInvalid level!\033[00m\n')
os.system("cls" if os.name=="nt" else "clear")
import base64, codecs
for j in range(n):
    based=base64.b64encode(bytes(code, 'utf-8'))
    a=[]
    for i in range(0, len(based), int(len(based)/4)):
        a.append(based[i : i + int(len(based)/4)].decode('utf-8'))
    if not (j+1)==n:
        prem="""#Obfuscated using BlankOBF\n#https://github.com/Blank-c/BlankOBF\n"""
    else:
        prem="""#Obfuscated using BlankOBF\n#https://github.com/Blank-c/BlankOBF\n\nimport base64, codecs\n"""
    code=rf"""{prem}magic = '{a[0]}'
love= '{codecs.encode(a[1], "rot13")}'
god='{a[2]}'
destiny = '{codecs.encode(a[3], "rot13")}'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))"""
filename=fr"obfuscated/{filename}"
if not os.path.exists(os.path.dirname(filename)):
    os.makedirs(os.path.dirname(filename))
with open(os.path.dirname(filename)+"/"+os.path.basename(filename), "w") as e:
    e.write(code)
print(f"\033[92mObfuscated and saved as \"{os.path.dirname(filename)}/{os.path.basename(filename)}\"!\033[00m")
if os.name=='nt':
    print('\n(Press any key to exit)\n')
    os.system('pause > NUL')
else:
    input('\n(Press enter to exit)')
    os._exit(1)