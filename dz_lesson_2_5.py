my_prices = [57.8, 46.51, 97, 33, 25.05, 10.5, 39.5, 50.98, 245]
for my_price in my_prices:
    rub = int(my_price)
    kk = (my_price - int(my_price)) * 100
    print(f'{rub} руб {kk:02.0f} коп')



my_prices = [57.8, 46.51, 97, 33, 25.05, 10.5, 39.5, 50.98, 245]
print(id(my_prices))
my_prices.sort()
print(id(my_prices))
for my_price in my_prices:
    rub = int(my_price)
    kk = (my_price - int(my_price)) * 100
    print(f'{rub} руб {kk:02.0f} коп')


my_prices = [57.8, 46.51, 97, 33, 25.05, 10.5, 39.5, 50.98, 245]
for my_price in sorted(my_prices)[::-1][:5]:
    rub = int(my_price)
    kk = (my_price - int(my_price)) * 100
    print(f'{rub} руб {kk:02.0f} коп')
