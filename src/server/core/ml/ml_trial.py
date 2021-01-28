from src.server.core.ml import MachineLearning
from src.server.aop import AnalyzerAspect
from src.server.core.ml.utils import parse_data, spans_to_words, parse_aop_log
import os, sys


####################
# Global Variables #
####################
aop_output_file   = "aop.log"
trial_input_file  = "tsd_trial.csv"
trial_debug_file  = "trial_debug.txt"
trial_output_file = "spans-pred.txt"
gold_output_file  = "spans-gold.txt"
#######################################

trial_data = parse_data(trial_input_file)
input_contor = 0

feature_method = 0
if len(sys.argv) > 1 and int(sys.argv[1]) >=0 and int(sys.argv[1]) <= 1:
    feature_method = int(sys.argv[1])

aa = AnalyzerAspect()
ml = MachineLearning(feature_method)
aa.apply(ml)

ok    = 0
notok = 0

common_idx_count = 0
plus_idx_count   = 0
minus_idx_count  = 0 

common_words_count = 0
plus_words_count   = 0
minus_words_count  = 0

# Remove aop log file
if os.path.exists(aop_output_file):
    os.remove(aop_output_file)

#################
# Opening files #
#################
debug_file = open(trial_debug_file, "w")
output_file = open(trial_output_file, "w")
###########################################

for entry in trial_data:

    result = ml.analyze(entry[1])
    output_file.write(str(input_contor) + '\t' + str(result) + '\n')
    input_contor += 1

    expected_words = spans_to_words(entry[0], entry[1])
    result_words  = spans_to_words(result,   entry[1])

    common_idx = list( set(result) & set(entry[0]) )
    minus_idx  = list( set(entry[0]) - set(result) )
    plus_idx   = list( set(result) - set(entry[0]) ) 

    common_words = list( set(result_words) & set(expected_words)  ) 
    plus_words   = list( set(result_words) - set(expected_words) )
    minus_words  = list( set(expected_words) - set(result_words) )

    debug_file.write(entry[1] + "\n")
    debug_file.write("----------------\n")
    debug_file.write("expected: " + str(entry[0]) + "\n")
    debug_file.write("result:  " + str(result)   + "\n")
    debug_file.write("----------------\n")
    debug_file.write("minus: " + str(minus_idx) + "\n")
    debug_file.write("common: "   + str(common_idx) + "\n")
    debug_file.write("plus: " + str(plus_idx) + "\n")
    debug_file.write("----------------\n")
    debug_file.write("expected words: " + str(expected_words) + "\n")
    debug_file.write("result words: "   + str(result_words)   + "\n")
    debug_file.write("minus words: " + str(minus_words) + "\n")
    debug_file.write("common words: " + str(common_words) + "\n")
    debug_file.write("plus words: " + str(plus_words) + "\n\n")


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

#################
# Closing files #
#################
debug_file.close()
output_file.close()
###################

print("\nIdentical: " + str(ok) + "/" + str(notok + ok))
print("-------------")
print("Common idx count: " + str(common_idx_count))
print(" Minus idx count: " + str(minus_idx_count))
print("  Plus idx count: " + str(plus_idx_count))
print("-------------")
print("Common words count: " + str(common_words_count))
print(" Minus words count: " + str(minus_words_count))
print("  Plus words count: " + str(plus_words_count))
print("-------------")

functions_times = parse_aop_log(aop_output_file)
for function in functions_times:

    average_time = functions_times[function]["time"] / functions_times[function]["count"]

    print(function + "()")
    print("Total time: " + str(functions_times[function]["time"]) + " ms")
    print("Average time: " + str(round(average_time,2)) + " ms\n")

