import requests
from requests.structures import CaseInsensitiveDict
from time import sleep


url = "https://replicate.com/api/models/stability-ai/stable-diffusion/versions/a9758cbfbd5f3c2094457d996681af52552901775aa2d6dd0b17fd15df959bef/predictions"

headers = CaseInsensitiveDict()
headers["x-csrftoken"] = "wS1EI34eCgHhS467ioCS9x791H1XGlPV7tIun1plnKUtsZXlFP0ev6lqYMknFAJ5"
headers["Content-Type"] = "application/json"
headers["cookie"] = "replicate_anonymous_id=29a142f6-b258-403a-8427-417fbdbd1cfb; rl_page_init_referrer=RudderEncrypt%3AU2FsdGVkX19XDtKPT3923waebRD%2Boq3WgQtdbJOMBTBCk3tRjwB3FS%2BAVvLZ378U; rl_page_init_referring_domain=RudderEncrypt%3AU2FsdGVkX19dYJd9Sa3JliQ%2Bz1pOSoe0I9YY8dQT0JGnykCb90aIlg0eQS8txAaL; csrftoken=wS1EI34eCgHhS467ioCS9x791H1XGlPV7tIun1plnKUtsZXlFP0ev6lqYMknFAJ5; sessionid=n4a1u492hhe5qmeznf6rwfhdarmkadr5; rl_user_id=RudderEncrypt%3AU2FsdGVkX19tDmu%2FqR7IfWwgWfDttklVESrSnz6w8Lk%3D; rl_group_id=RudderEncrypt%3AU2FsdGVkX19trQY0UUYUnbwqRoeiIXo%2Blesk4BgwlU8%3D; rl_trait=RudderEncrypt%3AU2FsdGVkX1%2BwozpvaoN1Kn%2FxZpHMPfHF16W3KyMiXi4%3D; rl_group_trait=RudderEncrypt%3AU2FsdGVkX1%2FIuaaxxQR7LaHaK6Ldb4EVirgTGNzXOsI%3D; rl_anonymous_id=RudderEncrypt%3AU2FsdGVkX1%2BzHTdUuWYG%2BNfyRwwMPxKrD4Tsjt1nQupHB0QdSuVpGQFSM897jqCXEohJwTrHSebsXjyerNv%2FGQ%3D%3D; rl_session=RudderEncrypt%3AU2FsdGVkX19SQLQTbljYhIVsiVz4SM4Dvkhoi4zXHp8UVtb2XrRJYyVqcQqjBYGEglIdJ8alHMfhknjIqLfqCo4Ebw69yXvjm%2FwRNjS9Gl8cyQkN8EoMmZw40V2pMh1SJFm4YpGq1lF%2Bz1wbsrWkLw%3D%3D"

prompt = "A little baby"
width = 512
height = 512
num_outputs = "1"
steps = 50

def gen_image(prompt):
    data = '{"inputs":{"width":512,"height":512,"num_outputs":"1","guidance_scale":7.5,"prompt_strength":0.8,"num_inference_steps":50,"prompt":"'+prompt+'"}}'
    
    resp = requests.post(url, headers=headers, data=data)
    
    uuid = resp.json()['uuid']
    
    url2 = f'https://replicate.com/api/models/stability-ai/stable-diffusion/versions/a9758cbfbd5f3c2094457d996681af52552901775aa2d6dd0b17fd15df959bef/predictions/{uuid}'
    
    while True:
        res = requests.get(url2,headers=headers).json()
        try:
            output = res['prediction']['output'][0]
            return output
        except:
            continue
    
