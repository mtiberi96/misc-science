def boltzmann_1(temp): # Function given a known temperature (option 1)
    sigma = 5.67e-8 # w m-2 k-4
    energy = sigma*(abs(temp)**4)
    return energy
def boltzmann_2(energy): # Function given a known value of emitted radiation (option 2)
    sigma = 5.67e-8 # w m-2 k-4
    temp = (energy/sigma)**(1/4)
    return temp

def main():
    opt = input('Calculate for emitted radiation (1) or black body temperature (2):') # User chooses what to calculate based on its needs
    if (opt == '1'):
        temp = float(input('Introduce a temperature (K):')) # Temperature input in degrees kelvin
        print(f'The amount of emitted radiation is: {str(float(round(boltzmann_1(temp),2)))} W') # Output emitted radiation in watts // Calls boltzmann_1
    if (opt == '2'):
        energy = float(input('Introduce emitted radiation (W):')) # Emitted radiation input in watts
        print(f'The temperature is: {str(float(round(boltzmann_2(energy),2)))} K') # Output temperature in degrees kelvin // Calls boltzmann_2

while True:
    main() # Prevents script from closing after finishing execution (user must terminate manually with Ctrl-C) 

 