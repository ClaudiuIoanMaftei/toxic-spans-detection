# Toxic Spans Detection

https://competitions.codalab.org/competitions/25623

# To run tests

Add your tests in the ``tests`` directory, creating a similar folder structore to the ``src`` folder. For example, for DL component, place tests under ``tests/dl/<module_name>``.
Every test file should correspond to a source test file, and should be named using the format ``test_<component/class>.py``. Pytest will search for this specific `test_*.py` files and run all the `test_*` methods


Install pytest library (PyCharm will automatically detect it from the requirements.txt and a restart might be needed to have the executable in the PATH).

If you cannot run `pytest` command, try installing it manually with pip/pip3. Ultimately, run `python -m pytest` to run it without having the executable in the ```$PATH``` variable.

# To run ML component

Unzip the archive found in the directory src/server/core/ml/data

# To run DL component

The DL component uses TensorFlow and keras to apply a CNN model over the given input. In order to install these, there are a few steps you need to follow first:

### Prerequisites

TensorFlow only works with Python up to 3.8. The following guide has been tested with 3.7, and might work with 3.8 as well, but the tensor flow version
might need to be adjusted. The current used version is ```tensorflow~=2.4.0```

* Make sure spacy is installed properly. After installing it with pip, run something like```C:\Users\<username>\PycharmProjects\TAIP\venv\Scripts\python.exe -m spacy download en```
, using the path of the python interptetor used by PyCharm
* Install VisualStudio 2019. You will only need the basic C++ package from this instalation
* Install CUDA library from [here](https://developer.nvidia.com/cuda-downloads?target_os=Windows&target_arch=x86_64&target_version=10&target_type=exelocal). Use  ```exe(network)```
option, as the other one seems to have trouble finding visual studio 19.
* (Optional, for training) install [cuDNN](https://developer.nvidia.com/rdp/cudnn-download). For this a developer account is needed, which will take about 5 minutes to create 
    * If you will install cuDNN, you need to move the files from the ```lib``` ```include``` and ```bin``` in the same directories, in the CUDA instalation folder.
    Essentially, cuDNN brings more libraries for the basic CUDA library, so they need to be merged.
* Finnaly, add a global environment variable ```CUDA_PATH``` with the CUDA library path (including version). If you chose the default instalation,
this path will be ```C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v11.2```
* A restart to PyCharm might be needed after this

### For training

Training the DL model will take quite some time, and at the end a serialization process will write it to disk. To begin this sequence, run

```shell script
python -m src/server/core/dl/__init__.py -train <training_data_path>
```
By default, the ```training_data_path``` is  ```datasets/trd_train.csv```

If the serialized model is not present, the DL component will throw an initialization exception. The model will be present on github.
