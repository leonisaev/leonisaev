def fizzbuzz(n):
    if is_dividabale_by(n, 3) and is_dividabale_by(n, 5):
        return "fizzbuzz"
    if is_dividabale_by(n,3):
        return "fizz"
    if is_dividabale_by(n, 5):
        return "buzz"
    return str(n)


def is_dividabale_by(n, div):
    return n % div == 0
