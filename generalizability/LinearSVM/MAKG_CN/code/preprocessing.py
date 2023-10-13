
import pandas as pd

import re

data_dir = 'path/to/the/folder/where/csv/data/is/stored'
def create_dataframe():

    links_file0 = data_dir + '/StandardSchLink_paper_dataset.csv'
    links_file1 = data_dir + '/StandardSchLink_dataset_paper.csv'
    entities = data_dir + '/publications.csv'
    entities_abs = data_dir + '/publications_abs.csv'
    dataframe_final = data_dir + '/Abstract_New_Database.txt'
    publications = pd.read_csv(entities)
    publications_abs = pd.read_csv(entities_abs)
    ptod = pd.read_csv(links_file0)
    dtop = pd.read_csv(links_file1)
    distinct_pub_dtop = dtop['Object'].unique()
    distinct_pub_dtop = list(set(list(distinct_pub_dtop)))

    distinct_pub_ptod = ptod['Subject'].unique()
    distinct_pub_ptod = list(set(list(distinct_pub_ptod)))
    distinct_pubs = list(set(distinct_pub_ptod + distinct_pub_dtop))

    distinct_data_dtop = dtop['Subject'].unique()
    distinct_data_dtop = list(set(list(distinct_data_dtop)))

    distinct_data_ptod = ptod['Object'].unique()
    distinct_data_ptod = list(set(list(distinct_data_ptod)))
    distinct_data = list(set(distinct_data_dtop + distinct_data_ptod))
    print(len(distinct_data))
    print(len(distinct_pubs))

    mask0 = (publications.iloc[:, 0].isin(distinct_pubs))
    final_df_publications = publications[mask0]

    mask0 = (publications_abs.iloc[:, 0].isin(distinct_pubs))
    final_df_publications_abs = publications_abs[mask0]
    final_df_publications_abs = final_df_publications_abs.rename(columns={'Subject': 'ID', 'Object': 'Abstract'})

    final_df_publications = final_df_publications.rename(columns={'Subject': 'ID', 'Object': 'Title'})

    result_df = final_df_publications.merge(final_df_publications_abs, on='ID', how='left')
    g = open(dataframe_final,'w')
    count = 0
    result_df = result_df.fillna('')
    for index, row in result_df.iterrows():
        identifier = row['ID']
        testo = row['Title']

        if not row['Abstract'] == '':
            testo = row['Title'] + ' ' + row['Abstract']
        testo = re.sub(r'[^a-zA-Z0-9 ]', '', testo)
        filtered_df = ptod[ptod['Subject'] == identifier]
        filtered_df_1 = dtop[dtop['Object'] == identifier]
        datasets_list_0 = filtered_df['Object'].tolist()
        datasets_list_1 = filtered_df_1['Subject'].tolist()
        datasets = list(set(datasets_list_0+datasets_list_1))
        datasets = ', '.join(datasets)



        new_row = identifier + '\t'+ testo + '\t'+datasets+'\n'
        g.write(new_row)
        count +=1
        print(new_row)
    print(count)


def create_titles_txt():

    links_file0 = data_dir + '/StandardSchLink_paper_dataset.csv'
    links_file1 = data_dir + '/StandardSchLink_dataset_paper.csv'
    entities = data_dir + '/datasets.csv'
    titles = data_dir + '/titles.txt'
    datasets = pd.read_csv(entities)
    ptod = pd.read_csv(links_file0)
    dtop = pd.read_csv(links_file1)
    distinct_pub_dtop = dtop['Object'].unique()
    distinct_pub_dtop = list(set(list(distinct_pub_dtop)))

    distinct_pub_ptod = ptod['Subject'].unique()
    distinct_pub_ptod = list(set(list(distinct_pub_ptod)))
    distinct_pubs = list(set(distinct_pub_ptod + distinct_pub_dtop))

    distinct_data_dtop = dtop['Subject'].unique()
    distinct_data_dtop = list(set(list(distinct_data_dtop)))

    distinct_data_ptod = ptod['Object'].unique()
    distinct_data_ptod = list(set(list(distinct_data_ptod)))
    distinct_data = list(set(distinct_data_dtop + distinct_data_ptod))
    print(len(distinct_data))
    print(len(distinct_pubs))

    mask0 = (datasets.iloc[:, 0].isin(distinct_data))
    final_df_datasets = datasets[mask0]
    # Open the file for writing
    with open(titles, 'w') as file:
        # Iterate through the DataFrame and write titles to the file
        for title in final_df_datasets['Object']:
            file.write(title + '\n')



if __name__ == '__main__':
    create_dataframe()
    create_titles_txt()


