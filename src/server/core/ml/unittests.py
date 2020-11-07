def regression_tests(ml):

    failed_tests = 0

    # Test1 : Hey Stupid
    if ml.analyze("Hey stupid") == []:
        print("Test1 OK")
    else:
        print("Test1 NOT OK")
        failed_tests += 1

    return failed_tests


def test(ml):

    failed_tests = 0

    failed_tests += regression_tests(ml)

    return failed_tests