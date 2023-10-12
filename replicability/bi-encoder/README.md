The source code and data used to replicate the bi-encoder retriever are available [here](https://github.com/viswavi/datafinder/tree/main).

We provided two files:
- the testa data : this file contains the test query set except for thoe duplicated keyphrase queries which were excluded
- the qrels file : they have been generated relying on the original qrels provided for the fullsentence queries. We mapped the QueryID of the full sentence queries to the QueryID of the keyphrase queries.

To run the keyphrase part, remember to use these qrels and test files.

