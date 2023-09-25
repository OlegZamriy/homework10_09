zarplata = float(input("Введіть зарплату за місяць: "))
kredit = float(input("Введіть суму місячного платежу за кредитом: "))
komunalni_poslugy = float(input("Введіть заборгованість за комунальні послуги: "))

zastraha = zarplata - (kredit + komunalni_poslugy)

print(f"Сума, яка залишиться у вас після всіх виплат: {zastraha}")
