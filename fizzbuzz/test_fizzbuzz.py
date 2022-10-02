from pytest import mark

from fizzbuzz import fizzbuzz


@mark.parametrize("num", [1, 2, 4])
def test_given_any_number_that_is_not_dividabale_by_3_and_5_return_number_itself(num):
    res = fizzbuzz(num)
    assert res == str(num)


@mark.parametrize("num", [3, 6, 9])
def test_given_any_number_that_is_dividabale_by_3_but_not_by_5_return_fizz(num):
    res = fizzbuzz(num)
    assert res == "fizz"


@mark.parametrize("num", [5, 10, 20])
def test_given_any_number_that_is_dividabale_by_5_but_not_by_3_return_buzz(num):
    res = fizzbuzz(num)
    assert res == "buzz"


@mark.parametrize("num", [15, 30, 45])
def test_given_any_number_that_is_dividabale_by_3_and_by_5_return_buzz(num):
    res = fizzbuzz(num)
    assert res == "fizzbuzz"