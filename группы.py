gen = 0
while gen < 20: #25 для сложения
    i=0
    mass_values = []
    gen +=1
    print('\nГенератор: ', gen, '\n')
    while i<20: #25 для сложения
        mass = pow(gen, i, 25) #для умножения
        #mass = (gen*i)%25 #для сложения
        mass_values.append(mass) 
        i += 1
    print('Несортированный: \n',mass_values, '\n')
    mass_values.sort()
    wordes = ' '.join(map(str, mass_values))
    print('sorted: \n', wordes) 