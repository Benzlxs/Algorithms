"""
To check whether givan tree is a balanced tree or not
"""





def balance_soltuion(root):
    if root is None:
        return 0
    left = balance_soltuion(root.left)
    if left==-1: return -1
    right = balance_soltuion(root.right)
    if right==-1: return -1
    if abs(left - right) > 1: return -1
    return max(left, right) + 1



if __name__=="__main__":
    re = balance_soltuion(root)

    if re == -1:
        return False
    else:
        return True
