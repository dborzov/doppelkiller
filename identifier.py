import shutil

inx = open('index1.csv','rb').readlines()
counter = {}
for line in inx:
    filename, sha1 = line.split(' ')
    sha1 = sha1.rstrip()
    counter[sha1] = filename

inx2 = open('index2.csv','rb').readlines()
for line in inx2:
    filename, sha1 = line.split(' ')
    sha1 = sha1.rstrip()
    if sha1 in counter:
        shutil.move('Nika Rome/DCIM/100OLYMP/'+filename,'../Pictures/Duplicates')
        print 'Moving file: ', filename
