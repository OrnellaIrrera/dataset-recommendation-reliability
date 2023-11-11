The source code and data are available [here](https://github.com/xuwang0010/datarecommend).

We provided the Dockerfile useful to run the code without installing all the needed dependencies. The command to run the code is the same provided in the replicability section of this repository, in particular:



first build the image

`docker build -t datarecommendimage .`

Create and run container

`docker run --rm -ti --name testimage_datarecommend -v path/to/your/data/folder/where/all/the/files/are:/code/data datarecommendimage:latest python3 Recommendation.py -data=/code/data -random=1 -hop=3 -out=/path/where/you/want/to/store/results`

