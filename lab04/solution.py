names =  ["Аня", "Боря", "Вика"]
scores = [7.0,   9.0,    9.0]


def winner(names, scores):
    if not scores: return ""
    best_score = max(scores)
    best_index = scores.index(best_score)
    return names[best_index]

def average(scores):
    if not scores: return 0.0
    return round(sum(scores) / len(scores), 2)

def ranking(names, scores):
    id = list(range(len(scores)))
    for i in range(len(id)):
        for j in range(i + 1, len(id)):
            if scores[id[j]] > scores[id[i]]:
                id[i], id[j] = id[j], id[i]
    res = []
    for i in id:
        res.append(names[i])
    return res

def above_average(names, scores):
    avg = average(scores)
    res = []
    for i in range(len(scores)):
        if scores[i] > avg: res.append(names[i])
    return res
