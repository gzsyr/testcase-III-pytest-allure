import yaml


def replace():
    """替换字符串"""
    _params = {"name": "12344"}
    ss = "xxxxxxxxxxxx ${name} lllllllll"
    for key, value in _params.items():
        ss = ss.replace(f'${{{key}}}', value)
    print(ss)

def yaml_load(path, name):
    with open(path, encoding="utf-8") as f:
        steps = yaml.safe_load(f)[name]
        print(steps)
    for step in steps:
        # element = None
        # if "by" in step.keys():
        # element = self.find(step["by"], step["locator"])
        if "action" in step.keys():
            action = step["action"]
            if "click" == action:
                self.find(step["by"], step["locator"]).click()
            if "send" == action:
                value = step["value"]
                self.find(step["by"], step["locator"]).send_keys(value)
                print(f"send({value})")