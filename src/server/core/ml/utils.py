import csv, re

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


# Parse aop log
def parse_aop_log(file):
    file = open(file, encoding="utf-8")
    rows = file.read().split("\n")
    file.close()

    functions = {}

    for row in rows[1:]:
        match = re.match(r"([a-zA-Z\.]+)\(\): ([0-9]+) ms", row)
        if match:

            function_name = match.group(1)
            time = match.group(2)

            if function_name not in functions:

                functions[function_name] = {
                    "time": int(time),
                    "count": 1
                }

            else:

                functions[function_name]["time"] += int(time)
                functions[function_name]["count"] += 1

    return functions
