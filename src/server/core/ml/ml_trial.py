from src.server.core.ml import MachineLearning
from src.server.aop import AnalyzerAspect
from src.server.core.ml.utils import parse_data

trial_data = parse_data("tsd_trial.csv")

aa = AnalyzerAspect()
ml = MachineLearning()
aa.apply(ml)

ok    = 0
notok = 0

file = open("trial.output", "w")


for entry in trial_data:

    result = ml.analyze(entry[1])
    file.write(str(result)+"\n") 

    if entry[0] == result:
        ok += 1
    else:
        notok += 1

file.close()

print(str(ok) + "/" + str(notok))
