from typing import Optional, List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def add_two_numbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    if l1 is None and l2 is None:
        return None
    node = ListNode()
    if l1 is None:
        return l2
    if l2 is None:
        return l1
    node = l1
    start_node = node
    carry = 0
    l2_val = 0
    while l1 is not None or l2 is not None:
        if l2 is None:
            l2_val = 0
        else:
            l2_val = l2.val
        sum_val = l1.val + l2_val + carry
        carry = sum_val // 10
        sum_val = sum_val % 10
        l1.val = sum_val
        if carry == 1 and l1.next is None:
            l1.next = ListNode(val=carry)
            carry = 0
            l1 = l1.next
            if l2 is not None:
                l2 = l2.next
            continue
        if l1.next is None and l2 is not None:
            l1.next = l2.next
            l2.next = None
        l1 = l1.next
        if l2 is not None:
            l2 = l2.next

    return start_node


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


if __name__ == '__main__':
    arr = [[9, 9, 9, 9, 9], [2, 3, 1]]
    t = get_list_nodes(arr)
    result = add_two_numbers(t[0], t[1])
    print(result)
