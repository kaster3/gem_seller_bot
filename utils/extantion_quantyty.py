def find_quantity(string: str) -> int:
    result = 0
    if string.find("гемов"):
        result = int(string.split()[0])
    return result
