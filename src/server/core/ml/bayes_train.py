
def semeval_train():
    bb = BayesBank()

    train_data = parse_data("tsd_train.csv")

    for entry in train_data:
        print(entry)
        preproc = PreProcessor()
        results = preproc.preprocess(entry[1])

        tokens = results.data["tokens"]
        lemmas = results.data["lemmas"]
        uniq_lemmas = list(set(lemmas))
        toxic_words = []

        curr_word = ""
        last_idx = 0
        if len(entry[0]) > 0:
            last_idx = entry[0][0]

        for idx in entry[0]:
            curr_word += entry[1][idx]
            if idx > last_idx + 1:
                toxic_words += curr_word.split(" ")
                curr_word = ""
            last_idx = idx
        if curr_word != "":
            toxic_words += curr_word.split(" ")

        for idx in range(0, len(tokens)):
            token = tokens[idx]
            lemma = lemmas[idx]

            lemmas_wo = list(uniq_lemmas)
            lemmas_wo.remove(lemma)
            for i in range(0, len(lemmas_wo)):
                lemmas_wo[i] = lemmas[i]

            if token in toxic_words:
                bb.train(lemma, lemmas_wo, "toxic")
            else:
                bb.train(lemma, lemmas_wo, "non_toxic")

    bb.serialize()
