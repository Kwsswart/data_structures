import pytest

from data_structures import SimpleQueue


@pytest.fixture
def queue_obj():
    return SimpleQueue()


@pytest.fixture
def example_list():
    return [1, 2, 3, 4]


def test_is_empty(queue_obj):
    assert queue_obj.is_empty()


def test_is_empty_false(queue_obj, example_list):
    queue_obj.enqueue(example_list[1])
    assert not queue_obj.is_empty()


def test_enqueue(queue_obj, example_list):
    for i in example_list:
        queue_obj.enqueue(i)
    assert queue_obj.queue == example_list


def test_dequeue_empty(queue_obj):
    assert not queue_obj.dequeue()


def test_dequeue(queue_obj, example_list):
    for i in example_list:
        queue_obj.enqueue(i)
    assert queue_obj.dequeue() == example_list[0]


def test_peek_empty(queue_obj):
    assert not queue_obj.peek()


def test_peek(queue_obj, example_list):
    for i in example_list:
        queue_obj.enqueue(i)
    assert queue_obj.peek() == example_list[0]
