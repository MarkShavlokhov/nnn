salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен

money_capital = 0

for month in range(1, months + 1):
    deficit = spend - salary
    if deficit > 0:
        money_capital += deficit
        spend *= (1 + increase)
# TODO Рассчитайте подушку безопасности, чтобы протянуть 10 месяцев без долгов
money_capital = round(money_capital)
print(f"Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
