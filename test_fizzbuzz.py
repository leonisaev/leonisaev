def fizzbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        return "fizzbuzz"
    if n % 3 == 0:
        return "fizz"
    if n % 5 == 0:
        return "buzz"
    return str(n)


def test_with_1():
    res = fizzbuzz(1)
    assert res == "1"

def test_with_2():
    res = fizzbuzz(2)
    assert res == "2"


def test_with_3():
    res = fizzbuzz(3)
    assert res == "fizz"


def test_with_5():
    res = fizzbuzz(5)
    assert res == "buzz"


def test_with_6():
    res = fizzbuzz(6)
    assert res == "fizz"


def test_with_10():
    res = fizzbuzz(10)
    assert res == "buzz"

def test_with_15():
    res = fizzbuzz(15)
    assert res == "fizzbuzz"