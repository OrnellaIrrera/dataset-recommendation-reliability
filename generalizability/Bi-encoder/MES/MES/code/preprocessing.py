
import pandas as pd

import random
def get_negatives(id_to_exclude):
    df = pd.read_csv('did.csv')
    df['did'] = df['did'].apply(lambda x: x.replace('"',''))
    sample_n = []
    ids = df['did'].values.tolist()
    not_found = True
    i = 0

    sample_n = random.sample(ids, 10)
    double = [x for x in sample_n if x in id_to_exclude]
    i+=1
    if len(double) > 0:
        sample_n = [x for x in sample_n if x not in double]
    return sample_n



def train_test_data_title_query():
    f = open('path/to/split/split_train_test.json', 'r')
    train_file = open('path/to/title_query/train_data.jsonl', 'w')
    test_file = open('path/to/title_query/test_data.jsonl', 'w')
    df = pd.read_csv('../data/pub.csv')
    data = json.load(f)
    data = data['training']
    queries = data['queries']
    query_ids = data['query_ids']
    datasets = data['datasets']
    # assert len(queries) != len(query_ids) != len(datasets)
    for i in range(0,len(queries)):
        jsonl = {}
        doc_id = query_ids[i]
        ids1 = df['id'].tolist()
        pubrow = df[df['id']== '"'+doc_id+'"']
        abstract = pubrow['abstract'].iloc[0][1:-1]
        title = pubrow['title'].iloc[0][1:-1]
        try:
            year = pubrow['year'].iloc[0][1:-1].split('-')[0][0:4]
        except:
            year = '2000'
        if len(year) == 0:
            year = '2000'
        jsonl['year'] = int(year)
        dataset = datasets[i]
        jsonl['paper_id'] = doc_id
        jsonl['positives'] = dataset
        jsonl['negatives'] = get_negatives(dataset)
        jsonl['abstract'] = abstract.replace('"','')
        jsonl['title'] = title.replace('"','')
        jsonl['query'] = title.replace('"','')

        train_file.write(json.dumps(jsonl))
        train_file.write('\n')



    data = data['test']
    queries = data['queries']
    query_ids = data['query_ids']
    datasets = data['datasets']
    # assert len(queries) != len(query_ids) != len(datasets)
    for i in range(0,len(queries)):
        jsonl = {}
        doc_id = query_ids[i]
        ids1 = df['id'].tolist()
        pubrow = df[df['id']== '"'+doc_id+'"']
        abstract = pubrow['abstract'].iloc[0][1:-1]
        title = pubrow['title'].iloc[0][1:-1]
        try:
            year = pubrow['year'].iloc[0][1:-1].split('-')[0][0:4]
        except:
            year = '2000'
        if len(year) == 0:
            year = '2000'
        jsonl['year'] = int(year)
        dataset = datasets[i]
        jsonl['paper_id'] = doc_id
        jsonl['positives'] = dataset
        jsonl['negatives'] = get_negatives(dataset)
        jsonl['abstract'] = abstract.replace('"','')
        jsonl['title'] = title.replace('"','')
        jsonl['query'] = title.replace('"','')

        test_file.write(json.dumps(jsonl))
        test_file.write('\n')




def train_test_data_abstract_query():
    f = open('path/to/split/split_train_test.json', 'r')
    train_file = open('path/to/abstract_query/train_data.jsonl', 'w')
    test_file = open('path/to/abstract_query/test_data.jsonl', 'w')
    df = pd.read_csv('../data/pub.csv')
    data = json.load(f)
    data = data['training']
    queries = data['queries']
    query_ids = data['query_ids']
    datasets = data['datasets']
    # assert len(queries) != len(query_ids) != len(datasets)
    for i in range(0,len(queries)):
        jsonl = {}
        doc_id = query_ids[i]
        ids1 = df['id'].tolist()
        pubrow = df[df['id']== '"'+doc_id+'"']
        abstract = pubrow['abstract'].iloc[0][1:-1]
        title = pubrow['title'].iloc[0][1:-1]
        try:
            year = pubrow['year'].iloc[0][1:-1].split('-')[0][0:4]
        except:
            year = '2000'
        if len(year) == 0:
            year = '2000'
        jsonl['year'] = int(year)
        dataset = datasets[i]
        jsonl['paper_id'] = doc_id
        jsonl['positives'] = dataset
        jsonl['negatives'] = get_negatives(dataset)
        jsonl['abstract'] = abstract.replace('"','')
        jsonl['title'] = title.replace('"','')
        jsonl['query'] = abstract.replace('"','')

        train_file.write(json.dumps(jsonl))
        train_file.write('\n')



    data = data['test']
    queries = data['queries']
    query_ids = data['query_ids']
    datasets = data['datasets']
    # assert len(queries) != len(query_ids) != len(datasets)
    for i in range(0,len(queries)):
        jsonl = {}
        doc_id = query_ids[i]
        ids1 = df['id'].tolist()
        pubrow = df[df['id']== '"'+doc_id+'"']
        abstract = pubrow['abstract'].iloc[0][1:-1]
        title = pubrow['title'].iloc[0][1:-1]
        try:
            year = pubrow['year'].iloc[0][1:-1].split('-')[0][0:4]
        except:
            year = '2000'
        if len(year) == 0:
            year = '2000'
        jsonl['year'] = int(year)
        dataset = datasets[i]
        jsonl['paper_id'] = doc_id
        jsonl['positives'] = dataset
        jsonl['negatives'] = get_negatives(dataset)
        jsonl['abstract'] = abstract.replace('"','')
        jsonl['title'] = title.replace('"','')
        jsonl['query'] = abstract.replace('"','')

        test_file.write(json.dumps(jsonl))
        test_file.write('\n')




def create_mes_qrels_file():
    """The query id is the title of the publication
    the docid is the id of the dataset

    the queries have the _ instead of the ' '
    """
    # df = pd.read_csv('./data_0/mes/qrels.csv')
    df = pd.read_csv('../data/qrels_abs.csv')
    docs = []

    f = open('path/to/abstract_query/test_dataset_collection.qrels', 'w')
    line_head = 'QueryID\t0\tDocID\trelevance'
    f.write(line_head)
    f.write('\n')
    for i,row in df.iterrows():
        queryID = row['QueryID'][1:-1].replace(' ','_')

        line = queryID + '\t' + row['Q0'] + '\t' + row['DocID'] + '\t' + str(row['relevance']) + '\n'
        line = line.replace('"', '')
        if row['DocID'] not in docs:
            f.write(line)
            docs.append(row['DocID'])


def process_dataset_collection():
    df = pd.read_csv('path/to/search_collection.csv')
    f = open('path/to/title_query/dataset_search_collection.jsonl', 'w')

    for i,row in df.iterrows():
        json_l = {}
        json_l['id'] = row['id'].replace('"', '')
        contents = row['contents'].replace('"', '')[1:-1]
        json_l['contents'] = contents
        json_l['variants'] = row['variants'].replace('"', '')[1:-1].split(', ')
        json_l['title'] = row['title'].replace('"', '')[1:-1]
        try:

            json_l['year'] = row['year'].replace('"', '')[1:-1].split('-')[0][0:4]
        except:
            json_l['year'] = '2000'
        if len(json_l['year']) == 0:
            json_l['year'] = '2000'
        json_l['year'] = int(json_l['year'])
        json_l['structured_info'] = row['structured_info'].replace('"', '')[1:-1]
        f.write(json.dumps(json_l))
        f.write('\n')




if __name__ == '__main__':
    train_test_data_abstract_query()
    train_test_data_title_query()


