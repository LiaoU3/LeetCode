# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def List2TreeNode(ls = []):
    pass

# Create a list from a ListNode
def TreeNode2List(root):
    ret = [root.val]

    curr = [root]
    keep_going = True
    while keep_going:
        nxt = []
        keep_going = False
        for node in curr:
            if node != None:
                keep_going = True
                left  = node.left
                right = node.right
                nxt.append(left)
                nxt.append(right)
            else:
                nxt.append(None)
                nxt.append(None)

        if len(set(nxt))!=1:
            for node in nxt:
                if node == None:
                    ret.append(node)
                else:
                    ret.append(node.val)
        curr = nxt
    for i in range(len(ret)-1, -1, -1):
        if ret[i] == None:
            ret.pop()
        else:
            break
    return ret