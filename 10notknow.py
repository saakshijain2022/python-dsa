1
2 1
3 2 1
4 3 2 1

def solve(root, low, high):

    current_sum = 0

    if not root:
        return 0

    if low <= root.val <= high:
        current_sum += root.val

    if low < root.val:
        current_sum += solve(root.left, low, high)

    if high > root.val:
        current_sum += solve(root.right, low, high)

    return current_sum
[8:14 PM]
def solve(root):

    inorder_arr = []

    def inorder(root, arr):
        if root:
            inorder(root.left, arr)
            arr.append(root)
            inorder(root.right, arr)

    inorder(root, inorder_arr)

    sorted_arr = sorted([node.val for node in inorder_arr])

    for i in range(len(sorted_arr)):
        inorder_arr[i].val = sorted_arr[i]

    return root