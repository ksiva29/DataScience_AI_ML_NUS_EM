from src.tensorflow_example import build_simple_model, train_simple_model


def test_build_simple_model() -> None:
    model = build_simple_model()
    assert model is not None


def test_train_simple_model() -> None:
    model = train_simple_model()
    assert model is not None
