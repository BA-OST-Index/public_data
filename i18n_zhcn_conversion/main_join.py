import json
import os
from collections import OrderedDict

BASE_DIR = "./original"
all_json_files = OrderedDict({
    "cf": ["auto_stu_first.json", "char_first.json"],
    "cl": ["auto_stu_last.json"],
    "sn": ["auto_l10n_school_short.json", "auto_l10n_school_long.json"],
    "cn": ["auto_l10n_club.json"],
    "et": ["etc.json"],
    "ra": ["auto_raid_total.json", "auto_raid_world.json"]
})

result = OrderedDict()
for (tag_name, files) in all_json_files.items():
    for file in sorted(files, key=lambda x: x.encode("utf8")):
        path = os.path.join(BASE_DIR, file)

        with open(path, mode="r", encoding="utf8") as f:
            content = json.load(f)

        content2 = [[value.encode("gbk") for value in entry] for entry in content]
        content2.sort(key=lambda x: tuple(x))
        content2 = [[value.decode("gbk") for value in entry] for entry in content2]

        if tag_name not in result.keys():
            result[tag_name] = []
        result[tag_name].extend(content2)

with open("./export/i18n_zhcn_all.json", mode="w", encoding="utf8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)
with open("./export/i18n_zhcn_all_min.json", mode="w", encoding="utf8") as f:
    json.dump(result, f, ensure_ascii=False)
