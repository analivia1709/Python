preco = float(input('Entre with price do produto: '))
discount = (preco * 5 ) / 100
newpreco= preco - discount
print ('The new price of your product is {} the discount was of {}'.format(newpreco, discount))