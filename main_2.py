surname = input("Bаше прізвище: ").upper()

letter = max(surname, key = surname.count)
print(f"Найчастіша літера: {letter}")