salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
m = 0
c = spend

for month in range(months):
    d = c - salary
    m += d
    if month < months -1:
        c = c * (1+increase)

print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", round(m))
