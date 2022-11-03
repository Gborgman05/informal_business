import ast
from pprint import pprint
def merge_manifests(man_1, man_2):
    """incomplete"""
    output_name = "merged.manifest"
    rel_path = "./downloads/"
    with open(rel_path + man_1, "r") as f1:
        f1_lines = f1.readlines()
    print(f1_lines[0])
    dicts = [ast.literal_eval(line) for line in f1_lines]


if __name__ == "__main__":
    merge_manifests("dxdub-labeling-clone1.manifest", "hyderabad_10_30.manifest")