# automation
""" A simple python script for setting up and submitting batches of iSALE jobs through SLURM. Meant for use in the terminal. 

This is intended to allow a user to quickly and easily set up a batch of jobs from a single master script that creates a run directory with specific material and asteroid input decks before submitting the job over slurm.  

This script uses python's os and sys modules to create the run directories and drop commands into the command line
The architecture follows a main script and a directory that the script is dependent upon to carry out its tasks. This 'depedencies' folder includes template files for both the asteroid.inp and the material.inp files. Within these files are string variables enclosed in curly brackets (i.e. '{var}') that are picked up and replaced with user-specified values for that variable. The curly brackets are meerly a convenient way to pick up the specific string values to be replaced by python's string.replace() function. 

If a batch, rather than a single job as given in this skelatal script, of jobs is desired to be submitted in one script, there is a commented out section of the script that can do this. This involves telling the code to create several directories, then copying a modified copydir into each directory. Rather than replacing a bracket-delineated variable with a single variable, a list can be specified:

    B =["3.0D+10","4.0D+10","5.0D+10","6.0D+10","7.0D+10"]
  
    for val in range(0, len(B)):
      with open('file') as tmp, open('other_file') as o:
        for line in tmp:
          line=line.replace("{B}",B[val])
        
          o.write()
      o.close()
    
In this way, multiple jobs can easily be submitted through this simple script.     

As the master script replaces variables within the input decks, they are written into the copy directory (overwriting any existing input decks). The copy directory is then copied into a directory whose name is specified by the user, and the jobs are submitted to run in the background. 

Cheers!
"""
