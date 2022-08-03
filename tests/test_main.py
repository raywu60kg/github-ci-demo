from src.main import main


def test_main():
    return_from_main = main(1)
    assert return_from_main == 2
