tuhat = 1
print('kolmella jaolliset luvut välillä 1-1000:')
while tuhat < 1001:
   if tuhat % 3 == 0:
       print(f'{float(tuhat)}')
       tuhat = tuhat + 1
   else:
       tuhat = tuhat + 1