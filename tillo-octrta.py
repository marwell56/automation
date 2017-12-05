# This is going to be based on memory of the scripts I worked on this summer... So octrta... 
# In order, this will do: 1. replace values in the template within a dependencies directory with desired parameters
#                          2. Place these new eos files in the proper location, run iSALe, cut it off after a brief period
#                          3. Move the generated SETUP/hugoniot etc. file to one under a name numbered based on how many runs
#                          4. runs will be defined within the nested do loop. b will be the constant, the files -> local folder
#                          5. Then it will call the plotting script to read in all data and plot on large, well defined plot
#                          6. As more data added, specifiers for the plotting will be given... marker, color, within a do loop
#
#


import os
import sys
import time

B =["7.5D+10"] #["3.0D+10","4.0D+10","5.0D+10","6.0D+10","7.5D+10"] 
E0 = ["14.D+7"]#["1.0D+7","8.0D+7","11.0D+7"]#,"14.0D+7","16.0D+7"]
b= "0.45"
a = "0.55"

# Instead of plotting dictionary, I need a way to distinguish between the generated hugoniot files, down here

i = 0
j = 0

command = 'cp demo2D/SETUP/hugoniot-myshale-shale__-tillo.txt dependencies/txtdata/hugoniot{i}{j}'

for value in range(0, len(E0)):
    
    for val in range(0, len(B)):
        command=command.replace('{i}', str(value))
        command = command.replace('{j}', str(val))
	print(command)

        # This next bit writes the eos file and places it in the eos directory from a template
        
        with open('dependencies/tempshale__.tillo', 'r') as template, open('eos/shale__.tillo', 'w') as f:
            for line in template:
                line = line.replace("{B}",B[val])
                line = line.replace("{E0}",E0[value])
                line = line.replace("{b}", b)
                line = line.replace("{a}", a)
                
                f.write(line)
        f.close()
       
        # Here is where each will be run and the hugoniot file moved... 
        os.system('./iSALE2D')
#        time.sleep(5) The terminal should be held hostage anyway by the process..... Should cont. after
	os.system(command)
	command = 'cp demo2D/SETUP/hugoniot-myshale-shale__-tillo.txt dependencies/txtdata/hugoniot{i}{j}'

        j = j + 1
        
    i = i + 1
    
os.chdir('dependencies')
os.system('pwd')

os.system('python hugoniot.py')
os.chdir('..')
