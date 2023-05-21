#test_with_pytest.py

from pytest import mark


@mark.smoke
def test_always_passes():
    assert True


def test_always_fails():
    assert False

@mark.regression
def test_uppercase():
    assert "loud noises".upper() == "LOUD NOISES"

@mark.smoke
def check_reversed():
    assert list(reversed([1,2,3,4,5]))==[5,4,3,2,1]


def test_some_primes():
    assert 49 in {
        num
        for num in range(1,50)
        if num !=1 and not any([num%div == 0 for div in range(2, num)])
        }

