from src.server.aop import AnalyzerAspect
from src.server.core.ml import MachineLearning

aspect = AnalyzerAspect()
ml = MachineLearning()

aspect.apply(ml)
print(ml.analyze("You are an idiot"))
