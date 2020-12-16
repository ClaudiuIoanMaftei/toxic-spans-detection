from src.server.core.ml import MachineLearning
from src.server.aop import AnalyzerAspect
from src.server.core.ml.bayes import  parse_data

trial_data = parse_data("tsd_trial.csv")

aa = AnalyzerAspect()
ml = MachineLearning()
aa.apply(ml)

ok    = 0
notok = 0

for entry in trial_data:
    if entry[0] == ml.analyze(entry[1]):
        ok += 1
    else:
        notok += 1

print(str(ok) + "/" + str(notok))