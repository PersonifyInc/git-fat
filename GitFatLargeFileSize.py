# import mmap
import sys
import os
path = "G:/DebugGitFatPackage/Fat/sequences/TeleporterPgrsCam/r2-2017-05-13-simon-sit-still31.h5"
READ_BLOCK_SIZE = 4096

# def readFile(path):
def readFile(f):
    bytecount = 0L
    while True: 
        piece = f.read(READ_BLOCK_SIZE)
        bytecount += len(piece)
        if not piece: 
            break 
        yield piece
        # print "---Bytecount is {}".format(bytecount) 
    # with open(path, 'rb') as f:
        # while True: 
            # piece = f.read(READ_BLOCK_SIZE)
            # bytecount += len(piece)
            # if not piece: 
                # break 
            # yield piece
            # print "---Bytecount is {}".format(bytecount) 

count = 0L
with open(path, 'rb') as f:
    cache = open('I:/r2-2017-05-13-simon-sit-still31.h5', 'wb')
    sys.stdin = f
    sys.stdout = cache
    with os.fdopen(cache.fileno(), 'wb') as temp:
        print "---Size of stdin file id is {}, sys.stdin is {}".format(f.fileno(), os.fstat(f.fileno()).st_size)
        print "---Size of stdout file id is {}, sys.stdin is {}".format(cache.fileno(), os.fstat(cache.fileno()).st_size)
        # 
        outstream = temp
        for piece in readFile(sys.stdin):
            outstream.write(piece)
            count += len(piece)
            # print "."
        outstream.flush()
        print "---Bytecount is {}".format(count)