
import pandas as pd

def convert_csv(csv):
    df = pd.read_csv(csv)
    g = open('../../data/mes/Abstract_New_Database.txt','w')
    df = df.dropna()
    for index, row in df.iterrows():
        print(row)
        print('\n')
        line = row['pid']+'\t'+row['description']+'\t'+row['datasets'][1:-1]
        line = line.replace('"','')
        print(line)
        # break
        g.write(line)
        g.write('\n')


def convert_csv_titles(csv):
    df = pd.read_csv(csv)
    g = open('../../data/mes/Dataset_Titles.txt', 'w')
    print(df.shape)
    for index, row in df.iterrows():
        g.write(row['title'][3:-3].replace('\n',''))
        g.write('\n')


if __name__ == '__main__':
    convert_csv('/path/to/csv')
    convert_csv_titles('/path/to/csv')


