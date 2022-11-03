import ast
import json
from pprint import pprint
def merge_manifests(man_1, man_2):
    """incomplete"""
    # output_name = "merged.manifest"
    # rel_path = "./downloads/"
    rel_path = ""
    with open(rel_path + man_1, "r") as f1:
        f1_lines = f1.readlines()
    # print(f1_lines[0])
    # dicts = [ast.literal_eval(line) for line in f1_lines]
    objs = []
    for st in f1_lines:
        print(st)
        i = json.loads(st)
        objs.append(i)
    
    pprint(objs)


if __name__ == "__main__":
    merge_manifests("merged.manifest", "hyderabad_10_30.manifest")