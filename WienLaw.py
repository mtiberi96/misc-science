def wien_wvlngth(temp): # Function given a known temperature (option 1)
    b = 2898
    try:
        wvlngth = b/temp
        return wvlngth
    except ZeroDivisionError:
        print('ERROR: Invalid input - absolute zero')     
def wien_temp(wvlngth): # Function given a known wavelength of emission (option 2)
    b = 2898
    try:
        temp = b/wvlngth
        return temp
    except ZeroDivisionError:
        print('ERROR: Invalid input - wavelength zero')
def main():
    opt = input('Calculate for wavelength (1) or temperature (2):') # User chooses what to calculate based on its needs
    if (opt == '1'):
        temp = float(input('Enter a temperature (K):')) # Temperature input in degrees kelvin
        print(f'Wavelength is:{str(float(round(wien_wvlngth(temp),2)))} um') # Output wavelength of emission in micrometers // Calls wien_wvlength
    elif (opt == '2'):
        wvlngth = float(input('Enter a wavelength (um):')) # Wavelength of emission input in watts
        print(f'Temperature is: {str(float(round(wien_temp(wvlngth),2)))} K') # Output temperature in degrees kelvin // Calls wien_temp

while True:
    main() # Prevents script from closing after finishing execution (user must terminate manually with Ctrl-C)









        

