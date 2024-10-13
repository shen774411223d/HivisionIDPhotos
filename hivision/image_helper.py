import requests
import base64


# 将一张网络图片转换成base64格式,注意,转换后的结果不带 'data:image/jpeg;base64'前缀
def image_to_base64(img_url: str, base64_prefix: bool = False):
    response = requests.get(img_url)
    if response.status_code == 200:
        image_data = response.content
        base64_encoded = base64.b64encode(image_data).decode("utf-8")
        if base64_prefix:
            return f"data:image/jpeg;base64,{base64_encoded}"
        else:
            return base64_encoded
    else:
        return None
