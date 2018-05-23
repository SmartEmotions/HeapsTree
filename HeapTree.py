"""
Proyect :  Graphics Heaps Trees
Version :  V. 1.2.3
Autors  :  Dario Criollo(Graphic Desing)
        :  Carlos Guadir(Code Desing)
"""
from ImportProducts import ImportProducts  
class TreeNode():
    """
    Clase que implementa los nodos que un Tree va a manejar, los nodos
    tienen tres atributos, uno de ellos es un objeto y los otros dos
    son apuntadores hacia nodos de derecha o izquierda que tambien se 
    les puede denominar hijos.
    """
    def __init__(self, key):
        """
        Metodo constructor que realiza una instancia de un TreeNode;
        Inizializa sus atributos.
        :key: Objeto a encapsular en un TreeNode.
        :left & right: apuntadores a otros nodos
        """
        __slots__ = {'_key', '_left', '_right'}
        self._key = key
        self._left = None
        self._right = None

    def __str__(self):
        return str(self._key)
        

class HeapTree():
    """
    Clase que implementa un HeapTree.
    """
    def __init__(self):
        """
        Metodo constructor que realiza una instancia de un HeapTree;
        Inicializa su unico atributo raiz(root).
        """
        self._root = None
        self._save = []
        
    def is_empty(self):
        """
        Metodo que permite saber si un HeapTree esta vacio.
        :return: True si el HeapTree esta vacio, o False si la raiz
        guarda objetos o mas nodos.
        :rtype: booleano
        """
        return self._root is None
        
    def __len__(self):
        """Metodo que retorna cuantos nodos tiene el HeapTree
        este metodo cuenta hojas, nodos y raiz, retornando el valor 
        total de estos.
        :return: valor entero con la suma de todos los nodos.
        :rtype: int(entero)
        """
        return self.__size(self._root)    
        
    def __size(self, subtree):
        """Metodo recursivo o ayudante del metodo __len__ este 
        metodo recorre cada nodo, y cuenta la cantidad de los mismos
        sumando mas uno cada vez que un nodo no esta vacio
        :return: valor entero resultante de la suma total en el recorrido
        :rtype: int(entero)
        """
        if subtree is None:
            return 0
        else:
            return(1 + self.__size(subtree._left) +
                   self.__size(subtree._right))
    
    def inodes(self):
        """Metodo que retorna la cantidad de nodos dentro del arbol
        es decir que se retorna la cantidad de nodos que tienen hijos
        por derecha o izquierda. En este metodo no se cuenta a _root como nodo
        :return: Dado que las hojas no son nodos ni el root es nodo
        entonces se resta al total de nodos en el arbol.
        :rtype: int(entero)
        """
        if len(self) <= 2:
            return 0
        return ((len(self))- (1 + self.__leaves(self._root)))
        
    
    def leaves(self, subtree):
        """Metodo que cuenta las hojas del BinaryTree
        :return: Este valor es un entero que se recibe 
        desde la funcion de ayuda para esta misma funcion, el 
        valor se recibe y se retorna.
        """
        return (self.__leaves(subtree))

    def __leaves(self, subtree):
        """Metodo invocado para recorrer el BinaryTree
        este metodo inicia un conteo en cero y empieza a buscar 
        nodos sin hijos a derecha o izquierda, si el condicional
        se cumple entonces se suma mas uno en la lista de hojas
        :return: un entero con la sumas de todas las 
        hojas encontradas dentro del BinaryTree
        :rtype: int(entero)
        """
        count = 0
        if subtree is not None:
            if (subtree == self._root and subtree._left is None and
                subtree._right is None):
                return 0
            if subtree._left is None and subtree._right is None:
                count = 1
            if subtree._left is not None:
                count = count + self.__leaves(subtree._left)
            if subtree._right is not None:
                count = count + self.__leaves(subtree._right)
        return count
                   
    def depth(self, subtree):
        if subtree is None:
            return -1
        else:
            return self.__depth(subtree)
    
        
    def __depth(self,subtree, depth=-1):
        if subtree is None:
            return depth
        return max(self.__depth(subtree._left) + 1,
                   self.__depth(subtree._right) +1)

    def search(self, key_search):
        """Este metodo busca un dato(key_search) dentro del arbol, si
        el dato es encontrado confirma el hallazgo
        :return: Retorna True si el dato ha sido encontrado
                 si el dato no fue encontrado en todo el arbol retorna False
        :rtype: booleano
        """
        return self.__search(self._root, key_search)

    def __search(self, subtree, key_search):
        """Iteracion(ayuda) al metodo search, aquie se busca en todos
        las ramas del arbol el dato a buscar, si el dato se encuentra
        retorna el valor boleano a la funcion principal
        """
        if subtree is not None:
            if subtree._key == key_search:
                return True
            elif subtree._key > key_search:
                return(self.__search(subtree._left, key_search) or
                       self.__search(subtree._right, key_search))
            else:
                return(self.__search(subtree._right, key_search) or
                       self.__search(subtree._left, key_search))
        return False

    def find(self, key_find):
        """Metodo para encontrar un dato dentro del arbol
        este metodo me devuelve el objeto encontrado
        :key_find: Objeto a buscarse
        :return: si el objeto se encuentra retorna el mismo
                 sino es encontrado, retorna None
        :rtype: object
        """
        return self.__find(self._root, key_find)

    def __find(self, subtree, key_find):
        """Iteracion de la funcion find, esta funcion me recibe
        la referencia del arbol y tambien cual es el objeto a encontrar
        :subtree: arbol(sub-arbol) en el que se buscara el objeto
        :key_find: Objeto a buscar
        :return: Object si se encuentra, None sino no se encuentra
        :rtype: Object
        """
        if subtree is not None:
            if subtree._key == key_find:
                return subtree._key
            elif subtree._key > key_find:
                return(self.__find(subtree._left, key_find) or
                       self.__find(subtree._right, key_find))
            else:
                return(self.__find(subtree._right, key_find) or
                       self.__find(subtree._left, key_find))
        return None
                    
    def insert(self, new_key):
        """Metodo para adicionar un objeto o dato en el arbol
        El dato entra a ser comparado con los datos existentes
        y segun su superioridad se hubicara en un nivel dentro
        del HeapTree.
        """
        if self.is_empty():
            self._root = self.__insert(self._root, new_key)
        elif not self.search(new_key):
            self._root = self.__insert(self._root, new_key)
        else:
            print('No se inserto')
        
    def __insert(self, subtree, new_key):
        """Metodo de ayuda en la iteracion para la entrada de nuevo
        dato new_key.
        """
        if self.is_empty():
            self._root = TreeNode(new_key)
        if subtree is None:
            subtree = TreeNode(new_key)          
        elif subtree._left is None:
            subtree._left = self.__insert(subtree._left, new_key)
        elif subtree._right is None:
            subtree._right = self.__insert(subtree._right, new_key)    
        elif ((self.leaves(subtree._left)) / 2) == self.leaves(subtree._right):
            self.__insert(subtree._right, new_key)    
        elif pow(2, (self.depth(subtree))) == self.leaves(subtree):
            self.__insert(subtree._left, new_key)
        elif pow(2, self.depth(subtree._left)) > self.leaves(subtree._left):
            self.__insert(subtree._left, new_key)
        else:
            self.__insert(subtree._right, new_key)   
        self.__balanceoarbol(self._root, None) 
        return subtree
        
    def changeValuesProduct(self):
        self.__balanceoarbol(self._root, None)
        
    def __balanceoarbol(self, subtree, parent):
        if subtree is not None:
            if parent is not None and subtree._key < parent._key:
                iteracionData = parent._key
                parent._key = subtree._key
                subtree._key = iteracionData
                return
            if subtree._left is None and subtree._right is None:
                return
            elif subtree._key > subtree._left._key and subtree._right is None:
                self.__balanceoarbol(subtree._left, subtree)
                self.__balanceoarbol(subtree._right, subtree)
            elif subtree._key > subtree._left._key and subtree._key > subtree._right._key:
                 if subtree._right._key < subtree._left._key:
                     self.__balanceoarbol(subtree._right, subtree)
                     self.__balanceoarbol(subtree._left, subtree)
                 else:
                     self.__balanceoarbol(subtree._left, subtree)
                     self.__balanceoarbol(subtree._right, subtree)
            else:
                self.__balanceoarbol(subtree._right, subtree)
                self.__balanceoarbol(subtree._left, subtree)
        return
        
    def delete(self):
        if not self.is_empty():
            self.__delete(self._root, None)
        
    def __delete(self, subtree, parent):
        if subtree is not None:
            if len(self) == 1:
                self._root = None
            elif subtree._left is None and subtree._right is None:
                self._root._key = subtree._key
                if parent._left == subtree:
                    parent._left = None
                else:
                    parent._right = None
            elif subtree._right is None and subtree._left is not None:
                self._root._key = subtree._left._key
                subtree._left = None
            elif (self.leaves(subtree._left) / 2 == self.leaves(subtree._right) and
                 pow(2, (self.depth(subtree._right))) == self.leaves(subtree._right)):
                self.__delete(subtree._left, subtree)
            elif pow(2, (self.depth(subtree))) == self.leaves(subtree):
                self.__delete(subtree._right, subtree)
            elif pow(2, (self.depth(subtree._left))) > self.leaves(subtree._left):
                self.__delete(subtree._left, subtree)
            elif pow(2, (self.depth(subtree._right))) > self.leaves(subtree._right):
                self.__delete(subtree._right, subtree)
            elif self.depth(subtree) <= 1:
                subtree = self.__delete(subtree._left, subtree)
            else:
                subtree = self.__delete(subtree._right, subtree)
            self.__balanceoarbol(self._root, None)
            return subtree
            
    def saveTree(self):
        saveTreeList = []
        if not self.is_empty():
            saveTreeList.append(self._root._key)
            while not self.is_empty():
                self.__saveTree(self._root, None)
                if self._root is not None:
                    saveTreeList.insert(1, self._root._key)
        return saveTreeList
    
    def __saveTree(self, subtree, parent):
        if subtree is not None:
            if len(self) == 1:
                self._root = None
            elif subtree._left is None and subtree._right is None:
                self._root._key = subtree._key
                if parent._left == subtree:
                    parent._left = None
                else:
                    parent._right = None
            elif subtree._right is None and subtree._left is not None:
                self._root._key = subtree._left._key
                subtree._left = None
            elif (self.leaves(subtree._left) / 2 == self.leaves(subtree._right) and
                 pow(2, (self.depth(subtree._right))) == self.leaves(subtree._right)):
                self.__saveTree(subtree._left, subtree)
            elif pow(2, (self.depth(subtree))) == self.leaves(subtree):
                self.__saveTree(subtree._right, subtree)
            elif pow(2, (self.depth(subtree._left))) > self.leaves(subtree._left):
                self.__saveTree(subtree._left, subtree)
            elif pow(2, (self.depth(subtree._right))) > self.leaves(subtree._right):
                self.__saveTree(subtree._right, subtree)
            elif self.depth(subtree) <= 1:
                subtree = self.__saveTree(subtree._left, subtree)
            else:
                subtree = self.__saveTree(subtree._right, subtree)
            return subtree
