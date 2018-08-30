# 4315ProgramAssignment1

Clone
To clone a remote file is to copy the remote contents to your local area.

git clone git@bitbucket.org:technicool/time-keeper.git
You will now have a directory created with the code.

Process
We have 2 main branches
*master* is the production branch and is deployed to production serverts. This is versioned.
*test* is the test branch used for testing.
For development we create branches that have the name of tickets.

Developing
Create a ticket branch
Say your ticket is T41 then first you need to create the branch.

git checkout -b T41 test
git push origin T41
You can see what branches you have by doing

git branch
Code
Now you can code and test and do everything you need to do.

check in your code
To check in your code to your dev ticket use the following:

git status
git add *
git commit -m "T41: I did blah blah"
git push origin T41
Merge your changes into Test branch
Create a merge request
