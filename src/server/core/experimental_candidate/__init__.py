import pandas as pd
from ast import literal_eval

trial = pd.read_csv("tsd_train.csv")
trial["spans"] = trial.spans.apply(literal_eval)


allToxic = set()
allNonToxic = set()

def transformToCustom(spans, text):
    # print(spans, text)

    lastSpanIndex = 0
    currentSpanIndex = 1

    while (currentSpanIndex < len(spans)):
        while(spans[currentSpanIndex] - spans[currentSpanIndex - 1] == 1):
            currentSpanIndex += 1
            if (currentSpanIndex == len(spans)):
                break

        # print(spans[lastSpanIndex], spans[currentSpanIndex - 1])

        # print(text[spans[lastSpanIndex]:spans[currentSpanIndex - 1] + 1])
        word = text[spans[lastSpanIndex]:spans[currentSpanIndex - 1] + 1]

        if(len(word.split()) == 1 and word.isalpha()):
            allToxic.add(word.lower())


        lastSpanIndex = currentSpanIndex

        currentSpanIndex += 1


for i, row in trial.iterrows():
    transformToCustom(row.spans, row.text)

    # if (i > 5):
    #     break

# print(len(allToxic))
# for i in allToxic:
#     print(i)

for i, row in trial.iterrows():
    # transformToCustom(row.spans, row.text)
    words = row.text.split()
    for word in words:
        lowerWord = word.lower()
        if(lowerWord not in allToxic and lowerWord.isalpha()):
            allNonToxic.add(lowerWord)

print(len(allToxic))
print(len(allNonToxic))

toxicDataFrame = [[x, "toxic"] for x in allToxic]

for x in allNonToxic:
    toxicDataFrame.append([x, 'non toxic'])

data = pd.DataFrame(toxicDataFrame, columns=["word", "class"])

# print(data)
data.to_csv("tsd_train_modified.csv", index=False)

