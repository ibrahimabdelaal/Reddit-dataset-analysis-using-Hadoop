# Reddit-dataset-analysis-using-Hadoop

# Dataset Description

This repository contains a dataset for analysis and processing. The dataset is provided as a compressed bzip2 file, which, upon decompression, expands to a size of 31.6 GB. To facilitate easier handling, we have created a sample file consisting of 3925 lines and saved it as a text file.

# Data Analysis

During the analysis of the dataset, we observed some interesting patterns and encountered specific data issues. One notable observation is that the "downs" field consistently contains the value "zero" across all the sampled data, indicating a common occurrence. Additionally, we noticed the presence of noise in the dataset, with some "ups" values being represented as negative numbers. These observations suggest the presence of data problems and noise that need to be addressed during further analysis.

# Challenges and Solutions

Throughout the project, we faced various challenges and devised effective solutions to overcome them. One significant challenge was representing the rate of reply and the controversiality of comments. To address this, we decided to utilize the "score" field as a measure of controversiality, as we noticed a correlation between the "score" and "ups" values.

Optimizations were also implemented to improve the efficiency of the code. For example, when determining the top subreddits with the most topics, we combined the two map-reduce jobs into a single job. This approach was more efficient, considering that we were working with a sample from the large dataset. Additionally, we incorporated a combiner to reduce the workload in the reducer function.

# Code Structure and Pipeline
The code is organized into different tasks, each serving a specific purpose within the pipeline.

* Task 1: Most discussed/used topics associated with every subreddit and username (with a focus on top subreddits)

Mapper: Generates the output by mapping the subreddit_id, link_id, and '1'.

Combiner: Calculates the occurrence count for each topic based on the link_id and subreddit_id.

Reducer: Determines the five most discussed subreddits and identifies the two most discussed topics within each subreddit.

sample out :
![image](https://github.com/ibrahimabdelaal/Reddit-dataset-analysis-using-Hadoop/assets/49596777/944d9859-b3c5-46f6-8620-ca5bd29874d1)


* Task 2: Rate of replies compared to the controversiality of comment/post

Mapper: Produces the output by mapping the parent_id, controversiality score (contra), link_id, and '1'.

Reducer: Determines the main comment by checking the equality of parent_id and link_id. It calculates the number of replies for each link_id and presents the comments with their corresponding number of replies and scores.

sample out :

![image](https://github.com/ibrahimabdelaal/Reddit-dataset-analysis-using-Hadoop/assets/49596777/67cfd82d-f394-4693-a38c-b52d006df7dc)


* Task 3: Topics that yield the highest number of upvotes and/or lowest number of downvotes

Mapper: Generates the output by mapping the link_id, corresponding ups, and downs.

Reducer: Aggregates the upvotes and downvotes for each link_id and selects the two highest upvotes and lowest downvotes along with their link_id.

sample out :
![image](https://github.com/ibrahimabdelaal/Reddit-dataset-analysis-using-Hadoop/assets/49596777/585ed572-fa30-4924-9e8a-c13372cabc89)

* Task 4 (Creative/Innovative Requirement): Identifying the most active author on a subreddit

Mapper: Produces the output by mapping the subreddit_id and the author.

Reducer: Counts the occurrences of each author in each subreddit and determines the most active author based on their frequency.

result :
![image](https://github.com/ibrahimabdelaal/Reddit-dataset-analysis-using-Hadoop/assets/49596777/29cdc36f-fc76-4348-b03a-224dffee4151)


Please refer to the code files and comments within the code for a detailed understanding of the implementation.
