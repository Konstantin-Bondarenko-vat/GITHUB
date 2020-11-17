##########################################################################
'''Task 2. Написати функцію < bank > , яка працює за наступною логікою:
користувач робить вклад у розмірі < a > одиниць строком на
< years > років під < percents > відсотків
(кожен рік сума вкладу збільшується на цей відсоток,
ці гроші додаються до суми вкладу і в наступному році на них
також нараховуються відсотки). Параметр < percents > є необов'язковим
і має значення по замовчуванню < 10 > (10%). Функція повинна
принтануть і вернуть суму, яка буде на рахунку.'''
##########################################################################
def bank(deposit,years,percents):
    
    sum_percents=float()
    for i in range(years):
        sum_percents=(deposit*percents/100)
        deposit+=sum_percents      
    print('sum=',deposit)
    return deposit
######################################
deposit=float(input('Input Deposit: '))
years=int(input('Input Deposit term years: '))
percents=input('Input Interest rate: ')
if percents.isnumeric():
    percents=float(percents)
else:
    percents=10
bank(deposit,years,percents)

