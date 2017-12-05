import matplotlib.pyplot as plt
import scipy
import numpy as np
import csv
import glob
import os, sys

# Lets start with the tedious task of converting the hugoniot data into 
# numpy arrays? No need to go that deep. lists are okay...... Note: the units matter.
# In the true data, data given in g/cm3, km/s, 2, 1, 1, GPa, kJ/g, Ref... 
# It appears that iSALE might be in CGS units? Surprisingly low pressure throughout this thpough..... 

def Truedat():

    # Time for Shale data from Trunin

    rho0 = [2.77e3,2.77e3,2.77e3,2.77e3,2.77e3,2.77e3,2.77e3,2.77e3,2.77e3, 2.77e3,2.77e3,2.77e3,2.77e3,2.77e3,2.77e3,2.77e3,2.77e3,2.77e3,2.77e3 ]
    D = [5.55e3, 5.78e3, 5.83e3, 6.06e3, 6.06e3, 6.40e3, 6.42e3, 6.77e3, 7.45e3, 8.10e3, 8.90e3, 9.75e3, 12.14e3, 12.00e3, 12.83e3, 13.92e3, 15.16e3, 15.44e3, 16.42e3]
    U = [0.720e3, 1.26e3, 1.50e3, 1.82e3, 1.97e3, 2.29e3, 2.40e3, 2.46e3, 3.04e3, 3.24e3, 3.84e3, 4.41e3, 6.12e3, 6.21e3, 6.67e3, 7.47e3, 8.43e3, 8.62e3, 9.37e3]
    rho = [3.19e3, 3.55e3, 3.74e3, 3.96e3, 4.10e3, 4.32e3, 4.43e3, 4.35e3, 4.68e3, 4.63e3, 4.88e3, 5.07e3, 5.60e3, 5.73e3, 5.76e3, 5.98e3, 6.23e3, 6.26e3, 6.45e3]
    sigma = [1.15, 1.28, 1.35, 1.43, 1.48, 1.56, 1.60, 1.57, 1.69, 1.67, 1.76, 1.83, 2.02, 2.07, 2.08, 2.16, 2.25, 2.26, 2.33]
    p = [11.07e9, 20.17e9, 24.22e9, 30.55e9, 33.07e9, 40.60e9, 42.68e9, 46.13e9, 62.73e9, 72.70e9, 94.67e9, 119.1e9, 205.8e9, 206.4e9, 237.0e9, 288.0e9, 354.0e9, 368.7e9, 426.2e9]
    E =[0.26e3, 0.79e3, 1.13e3, 1.66e3, 1.94e3, 2.62e3, 2.88e3, 3.03e3, 4.62e3, 5.25e3, 7.37e3, 9.72e3, 18.73e3, 19.28e3, 22.24e3, 27.90e3, 35.53e3, 37.15e3, 43.90e3]
    Ref = [14, 14, 14, 14, 14, 3, 14, 14, 14, 3, 14, 3, 14, 3, 14, 14, 14, 14, 3]
    
    v = []
    P= []
    # Calculate the specific volume, but also convert all of these to mks 
    
    for value in range(0, len(rho)): # Calculate the specific volume
        v.append((1/(float(rho[value])))) # Now in cm3/g..... Convert to m3/kg

    for valu in range(0, len(p)): # Convert P to PA from 
        P.append(1/(float(p[valu])))    
        
    td = [rho0, D, U, rho, sigma, p, E, v, Ref]
    print(td)
    
    return(td)
    
# And now the part that requires brain power... Plot what against what?
# I am looking for those last parameters from the hugoniot.... 
# Back to Jay's Book

#Define the arrays that the new data will be dropped into

def Readdat():

    rd = []
    
    for file in os.listdir('txtdata'):
        
        data = []
        i = file[-2] # E0
        j = file[-1] # B
        
        # Defining the colors and marjers based on input
        
        if i== '0':
            data.append('+')
        elif i== '1':
            data.append('v')
        elif i== '2':
            data.append('p')
        elif i== '3':
            data.append('d')
        elif i== '4':
            data.append('*')
        else:
            print('Something is wrong in the source directory')
            
            
        if j == '0': 
            data.append('g')            
        elif j == '1': 
            data.append('m')
        elif j == '2': 
            data.append('y')        
        elif j == '3': 
            data.append('c')        
        elif j == '4': 
            data.append('b')        
        else:
            print('something else')
            
        # Initiate rest of lists that will become the data-bearers
        rho= []
        distension = []
        V  = []
        P=[]
        t = []
        sie  = []
        c = []
        up = []
        u = []
        entropy = []

        # Here is where I add everzthing to a list... But I need a way to distinguish the lists per piece
        # of data.... There are 25 data files to plot and compare

        path = 'txtdata/{file}'
        
        path = path.replace('{file}', file)
        
        delim_whitespace = True

        with open(path, 'r') as datfile:

            for line in datfile:
                li = line.strip()
        
                if li.startswith('#'): 
                    continue
            
                else: 
                    m = li.split()
            
                    rho.append(m[0])
                    distension.append(m[1])
                    V.append(m[2])
                    P.append(m[3])
                    t.append(m[4])
                    sie.append(m[5])
                    c.append(m[6])
                    up.append(m[7])
                    u.append(m[8])
                    entropy.append(m[9])
            
        # So now I have arrays out here
    
        data.append(rho)
        data.append(distension)
        data.append(V)
        data.append(P)
        data.append(t)
        data.append(sie)
        data.append(c)
        data.append(up)
        data.append(u)
        data.append(entropy)
        rd.append(data)
    return(rd)

###
# Now to compare the data
###

def Compare(td, rd):
    
    # Now I have two data arrays and want to plot a pv diagram????
    # how about a PV diagram along with a couple other parameters just to see if other things will be more revealing... Don't care about temperature, but I do care about up, u are important
    
    for value in range(0, len(rd)):  
        mark = rd[value][0]
        c = rd[value][1]
        
        plt.plot(rd[value][4], rd[value][5], marker=str(rd[value][0]), color=rd[value][1])                
        
    plt.plot(td[7], td[5], linestyle='solid', marker='o', color='red')
    plt.xlabel('Specific Volume')
    plt.ylabel('Pressure')
    plt.title('Checking parameters, V vs P')
    
    plt.savefig('output/PV_b0_E14_a49_45.png')
    plt.show()


    #Plot a up vs u to check it up just in case 
    for value in range(0, len(rd)):
        
        plt.plot(rd[value][9], rd[value][10], marker=rd[value][0], color=rd[value][1])                
        
    plt.plot(td[2], td[1], linestyle='solid', marker='o', color='red')
    plt.xlabel('Specific Volume')
    plt.ylabel('Pressure')
    plt.title('Checking parameters, V vs P')
    
    plt.savefig('output/UpU_b0_E14_a49_45.png')
    plt.show()    

def main():
    n = Truedat()
    m = Readdat()
    
    Compare(n, m)
    
main()
