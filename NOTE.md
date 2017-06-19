1. New sequences are put at "\\servervn\Team\UE\sequences\Teleport" example: r0-2017-06-15-jim-walking.h5
2. Line of code encounter issue: 
    In def readblocks(stream): line "data = stream.read(BLOCK_SIZE)"
3. Work around:
    Doubt issue cause by Windows LLP64
    Issue works in Linux
4. Investigate result:
    Python 64 works with large file
    Git's WINGM work with large file
        



Q&A to author:
A:   
    Hi, sorry about the delay.  (I've been hosting a conference.)  What
    architecture are you on?  What do you get if you fire up python and
    print sys.maxint?  Also with respect to memory usage on large files,
    Python is telling me inconsistent information from "top".  I'll look
    into this further as time allows.
TQ Q: 

    Hi,

    Thanks so much for your reply. Here's my machine information:
    1. Hardware:
        - Core I5-4200U, Windows 10 Home 64bit, RAM 4GBs.
    2. Software:
        - Git: 2.8.3 64 bits
        - Python: PYTHON VERSION IS 2.7.12 |Anaconda custom (64-bit)| (default, Jun 29 2016, 11:07:13) [MSC v.1500 64 bit (AMD64)]

    3. Investigating:
        - Print out "Sys.maxint" in git-fat and it return 2147483647
        - When use git-fat (with "git add <large file size>", it runs git-filter-clean command) and calls readblocks() method, it always read to 174559115 bytes, and return empty (as same behavior as end of file). I tried some better machines: Core I7-6500, RAM 32 GBs, Windows 10 Pro and same git 64 versions and python 64 bit versions but encounter same problem (but it only read to 90 MBs and get return empty).
    Looks like file object.read() methods have problem.
        - Also did some experiments as below:
           a. Try to use git to add the same file (8.6GBs) and it works (there's git object which same size in .git/pack/objects folder) ==> So git can deal with large file.
           b. Try to access git bash, use shell script to read and write that file, shell script can create same size file ==> So Git's MINGW enviroment works with large file size.
       
A:
    I assume this is because Windows is LLP64 versus most every other system
    which is LP64.  Adding large files works on Linux in my tests.  Can you
    check out branch 'jed/largefile' and try that.  If it fixes the problem,
    it's just an issue with Python int versus long.  But I somewhat doubt it
    will work in which case it may be some deeper Windows issue.  I haven't
    used Windows in 20 years so I don't know if I'll be able to guess the
    problem.