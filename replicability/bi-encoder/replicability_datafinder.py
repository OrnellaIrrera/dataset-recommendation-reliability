import json

def create_test_data_df():
    titles = []
    k = 0
    f = open('path_to/test_data.jsonl', 'r')
    g = open('path_to/test_data_keyword.jsonl', 'r')

    for line in f.readlines():
        data = json.loads(line)
        # skip duplicated query definitions
        if data['keyphrase_query'] not in titles:
            g.write(line)
        titles.append(data['keyphrase_query'])


def adapt_to_keyphrase():
    f = open('path_to/test_dataset_collection.qrels','r')
    ff = open('path_to/test_dataset_collection_keyword.qrels','w')
    ff.write('QueryID\tQ0\tDocID\trelevance\n')


    g = open('test_data_df.jsonl','r')
    lines = g.readlines()
    lines_f = f.readlines()

    for line in lines:
        data = json.loads(line)
        kq = data['keyphrase_query']
        q = data['query']

        q = q.replace(' ','_')
        kq = kq.replace(' ','_')
        for line2 in lines_f:
            line = line2.split('\t')
            qu = line[0]
            ll = '\t'+'\t'.join(line[1::])
            if q == qu:
                new_l = kq + ll
                ff.write(new_l)
