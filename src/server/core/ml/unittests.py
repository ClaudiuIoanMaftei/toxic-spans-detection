def regression_tests(ml):

    # Test1 : Hey Stupid
    if ml.analyze("Hey stupid") == [4, 5, 6, 7, 8, 9]:
        print("Test1 OK")
    else:
        print("Test1 NOT OK")


def test(ml):
    regression_tests(ml)