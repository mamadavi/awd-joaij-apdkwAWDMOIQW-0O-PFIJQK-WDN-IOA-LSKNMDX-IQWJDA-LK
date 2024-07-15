import subprocess
import os
from colorama import Fore, Style, init

# Установка зависимостей (только если их нет)
try:
  os.system("sudo apt install nmap nuclei assetfinder subfinder finalrecon lolcat")
  os.system("pip3 install colorama")
except:
  pass

# Очистка консоли
os.system("printf '\033c'")

# Логотип
init(autoreset=True)  # Автоматический сброс цвета после каждой строки

print(Fore.LIGHTMAGENTA_EX + "   /$$$$$$   /$$$$$$  /$$   /$$ /$$   /$$ /$$$$$$$   /$$$$$$  ")
print(Fore.LIGHTMAGENTA_EX + "  /$$__  $$ /$$__  $$| $$  /$$/| $$  | $$| $$__  $$ /$$__  $$ ")
print(Fore.LIGHTMAGENTA_EX + " | $$  \__/| $$  \ $$| $$ /$$/ | $$  | $$| $$  \ $$| $$  \ $$ ")
print(Fore.LIGHTMAGENTA_EX + " |  $$$$$$ | $$$$$$$$| $$$$$/  | $$  | $$| $$$$$$$/| $$$$$$$$ ")
print(Fore.LIGHTMAGENTA_EX + "  \____  $$| $$__  $$| $$  $$  | $$  | $$| $$__  $$| $$__  $$ ")
print(Fore.LIGHTMAGENTA_EX + "  /$$  \ $$| $$  | $$| $$\  $$ | $$  | $$| $$  \ $$| $$  | $$ ")
print(Fore.LIGHTMAGENTA_EX + " |  $$$$$$/| $$  | $$| $$ \  $$|/ $$$$$$/| $$  | $$| $$  | $$ ")
print(Fore.LIGHTMAGENTA_EX + "  \______/ |/  |/|/  \/ \______/     |/  |/  |/  |/    |/     ")
print(Style.RESET_ALL)

while True:
  # Главное меню
  print(Fore.CYAN + "                         Main Menu:")
  print(Fore.CYAN + "1. Pentesting  2. Doxing  3. DDoS  4. Exit to Terminal")
  print(Style.RESET_ALL)

  choice = input("Make a choice: ")

  if choice == '1':
    # Меню Пентестинга
    while True:
      print(Fore.CYAN + "Pentesting Menu:")
      print(Fore.CYAN + "1. Start  2. Back to Menu ")
      print(Style.RESET_ALL)

      pentest_choice = input("Make a choice: ")

      if pentest_choice == '1':
        # Запускаем пентестинг
        print(Fore.CYAN + "Maden by WIGIL and Akiyama")
        print(Style.RESET_ALL)

        target = input("Enter url (site.com): ")
        nmap_result = input("Enter name and location of nmap scan result (result.xml): ")

        os.system(f"nmap -sV -Pn -sC --script vulners -n -O -oX {nmap_result} {target}")
        os.system(f"nuclei -target {target}")
        os.system(f"assetfinder {target}")
        os.system(f"subfinder -d {target}")

        threads = input("Nuber of port scan threads: ")
        dir_threads = input("Number of directory enum threads: ")

        os.system(f"finalrecon -pt {threads} -dt {dir_threads} --full https://{target}")
        os.system(f"searchsploit --nmap {nmap_result}")

        break # Выходим из меню пентестинга

      elif pentest_choice == '2':
        print(Fore.CYAN + "Back to Menu")
        print(Style.RESET_ALL)
        break # Возвращаемся в главное меню

      else:
        print(Fore.RED + "Invalid Choice.")
        print(Style.RESET_ALL)

  elif choice == '2':
    # Меню Доксинга
    while True:
      print(Fore.CYAN + "Doxing Menu:")
      print(Fore.CYAN + "1. Start  2. Back to Menu")
      print(Style.RESET_ALL)

      doxing_choice = input("Make a choice: ")

      if doxing_choice == '1':
        # Код для запуска доксинга
        # ...
        # Дополнительные действия
        # ...
        break # Выходим из меню доксинга

      elif doxing_choice == '2':
        print(Fore.CYAN + "Back to Menu")
        print(Style.RESET_ALL)
        break # Возвращаемся в главное меню

      else:
        print(Fore.RED + "Invalid Choice")
        print(Style.RESET_ALL)

  elif choice == '3':
    # Меню DDoS
    while True:
      print(Fore.CYAN + "DDoS Menu:")
      print(Fore.CYAN + "1. Start  2. Back to Menu")
      print(Style.RESET_ALL)

      ddos_choice = input("Make a choice: ")

      if ddos_choice == '1':
        # Код для запуска DDoS
        # ...
        # Дополнительные действия
        # ...
        break # Выходим из меню DDoS

      elif ddos_choice == '2':
        print(Fore.CYAN + "Back to Menu")
        print(Style.RESET_ALL)
        break # Возвращаемся в главное меню

      else:
        print(Fore.RED + "Invalid Choice")
        print(Style.RESET_ALL)

  elif choice == '4':
    print(Fore.CYAN + "Exit")
    print(Style.RESET_ALL)
    break # Выходим из программы

  else:
    print(Fore.RED + "Invalid Choice")
    print(Style.RESET_ALL)

print(Fore.CYAN + "Bye!")
print(Style.RESET_ALL)
