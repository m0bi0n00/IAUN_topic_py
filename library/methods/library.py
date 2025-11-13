
# 1️ capitalize
def my_capitalize(s: str) -> str:
    if not s:
        return ""
    first = s[0]
    rest = ""
    # lower-case the rest manually
    for ch in s[1:]:
        if 'A' <= ch <= 'Z':
            rest += chr(ord(ch) + 32)
        else:
            rest += ch
    # upper-case first letter manually
    if 'a' <= first <= 'z':
        first = chr(ord(first) - 32)
    return first + rest


# 2️ casefold (simple lowercase)
def my_casefold(s: str) -> str:
    result = ""
    for ch in s:
        if 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result


# 3️ count(substring)
def my_count(s: str, sub: str) -> int:
    count = 0
    for i in range(len(s) - len(sub) + 1):
        match = True
        for j in range(len(sub)):
            if s[i + j] != sub[j]:
                match = False
                break
        if match:
            count += 1
    return count


# 4️ endswith
def my_endswith(s: str, suffix: str) -> bool:
    if len(suffix) > len(s):
        return False
    return s[len(s) - len(suffix):] == suffix


# 5️ find
def my_find(s: str, sub: str) -> int:
    for i in range(len(s) - len(sub) + 1):
        match = True
        for j in range(len(sub)):
            if s[i + j] != sub[j]:
                match = False
                break
        if match:
            return i
    return -1


# 6️ index
def my_index(s: str, sub: str) -> int:
    pos = my_find(s, sub)
    if pos == -1:
        raise ValueError("substring not found")
    return pos


# 7️ isdigit
def my_isdigit(s: str) -> bool:
    if not s:
        return False
    for ch in s:
        if not ('0' <= ch <= '9'):
            return False
    return True


# 8️ islower
def my_islower(s: str) -> bool:
    has_lower = False
    for ch in s:
        if 'A' <= ch <= 'Z':
            return False
        if 'a' <= ch <= 'z':
            has_lower = True
    return has_lower


# 9️ isupper
def my_isupper(s: str) -> bool:
    has_upper = False
    for ch in s:
        if 'a' <= ch <= 'z':
            return False
        if 'A' <= ch <= 'Z':
            has_upper = True
    return has_upper


# 10 strip
def my_strip(s: str) -> str:
    start = 0
    end = len(s) - 1
    while start <= end and s[start] == " ":
        start += 1
    while end >= start and s[end] == " ":
        end -= 1
    return s[start:end + 1]


# 1️1️ replace
def my_replace(s: str, old: str, new: str) -> str:
    result = ""
    i = 0
    while i < len(s):
        match = True
        if i + len(old) <= len(s):
            for j in range(len(old)):
                if s[i + j] != old[j]:
                    match = False
                    break
        else:
            match = False

        if match:
            result += new
            i += len(old)
        else:
            result += s[i]
            i += 1
    return result


# 1️2️ rsplit
def my_rsplit(s: str, sep: str = " ") -> list:
    parts = []
    temp = ""
    i = len(s) - 1
    while i >= 0:
        if s[i:i+len(sep)] == sep:
            parts.insert(0, temp)
            temp = ""
            i -= len(sep)
        else:
            temp = s[i] + temp
            i -= 1
    parts.insert(0, temp)
    return parts


# 1️3️ lsplit
def my_lsplit(s: str, sep: str = " ") -> list:
    parts = []
    temp = ""
    i = 0
    while i < len(s):
        if s[i:i+len(sep)] == sep:
            parts.append(temp)
            temp = ""
            i += len(sep)
        else:
            temp += s[i]
            i += 1
    parts.append(temp)
    return parts


# 1️4️ swapcase
def my_swapcase(s: str) -> str:
    result = ""
    for ch in s:
        if 'a' <= ch <= 'z':
            result += chr(ord(ch) - 32)
        elif 'A' <= ch <= 'Z':
            result += chr(ord(ch) + 32)
        else:
            result += ch
    return result
