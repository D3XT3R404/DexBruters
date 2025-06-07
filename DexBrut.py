import pyzipper
import os
from tqdm import tqdm
from colorama import Fore, Style, init

init(autoreset=True)

BANNER = f"""
{Fore.LIGHTMAGENTA_EX}

██▄   ▄███▄      ▄  ███   █▄▄▄▄  ▄     ▄▄▄▄▀ ▄███▄   
█  █  █▀   ▀ ▀▄   █ █  █  █  ▄▀   █ ▀▀▀ █    █▀   ▀  
█   █ ██▄▄     █ ▀  █ ▀ ▄ █▀▀▌ █   █    █    ██▄▄    
█  █  █▄   ▄▀ ▄ █   █  ▄▀ █  █ █   █   █     █▄   ▄▀ 
███▀  ▀███▀  █   ▀▄ ███     █  █▄ ▄█  ▀      ▀███▀   
              ▀            ▀    ▀▀▀                  
         ZIP Bruter By David
"""

def brute_force_zip(zip_path, wordlist_path):
    try:
        with open(wordlist_path, 'r', encoding='utf-8', errors='ignore') as f:
            passwords = [line.strip() for line in f if line.strip()]

        print(f"{Fore.YELLOW}[+] Total Passwords: {len(passwords)}{Style.RESET_ALL}\n")

        with pyzipper.AESZipFile(zip_path) as zf:
            for pwd in passwords:
                print(f"{Fore.LIGHTBLACK_EX}[-] Mencoba: {pwd}{Style.RESET_ALL}")
                try:
                    zf.pwd = pwd.encode('utf-8')
                    zf.extractall()
                    print(f"\n{Fore.GREEN}[✓] Password ditemukan: {pwd}{Style.RESET_ALL}")
                    return
                except:
                    continue

        print(f"\n{Fore.RED}[-] Gagal menemukan password.{Style.RESET_ALL}")

    except Exception as e:
        print(f"{Fore.RED}[!] Terjadi error: {e}{Style.RESET_ALL}")

def main():
    print(BANNER)
    zip_path = input(f"{Fore.BLUE}ZIP File Path: {Style.RESET_ALL}")
    wordlist_path = input(f"{Fore.BLUE}Wordlist Path : {Style.RESET_ALL}")
    brute_force_zip(zip_path.strip(), wordlist_path.strip())

if __name__ == '__main__':
    main()
