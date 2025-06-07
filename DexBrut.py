import os
import sys

try:
    import pyzipper
except ImportError:
    print("[!] Module 'pyzipper' belum terinstall bosh. Install dengan: pip install pyzipper")
    print("[!] ika gagal coba : pip install pyzipper --break-system-packages")
    sys.exit(1)

try:
    import rarfile
except ImportError:
    print("[!] Module 'rarfile' belum terinstall kawan. Install dengan: pip install rarfile")
    print("[!] ika gagal coba : pip install rarfile --break-system-packages")
    sys.exit(1)

try:
    import py7zr
except ImportError:
    print("[!] Module 'py7zr' belum terinstall anjay. Install dengan: pip install py7zr")
    print("[!] ika gagal coba : pip install py7zr --break-system-packages")
    sys.exit(1)

try:
    from colorama import Fore, Style, init
except ImportError:
    print("[!] Module 'colorama' belum terinstall tuan. Install dengan: pip install colorama")
    print("[!] jika gagal coba : pip install colorama --break-system-packages")
    sys.exit(1)

init(autoreset=True)

BANNER = f"""
{Fore.RED}
██▄   ▄███▄      ▄  ███   █▄▄▄▄  ▄     ▄▄▄▄▀ ▄███▄   
█  █  █▀   ▀ ▀▄   █ █  █  █  ▄▀   █ ▀▀▀ █    █▀   ▀  
█   █ ██▄▄     █ ▀  █ ▀ ▄ █▀▀▌ █   █    █    ██▄▄    
█  █  █▄   ▄▀ ▄ █   █  ▄▀ █  █ █   █   █     █▄   ▄▀ 
███▀  ▀███▀  █   ▀▄ ███     █  █▄ ▄█  ▀      ▀███▀   
              ▀            ▀    ▀▀▀                  
                   By David(D3XT3R)
{Fore.GREEN}Simple & Multi Bruteforce(ZIP, RAR, 7z)
{Fore.GREEN}[!] Wordlist Harap Membuat Sendiri [!] 
"""

def try_zip(file_path, password):
    try:
        with pyzipper.AESZipFile(file_path) as zf:
            zf.pwd = password.encode('utf-8')
            zf.testzip()
        return True
    except RuntimeError:
        return False
    except Exception:
        return False

def try_rar(file_path, password):
    try:
        with rarfile.RarFile(file_path) as rf:
            rf.extractall(pwd=password)
        return True
    except rarfile.BadRarFile:
        return False
    except rarfile.RarWrongPassword:
        return False
    except Exception:
        return False

def try_7z(file_path, password):
    try:
        with py7zr.SevenZipFile(file_path, mode='r', password=password) as sz:
            sz.extractall()
        return True
    except py7zr.exceptions.PasswordRequired:
        return False
    except py7zr.exceptions.Bad7zFile:
        return False
    except Exception:
        return False

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(BANNER)
	##Script By D3XT3R404

    print(f"{Fore.MAGENTA}Masukkan path/nama filenya (zip/rar/7z): ", end="")
    file_path = input().strip()
    if not os.path.isfile(file_path):
        print(f"{Fore.RED}[!] File tidak ditemukan!")
        sys.exit(1) ##D3XT3RH3R3

    print(f"{Fore.MAGENTA}Masukkan path wordlist: ", end="")
    wordlist_path = input().strip()
    if not os.path.isfile(wordlist_path):
        print(f"{Fore.RED}[!] Wordlist tidak ditemukan!")
        sys.exit(1)

    ext = file_path.split('.')[-1].lower()
    try_function = None

    if ext == 'zip':
        try_function = try_zip
    elif ext == 'rar':
        try_function = try_rar
    elif ext == '7z':
        try_function = try_7z
    else:
        print(f"{Fore.RED}[!] Tipe file tidak didukung! Gunakan zip, rar, atau 7z.")
        sys.exit(1) ##davidhere

    print(f"{Fore.BLUE}[+] Memulai bruteforce pada: {file_path} ...")
    with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
        for line in f:
            password = line.strip()
            if not password:
                continue
            print(f"{Fore.YELLOW}[-] Mencoba: {password}")
            if try_function(file_path, password):
                print(f"\n{Fore.GREEN}[✓] Password ditemukan: {password}")
                return
    print(f"\n{Fore.RED}[!] Password tidak ditemukan di wordlist.")

if __name__ == '__main__':
    main()
