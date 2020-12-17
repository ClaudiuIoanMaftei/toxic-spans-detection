from src.server.core.ml import MachineLearning
from src.server.aop import AnalyzerAspect
from src.server.core.ml.utils import parse_data, spans_to_words

trial_data = parse_data("tsd_trial.csv")

aa = AnalyzerAspect()
ml = MachineLearning()
aa.apply(ml)

ok    = 0
notok = 0

common_idx_count = 0
plus_idx_count   = 0
minus_idx_count  = 0 

common_words_count = 0
plus_words_count   = 0
minus_words_count  = 0


file = open("trial.output", "w")


for entry in trial_data:

    result = ml.analyze(entry[1])

    expected_words = spans_to_words(entry[0], entry[1])
    result_words  = spans_to_words(result,   entry[1])

    common_idx = list( set(result) & set(entry[0]) )
    minus_idx  = list( set(entry[0]) - set(result) )
    plus_idx   = list( set(result) - set(entry[0]) ) 

    common_words = list( set(result_words) & set(expected_words)  ) 
    plus_words   = list( set(result_words) - set(expected_words) )
    minus_words  = list( set(expected_words) - set(result_words) )

    file.write(entry[1] + "\n")
    file.write("----------------\n")
    file.write("expected: " + str(entry[0]) + "\n")
    file.write("result:  " + str(result)   + "\n")
    file.write("----------------\n")
    file.write("minus: " + str(minus_idx) + "\n")
    file.write("common: "   + str(common_idx) + "\n")
    file.write("plus: " + str(plus_idx) + "\n")
    file.write("----------------\n")
    file.write("expected words: " + str(expected_words) + "\n")
    file.write("result words: "   + str(result_words)   + "\n")
    file.write("minus words: " + str(minus_words) + "\n")
    file.write("common words: " + str(common_words) + "\n")
    file.write("plus words: " + str(plus_words) + "\n\n")


    if entry[0] == result:
        ok += 1
    else:
        notok += 1
    
    common_idx_count += len(common_idx)
    plus_idx_count   += len(plus_idx)
    minus_idx_count  += len(minus_idx)
    
    common_words_count += len(common_words)
    plus_words_count += len(plus_words)
    minus_words_count += len(minus_words)

file.close()

print("Identical: " + str(ok) + "/" + str(notok + ok))
print("-------------")
print("Common idx count: " + str(common_idx_count))
print(" Minus idx count: " + str(minus_idx_count))
print("  Plus idx count: " + str(plus_idx_count))
print("-------------")
print("Common words count: " + str(common_words_count))
print(" Minus words count: " + str(minus_words_count))
print("  Plus words count: " + str(plus_words_count))
