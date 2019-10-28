import maths_func

def test_add():
    assert maths_func.add(7, 3) == 10
    assert maths_func.add(7) == 9 

def test_product():
    assert maths_func.product(5, 4) == 20
    assert maths_func.product(5) == 10