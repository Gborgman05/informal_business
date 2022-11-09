def rm_data(count, identifier, in_name, out_name):
    """removes *count* rows that contain identifier and saves to out_name"""
    with open(in_name, "r") as f:
        lines = f.readlines()
    with open(out_name, "w") as f:
        for line in lines:
            if count > 0 and identifier in line:
                count -= 1
            else:
                f.write(line)


    

def count_rows(identifier, in_name):
    """counts the number of rows containing identifier"""
    with open(in_name, "r") as f:
        lines = f.readlines()
    return len([1 for line in lines if identifier in line])


if __name__ == "__main__":
    print(count_rows("Not Informal", "80_20.manifest"))
    print(count_rows('"Informal"', "80_20.manifest"))

    # rm_data(830,"Not Informal","merged3.manifest", "80_20.manifest" )


