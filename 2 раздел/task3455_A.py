'''
 _        __                            _   _                              _
(_)_ __  / _| ___  _ __ _ __ ___   __ _| |_(_) ___ ___     _ __ ___   __ _(_)
| | '_ \| |_ / _ \| '__| '_ ` _ \ / _` | __| |/ __/ __|   | '_ ` _ \ / _` | |
| | | | |  _| (_) | |  | | | | | | (_| | |_| | (__\__ \   | | | | | | (_| | |
|_|_| |_|_|  \___/|_|  |_| |_| |_|\__,_|\__|_|\___|___/___|_| |_| |_|\__,_|_|
 _   _                             ____              |_____|
| |_| |__   ___ _ __ ___   ___    |___ \
| __| '_ \ / _ \ '_ ` _ \ / _ \     __) |
| |_| | | |  __/ | | | | |  __/    / __/
 \__|_| |_|\___|_| |_| |_|\___|___|_____|
 _            _    _____ _  _|_____|____        _
| |_ __ _ ___| | _|___ /| || || ___| ___|      / \     _ __  _   _
| __/ _` / __| |/ / |_ \| || ||___ \___ \     / _ \   | '_ \| | | |
| || (_| \__ \   < ___) |__   _|__) |__) |   / ___ \ _| |_) | |_| |
 \__\__,_|___/_|\_\____/   |_||____/____/___/_/   \_(_) .__/ \__, |
                                       |_____|        |_|    |___/

'''


import math

a = int(input())
b = int(input())
c = math.sqrt(a**2 + b**2)

print(f"{c:.10f}")
