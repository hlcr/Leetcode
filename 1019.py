def nextLargerNodes(head):
    """
    :type head: ListNode
    :rtype: List[int]
    """
    result = []
    stack = []
    i = 0
    while head:
        result.append(0)
        while stack and stack[-1] < head.val:
            result[stack.pop()[0]] = head.val
        stack.append([i, head.val])
        i += 1
        head = head.next
    return result