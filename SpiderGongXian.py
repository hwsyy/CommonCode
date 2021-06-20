import json
import re

import requests

url_source = "https://cl.do56.xyz/index.php?u=558551&ext=25120"


def get_first():
    header = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
        "referer": "https://1024dasehn.github.io/"
    }
    res = requests.get(url_source, headers=header)
    # print(res.content.decode("gbk"))
    html = res.content.decode("gbk")
    cookies = res.cookies.get_dict()
    # cookie = requests.utils.dict_from_cookiejar(cookies)
    cookie_list = []
    for k, v in cookies.items():
        cookie_list.append(f"{k}={v}")
    print(cookie_list)
    u = re.search(r'u=(.*?)&', html).group(1)
    print(u)
    vcencode = re.search(r'vcencode=(.*?)"', html).group(1)
    print(vcencode)
    url = re.search(r'url" value="(.*?)"', html).group(1)
    print(url)
    ext = re.search(r'ext" value="(.*?)"', html).group(1)
    print(ext)
    adsaction = re.search(r'adsaction" value="(.*?)"', html).group(1)
    print(adsaction)
    needMap = {}
    if u and vcencode and url and ext and adsaction:
        needMap = {
            "u": u,
            "vcencode": vcencode,
            "url": url,
            "ext": ext,
            "adsaction": adsaction,
            "cookie": ";".join(cookie_list)
        }
        return needMap
    else:
        return needMap


def send_second(need):
    u = need.get("u")
    vcencode = need.get("vcencode")
    cookie = need.get("cookie")
    url = f"https://cl.do56.xyz/index.php?u={u}&vcencode={vcencode}"
    header = {
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.106 Safari/537.36",
        "referer": url_source,
        "cookie": cookie
    }
    form_data = {
        "url": need.get("url"),
        "ext": need.get("ext"),
        "adsaction": need.get("adsaction")
    }
    res = requests.post(url, headers=header, data=form_data)
    html = res.content.decode("gbk")
    print(html)


if __name__ == '__main__':
    need = get_first()
    send_second(need)
