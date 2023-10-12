import os



def write_results():

    files = os.listdir(basepath+'path/to/results/')
    results = open(basepath+'path(to/save/combined/results/filename.txt','w')
    # iterate over all the  files created during the execution of Recommend.py
    for file in files:
        print(file)
        f = open(basepath+'path/where/datarecommend/stored/results/'+file,'r')
        lines = f.readlines()
        total_T = 0
        total_G = 0
        total_N = 0
        title = '.'.join(file.split('.')[0:-1])
        for line in lines:
            values = line.split()
            T = float(values[1])
            G = float(values[2])
            N = float(values[3])
            total_T += T
            total_G += G
            total_N += N

        precision = total_T/total_N
        recall = total_T/total_G
        F1 = (precision*recall)/(precision+recall)*2
        l = title + '\t' + str(precision) + '\t' + str(recall) +'\t' + str(F1)+'\n'
        results.write(l)

if __name__ == '__main__':
    write_results()
