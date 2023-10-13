import pandas as pd

# --- datafinder
def create_titles():
    g = open('../data/datafinder/Dataset_Titles.txt', 'w')
    f = open('path/to/datafinder/search/collection/dataset_search_collection.jsonl', 'r')
    lines = f.readlines()
    for line in lines:
        data = json.loads(line)
        title = data['title'] +'\n'
        g.write(title)
    f.close()
    g.close()


def create_dataframe():

    """This method unifies train and test data"""

    g = open('../data/datafinder/Abstract_New_Database_1.txt', 'w')
    # train
    train_file = open('path/to/datafinder/training/set/train_data.jsonl', 'r')
    lines = train_file.readlines()
    for line in lines:
        data = json.loads(line)
        id = data['paper_id']
        abs = data['abstract']
        pos = ', '.join(data['positives'])
        line_to_add = id +'\t'+abs+'\t'+pos+'\n'
        g.write(line_to_add)
    print(len(lines))
    test_file = open('path/to/datafinder/test/set/test_data.jsonl', 'r')
    lines_test = test_file.readlines()
    for line in lines_test:
        data = json.loads(line)
        id = 'test_'+str(lines_test.index(line))
        abs = data['abstract']
        pos = ', '.join(data['documents'])
        line_to_add = id +'\t'+abs+'\t'+pos+'\n'
        g.write(line_to_add)
    print(len(lines_test))


if __name__ == '__main__':
    convert_csv('/path/to/csv')
    convert_csv_titles('/path/to/csv')


