import boto3
import cv2
from datetime import datetime
import glob
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import csv
import os

TEMP_DIRECTORY = './tmp/'
IMAGE_MODEL_ARN = "arn:aws:rekognition:us-west-2:099295524168:project/st-vrain-fight-detection-ratio-adjusted-1/version/st-vrain-fight-detection-ratio-adjusted-1.2022-05-01T14.51.16/1651441876871"
MIN_CONFIDENCE = 1
CONFIDENCE_LEVEL=50

# You will need an AWS Secret Key to run this code locally
# In the console under your IAM user create an Access key from the Security Credentials tab
# If you have the AWS cli installed you can create a default profile with your AWS Access key 
# OR a custom profile that lives in ~/.aws/credentials you can create an entry for this AWS account similar to
#[informalbus]
#region=us-east-1
#aws_access_key_id=AKIAROHTZOVEOXTZH5HJ
#aws_secret_access_key=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
# Lots of ways to do this so you can read more here:
#https://boto3.amazonaws.com/v1/documentation/api/latest/guide/credentials.html

session = boto3.Session(
    region_name='us-east-1',
    profile_name='informalbus'
)


model_client = session.client('rekognition')

def get_inference(photo, bucket):
    response = model_client.detect_custom_labels(Image={'S3Object': {'Bucket': bucket, 'Name': photo}},
                                                     MinConfidence=MIN_CONFIDENCE,
                                                     ProjectVersionArn=IMAGE_MODEL_ARN)
    print(response)
    labels = response['CustomLabels']
    for label in labels:
        if label["Name"] == "Fight" and label["Confidence"] > CONFIDENCE_LEVEL :
            return True
    return False



def detect_custom_labels_local_file(photo):
    retval = (False,0)
    with open(photo, 'rb') as image:
        response = model_client.detect_custom_labels(Image={'Bytes': image.read()},
                                                MinConfidence=MIN_CONFIDENCE,
                                                ProjectVersionArn=IMAGE_MODEL_ARN)
    #print(response)    
    labels = response['CustomLabels']
    for label in response['CustomLabels']:
        if label['Name'] == 'Fight' and label['Confidence']>CONFIDENCE_LEVEL:
            print (photo, '->', label['Name'] + ' : ' + str(label['Confidence']))
            retval = (True,label['Confidence'])
    return retval #len(response['CustomLabels'])


# This function will open the image and place a label with the confidence score
def label_image(f, text):
    image_font = ImageFont.truetype("DejaVuSansMono.ttf", 64)
    image = Image.open(f)
        
    draw = ImageDraw.Draw(image)
    draw.text((1000, 750 ), text, font=image_font, fill =(255, 0, 0))
    image.show()
    #image.save(f)



def main():
    
    inference_count = 0
    print(os.getcwd())
    # Open up a TXT file with files names to send to Custom Labels
    # file format is just 
    # testimage-1.jpg
    # testimage-2.jpg
    with open('images.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        counter = 0
        for f in csv_reader:
            image_file = TEMP_DIRECTORY + f[0]
            print (image_file)
            # If you want to store the test inages in a bucket you can use get_inference
            result = detect_custom_labels_local_file(image_file)
            if result[0]:
                inference_count += 1
                label_image(image_file, 'INFORMAL\n'+str(result[1]))
            else:
                inference_count = 0
                label_image(image_file, 'NOT INFORMAL')
            print(inference_count)
            if inference_count >= 3:
                print ('FOUND INFORMAL BUSINESSES')
            counter += 1
 


if __name__ == "__main__":
    main()