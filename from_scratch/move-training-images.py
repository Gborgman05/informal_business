import boto3
import json
import os


MANIFEST_FILE = 'DataCleaning/testing_manifest_with_validation.json'
INPUT_IMAGE_BUCKET  = 'dxhub-svvsd-unlabeled-images'
OUTPUT_IMAGE_BUCKET = 'dxhub-svvsd-labeled-images'
OUTPUT_IMAGE_PATH = '/Users/dkraker/Documents/workspace/stvrain/images-for-training/testing/'


def main(): 
    s3 = boto3.client('s3')

    #split training data into train and validation for pytorch ML model
    file = open(MANIFEST_FILE, 'r')
    lines = file.readlines()
    # Go through each line grab json object push into list
    # GOAL: break training into 80/20
    data = {}
    i=0
    for index, line in enumerate(lines):
        i+=1
        #print("Line {}: {}".format(index, line.strip()))
        data = json.loads(line)
        label = data["st-vrain-labeling4-clone-metadata"]["class-name"]
        # grab key
        s3_file = data["source-ref"].rpartition('/')[-1]
        print("Downloading ", s3_file)
        s3.download_file(INPUT_IMAGE_BUCKET, s3_file , OUTPUT_IMAGE_PATH + "/"+ label + "/" + s3_file)

    
    # positive_entries = list(filter(lambda entry: entry['st-vrain-labeling4-clone-metadata']['class-name'] == "Fight", lines))

    # negative_entries = list(filter(lambda entry: entry['st-vrain-labeling4-clone-metadata']['class-name'] == "No Fight",
    #                                lines))

    # target_num_neg_entries = ((len(positive_entries) * 100) / 20) - len(positive_entries)

    # while len(negative_entries) > target_num_neg_entries:
    #     negative_entries.pop(random.randint(0, len(negative_entries) - 1))

    # for entry in positive_entries:
    #     print(entry)

    # for entry in negative_entries:
    #     print(entry)

    
    


    file.close()
    
######
    # valid_entries = list(filter(lambda entry: 'class-name' in entry['st-vrain-labeling4-clone-metadata'].keys(),
    #                             entries))
    
main()