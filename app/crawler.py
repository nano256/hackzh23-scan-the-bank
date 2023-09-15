'''
This is a simple crawler that you can use as a boilerplate for your own 
implementation. The crawler checks for `.txt` files that contain the word 
"hello". Try to modify this simple implementation so that it finds 
sensitive data and then expand your crawler from there.

You change the code however you want, just make sure that following 
things are satisfied:

- Grab the file from the directory "../files" relative to this script
- If you usePython packages, add a "requirements.txt" to your submission
- Save your labels as a pickled dictionary in the same directory as the crawler script. Use the filename as the key 
  and the value is a string that is "true" for a file containing sensitive 
  data, "false" for files with non-sensitive data and "review" when unsure 
  about the content of the file.
'''

import os
from pathlib import Path
import pickle


def save_dict_as_pickle(dictionary, filename):
    with open(filename, 'wb') as handle:
        pickle.dump(labels, handle, protocol=pickle.HIGHEST_PROTOCOL)


def classifier(file_path):
    # Check the data type
    if file_path.suffix == '.txt':
        # Open the file to read out the content
        with open(file_path) as f:
            file_content = f.read()
            # If the file contains the word "hello" label it as true
            if file_content.find('hello') != -1:
                return 'true'
            else:
                return 'false'
    else:
        # If it is not a `.txt` file the set the label to "review"
        return 'review'


if __name__ == "__main__":
    # Get the path of the directory where this script is in
    script_dir_path = Path(os.path.realpath(__file__)).parents[0]
    # Get the path containing the files that we want to label
    file_dir_path = script_dir_path.parents[0] / 'files'

    # Initialize the label dictionary
    labels = {}

    # Loop over all items in the file directory
    for file_name in os.listdir(file_dir_path):
        file_path = file_dir_path / file_name
        labels[file_name] = classifier(file_path)

    # Save the label dictionary as a Pickle file
    save_dict_as_pickle(labels, script_dir_path / 'crawler_labels.pkl')