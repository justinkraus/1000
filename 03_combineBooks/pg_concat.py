import os
from top_1k import book_files

def concatFiles():
    path = os.getcwd()
    # files = os.listdir(path)
    files = book_files
    with open("1000_First_Pages.txt", "w") as fo: 
    	cover = open(os.path.join(path, 'cover.txt'), encoding="utf8", errors='ignore').read()
    	fo.write(cover)
    	for infile in files:
        	with open(os.path.join(path, infile), encoding="utf8", errors='ignore') as fin:
        		temp = filter(str.isdigit, infile)
        		nums = "".join(temp)
        		print(nums)
        		words = fin.read()[0:5000]
        		fo.write('PG #: ' + nums + '\n' + 'https://www.gutenberg.org/ebooks/' + nums + '\n' + '\n' + str(words) + '\n' + '------------------------------------------------------------------------' + '\n' + '\n')
    	book_index = open(os.path.join(path, 'book_metadata.csv'), encoding="utf8", errors='ignore').read()
    	fo.write(book_index)
                # for line in fin:
                # 	print(line)
                    # words = line.split()
                    # print(words)
                    # fo.write(str(words[0:1000]))


concatFiles()
