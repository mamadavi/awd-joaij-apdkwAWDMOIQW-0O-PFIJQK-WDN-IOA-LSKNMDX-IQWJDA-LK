
print(" █████╗ ██╗  ██╗██╗██╗   ██╗ █████╗ ███╗   ███╗ █████╗     ███████╗ ██████╗ ███████╗████████╗")
print("██╔══██╗██║ ██╔╝██║╚██╗ ██╔╝██╔══██╗████╗ ████║██╔══██╗    ██╔════╝██╔═══██╗██╔════╝╚══██╔══╝")
print("███████║█████╔╝ ██║ ╚████╔╝ ███████║██╔████╔██║███████║    ███████╗██║   ██║█████╗     ██║   ")
print("██╔══██║██╔═██╗ ██║  ╚██╔╝  ██╔══██║██║╚██╔╝██║██╔══██║    ╚════██║██║   ██║██╔══╝     ██║   ")
print("██║  ██║██║  ██╗██║   ██║   ██║  ██║██║ ╚═╝ ██║██║  ██║    ███████║╚██████╔╝██║        ██║   ")
print("╚═╝  ╚═╝╚═╝  ╚═╝╚═╝   ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝╚═╝  ╚═╝    ╚══════╝ ╚═════╝ ╚═╝        ╚═╝   ")
print("                                                                           Maden With WIGIL  ")
                                                                                             

while True:
  print("Main Menu:")
  print("1. Pentesting  2. Doxing  3. DDoS  4. Exit to Terminal")

  choice = input("Make a choice: ")

  if choice == '1':
    while True:
      print("Pentesting Menu:")
      print("1. Start  2. Back to Menu")

      pentest_choice = input("Make a choice: ")

      if pentest_choice == '1':
        # Код для запуска пентеста
        # ...
        # Дополнительные действия
        # ...

        break  # Выходим из внутреннего цикла меню Пентест
      elif pentest_choice == '2':
        print("Back to Menu")
        break  # Выходим из внутреннего цикла меню Пентест
      else:
        print("Invalid Choice.")

  elif choice == '2':
    while True:
      print("Doxing Menu:")
      print("1. Start  2. Back to Menu")

      doxing_choice = input("Make a choice: ")

      if doxing_choice == '1':
        # Код для запуска доксинга
        # ...
        # Дополнительные действия
        # ...
        break  # Выходим из внутреннего цикла меню Доксинг
      elif doxing_choice == '2':
        print("Back to Menu")
        break  # Выходим из внутреннего цикла меню Доксинг
      else:
        print("Invalid Choice")

  elif choice == '3':
    # Меню DDoS
    while True:
      print("DDoS Menu:")
      print("1. Start  2. Back to Menu")

      ddos_choice = input("Make a choice: ")

      if ddos_choice == '1':
        # Код для запуска DDoS
        # ...
        # Дополнительные действия
        # ...
        break  # Выходим из внутреннего цикла меню DDoS
      elif ddos_choice == '2':
        print("Back to Menu")
        break  # Выходим из внутреннего цикла меню DDoS
      else:
        print("Invalid Choice")

  elif choice == '4':
    print("Exit")
    break  # Выходим из внешнего цикла (главного меню)
  else:
    print("Invalid Choice")

print("Bye!")



print("TRY TO FIND A KEY")
