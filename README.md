# Tyler Jennings - Serif Health Take Home Submission
Solution took around 2 hours.

## Why Python
[Install Python 3](https://www.python.org/downloads/)
- Popular language with many libraries to take advantage of.
- Extremely common language to be used in the Data Engineering field. Including at Serif Health in Databricks.
- I'm familiar with using Python to work with json files.

## IJSON library:
Install this library: ```pip install ijson```
- First thing I noticed about this challenge was the very large json file.
- IJSON library loads json files iteratively. Vastly reducing memory usage.
- I am able to stream through the file on my small laptop with no issues.
- Takes less than 1 minute and 30 seconds to run.

## My solution
- Function that takes a json file as a parameter called parse_json
- Open json file in read mode as a binary file
- Create a IJSON parser with the file to parse the file line by line to save memory
- Iterate through the file checking for the correct New York PPO description
- Write the URLs to an output file.

## Tradeoffs
- I could have added a piece of code to the script that would parse through the file from the URL. Removing the need to download and unzip manually. This solution would potentially be more optimal for automation.
- Given more time I would have liked to look through the data more to confirm I wasn't missing any URLs, as well as use the Anthem EIN lookup tool more.
- Would have liked to parameterize the script to accept the json filename. Again would be useful for automation.
- Version control could have been better. i.e. More commits, created a separate branch and not working from the master branch. Thing I would absolutely do on the job but given 2 hours I wanted to focus on the challenge itself more.
- Definitely could have added more error checking and testing.

## Questions
Question: How do you handle the file size and format efficiently, when the uncompressed file will exceed memory limitations on most systems?  
Answer: I utilized IJSON library to parse the file iteratively.

Question: When you look at your output URL list, which segments of the URL are changing, which segments are repeating, and what might that mean?  
Answer: 1. there is 01_of_03, 02_of_03, etc... This suggests that the files have been broken up into parts. 2. There is the expires date, seems to be the same for the parts of the same files but different for each separate files. Suggest to me that each file has its own expiration. 3. Each file has a signature, some of the signatures are exactly the same for different files. A signature in a url usally indicated specified permission and time. The repeating signatures could be that they have the same permissions or expiration dates.

Question: Is the description field helpful? Complete? Is Highmark the same as Anthem?  
Answer: It seems the description field indicates the state and some plan info. I found this to be useful. From what I gather Highmark and Anthem are the same as they always have Anthem in the URL and this file is for Anthem.

Question: Anthem has an interactive MRF lookup system. This lookup can be used to gather additional information - but it requires you to input the EIN or name of an employer who offers an Anthem health plan: Anthem EIN lookup. How can you find a businesss likely to be in the Anthem NY PPO? How can you use this tool to confirm which underlying file(s) represent the Anthem NY PPO?  
Answer: You can manually look at the descriptions to see if a company is within Anthem NY PPO and then search the EIN or business name in the lookup tool to confirm it. Similarily once confirmed you can then look at there file names to find a pattern that matches with all NY Anthem PPO.

## Final thoughts
I found this to be a fun challenge. I enjoyed digging into the data and I found the set of constraints to be very interesting. I especially enjoyed coming up with a solution to the memory issues due to the filesize. I look forward to hearing back!