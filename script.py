from googlesearch import *
print('''
 _       _____   _   _   _   __ ______  __   __  _   _ 
| |     |_   _| | \ | | | | / / | ___ \ \ \ / / | \ | |
| |       | |   |  \| | | |/ /  | |_/ /  \ V /  |  \| |
| |       | |   | . ` | |    \  |    /   /   \  | . ` |
| |____  _| |_  | |\  | | |\  \ | |\ \  / /^\ \ | |\  |
\_____/  \___/  \_| \_/ \_| \_/ \_| \_| \/   \/ \_| \_/

========================================================                                                       
==  • CODED BY : ABDULRAHMAN ABOULDAHAB               ==
==  • AKA      : RXN / ROOTXNOVA                      ==
==  • FACEBOOK : WelcomeAbdulrahman.Official          ==
==  • GITHUB   : rootxnova                            ==
==  • TWITTER  : 3OOOBAAD                             ==
==  • ASKFM    : xXxROOTxXx                           ==
========================================================
''')
tar = input(' ♦ Enter Keyword Here : ')
for url in search(tar,stop=500000000000000000000000000000000000000000000000000000):
    with open('result.txt','a+')as f:
        f.write(url+"\n")
