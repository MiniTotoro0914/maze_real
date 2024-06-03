import os
import getpass
from openai import OpenAI

API_KEY = 
os.environ["OPENAI_API_KEY"] = API_KEY
# os.environ['REQUESTS_CA_BUNDLE'] = 'Zscaler Root CA.crt'

# API_MODEL = 'gpt-3.5-turbo'


client = OpenAI()
client.api_key = API_KEY
response = client.images.generate(
    # API_KEY =API_KEY,
    model="dall-e-3",
    prompt="3次元を猫で表現した画像。上段にテキストでタイトル付与をする。",
    size="1024x1024",
    quality="standard",
    n=1,
)

image_url = response.data[0].url
print("end")
print(image_url)

# API_MODEL = "gpt-3.5-turbo"
# # API_MODEL =  'gpt-4-1106-preview'
# BASE_TXT = "以下のAとBの文章の類似度を10点満点で評価して、理由も述べてください。 \
# 以下のフォーマットで出力をお願いします。\
# 点数： \
# 理由：\
# A【{question}】\
# B【{answer}】"


# def query_gpt_chat(
#     model: str = API_MODEL, input_str: str = "test", filename: str = "test"
# ):
#     client = OpenAI(
#         # This is the default and can be omitted
#         api_key=API_KEY,
#     )
#     try:
#         response = client.chat.completions.create(
#             model=model,
#             temperature=0,
#             messages=[
#                 # {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": input_str}
#             ],
#         )
#         # result = response.choices[0]["message"]["content"]
#         # in_token_cnt = len(encoding.encode(prompt))
#         # out_token_cnt = len(encoding.encode(result))
#         # print(result)
#     except AttributeError as e:
#         error_message = f"Error: {e}"
#         print(error_message)
#         result = error_message
#     return response  # ,in_token_cnt,out_token_cnt


# def create_calc_message(base_txt: str, result_txt: str, base: str = BASE_TXT):
#     formatted_text = base.format(question=base_txt, answer=result_txt)
#     return formatted_text


# tmp = query_gpt_chat(input_str="A: これはペンです。B: これは鉛筆です。")
# print(tmp)
