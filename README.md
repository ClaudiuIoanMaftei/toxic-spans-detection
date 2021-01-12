# Toxic Spans Detection

https://competitions.codalab.org/competitions/25623

# To run tests

Add your tests in the ``tests`` directory, creating a similar folder structore to the ``src`` folder. For example, for DL component, place tests under ``tests/dl/<module_name>``.
Every test file should correspond to a source test file, and should be named using the format ``test_<component/class>.py``. Pytest will search for this specific `test_*.py` files and run all the `test_*` methods


Install pytest library (PyCharm will automatically detect it from the requirements.txt and a restart might be needed to have the executable in the PATH).

If you cannot run `pytest` command, try installing it manually with pip/pip3. Ultimately, run `python -m pytest` to run it without having the executable in the ```$PATH``` variable.
