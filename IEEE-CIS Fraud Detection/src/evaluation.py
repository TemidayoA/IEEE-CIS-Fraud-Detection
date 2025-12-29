from sklearn.metrics import precision_recall_curve

def optimal_threshold(y_true, y_prob, min_precision=0.9):
    precision, recall, thresholds = precision_recall_curve(y_true, y_prob)

    for p, r, t in zip(precision, recall, thresholds):
        if p >= min_precision:
            return t

    return 0.5
