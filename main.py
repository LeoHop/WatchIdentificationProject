
import io
import os

"""
Best images:

Apperal API:
https://www.thesun.co.uk/wp-content/uploads/2018/01/nintchdbpict000307453429.jpg
https://k8q7r7a2.stackpathcdn.com/wp-content/uploads/2021/02/Bell-and-Ross-official-partner-patrouille-de-france-1.jpg
https://i.ytimg.com/vi/CFE3MW39nZA/hqdefault.jpg?sqp=-oaymwEXCOADEI4CSFryq4qpAwkIARUAAIhCGAE=&rs=AOn4CLCWsCFU0SVLxzVcFKq9DUISUhz4jg

Logo API:
https://i.ytimg.com/vi/XoljX3k4p8c/maxresdefault.jpg
https://content.rolex.com/dam/watches/family-pages/oyster-perpetual/new-oyster-perpetual-41-m124300-0001-share.jpg
https://www.jaeger-lecoultre.com/content/dam/rcq/jlc/13/49/10/7/1349107.png

Both:
https://cdn.shopify.com/s/files/1/0195/2352/files/pasted_image_0_1_80b8a79b-7101-4ee0-8bc4-a3f2224af7d0.jpg
https://revolutionwatch.com/wp-content/uploads/2020/10/17-Patek-Philippe-24.jpg
https://static.patek.com/images/articles/thumbs/twitter/5327J_001.jpg
https://k8q7r7a2.stackpathcdn.com/wp-content/uploads/2019/10/Panerai-Luminor-Marina-Titanio-DLC-Bucherer-BLUE-PAM0102-8.jpg

Two sided images:
http://superwatchman.com/wp-content/uploads/2020/04/95644707_262648874865096_5718796065787979343_n.jpg
https://wpusa-aws-media.s3-accelerate.amazonaws.com/2015/10/Ed%20with%20watch.jpg
https://media.gq.com/photos/5f4019cec22d07d47bca406c/master/pass/wotw-biden.jpg
"""


myUrl = input("Please enter an image address: ")


import json




from clarifai_grpc.channel.clarifai_channel import ClarifaiChannel
from clarifai_grpc.grpc.api import resources_pb2, service_pb2, service_pb2_grpc
from clarifai_grpc.grpc.api.status import status_pb2, status_code_pb2

with open('clarifaiApiKey.json') as data_file:
    data = json.load(data_file)

apiKey = data['API key']


metadata = (('authorization', f'Key {apiKey}'),)
# print(metadata)

print("")

channel = ClarifaiChannel.get_grpc_channel()
stub = service_pb2_grpc.V2Stub(channel)

userDataObject = resources_pb2.UserAppIDSet(user_id='{Leo Hoplamazian}', app_id='{3d4743c512f84168a861187688fcc389}')

# Insert here the initialization code as outlined on this page:
# https://docs.clarifai.com/api-guide/api-overview/api-clients#client-installation-instructions

post_model_outputs_response = stub.PostModelOutputs(
    service_pb2.PostModelOutputsRequest(
        #user_app_id=userDataObject.app_id,  # The userDataObject is created in the overview and is required when using a PAT
        model_id="apparel-recognition",
        # version_id="{THE_MODEL_VERSION_ID}",  # This is optional. Defaults to the latest model version.
        inputs=[
            resources_pb2.Input(
                data=resources_pb2.Data(
                    image=resources_pb2.Image(
                        url=myUrl
                    )
                )
            )
        ]
    ),
    metadata=metadata
)



if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
    print("There was an error with your request!")
    print("\tCode: {}".format(post_model_outputs_response.outputs[0].status.code))
    print("\tDescription: {}".format(post_model_outputs_response.outputs[0].status.description))
    print("\tDetails: {}".format(post_model_outputs_response.outputs[0].status.details))
    raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)

# Since we have one input, one output will exist here.
output = post_model_outputs_response.outputs[0]


MenProb = 0
WomenProb = 0

for concept in output.data.concepts:
    if concept.name == "Men's Watch" and concept.value >= 0.50:
        # print("%s %.2f" % (concept.name, concept.value))
        MenProb = concept.value
    elif concept.name == "Women's Watch" and concept.value >= 0.50:
        # print("%s %.2f" % (concept.name, concept.value))
        WomenProb = concept.value


if MenProb >= WomenProb:
    print("Prediction: Men's Watch Detected")
elif MenProb < WomenProb:
    print("Prediction: Women's Watch Detected")
elif MenProb == 0 and WomenProb == 0:
    print("No watches detected, please try another image")



# Google Vision API for Logo Detetction

def detect_logos_uri(uri):
    # GOOGLE_APPLICATION_CREDENTIALS = "/Users/leohop/Desktop/Algo/finalAIProject/cred.json"

    """Detects logos in the file located in Google Cloud Storage or on the Web.
    """
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()
    image = vision.Image()
    image.source.image_uri = uri

    response = client.logo_detection(image=image)
    logos = response.logo_annotations

    printed = False

    for logo in logos:
        if printed == False:
            print("Brand:", logo.description)
            printed = True

    # for logo in logos:
    #     print(logo.description)


    if response.error.message:
        raise Exception(
            '{}\nFor more info on error messages, check: '
            'https://cloud.google.com/apis/design/errors'.format(
                response.error.message))

# detect_logos_uri("https://alexisperrier.com/assets/gcp/google_cloud_storage.png")

detect_logos_uri(myUrl)





# Trying to add a celebrity component into this:


# with open('clarifaiApiKey.json') as data_file:
#     data = json.load(data_file)
#
# apiKey = data['API key']
#
#
# metadata = (('authorization', f'Key {apiKey}'),)
# # print(metadata)
#
# channel = ClarifaiChannel.get_grpc_channel()
# stub = service_pb2_grpc.V2Stub(channel)
#
# userDataObject = resources_pb2.UserAppIDSet(user_id='{Leo Hoplamazian}', app_id='{3d4743c512f84168a861187688fcc389}')
#
#
# post_model_outputs_response = stub.PostModelOutputs(
#     service_pb2.PostModelOutputsRequest(
#         #user_app_id=userDataObject.app_id,  # The userDataObject is created in the overview and is required when using a PAT
#         model_id="celebrity-face-detection",
#         # version_id="{THE_MODEL_VERSION_ID}",  # This is optional. Defaults to the latest model version.
#         inputs=[
#             resources_pb2.Input(
#                 data=resources_pb2.Data(
#                     image=resources_pb2.Image(
#                         url=myUrl
#                     )
#                 )
#             )
#         ]
#     ),
#     metadata=metadata
# )
#
#
# if post_model_outputs_response.status.code != status_code_pb2.SUCCESS:
#     print("There was an error with your request!")
#     print("\tCode: {}".format(post_model_outputs_response.outputs[0].status.code))
#     print("\tDescription: {}".format(post_model_outputs_response.outputs[0].status.description))
#     print("\tDetails: {}".format(post_model_outputs_response.outputs[0].status.details))
#     raise Exception("Post model outputs failed, status: " + post_model_outputs_response.status.description)
#
# # Since we have one input, one output will exist here.
# output = post_model_outputs_response.outputs[0]
#
# printedCeleb = False
# # print(type(output.data))
# # print(output.data)
# for concept in output.data.concepts:
#
#     if printedCeleb == False:
#         print("Celebrity Seen: ", concept.name)
#         printedCeleb = True


