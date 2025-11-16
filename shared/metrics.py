from sklearn.metrics import f1_score

def macro_f1(preds, labels):
    return f1_score(labels, preds, average='macro')

