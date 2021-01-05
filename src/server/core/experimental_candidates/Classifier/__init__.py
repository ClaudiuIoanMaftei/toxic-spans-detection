from weka.classifiers import Classifier
c = Classifier(name='weka.classifiers.lazy.IBk', ckargs={'-K':1})
c.train('training.arff')
predictions = c.predict('query.arff')