import pytest

from data_structures import Stack


@pytest.fixture
def stack_obj():
    return Stack()


def test_is_empty(stack_obj):
    assert stack_obj.is_empty()


def test_push(stack_obj):
    expected_value = 1
    stack_obj.push(expected_value)
    assert expected_value in stack_obj.stack


def test_is_not_empty(stack_obj):
    stack_obj.push(1)
    assert not stack_obj.is_empty()


def test_pop_when_empty(stack_obj):
    assert not stack_obj.pop()


def test_pop(stack_obj):

    expected_value = 3
    example_list = [1, 2, 3]
    for value in example_list:
        stack_obj.push(value)

    assert stack_obj.pop() == expected_value


def test_peek(stack_obj):

    expected_value = 1
    stack_obj.push(expected_value)
    assert stack_obj.peek() == expected_value


def test_peek_when_empty(stack_obj):
    assert not stack_obj.peek()


def test_get_stack(stack_obj):
    expected_result = [1, 2, 3]
    for value in expected_result:
        stack_obj.push(value)

    assert stack_obj.get_stack() == expected_result

