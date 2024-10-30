import math
salary = 5000  # Ежемесячная зарплата
spend = 6000  # Траты за первый месяц
months = 10  # Количество месяцев, которое планируется протянуть без долгов
increase = 0.03  # Ежемесячный рост цен
money_capital = 0
for i in range (months):
    money_capital += spend - salary
    spend *= increase + 1
money_capital = math.ceil(money_capital)
print("Подушка безопасности, чтобы протянуть {months} месяцев без долгов:", money_capital)
