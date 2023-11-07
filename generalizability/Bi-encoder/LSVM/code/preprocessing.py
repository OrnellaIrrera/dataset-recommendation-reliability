def create_linearsvm_qrels_file():

    """The query id is the title of the publication
    the docid is the id of the dataset

    the queries have the _ instead of the ' '
    """

    f = open('./path/to/linearsvm/test_dataset_collection.qrels','w')
    dataf = open('./path/to/linearsvm/used/in/LinearSVM/method/Abstracts_New_Database.txt')
    lines = dataf.readlines()
    line_head = 'QueryID\t0\tDocID\trelevance\n'
    f.write(line_head)
    for line in lines:
        datasets = line.split('\t')[2].replace('\n','').split(', ')
        query_id = line.split('\t')[1].replace('\n','').strip()
        for doc_id in datasets:
            line = query_id.replace(' ','_') + '\t' + "Q0" + '\t' + doc_id.strip() + '\t' + '1' + '\n'
            f.write(line)




def process_linearsvm_dataset_collection():
    df = pd.read_csv('data_0/mes/search_coll.csv')
    g = open('data_0/linearsvm/final/dataset_search_collection.jsonl', 'w')
    # Create an RDF graph

    k = 0
    # Load the N-Triples file into the graph
    file_path = "data_0/linearsvm/DSKG.nt"
    f = open(file_path,'r')
    lines = f.readlines()
    datasets_distinct = []
    for line in lines:
        line = line.split()
        if '/dataset/' in line[0].strip():
            datasets_distinct.append(line[0].strip())
    datasets_distinct = list(set(datasets_distinct))
    print(len(datasets_distinct))
    for d in datasets_distinct:
        print(datasets_distinct.index(d))
        title = ''
        description = ''
        for line in lines:
            line = line.split()
            if d == line[0].strip():
                if ('/title' in line[1].strip()):
                    title = line[2].strip()[1:-1]
                if ('/description' in line[1].strip()):
                    description = ' '.join(line[2::])[1:-1]
                if title != '' and description != '':
                    break
        id = d
        json_l = {}
        json_l['id'] = id[1:-1]
        json_l['contents'] = description
        json_l['structured_info'] = description
        json_l['title'] = title
        json_l['year'] = 0000
        json_l['variants'] = [id]
        g.write(json.dumps(json_l))
        g.write('\n')
