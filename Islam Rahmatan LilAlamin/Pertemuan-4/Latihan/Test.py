from colorama import Fore, Back, Style, init
init()
print(Fore.RED + 'Teks Merah')
print(Fore.GREEN + 'Teks Hijau')
print(Fore.BLUE + Back.YELLOW + 'Teks Biru, Bg Kuning')
print(Style.RESET_ALL + 'Kembali Normal')

C = Fore.CYAN
G = Fore.GREEN
R = Fore.RED
W = Fore.WHITE
Y = Fore.YELLOW
B = Fore.BLUE
M = Fore.MAGENTA


print(f"   {R}███{G}███{Y}███{B}███{M}███{C}███{W}   ")