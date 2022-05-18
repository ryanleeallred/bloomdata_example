import bloomdata.bloomdata as bd

def test_increment_int():
    assert bd.increment(3) == 4
    assert bd.increment(100) == 101
    assert bd.increment(-5) == -4


def test_increment_float():
    assert bd.increment(1.4) == 2.4
    assert bd.increment(0.0) == 1.0