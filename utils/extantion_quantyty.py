def find_quantity(string: str) -> int:
    if string.find("гемов") > 0:
        string = string.split()[1]
    return int(string)
