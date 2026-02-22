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

print(f"{C}                  {M}Alam{W}@{M}archlinux{W}")
print(f"{C}       /\\        {W}-----------------")
print(f"{C}      /  \\       {B}OS{W}: AlamOS (Arch Rolling Release)")
print(f"{C}     /    \\      {B}Kernel{W}: 6.9.420-LTS-edition")
print(f"{C}    /      \\     {B}Uptime{W}: 67 min ")
print(f"{C}   /   ,,   \\    {B}Packages{W}: 67 (pacman)")
print(f"{C}  /   |  |   \\   {B}Shell{W}: kitty 0.44.12")
print(f"{C} /_-''    ''-_\\  {B}Disk(/){W}: 78GB / 8TB ({G}0.95%{W})")
print(f"{C}                 {B}CPU{W}: Intel 9 Ultra 495 ")
print(f"{C}                 {B}GPU{W}: RTX 6090 Ti (Eaaa)")
print(f"{C}                 {B}VRam{W}: 64GB GDDR8 (Aduhaii)")
print(f"{C}                 {B}Memory{W}: 1.9GB / 192GB ({G}1%{W})")
print("")

print(f"   {R}███{G}███{Y}███{B}███{M}███{C}███{W}   ")