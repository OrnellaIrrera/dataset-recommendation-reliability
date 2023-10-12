# dataset-recommendation-reliability
This repository contains the code and data to replicate and generalize the following three methods:

 - #### LinearSVM
   This method has been described in:
   
   Färber, M., & Leisinger, A. K. (2021, October). Recommending datasets for scientific problem descriptions. In Proceedings of the 30th ACM International Conference on Information & Knowledge Management (pp. 3014-3018).

 - #### Bi-Encoder
    This method has been described in:
   
    Viswanathan, V., Gao, L., Wu, T., Liu, P., & Neubig, G. (2023). DataFinder: Scientific Dataset Recommendation from Natural Language Descriptions. arXiv preprint arXiv:2305.16636.

 - #### Ensemble CN
     This method is the ensemble of: BERT, BM25, citation network embeddings, co-authors embeddings, n-hops walk. It is described in:
   
   Wang, X., van Harmelen, F., Cochez, M., & Huang, Z. (2022, July). Scientific item recommendation using a citation network. In International Conference on Knowledge Science, Engineering and Management (pp. 469-484). Cham: Springer International Publishing.



### Replicability
Replicability, same setup different team, consisted in running the three methods and investigate whether we were able to obtain the same results stated in the original papers.
We provide a folder for each method. The original code and data used to replicability purposes is provided in the original papers' repositories, in particular:

- [LinearSVM](https://github.com/michaelfaerber/datarec)
- [Bi-encoder](https://github.com/viswavi/datafinder/tree/main)
   In [bi-encoder folder](replicability/bi-encoder) it is possible to find the qrels file used to run keyphrase queries.
- [Ensemble CN](https://github.com/xuwang0010/datarecommend) The file PaperAuthorsAffiliations.hdt to run the experiments has been requested to the original authors and is different from the one provided in the repository.

### Generalizability
Generalizability allowed us to investigate whether the three methods above are generalizable with other unseen datasets they are never tested with. In the [generalizability](generalizability) folder the code -- if different from those in the original repositories -- and our data are provided together with the instructions to run each method.


