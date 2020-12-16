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
