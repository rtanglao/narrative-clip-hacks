narrative-clip-hacks
====================

narrative clip hacks

1. hack 1 - since the narrative clip as of 26 march 2014, splits up files into 1 directory per day and reuses file names in different directories, to maintain the order you need to rename the files in the other directories, hence rename-starting-with.py
2. so find the last file name in day 1 and rename day 2 and day 3
3. e.g. if the last file name on march 25 is: 000999.jpg then 

        cd day 2; ./rename-starting-with-py 1000  (no need for leading zeros, the script will handle them)
