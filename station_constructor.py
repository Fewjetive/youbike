import json
def main():
    f = open("data\\2021-12-15\\1312.json", "r", encoding="utf-8")
    data = json.loads(f.read())
    concerned = open("concerned.txt", "w", encoding="utf-8")
    for item in data:
        if item["sna"].__contains__("臺大") or item["sna"].__contains__("公館"):
            concerned.writelines(item["sno"] + " " + item["sna"]+'\n')
    f.close()
    concerned.close()
if __name__ == '__main__':
    main()
    