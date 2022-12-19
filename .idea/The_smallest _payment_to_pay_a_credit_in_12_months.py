""" This programm is  searching for the smallest monthly payment such that we can pay off the entire balance within a year"""

balance = 320000
annualInterestRate = 0.2

prev_balancee =balance
update_bal =balance
low =balance /12
high =(balance *( 1 +annualInterestRate /12.0 )**12 ) /12.0
upbal =balance
x= (high + low) / 2.0

while abs(update_bal) > 0.0001:
    minim_m_payment = x
    prev_balance = balance
    for i in range(1, 13):
        minim_m_payment = x
        mont_un_payd_b = prev_balance - minim_m_payment
        update_bal = mont_un_payd_b + mont_un_payd_b * annualInterestRate / 12.0
        prev_balance = update_bal
    if update_bal < 0:
        high = x
        x = (low + high) / 2.0
    elif update_bal > 0:
        low = x
        x = (low + high) / 2.0

print('Lowest Payment is:', round(x, 2))