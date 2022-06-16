import pytest

from data_structures import Deque


@pytest.fixture
def deque_obj():
    return Deque()


@pytest.fixture
def example_list():
    return [1, 2, 3, 4]


def test_is_empty(deque_obj):
    assert deque_obj.is_empty()


def test_is_empty_false(deque_obj, example_list):
    deque_obj.add_to_rear(example_list[1])
    assert not deque_obj.is_empty()


def test_add_to_rear(deque_obj, example_list):
    for i in range(2):
        deque_obj.add_to_rear(example_list[i])
    assert deque_obj.queue[i] == example_list[i]


def test_add_to_front(deque_obj, example_list):
    for i in example_list:
        deque_obj.add_to_front(i)
    assert deque_obj.queue == example_list[::-1]


def test_remove_from_front(deque_obj, example_list):
    for i in example_list:
        deque_obj.add_to_front(i)
    expected_result = example_list[-1]
    assert deque_obj.remove_from_front() == expected_result


def test_remove_from_rear(deque_obj, example_list):
    for i in example_list:
        deque_obj.add_to_front(i)
    expected_result = example_list[0]
    assert deque_obj.remove_from_rear() == expected_result
