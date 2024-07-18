import re
def same_symbol(row):
    if len(row) == 0:
        return True
    else:
        row = re.sub("[a-z\n]", "", row)

        while len(row) != 0:
            if "[]" in row:
                row = row.replace("[]", "")
            elif "()" in row:
                row = row.replace("()", "")
            elif "{}" in row:
                row = row.replace("{}", "")
            elif "<>" in row:
                row = row.replace("<>", "")
            else:
                break
        print(row)
        if len(row) == 0:
            return True




with open ("input.txt", 'r') as file_read:
    with open ("output.txt", 'w') as file_write:
        for row in file_read:
            if same_symbol(row):
                file_write.write("true" + '\n')
            else:
                file_write.write("false" + '\n')