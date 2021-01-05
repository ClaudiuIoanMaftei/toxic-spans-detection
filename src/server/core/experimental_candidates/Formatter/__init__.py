import pandas as pd
from ast import literal_eval

dataRootPath = "src/server/core/experimental_candidates/data"

trial = pd.read_csv(dataRootPath + "tsd_train.csv")
trial["spans"] = trial.spans.apply(literal_eval)

toxicWords = set()
nonToxicWords = set()

def getToxicWordsFromSpanTextPair(spans, text):

    toxic = set()
    lastSpanIndex = 0
    currentSpanIndex = 1

    while (currentSpanIndex < len(spans)):
        while(spans[currentSpanIndex] - spans[currentSpanIndex - 1] == 1):
            currentSpanIndex += 1
            if (currentSpanIndex == len(spans)):
                break

        word = text[spans[lastSpanIndex]:spans[currentSpanIndex - 1] + 1]

        if(len(word.split()) == 1 and word.isalpha()):
            toxic.add(word.lower())

        lastSpanIndex = currentSpanIndex

        currentSpanIndex += 1

        return toxic


for i, row in trial.iterrows():
    toxicWords.add(getToxicWordsFromSpanTextPair(row.spans, row.text))

for i, row in trial.iterrows():
    words = row.text.split()
    for word in words:
        lowerWord = word.lower()
        if lowerWord not in toxicWords and lowerWord.isalpha():
            nonToxicWords.add(lowerWord)

toxicityDataFrame = [[x, "toxic"] for x in toxicWords]

for x in nonToxicWords:
    toxicityDataFrame.append([x, 'non toxic'])

data = pd.DataFrame(toxicityDataFrame, columns=["word", "class"])
data.to_csv(dataRootPath + "tsd_train_formatted.csv", index=False)

