# 1.UI
Web Interface using React.<br>
Containts an input field for the text to be analysed.<br>
Displays the text with the toxic spans highlighted.<br>

# 2.Server
Receives the request from the 1.UI.<br>
Returns the results from [Postprocessing](###2.3.Postprocessing) to the [UI](#1.UI).

### 2.1.Preprocessing
Preprocesses the text through normalization, lemmatization, stemming, etc...

### 2.2.Core
Encapsulates the detection methods.

##### 2.2.1.DL
Deep Learning approach using Neural networks.<br>
Returns toxic spans detected.

##### 2.2.2.ML
Machine Learning approach using statistics or deterministics algorithms.<br>
Returns toxic spans detected.

### 2.3.Postprocessing
Aggregates the output of the [Core](###2.2.Core) into one final result.