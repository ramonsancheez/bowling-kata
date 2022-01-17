from spinsCards import spinsCards    
import pytest

@pytest.mark.spinsCards
def test_funciona1():
    # Hitting pins total = 60
    pins = "12345123451234512345"
    total = 60
    SpinsCards = spinsCards(pins)
    assert SpinsCards.getTotal() == total

@pytest.mark.spinsCards
def test_funciona2():
    # test symbol -
    pins = "9-9-9-9-9-9-9-9-9-9-"
    total = 90
    SpinsCards = spinsCards(pins)
    assert SpinsCards.getTotal() == total

@pytest.mark.spinsCards
def test_funciona3():
    pins = "9-3561368153258-7181"
    total = 82
    SpinsCards = spinsCards(pins)
    assert SpinsCards.getTotal() == total

@pytest.mark.spinsCards
def test_funciona4():
    # test spare not extra
    pins = "9-3/613/815/-/8-7/8-"
    total = 121
    SpinsCards = spinsCards(pins)
    assert SpinsCards.getTotal() == total

@pytest.mark.spinsCards
def test_funciona5():
    # test strike
    pins = "X9-9-9-9-9-9-9-9-9-"
    total = 100
    SpinsCards = spinsCards(pins)
    assert SpinsCards.getTotal() == total

@pytest.mark.spinsCards
def test_funciona6():
    pins = "X9-X9-9-9-9-9-9-9-"
    total = 110
    SpinsCards = spinsCards(pins)
    assert SpinsCards.getTotal() == total

@pytest.mark.spinsCards
def test_funciona7():
    # two strikes in a row is a double
    pins = "XX9-9-9-9-9-9-9-9-"
    total = 120
    SpinsCards = spinsCards(pins)
    assert SpinsCards.getTotal() == total

@pytest.mark.spinsCards
def test_funciona8():
    # three strikes in a row is a triple
    pins = "XXX9-9-9-9-9-9-9-"
    total = 141
    SpinsCards = spinsCards(pins)
    assert SpinsCards.getTotal() == total

@pytest.mark.spinsCards
def test_funciona9():
    # one pin extra roll
    pins = "9-3/613/815/-/8-7/8/8"
    total = 131
    SpinsCards = spinsCards(pins)
    assert SpinsCards.getTotal() == total

@pytest.mark.spinsCards
def test_funciona10():
    pins = "5/5/5/5/5/5/5/5/5/5/5"
    total = 150
    SpinsCards = spinsCards(pins)
    assert SpinsCards.getTotal() == total

@pytest.mark.spinsCards
def test_funciona11():
    # two strikes in extra rolls
    pins = "9-9-9-9-9-9-9-9-9-XXX"
    total = 111
    SpinsCards = spinsCards(pins)

@pytest.mark.spinsCards
def test_funciona12():
    # one strike in extra roll
    pins = "8/549-XX5/53639/9/X"
    total = 149
    SpinsCards = spinsCards(pins)
    assert SpinsCards.getTotal() == total

@pytest.mark.spinsCards
def test_funciona13():
    # spare in extra roll
    pins = "X5/X5/XX5/--5/X5/"
    total = 175
    SpinsCards = spinsCards(pins)
    assert SpinsCards.getTotal() == total

@pytest.mark.spinsCards
def test_funciona14():
    # 12 strikes is a “Thanksgiving Turkey”
    # 2 strikes in extra rolls
    pins = "XXXXXXXXXXXX"
    total = 300
    SpinsCards = spinsCards(pins)
    assert SpinsCards.getTotal() == total