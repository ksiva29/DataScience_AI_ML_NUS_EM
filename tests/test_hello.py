from src.hello import train_sample_model


def test_train_sample_model_returns_reasonable_accuracy() -> None:
    accuracy = train_sample_model()
    assert 0.7 <= accuracy <= 1.0
