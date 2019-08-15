dic = {}

def somaVogal(text):
    if len(text) != 0:
        if 'a' in text:
            dic['a'] = text.count("a")
        if 'e' in text:
            dic['e'] = text.count("e")
        if 'i' in text:
            dic['i'] = text.count("i")
        if 'o' in text:
            dic['o'] = text.count("o")
        if 'u' in text:
            dic['u'] = text.count("u")
    else:
        return 0

somaVogal(text = raw_input())

print dic
