# Definition for singly-linked list with a random pointer.
class RandomListNode(object):
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None


class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """

        result_node = None
        result_dict = dict()
        pre_node = None

        while head:
            if head not in result_dict:
                result_dict[head] = RandomListNode(head.label)
            current_node = result_dict[head]

            if pre_node:
                pre_node.next = current_node
            else:
                result_node = current_node

            # if head.next:
            #     if head.next not in result_dict:
            #         result_dict[head.next] = RandomListNode(head.next.label)
            #     current_node.next = result_dict[head.next]

            if head.random:
                if head.random not in result_dict:
                    result_dict[head.random] = RandomListNode(head.random.label)
                current_node.random = result_dict[head.random]

            pre_node, head = current_node, head.next

        return result_node

