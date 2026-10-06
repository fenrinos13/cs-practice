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
