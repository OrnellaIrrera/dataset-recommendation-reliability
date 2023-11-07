

def create_qrels():
    """The query id is the title of the publication
    the docid is the id of the dataset

    the queries have the _ instead of the ' '
    """

    dataf = open(data_dir + 'path/to/makg/Abstract_New_Database.txt')
    f = open(data_dir + '/dataset_search_collection.qrels', 'w')
    lines = dataf.readlines()
    line_head = 'QueryID\t0\tDocID\trelevance\n'
    f.write(line_head)
    empty = 0
    for line in lines:
        datasets = line.split('\t')[2].replace('\n', '').split(', ')
        query_id = line.split('\t')[1].replace('\n', '').strip()
        if len(datasets) == 0:
            empty += 1
        for doc_id in datasets:
            line = query_id.replace(' ', '_') + '\t' + "Q0" + '\t' + doc_id.strip() + '\t' + '1' + '\n'
            f.write(line)
    print(empty)


def create_entire_collection_datasets():
    dataf = aux_get_dataset_dataframe('datasets')
    g = open(data_dir + '/dataset_collection.jsonl', 'w')
    print(dataf.shape)
    count = 0
    for index, row in dataf.iterrows():
        count += 1
        id = row["ID"]
        json_l = {}
        json_l['id'] = id
        json_l['contents'] = row['Title'] + ' ' + row['Abstract']
        json_l['structured_info'] = row['Title'] + ' ' + row['Abstract']
        json_l['title'] = row['Title']
        json_l['year'] = 0000
        json_l['variants'] = [id]
        g.write(json.dumps(json_l))
        g.write('\n')
    print(count)