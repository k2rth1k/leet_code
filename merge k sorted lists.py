from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def merge_k_lists(lists: List[Optional[ListNode]]) -> Optional[ListNode]:
    return merge(lists)
    pass


def merge(lists: List[Optional[ListNode]]):
    length = len(lists)
    if length == 1:
        return lists[0]
    l = length // 2
    left_half = lists[0:l]
    right_half = lists[l:]
    left_node = merge(left_half)
    right_node = merge(right_half)
    return merge_lists(left_node, right_node)

    pass


def merge_lists(left_list: Optional[ListNode], right_list: Optional[ListNode]) -> Optional[ListNode]:
    if left_list is None or right_list is None:
        return None
    if left_list is None:
        return right_list
    if right_list is None:
        return left_list

    start_node = ListNode()
    if left_list.val > right_list.val:
        start_node = ListNode(val=right_list.val)
        right_list = right_list.next
    else:
        start_node = ListNode(val=left_list.val)
        left_list = left_list.next
    node = start_node
    while left_list is not None or right_list is not None:
        if left_list is None and right_list is not None:
            start_node.next = ListNode(right_list.val)
            start_node = start_node.next
            right_list = right_list.next
        if right_list is None and left_list is not None:
            start_node.next = ListNode(left_list.val)
            start_node = start_node.next
            left_list = left_list.next
        if (left_list is not None and right_list is not None) and left_list.val <= right_list.val:
            start_node.next = ListNode(left_list.val)
            start_node = start_node.next
            left_list = left_list.next
        if (left_list is not None and right_list is not None) and left_list.val >= right_list.val:
            start_node.next = ListNode(right_list.val)
            start_node = start_node.next
            right_list = right_list.next
    return node


def get_list_nodes(list_of_list_nodes) -> List[Optional[ListNode]]:
    list_of_nodes = []
    for node_list in list_of_list_nodes:
        length = len(node_list)
        node = ListNode(val=node_list[0])
        previous_node = node
        for index in range(length):
            if index > 0:
                new_node = ListNode(val=node_list[index])
                previous_node.next = new_node
                previous_node = new_node
        list_of_nodes.append(node)
    return list_of_nodes


def get_list_node_values(lists: List[Optional[ListNode]]):
    list_node_values = []
    for list in lists:
        node = list
        values = []
        while node is not None:
            values.append(node.val)
            node = node.next
        list_node_values.append(values)
    return list_node_values


if __name__ == "__main__":
    arr = [[1, 2, 4, 5], [1, 1, 1, 1, 3, 4], [2, 5, 6, 9]]
    print(get_list_node_values(get_list_nodes(arr)))
    t = get_list_nodes(arr)
    # x = merge_lists(t[0], t[1])
    # print(x)
    y = merge_k_lists(t)
    print(y)
