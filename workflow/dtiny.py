import json
import sys
from workflow import Workflow, ICON_WEB, web


def main(wf):
    query = sys.argv[1]
    url = 'http://t.bdaily.club'
    params = json.dumps({"url": query})
    r = web.post(url, data=params)
    r.raise_for_status()

    result = r.json()
    if result["msg"] == "ok":
        data = result["data"]
        wf.add_item(title=data["tiny_url"], subtitle="tiny url")
        for url in data["hash_urls"]:
            wf.add_item(title=url, subtitle="hash url")
    else:
        wf.add_item(title=result["msg"])

    wf.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
