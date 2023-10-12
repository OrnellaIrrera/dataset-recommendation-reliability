The source code and data used to replicate the bi-encoder retriever are available [here](https://github.com/viswavi/datafinder/tree/main).

We provided two folders:
- code : scripts to produce test and qrels files
- data : test and qrels generated relying on the original qrels provided for the fullsentence queries. We mapped the QueryID of the full sentence queries to the QueryID of the keyphrase queries..
- results : our replication runs

To run the keyphrase part, remember to use these qrels and test files.
To evaluate the runs:

`trec_eval   -m map -m P -m recall  your_qrels.qrels your_run.trec `

