from aip import AipSpeech
import uuid


def get_map3(text, app_id, api_key, secret_key, mp3_dir):
    client = AipSpeech(app_id, api_key, secret_key)
    result = client.synthesis(text, 'zh', 1, {
        'vol': 5
    })
    path = mp3_dir + '/' + str(uuid.uuid1()) + '.mp3'
    if not isinstance(result, dict):
        with open(path, 'wb') as f:
            f.write(result)
    return path
