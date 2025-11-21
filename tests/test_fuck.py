import pytest  # type: ignore

from himmel import _float_to_int


@pytest.mark.parametrize(
    'input_float, expected_int',
    [
        (5.7, 5),
        (0.9, 0),
        (-3.2, -3),
        (-0.9, 0),
        (0.0, 0),
        (123456.789, 123456),
        (10.0, 10),
    ],
)
def test_float_to_int(input_float, expected_int) -> None:
    assert _float_to_int(input_float) == expected_int
