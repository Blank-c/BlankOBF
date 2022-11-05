import random, string, base64, codecs, argparse, os, sys

from textwrap import wrap
from zlib import compress
from marshal import dumps

from rich import _emoji_replace
from rich import *
from rich import box
from rich.panel import Panel
import os, sys

#Onl to prettify the output
class simplpromt():
    def __init__(self, custom_promt=None, Defaults=True) -> None:
        #clear cmd
        username = os.getlogin()
        self.username =  f'[blue]{username}[/]'
        
        self.control_panel = Panel
        self.instace = Panel
        
        current_path = os.getcwd()
        #format path
        current_path = current_path.replace('\\', '/')
        #remove D:
        self.current_path = current_path[2:]
        
        
        self.osx = sys.platform
        
        self.osxversion = sys.version
        
        self.sizes = os.get_terminal_size()
        
        
        
        if custom_promt:
            self.custom_promt = custom_promt
        else:
            self.old_promt = f"[green]BlankOBF@[/]{self.username}: {self.current_path} $"
            self.custom_promt = f"[green]BlankOBF@[/]{self.username}: {self.current_path} $"
        
        self.newnum = self.sizes[0]-len(self.custom_promt) if len(self.custom_promt)< self.sizes[0]/2 else self.sizes[0]*2
        
        if Defaults:
            print((self.instace(f"{self.custom_promt} \n[gray7]OS: {self.osx} {self.osxversion}[/] $", height=4, width=self.sizes[0]-self.newnum , border_style='grey39', box=box.HORIZONTALS)))

        
    def clear():
        def cls(func):
            def wrapper(*args, **kwargs):
                os.system('cls' if os.name == 'nt' else 'clear')
                func(*args, **kwargs)
            return wrapper
        return  cls
    

    @clear()
    def add_to_main(self, text, cls_previous=False):
        if cls_previous:
            self.custom_promt = self.old_promt
        self.custom_promt += f' {text}'
        
        print((self.instace(self.custom_promt, height=3, width=self.sizes[0]-self.newnum, border_style='grey39', box=box.HORIZONTALS)))
        

    def update(self, text):
        print(f"  {text}")

