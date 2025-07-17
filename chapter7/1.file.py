#Python can be used to perform operations on a file.(read and write data)
# Types of all files
# 1. Text files :- .txt, .docx, .log etc.
# 2. Binary files :- .mp4, .mov, .png, .jpeg etc.

# Open ,read and close file:
# Syntax:- f=open("file_name","mode")
#          file_name:- sample.txt , demo.docx
#          mode :- read mode(r) , write mode(w)
#          data = f.read()
#          f.close()

                       #MODE
#'r'         open for reading(default)
#'w'         open for writing, Truncating the file
#'x'         create a new file for writing
#'a'         open for writing, appending to the end of the file if it exists
#'b'         binary mode
#'t'         text mode(default)
#'+'         open a disk file for updating(reading and writing)