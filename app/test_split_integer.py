from app.split_integer import split_integer


def test_sum_of_the_parts_should_be_equal_to_value() -> None:
    result = split_integer(17, 4)
    assert sum(result) == 17
    result = split_integer(32, 6)
    assert sum(result) == 32


def test_should_split_into_equal_parts_when_value_divisible_by_parts() -> None:
    assert split_integer(10, 5) == [2, 2, 2, 2, 2]
    assert split_integer(12, 3) == [4, 4, 4]


def test_should_return_part_equals_to_value_when_split_into_one_part() -> None:
    assert split_integer(8, 1) == [8]
    assert split_integer(15, 1) == [15]


def test_parts_should_be_sorted_when_they_are_not_equal() -> None:
    result = split_integer(17, 4)
    assert result == sorted(result)
    result = split_integer(32, 6)
    assert result == sorted(result)


def test_should_add_zeros_when_value_is_less_than_number_of_parts() -> None:
    assert split_integer(3, 5) == [0, 0, 0, 1, 2]
    assert split_integer(2, 4) == [0, 0, 1, 1]
