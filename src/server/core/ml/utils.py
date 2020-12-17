import csv

###############
# Global Vars #
###############

data_path = "datasets/"


#############
# Functions #
#############

# Get toxic words from spans and text
def spans_to_words(spans, text):
	
    toxic_words = []
    curr_word = ""
    last_idx = 0
    if len(spans) > 0:
        last_idx = spans[0]

    for idx in spans:
        if idx > last_idx + 1:
            toxic_words += curr_word.split(" ")
            curr_word = text[idx]
        else:
            curr_word += text[idx]
        last_idx = idx
    if curr_word != "":
        toxic_words += curr_word.split(" ")

    return toxic_words


# Get data from csv
def parse_data(file):
    file = open(data_path + file, encoding="utf-8")
    entities = []
    csvreader = csv.reader(file, delimiter=',', quotechar='"')
    for row in list(csvreader)[1:]:
        spans = []
        text = row[1]
        spans_text = row[0][1:-1]
        for number in spans_text.split(", "):
            if number != '':
                spans.append(int(number))
        entities.append([spans, text])
    return entities

