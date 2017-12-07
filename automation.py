
# This script will create a directory with a user specified name, 
# edit the material and asteroid templates based on previous scripts
# and then copy everzthing into a new directory and submit the run

import os

#User specified values
dirname = 'sweep'

ast_details= {'{tend}':'1.D1'}
gameta=['1.D-3', '4.D-3', '8.D-3', '1.D-4']
gambeta=['1.D+1', '1.D+02', '5.D+2', '1.D+3']

# make target directory from home directory
path = '/home/mharwell/isale_runs/'
full_path = path+dirname
os.mkdir(full_path)
os.chdir(full_path)
os.system('pwd')

#Now we are within the batch run directory. Make new directories for each run 
# Read in temperary files, replace what needs to be replaced, then write into the 
#dependencies/copydir


j=0

for n in range(0, len(gameta)):
    i=0
    for m in range(0, len(gambeta)):
                
        direct = os.path.expanduser('~')+'/automation/dependencies'
        print(direct)
        
        with open(os.path.join(direct, 'tmp_asteroid.inp'),'r') as ast_temp, open(os.path.join(direct, 'copydir/asteroid.inp'), 'w') as fa:
            for line in ast_temp:
                for src, target in ast_details.iteritems():
                    line = line.replace(src,target)
        
                fa.write(line)
        fa.close()
    
    
        with open(os.path.join(direct, 'tmp_material.inp'), 'r') as mat_tmp, open(os.path.join(direct, 'copydir/material.inp'), 'w') as fm:
            for line in mat_tmp:
                line = line.replace('{gameta}', gameta[i])
                line = line.replace('{gambeta}', gambeta[j])
                fm.write(line)
        fm.close()
        
        os.mkdir('run'+str(i)+str(j))        
        os.chdir('run'+str(i)+str(j))
        os.system('cp -r ~/automation/dependencies/copydir/* .')        
        os.system('srun -N1 iSALE2D &')
        os.chdir('..')
        i+=1
    j+=1

#Now, the content of the copy driectory are placed in the target directory
# If multiple directories, then multiple runs.... Why don't I write this to be useful to me? 

