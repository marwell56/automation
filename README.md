# automation
""" A simple python script for setting up and submitting batches of iSALE jobs through SLURM. Meant for use in the terminal. Especially, though, this is meant as a quick introduction to git and github's useful features. 

To clone the repository into your own home space, find the green button on the github page that says 'clone or download.' You will find a weblink. Use the following commands to clone the directory into a directory of your chpoice. Within that directory:

git clone [ssh weblink]

Now you should be on the master branch. If you want to make edits without changing this branch, checkout a new branch:

git checkout -b [branch_name]

In the new branch, you can safely make changes and personalize things. When an edit is ready to be pushed to the master branch and on up to origin, use the following commands to check the status of your branch (what changes have been made but are not staged to be committed), add the changes to be pushed (stage them for pushing), commit the changes (with a comment, all need to be added with comments), and, finally, push the changes. 

git status

git add [list of files by name, separated by a space]

git commit -m [your comments]

git push [master branch, usually 'origin'] [working branch]


Now, if your branch is several commits behind another branch, you will need to pull the changes to update your own branch before you can commit your changes. There are two ways to accomplish this. The first way, using fetch and merge in two separate commands, is perhaps safer if there are a lot of people working on the same gitrepo. Git stores commits in the target branch that are not in your local branch in your local repository but does not merge them into your branch. You would then give the command to merge them into your branch when ready. This is useful when an update could break what you are working on.  

git fetch 

git merge [source] [target]

The way to do both at the same time, or fast-forward your branch to match the target, is: 

git pull

If you make a change and are unhappy with it and want to reset everything to master, run 

git reset --hard




The intent of the script itself:

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
