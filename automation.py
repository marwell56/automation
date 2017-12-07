
# This script will create a directory with a user specified name, 
# edit the material and asteroid templates based on previous scripts
# and then copy everzthing into a new directory and submit the run

import os

#User specified values
dirname = 'sweep'

ast_details= {'{tend}':'1.D2'}
mat_details= {'{gameta}':['1.D-3', '4.D-3', '8.D-3', '1.D-4'], '{gambeta}':['1.D+2', '1.D+02', '5.D+2', '1.D+3']}

# make target directory from home directory
path = '/home/mharwell/isale_runs/'
full_path = path+dirname
os.mkdir(full_path)
os.chdir(full_path)

#Now we are within the batch run directory. Make new directories for each run 
# Read in temperary files, replace what needs to be replaced, then write into the 
#dependencies/copydir

i=0
j=0

for n in range(0, len(mat_details['{gameta}'])):
    i+=1
    for m in range(0, len(mat_details['{gambeta}'])):
        j+=1
        # now to create the run directories
        os.mkdir('run'+str(i)+str(j))        
        
        with open('home/automation/dependencies/tmp_asteroid.inp') as ast_temp, open('home/automation/dependencies/copydir/asteroid.inp') as fa:
            for line in ast_temp:
                for src, target in ast_details.iteritems():
                    line = line.replace(src,target)
        
            fa.write()
        fa.close()
    
    
        with open('~/automation/dependencies/tmp_material.inp') as mat_tmp, open('~/automation/dependencies/copydir/material.inp') as fm:
            for line in mat_tmp:
                for src, target in mat_details.iteritems():
                    line = line.replace(src,target)
        
            fm.write()
        fm.close()
        
        os.chdir('run'+str(i)+str(j))
        os.system('cp ~/automation/copydir/* .')        
        os.system('srun -n1 iSALE2D &')
        os.system('cd ..')

#Now, the content of the copy driectory are placed in the target directory
# If multiple directories, then multiple runs.... Why don't I write this to be useful to me? 

