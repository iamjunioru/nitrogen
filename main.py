import ctypes
import string
import os
import time

USE_WEBHOOK = True

time.sleep(3)
os.system('cls' if os.name == 'nt' else 'clear')


try:  
    from discord_webhook import DiscordWebhook  
except ImportError:

    input(
        f"Module discord_webhook not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install discord_webhook'\nYou can ignore this error if you aren't going to use a webhook.\npressione enter para continuar.")
    USE_WEBHOOK = False
try: 
    import requests  
except ImportError:  

    input(
        f"Module requests not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install requests'\npressione enter para sair")
    exit() 
try: 
    import numpy  
except ImportError: 

    input(
        f"Module numpy not installed, to install run '{'py -3' if os.name == 'nt' else 'python3.8'} -m pip install numpy'\npressione enter para sair")
    exit() 


url = "https://github.com"
try:
    response = requests.get(url) 
    print("-internet check\n-internet check\n-internet check")
    time.sleep(.4)
except requests.exceptions.ConnectionError:

    input("você não tá conectado a internet. cheque sua conexão e tente novamente\npressione enter para sair")
    exit()  

class NitroGen: 
    def __init__(self):
        self.fileName = "nitrocodes.txt" 

    def main(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        if os.name == "nt": 
            print("")
            ctypes.windll.kernel32.SetConsoleTitleW(
                "gerador e checker de nitro por @iamjunioru")
        else:
            print(f'\33]0;gerador e checker de nitro por @iamjunioru\a',
                  end='', flush=True) 

        print("""** funciona, só precisa de sorte. :)
                                                        """)
        time.sleep(2) 
        
        self.slowType("feito por dream // @iamjunioru", .02)
        time.sleep(1)
        
        self.slowType(
            "\n- insira quantos codigos quer gerar e verificar: ", .02, newLine=False)

        try:
            num = int(input(''))
        except ValueError:
            input("[o que você especificou não é um número.]\npressione enter para sair")
            exit() 

        if USE_WEBHOOK:
            
            self.slowType(
                "- insira a url do webhook: ", .02, newLine=False)
            url = input('') 
            
            webhook = url if url != "" else None
            
            if webhook is not None:
                DiscordWebhook(
                        url=url,
                        content=f""" ❗ **um código nitro será gerado aqui.**
quando um codigo valido for encontrado, ele vai aparecer abaixo para ser resgatado. :)"""
                    ).execute()

        

        valid = []
        invalid = 0 
        chars = []
        chars[:0] = string.ascii_letters + string.digits

        
        c = numpy.random.choice(chars, size=[num, 23])
        for s in c:  
            try:
                code = ''.join(x for x in s)
                url = f"https://discord.gift/{code}" 

                result = self.quickChecker(url, webhook) 

                if result: 
                   
                    valid.append(url)
                else:  
                    invalid += 1 
            except KeyboardInterrupt:
                
                print("\ninterrompido pelo usuario")
                break 

            except Exception as e: 
                print(f" Error | {url} ") 

            if os.name == "nt":  
                ctypes.windll.kernel32.SetConsoleTitleW(
                    f"@iamjunioru - {len(valid)} valido | {invalid} invalido - by dream ") 
                print("")
            else:  
                
                print(
                    f'\33]0;@iamjunioru - {len(valid)} valido | {invalid}  invalido - by dream\a', end='', flush=True)

        print(f"""
resultados:
validos: {len(valid)}
invalidos: {invalid}
valid codes: {', '.join(valid)}""")

        
        input("\n! pressione Enter 5 vezes para fechar o programa.")
        [input(i) for i in range(4, 0, -1)] 


    def slowType(self, text: str, speed: float, newLine=True):
        for i in text:
            
            print(i, end="", flush=True)
            time.sleep(speed)
        if newLine:
            print()

    def quickChecker(self, nitro:str, notify=None):
        
        url = f"https://discordapp.com/api/v9/entitlements/gift-codes/{nitro}?with_application=false&with_subscription_plan=true"
        response = requests.get(url)

        if response.status_code == 200:
            print(f" valido | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            with open("nitrocodes.txt", "w") as file:
            
                file.write(nitro)

            if notify is not None:
                DiscordWebhook( 
                    url=url,
                    content=f"nitro valido! @everyone \n{nitro}"
                ).execute()

            return True

       
        else:
           
            print(f" invalido | {nitro} ", flush=True,
                  end="" if os.name == 'nt' else "\n")
            return False


if __name__ == '__main__':
    Gen = NitroGen()
    Gen.main()