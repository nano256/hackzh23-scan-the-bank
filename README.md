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

The `files` directory is where the files belong which the crawler has to label. We give you a few examples of files along with the corresponding labels so that you can examine their structure. You can download a ZIP file of them [here](https://drive.google.com/file/d/1Od4RSU7EdwOr6O2utblhjgLFGO-KBtHi/view?usp=sharing). Then create a `files` folder in the root directory of the repo and place the unzipped files in there. The labels can be found among the files in `labels.csv`. Don't worry about the naming of the other files, the names are randomized.

## Definition of Sensitive Data

Data that allows identification of a person only when combined with other pieces of information, including Customer identifiers, career data, and Personal IDs.

There are three kind of sensitive data: Direct, Indirect and Potential Indirect:

- Direct
  - Full Name
  - Email Address
  - Company name
  - RSA private key
- Indirect
  - Address (street, city and country)
  - Phone number
  - IBAN or any other kind of bank account number
- Potential Indirect
  - Nationality
  - Age
  - Gender
  - Professional qualification

The combination of one direct field plus any other (direct, indirect, potential indirect) is classified as sensitive data, except for RSA private keys which are always classified as sensitive. Otherwise, it is classified as **NON**-sensitive data.

### Examples

- Sensitive data: notice that in the following example only by having the full name of a person and its bank account we can already classify it as sensitive.
```
Customer Due Diligence (CDD) File:

Client Information:

    Client Name: Dr. Emma Müller
    Client ID/Account Number: CH6372246126343118257
    Client Type: Individual
    Client Nationality: Swiss
    Client Date of Birth: July 10, 1985
    Client Occupation: Medical Doctor
    Source of Wealth: Employment income, investment income

Client Background:

    Background Check: Client's background has been checked through available public records and KYC due diligence. No adverse information found.

Risk Assessment:

    Risk Category: Low to Moderate
    Risk Factors:
        Swiss nationality and residency provide lower jurisdictional risk.
        Stable employment income and investment income.
        No previous history of suspicious or high-risk transactions.
        No adverse findings in background checks.
```

- Non-sensitive data: notice that in the following example, only general information about people is mentioned, but we can't point someone in particular.
```
List of new customers that hired our Internet service:

| Phone Number   | IBAN     | Gender | Age |
|----------------|----------|--------|-----|
| +41 701562289  | CH123456 | Female | 27  |
| +58 4552226986 | 45612389 | Male   | 31  |
```

### Other Examples

- CV document with name and contact information given
```
     John Doe
     +41 76 999 88 88
     john.doe@gmail.com
```
- Email where name and IBAN of client is mentioned
```
    John Doe
    CH0001234567890123456
```
- CSV extract from system with phone, address and bank client number
```
    0770001122, "Bahnhofstrasse 1, Zürich 8001", JB-0000-1111-BANK, ...
```
- File with RSA private key
```
-----BEGIN RSA PRIVATE KEY-----
MIIEpAIBAAKCAQEAp78xAkQR1qqZMv7RUwDho3LstnZIiSPdxepjlzG/q7jRjYXY
F7wA/HypQoMXnoT/tCq0yAYrLu3q2sdBtVnzsUfIytMHJsrjbbkskWmvDsL5Vg4z
fuKZbvTZN2Li50LVa976I7gu0tGI7U18gCjjS4Pdxpx9QhdXGDxm193FNzx/KJaj
/6uKsOupaLquKh2yr+8tNYGFNL6n4nExzlRjhfku+md78VWtqblOagh1uaPEzy8V
Xrzyh/tDBnchfomqsv98L6JaNSXVkm2fgqVP55puMAm1j3rM/340dc3v7loCs2oz
UiSX36hozSs0Mryv3B9CKdX8oY/Zaxg9mZZM9QIDAQABAoIBABV1yf8MdszD+//w
ZhasmvFGa16ncL2suztN8mo+GNOO/C4TFLNqn6StjRjffQbQZIcn3INneKBTGzPc
gH1DMgA42wkJqNVPaPuZUEiVIOpuSqg1/mQJ+M+fXuetTLKB1BxuBQnLTyA04sPb
ISWjNXrsdpOpYwPwyPlmhtCwhEG91BtH4hRWo7d2oWb0ftzID/SakfY7QuSbqszG
nCgfszxp6obYgrq4F/j2PLk8Bp7iBv0n+mFusB+qL15UMp+diUlnH6K355gGpNGn
2lAKU4zvPCd5uHXoyc1zKnDSzHdITpsJKOkDIOMwsxO495DIR5pf8o1TTSK3xhKT
ykUd5OECgYEA4k1vqYm2QdrY+JtBTCIrLRxiMImqvIq0N1RExzjllGH2Si3XGpBF
01zn+UM/J2uqjqUYLMHbP1f4tTqKth4JvXYe8TzqcaZOMSERXZxDpKxcbv1jQp07
capCjjS3Jsitt4NgShlt2jZCjlq1XJHz9XmL1w5+07WCdkyEYj4LghUCgYEAvcKY
lwWYlVO1IAC4U1f4XJhte2vu7pc6975xJjB2j7BOzTwKWf+RANq++fLwykAPnJ0g
D1bvYJGMGTBebsmByNvrwUeR0Ol1VkiILFDokBY8DDLcMJfYe674xO7c3scSdFIs
tJ1jl/8iE4BQQxkg9TvKCY0//HUJJE0rDECJt2ECgYAzyQ6VWEsZtM/TzAtcNbF1
qDob61TjwkXNJ355rF503xnyDZ1cmckwveDjnGzWQ4ALFmJ6032teB8UsanOVP9b
mK0p/QuVKD5aZbvIlRqxkzOvvlI5iytwLkr+qbeDq4Z9KRYevsTxm1sNolpALbIK
6V6DvvBs1+tb0NS2eoY9pQKBgQC308v+gW1PO8g7OHdYReBT01Y8OlM8z0RQvCzg
0hIJIMM2DvP4O5w9N6vKd47MX0LAdXaZZZ5/7n/J5xGUQaF485NvqeWYfJEvBRTl
2XtyGhgRuTOV34PYTaixHrTZHADErtagIdhZZs+cFLGsTque5kzS9AMIjlhM0nTh
aaQAAQKBgQCj+zWabCXeE+GvT4NWev8IrbXne+PoNHE6s5Td0JaBBoDFtMetaX6j
zyOOOvH+51WXCZDdtqytF2o4UA/KgPl0KuaUSNFSG6UDvVQDAsVCBNBjrupcymzE
nVNEBUKeMqIZUEpgIdIq+SkFV1dUzTkGuSz6iuDvCP8Hx3S2ZB4Omw==
-----END RSA PRIVATE KEY-----
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

| True Label | Classification   |  Score |
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
