The source code and data are available [here](https://github.com/xuwang0010/datarecommend).

We did not rely on the file `PaperAuthorAffiliations.hdt` provided in the original repository since it was not correct. We had to contact the authors to get the original file.

In order to help in replication we provide the Dockerfile we instantiated in order to create a container with all the dependencies ready to use.

In order to run the code, the command to be run is the following:

first build the image

`docker build -t datarecommendimage .`


Create and run container

`docker run --rm -ti --name testimage_datarecommend -v path/to/your/data/folder/where/all/the/files/are:/code/data datarecommendimage:latest python3 Recommendation.py -data=/code/data -random=1 -hop=3 -out=/path/where/you/want/to/store/results`

