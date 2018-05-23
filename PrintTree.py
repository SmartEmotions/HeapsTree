def preorder(tree): 
    if(not tree.is_empty()):
        return __preorder(tree._root, [])
    else:
        return(['NONEIN'])


def posorder(tree):
    if(not tree.is_empty()):
        return __posorder(tree._root, [])
    else:
        return(['NONEIN'])


def inorder(tree):
    if(not tree.is_empty()):
        return __inorder(tree._root, [])
    else:
        return(['NONEIN'])


def __preorder(subtree, printTree):
    if subtree is not None:
        printTree.append([str(subtree._key.codeProduct),
                         str(subtree._key.nameProduct),
                         str(subtree._key.countryProduct),
                         str(subtree._key.costProduct),
                         str(subtree._key.cantProduct),
                         str(subtree._key.unitProduct),
                         str(subtree._key.arancelProduct)])
        __preorder(subtree._left, printTree)
        __preorder(subtree._right, printTree)
        return printTree


def __posorder(subtree, printTree):
    if subtree is not None:
        __preorder(subtree._left, printTree)
        printTree.append([str(subtree._key.codeProduct),
                         str(subtree._key.nameProduct),
                         str(subtree._key.countryProduct),
                         str(subtree._key.costProduct),
                         str(subtree._key.cantProduct),
                         str(subtree._key.unitProduct),
                         (str(subtree._key.arancelProduct) + '%')])
        __preorder(subtree._right, printTree)
        return printTree


def __inorder(subtree, printTree):
    if subtree is not None:
        __preorder(subtree._left, printTree)
        __preorder(subtree._right, printTree)
        printTree.append([str(subtree._key.codeProduct),
                         str(subtree._key.nameProduct),
                         str(subtree._key.countryProduct),
                         str(subtree._key.costProduct),
                         str(subtree._key.cantProduct),
                         str(subtree._key.unitProduct),
                         (str(subtree._key.arancelProduct) + '%')])
        return printTree
