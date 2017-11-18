README.md

This python utility is to extract text form all the PDF files in the input_dir.

Where this was used?

We wanted to find the error count send by pagerduty email (Gmail).
1. Label the alerts email
2. Download the .mbox archive using gmail export label.
3. Extract the downloaded archive and add the .mbox file to Apple mail application.
4. Using Apple mail, select the email and export as pdf to the input folder
Follow the below to run the utility

## Installing dependencies
	virtualenv virt_env
	pip install -r requirenements.pip

## Activate virtual env
	Ensure the virtual env is activated before executing below commands
	source virt_env/bin/activate

## Run
	Update PATTERN and input_dir as needed.
	$ python extract_matching_text.py > l.log

	Manually remove not required info from each line. Tip - use sublime column cmd+atl+drag.
	Run below to count num of duplicate lines and sort by count
	$ sort l.log | uniq -c | sort -bgr > l-count.log

