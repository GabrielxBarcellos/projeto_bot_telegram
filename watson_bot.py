import json
import watson_developer_cloud

assistant = watson_developer_cloud.AssistantV1(
    iam_apikey='c5aJ8E_FAgdrFWnCIrAvWdX4hB4QG722UuQyiRx2sUJt',
    version='2018-09-20',
    url='https://gateway.watsonplatform.net/assistant/api'
)

def mandar_msg_watson(mensagem):
    response = assistant.message(
    workspace_id='ce840347-0030-41f1-8f43-ac3d812ef0db',
        input={
            'text': mensagem
        }
    ).get_result()
    return response
'''json.dumps(response, indent=2)'''