class BlankOBF:
    def __init__(self, code, outputpath, simplypromt=None):
        self.code = code.encode()
        self.outpath = outputpath
        self.varlen = 6
        self.xorkey = "".join(random.choices(string.digits + string.ascii_letters, k = self.varlen)).encode()
        self.vars = {}
    
        if simplypromt is not None:
            self.simplypromt = simplypromt
            self.simplypromt.update(f"[{self.random_color()}]Running in echo mode\n[/]")
    
        self.marshal()
        self.encrypt1()
        self.encrypt2()
        self.encrypt3()
        self.finalize()

    @staticmethod
    def random_color():
        colors = ["green", "yellow", "magenta", "cyan"]
        return random.choice(colors)
    
    
    def generate(self, name):
        res = self.vars.get(name)
        if res is None:
            while True:
                res = "_" + "".join(random.choices(string.ascii_letters + string.digits, k = self.varlen))
                if res not in self.vars.values():
                    break
            self.vars[name] = res
        if self.simplypromt is not None:
            self.simplypromt.update(f"[{self.random_color()}]Generated variable {res}[/]")
        return res
        
        
        
    def compress(self):
        self.code = compress(self.code)
    
    def xorcrypt(self):
        self.code = list(self.code)
        for index, byte in enumerate(self.code):
            self.code[index] = byte ^ self.xorkey[index % len(self.xorkey)]
        self.code = bytes(self.code)
    
    def marshal(self):
        self.code = dumps(compile(self.code, "<string>", "exec"))
    
    def encrypt1(self):
        code = base64.b64encode(self.code).decode()
        partlen = int(len(code)/4)
        code = wrap(code, partlen)
        var1 = self.generate("a")
        var2 = self.generate("b")
        var3 = self.generate("c")
        var4 = self.generate("d")
        init = [f'{var1}="{codecs.encode(code[0], "rot13")}"', f'{var2}="{code[1]}"', f'{var3}="{code[2][::-1]}"', f'{var4}="{code[3]}"']
        
        
        
        random.shuffle(init)
        init = ";".join(init)
        if self.simplypromt is not None:
            self.simplypromt.update(f"[green b]Encrypt check 1 passed :star2:[/]")
        self.code = f'''
        
        
        
# Obfuscated using https://github.com/Blank-c/BlankOBF

{init};__import__("builtins").exec(__import__("marshal").loads(__import__("base64").b64decode(__import__("codecs").decode({var1}, __import__("base64").b64decode("{base64.b64encode(b'rot13').decode()}").decode())+{var2}+{var3}[::-1]+{var4})))
'''.strip().encode()
    
    def encrypt2(self):
        self.compress()
        self.xorcrypt()
        var1 = self.generate("e")
        var2 = self.generate("f")
        var3 = self.generate("g")
        var4 = self.generate("h")
        var5 = self.generate("i")
        var6 = self.generate("j")
        comments = list(["#____" + "".join(random.choices(string.ascii_letters + string.digits, k = len(self.xorkey))) for _ in range(29)]) + ["#____" + self.xorkey.decode()]

        random.shuffle(comments)
        comments = "# Obfuscated using https://github.com/Blank-c/BlankOBF\n\n" + "\n".join(comments)
        if self.simplypromt is not None:
            self.simplypromt.update(f"[green b]Encrypt check 2 passed :star2:[/]")
        self.code = f'''
{var5} = {self.code}
{var6} = __import__("base64").b64decode({base64.b64encode(comments.encode())}).decode().splitlines()
{var1} = [{var2}[5:].strip() for {var2} in {var6} if {var2}.startswith("#____")]
if len({var1}) < 30 or any([len(x) != {self.varlen} for x in {var1}]):
    __import__("os")._exit(0)
for {var3} in {var1}:
    {var6} = list({var5})
    {var4} = {var3}
    for {var2}, {var3} in enumerate({var5}):
        {var6}[{var2}] = {var3} ^ {var4}.encode()[{var2} % len({var4})]
        try:
            __import__("builtins").exec(__import__("zlib").decompress(bytes({var6})))
            __import__("os")._exit(0)
        except __import__("zlib").error:
            pass
'''.encode()

    def encrypt3(self):
        self.compress()
        data = base64.b64encode(self.code)
        self.code = f'import base64, zlib; exec(compile(zlib.decompress(base64.b64decode({data})), "<string>", "exec"))'.encode()
        if self.simplypromt is not None:
            self.simplypromt.update(f"[green b]Encrypt check 3 passed :star2:[/]")

    def finalize(self):
        if os.path.dirname(self.outpath).strip() != "":
            os.makedirs(os.path.dirname(self.outpath), exist_ok= True)
        with open(self.outpath, "w") as e:
            e.write(self.code.decode())

if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog= sys.argv[0], description= "Obfuscates python program to make it harder to read")
    parser.add_argument("FILE", help= "Path to the file containing the python code")
    parser.add_argument("-o", type= str, help= 'Output file path [Default: "Obfuscated_<FILE>.py"]', dest= "path")
    args = parser.parse_args()
    #check if echo exists

        
        
        
    if not os.path.isfile(sourcefile := args.FILE):
        print(f'No such file: "{args.FILE}"')
        os._exit(1)
    elif not sourcefile.endswith((".py", ".pyw")):
        print('The file does not have a valid python script extention!')
        os._exit(1)


        
    
    if args.path is None:
        args.path = "Obfuscated_" + os.path.basename(sourcefile)
    
    with open(sourcefile) as sourcefile:
        code = sourcefile.read()
    


    promt = simplpromt()
    obf = BlankOBF(code, args.path, simplypromt=promt)
    promt.update(f"[green]Obfuscation completed :white_heavy_check_mark:[/], [blue]Output file: {args.path} :file_folder:[/]")


        
        