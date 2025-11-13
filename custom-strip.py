def my_strip(s: str) -> str:
    start = 0
    end = len(s) - 1

    while start <= end and s[start] == " ":
        start += 1
    while end >= start and s[end] == " ":
        end -= 1

    return s[start:end + 1]

text = input("Enter a text: ")
cleaned = my_strip(text)
print("Result → ", cleaned)