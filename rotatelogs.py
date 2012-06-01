#****************************************************
import logging
from logging import handlers
#*****************************************************

my_logger = logging.getLogger('MyLogger')
my_logger.setLevel(logging.DEBUG)


filelocation = 'testrotatelogs.txt'
handler = handlers.RotatingFileHandler(filelocation, maxBytes=20000, backupCount=5)
# maxBytes = 20,000 means 20kB

my_logger.addHandler(handler)


text = "  sdfsdfdfsdfsdaf sdfsda ccccccccccccccccccccc cddddddddddddddddddd ddddddddddddddddddddddddd dddddddddddddddd dwe       ewffffffffwedfwf ewdfsadf sadfsadf sadfsad dsafdssssssssssss ssssssssssss ewwwwwwwwwwwww wwwwwwwwwwwwww rrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrrw                  wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww jjjjjjjjjjjjjjjjjjjjjjjjjjjjj kkkkkkkkkkkkkkkkk lllllllllllllllllllllll ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; kkkkkkkkkkkkkkkkkk ,,,,,,,,,,,,,,,,,,,, iiiiiiiiiiiiiiiiiiiiii oooooooooooooooooooooooo yuuuuuuuuuuuuuuuuuuuuuuuuuu ttttttttttttttttttttttt rrrrrrrrrrrrrrrrrrrrr eeeeeeeeeeeeeeeeeeeeeee dssssssssssssssssssssssss wwwwwwwwwwwwwwwwwwwwwwwwwwww vvvvvvvvvvvvvvvvvvvvvvvvv bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb ddddddddddddddddddddddddddddddddddd ssssssssssssssssssssssssssssssssssssssssssssssssssssssss wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee wwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwwww tttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt ttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttttt 655555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555555"

# Run this 20 times to see how many files are created  
for i in range(20):
    my_logger.debug(text)


    


