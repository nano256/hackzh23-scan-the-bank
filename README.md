<p align="center">
  <img src="./logo_hack_black.jpg" width="300" height="330">
</p>

# HackZurich 2023 - Scan the Bank Workshop
Welcome to the Scan the Bank Workshop. This README leads you through this challenge and contains all the relevant information. In case something is unclear don't hesitate to get in touch with us.

## Motivation
With the General Data Protection Regulation (GDPR) of the EU coming into effect, banks face the challenge to ensure compliance. GDPR Compliance means an organization that falls within the scope of the GDPR meets the requirements for properly handling personal data as defined in the law. The GDPR outlines certain obligations organizations must follow which limit how personal data can be used. Under these falls also the need of deleting personal information that does no longer need to be saved. To fulfill the requirements, organization must check vast amounts of data that was created before the initialization of GDPR and decide whether they contain any personal data or not. Also, in case that sensitive data is saved in wrong locations, we want a possibility to detect such data protection violations.

These tasks are not tractable solely by human labor and require an automated solution. A possible approach is a file crawler that labels documents that clearly aren't complying, as well as flagging uncertain cases for further human review.

## Your Task
Your challenge is building a fast and accurate data crawler that classifies whether a file is containing sensitive content or not and in doubt labels the document for further review. The files are a mix of different media and file types for which you have to find out approaches to identify their content. Below, you will find further details about the general structure of the challenge.

## Repo Structure
The general repo structure functions as boilerplate code to give you a jump-start. But it is also necessary to run your solution properly in the evaluation environment (more about this later). We recommend forking this repo and implementing your solution in the general project structure. Below some further explanations about the content of the repo.

The `app` directory contains the heart of your crawler. The `crawler.py` must contain your crawler. If you want to split up your code feel free to put more files in there but make sure that executing `crawler.py` is starting your algorithm. Put all packages that your solution needs in the `requirements.txt` file. [Here](https://pip.pypa.io/en/stable/reference/requirements-file-format/) you can find an explanation of the syntax of pip requirements files.

The `files` directory is where the files belong which the crawler has to label. We give you a few examples of files along with the corresponding labels so that you can examine their structure. You can download a ZIP file of them [here](https://drive.google.com/file/d/1KDqF4_NIhvvxdjyBgxTomzunPPWQxMDB/view?usp=sharing). Then create a `files` folder in the root directory of the repo and place the unzipped files in there. The labels can be found among the files in `labels.csv`. Don't worry about the naming of the other files, the names are randomized.

## Definition of CID (Client Identifying Data)

Data that allows identification of a client only when combined with other pieces of information, including Customer identifiers, career data, and Personal IDs.

There are three kind of CID: Direct CID, Indirect CID and Potential Indirect CID, but what makes it CID is the combination of different fields. In this challenge we will focus on the following ones:

1. Combination of at least three of following values:
- Full Name
- Address (street, city and country)
- Phone number
- Email Address
- IBAN or any other kind of bank account number
- Bank client number, with default format: JB-####-####-BANK
- Company name
2. One of following pairs:
  - Full Name + IBAN
  - Full Name + bank client number, with default format: JB-####-####-BANK
3. Private RSA keys

Examples:
- cv document with name and contact information given, e.g.
```
     John Doe
     +41 76 999 88 88
     john.doe@gmail.com
```
- email where name and IBAN of client is mentioned, e.g.
```
    John Doe
    CH0001234567890123456
```
- csv extract from system with phone, address and bank client number, e.g.:
```
    0770001122, "Bahnhofstrasse 1, Zürich 8001", JB-0000-1111-BANK, ...
```

## Tips
### Analyze The Sample Data
Before you start building your awesome crawler, analyze the sample data properly and ask yourself fundamental questions about the problem structure. What file types exist? How does the file content look like when you open them? Can you identify the sensitive content? Which file types should you prioritize?

### Handy Tools & Concepts
There are many tools out there that can do a lot of the heavy lifting for you. Already the built-in regex library of Python goes a long way. Take also a look at tools like [nltk](https://www.nltk.org/) that can do things like [Named Entity Recognition (NER)](https://medium.com/mysuperai/what-is-named-entity-recognition-ner-and-how-can-i-use-it-2b68cf6f545d). You can also try out using [pretrained Machine Learning models](https://huggingface.co/learn/nlp-course/chapter4/2?fw=pt), but be careful to stay within the Docker image size limits (see "Hand-In").

### Reuse & Chain Code
Sometimes you can restructure a specific file type so that you can use a classifier that you built for another file type. Try to modularize your code and reuse features that you already implemented. So you can build pipelines for different data types without reinventing the wheel. Per example for audio files you could build a speech-to-text module and feed its output in your already existing text classifier. But beware, errors tend to compound when chaining estimators. So choose wisely whether you give something a `false` instead of a `review` label.

### Check If Your Solution Runs Correctly
We check your solutions within a Docker image to ensure that your solution will also run on our hardware. We advise you to check your solution within Docker as well. [Install Docker](https://docs.docker.com/engine/install/) on your machine then go to the root directory of your local copy of this repo and run the command
```
docker build -t crawler .
```
This creates a Docker image from your `Dockerfile`. Afterwards you can run the container by entering following command in your terminal while being in the root directory of the repo.
```
docker run -v ./files:/files -v ./results:/results --network none crawler
```
The `-v` flag mounts the directories of your OS into the Docker container so that you don't have to copy all the files into it. Make sure that you already downloaded the sample files and copied them in the `files` directory, otherwise the container will complain if you launch it without `files` in place.

## Hand-In
Here some important points that you have to consider when handing in the solution:

- We run the evaluation without internet connection so that no web APIs can be used for the solution. 
- If you need an ML model or other downloadable content make sure to modify your `Dockerfile` so that it is downloaded in the `/app` directory when the image gets built. Also make sure that your Docker image is not bigger than 5GB.
- Your crawler must be activated by executing the `crawler.py` script, but you are allowed to add other Python files to the `app` directory.
- Make sure that your crawler returns its flags as a pickeled dictionary in directory `results`. The dictionary must have the filename, without path, as key and the corresponding flag, i.e. `'true'`, `'false'` or `'review'`, as value. Use the given boilerplate code as reference.
- To hand in your solution, fork this repo and commit your solution to your fork. If you want to keep your code private, you can add us as a collaborator in your repo (GitHub username: nano256).
- We will run all solutions with the evaluation dataset on identical hardware and later we will announce the scores of the individual teams.

## Rating System
The rating consists of two parts: the performance, i.e. how well the crawler classifies the files, and efficiency, i.e. how quick the crawler works through the files. 

80% of the total score are determined by the performance. Below we show the points which will be given for each possible configuration of classification and label. 

| Classification | Label   |  Score |
|----------------|---------|-------:|
| true           | true    |     20 |
| true           | false   |    -20 |
| true           | review  |    -10 |
| false          | false   |      2 |
| false          | true    |     -2 |
| false          | review  |     -1 |

The other 20% of the total score are determined by the efficiency of the solution. We will run all solutions on the same hardware and measure the time it takes for labeling all the data. The fastest solution will receive the maximum amount of points while the slowest solution will receive no points at all. The other teams will be graded by linearly interpolating between the slowest and fastest team.

Both parts of the score will be normalized and summed up to reveal the overall winner of the challenge.

## How to Reach Out to Us
During the challenge, we will be active on the HackZurich Discord server ([join here](https://discord.com/invite/uMwgYS8qhC)). Send a message in the corresponding channel or DM us. We will make it clear which accounts belong to our team in the challenge channel.
