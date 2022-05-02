import os
import re
import shutil

import requests

from yamlUtils import YamlUtils


def get_content():
    # proxies = {
    #     "http": "http://localhost:1080",
    #     "https": "http://localhost:1080",
    # }
    proxies = {}

    pawdroid = os.path.join("pawdroid")
    yamlUtils = YamlUtils(pawdroid)
    yamlUtils.clone_repo("https://github.com/Pawdroid/Free-servers.git")
    with open(os.path.join(pawdroid, "README.md"), "r", encoding='utf-8') as f:
        content = f.read()
        urls = re.findall(
            r"https?://shadowshare\.v2cross\.com/publicserver/servers/temp/\w+", content
        )
        if len(urls) > 0:
            url = urls[0]
            url = "https://subsc.ednovas.xyz/sub?target=clash&new_name=true&url={}&insert=false&config=https%3A%2F%2Fraw.githubusercontent.com%2FACL4SSR%2FACL4SSR%2Fmaster%2FClash%2Fconfig%2FACL4SSR_Online.ini".format(
                url
            )
            file = requests.get(url, proxies=proxies)
            with open("sub/pawdroid.yaml", "wb") as f:
                f.write(file.content)
    shutil.rmtree(pawdroid)


if __name__ == '__main__':
    get_content()
