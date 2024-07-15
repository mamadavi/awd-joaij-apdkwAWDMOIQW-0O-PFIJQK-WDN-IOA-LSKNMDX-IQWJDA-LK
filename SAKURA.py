import subprocess
import os
from colorama import Fore, Style, init


try:
  os.system("sudo apt install nmap nuclei assetfinder subfinder finalrecon lolcat")
except:
  pass


os.system("printf '\033c'")

init(autoreset=True)  

print(Fore.LIGHTMAGENTA_EX + "   /$$$$$$   /$$$$$$  /$$   /$$ /$$   /$$ /$$$$$$$   /$$$$$$  ")
print(Fore.LIGHTMAGENTA_EX + "  /$$__  $$ /$$__  $$| $$  /$$/| $$  | $$| $$__  $$ /$$__  $$ ")
print(Fore.LIGHTMAGENTA_EX + " | $$  \__/| $$  \ $$| $$ /$$/ | $$  | $$| $$  \ $$| $$  \ $$ ")
print(Fore.LIGHTMAGENTA_EX + " |  $$$$$$ | $$$$$$$$| $$$$$/  | $$  | $$| $$$$$$$/| $$$$$$$$ ")
print(Fore.LIGHTMAGENTA_EX + "  \____  $$| $$__  $$| $$  $$  | $$  | $$| $$__  $$| $$__  $$ ")
print(Fore.LIGHTMAGENTA_EX + "  /$$  \ $$| $$  | $$| $$\  $$ | $$  | $$| $$  \ $$| $$  | $$ ")
print(Fore.LIGHTMAGENTA_EX + " |  $$$$$$/| $$  | $$| $$ \  $$|/ $$$$$$/| $$  | $$| $$  | $$ ")
print(Fore.LIGHTMAGENTA_EX + "  \______/ |/  |/|/  \/ \______/     |/  |/  |/  |/    |/     ")
print(Fore.LIGHTMAGENTA_EX + "                                [ Maden by Akiyama and Wigil ]")
print(Style.RESET_ALL)

while True:
  # Главное меню
  print(Fore.CYAN + "                         Main Menu:")
  print(Fore.CYAN + "1. Pentesting  2. Doxing  3. DDoS  4. Exit to Terminal")
  print(Style.RESET_ALL)

  choice = input("Make a choice: ")

  if choice == '1':
    while True:
      print(Fore.CYAN + "Pentesting Menu:")
      print(Fore.CYAN + "1. Start  2. Back to Menu ")
      print(Style.RESET_ALL)

      pentest_choice = input("Make a choice: ")

      if pentest_choice == '1':
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

        break

      elif pentest_choice == '2':
        print(Fore.CYAN + "Back to Menu")
        print(Style.RESET_ALL)
        break

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
        break

      elif doxing_choice == '2':
        print(Fore.CYAN + "Back to Menu")
        print(Style.RESET_ALL)
        break

      else:
        print(Fore.RED + "Invalid Choice")
        print(Style.RESET_ALL)

  elif choice == '3':
    def show_attack_options():
        print("Choose the method of attack:")
        print("1. Karma-DDoS")
        print("2. Hammer DDoS")
        print("3. Botnet")

        attack_choice = input("Make a choice: ")

        if attack_choice == "1":
            print("Karma-DDoS Attack")
            
        # Запускаем Karma-DDoS атаку
        # ... (ваш код для Karma-DDoS)
        # Дополнительные действия
        # ...
        
        elif attack_choice == "2":
            print("Hammer-DDoS Attack")
            
        # Запускаем Hammer DDoS атаку
        # ... (ваш код для Hammer DDoS)
        # Дополнительные действия
        # ...
        
        elif attack_choice == "3":
            print("Botnet Attack")
            
        # Запускаем Botnet атаку
        # ... (ваш код для Botnet)
        # Дополнительные действия
        # ...
        
        else:
            print("Invalid Choice")

    while True:
        print("Menu:")
        print("1. Choose the method of attack")
        print("2. Back To Menu")

        choice = input("Make a choice: ")

        if choice == "1":
            show_attack_options()
        elif choice == "2":
            break
        else:
            print("Invalid Choice")

  elif choice == '4':
    print(Fore.CYAN + "Exit")
    print(Style.RESET_ALL)
    break

  else:
    print(Fore.RED + "Invalid Choice")
    print(Style.RESET_ALL)

print(Fore.CYAN + "Bye!")
print(Style.RESET_ALL)
print(Fore.CYAN + "Bye!")
print(Style.RESET_ALL)
