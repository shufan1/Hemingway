# Topic Modeling on Hemingway's The Sun Also Rises with AWS Comprehend


I broke down Hemingway's novel The Sun Also Rises into smaller chucks of text by grouping every 6 lines together in a python script. The script write each smaller chunk of texts as one line in an input text file ("inputSAR.txt"). This input file was uploaded to an S3 bucket (folder). AWS Comprehend suggested to have at least 1000 documents and each document with at least 3 lines for topic modeing with LDA. In boto3, Amazon Comprehend was called and NLP analysis job for topic modeling was created. The output is sent to a designated S3 bucket folder. The output includes two csv files, one lists the topic proportion for each text and another one gives the word proportion for each topic. Then I used Quicksights to visualize the results. 


The most popular topic is Topic 1, 2, 5 and 4. 
