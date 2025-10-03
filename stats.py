def get_num_words(content):
    return len(content.split())

def get_count_characters(content):
    res = {}
    for ch in content.lower():
        if ch not in res:
            res[ch] = 0
        res[ch] += 1
    return res

def sorting_dict(d):
    return dict(sorted(d.items(), key=lambda x: -x[1]))