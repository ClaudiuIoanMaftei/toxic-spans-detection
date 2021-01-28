from src.server.core.ml import MachineLearning
from src.server.aop import AnalyzerAspect
from src.server.core.ml.utils import parse_test_data, spans_to_words, parse_aop_log
import os, sys


####################
# Global Variables #
####################
aop_output_file   = "aop.log"
test_input_file  = "tsd_test.csv"
trial_debug_file  = "test_debug.txt"
trial_output_file = "spans-pred.txt"
#######################################

test_data = parse_test_data(test_input_file)
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
debug_file = open(trial_debug_file, "w", encoding="utf-8")
output_file = open(trial_output_file, "w")
###########################################

contor = 0
for text in test_data:

    result = ml.analyze(text)
    output_file.write(str(contor) + "\t")
    output_file.write(str(result) + '\n')

    input_contor += 1

    result_words  = spans_to_words(result,   text)

    debug_file.write(text + "\n")
    debug_file.write("----------------\n")
    debug_file.write("result:  " + str(result)   + "\n")
    debug_file.write("----------------\n")
    debug_file.write("result words: "   + str(result_words)   + "\n\n")

    contor += 1

#################
# Closing files #
#################
debug_file.close()
output_file.close()
###################

functions_times = parse_aop_log(aop_output_file)
for function in functions_times:

    average_time = functions_times[function]["time"] / functions_times[function]["count"]

    print(function + "()")
    print("Total time: " + str(functions_times[function]["time"]) + " ms")
    print("Average time: " + str(round(average_time,2)) + " ms\n")

