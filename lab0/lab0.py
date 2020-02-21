from lab0_utilities import *
        
class Languages:
        def __init__(self):
                self.data_by_year = {}

        def build_trees_from_file(self, file_object):
                # implement
                file_object.readline()
                for line in file_object:
                        value = line.strip().split(',')
                        value[0] = int(value[0])
                        value[2] = int(value[2])
                        if(value[0] not in self.data_by_year):
                                self.data_by_year[value[0]] = BalancingTree(Node(LanguageStat(value[1], value[0], value[2])))
                        else:
                                self.data_by_year[value[0]].balanced_insert(Node(LanguageStat(value[1], value[0], value[2])))
                return self.data_by_year


        def query_by_name(self, language_name):
                # implement
                new_dict = {}
                for i in self.data_by_year:
                        if self.data_by_year[i].root == None:
                                    return False                        
                        peek = self.data_by_year[i].root
                        while(peek != None):
                                if peek.val.name == language_name:
                                        new_dict[peek.val.year] = peek.val.count
                                        break
                                elif peek.val.name > language_name:
                                        peek = peek.left
                                else:
                                        peek = peek.right                               
                return new_dict
                                
        def inorder(self, curr_node):
                if(curr_node is not None):
                        return self.inorder(curr_node.left) + [curr_node.val]+ self.inorder(curr_node.right)
                else:
                        return []
        
        def query_by_count(self, threshold = 0):
                # implement
                new_dict = {}
                array = []
                for i in self.data_by_year:
                        peek = self.data_by_year[i].root
                        array = self.inorder(peek)
                        setr = set(array)
                        for i in setr:
                                if i.count >= threshold:
                                        if(i.year not in new_dict):
                                                new_dict[i.year] = [i.name]
                                        else:
                                                new_dict[i.year].append(i.name)
                return new_dict
                
class BalancingTree:
        def __init__(self, root_node):
                self.root = root_node
        
        def balanced_insert(self, node, curr = None):
                curr = curr if curr else self.root
                self.insert(node, curr) 
                self.balance_tree(node)

        def insert(self, node, curr = None):
                curr = curr if curr else self.root
                # insert at correct location in BST
                if node._val < curr._val:
                        if curr.left is not None:
                                self.insert(node, curr.left)
                        else:
                                curr.left = node
                                node.parent = curr
                else:
                        if curr.right is not None:
                                self.insert(node, curr.right)
                        else:
                                curr.right = node
                                node.parent = curr
                self.update_height(curr)
                return
                
        def update_bf_insert(self, n):
                # Update the balance factors and possibly re-balance
                if n.bf < -1 or n.bf > 1:
                        self.rebalance(n)
                        return
                if n.parent:
                        if n.parent.left is n:
                                n.parent.bf -= 1
                        else:
                               n.parent.bf += 1 
                        #print("{}, {}".format(self.height(n), self.find_balance_factor(n.parent) == n.parent.bf))
                        if not n.parent.bf == 0:
                                self.update_bf_insert(n.parent)

        def rebalance(self, n):
                if n.bf > 0:
                        if n.right and n.right.bf >= 0:
                                self.left_rotate(n)
                        else:
                                self.right_rotate(n.right)
                                self.left_rotate(n)
                else:
                        if n.left and n.left.bf <= 0:
                                self.right_rotate(n)
                        else:
                                self.left_rotate(n.left)
                                self.right_rotate(n)    
                
        def balance_tree(self, node):
                # implement
                self.update_bf_insert(node)
         
        
        def update_height(self, node):
                node.height = 1 + max(self.height(node.left), self.height(node.right))
        
        
        def height(self, node):
                if node is None:
                        return -1
                else:
                        self.update_height(node)
                        return node.height
        
        def left_rotate(self, z):
                y = z.right
                y.parent = z.parent  
                if y.parent is None:
                        self.root = y
                else:
                        if y.parent.left is z:
                                y.parent.left = y
                        elif y.parent.right is z:
                                y.parent.right = y
                z.right = y.left
                if z.right is not None:
                        z.right.parent = z
                y.left = z
                z.parent = y
                self.update_height(z)
                self.update_height(y)
                self.find_balance_factor(z)
                self.find_balance_factor(y)                
                #y.bf = y.bf -1 - min(0, z.bf)
                #z.bf = z.bf -1 + max(0, y.bf)
                
        
        def right_rotate(self, z):
                # implement
                # use left_rotate as a reference
                '''
                z.parent = y
                self.update_height(z)
                self.update_height(y)
                '''
                y = z.left
                y.parent = z.parent  
                if y.parent is None:
                        self.root = y
                else:
                        if y.parent.right is z:
                                y.parent.right = y
                        elif y.parent.left is z:
                                y.parent.left = y
                z.left = y.right
                if z.left is not None:
                        z.left.parent = z
                y.right = z
                z.parent = y
                self.update_height(y)
                self.update_height(z)
                self.find_balance_factor(y)
                self.find_balance_factor(z)
                
                #z.bf = z.bf + 1 - min(0, y.bf)
                #y.bf = y.bf + 1 + max(0, z.bf)
                
        def find_balance_factor(self, node):
                # implement
                if not node:
                    return 0
                else:
                        node.bf = self.height(node.right) - self.height(node.left)
                        return self.height(node.right) - self.height(node.left)
        def preorder(self, curr_node):
                if curr_node!= None:e:
                         
                        if abs(self.find_balance_factor(curr_node)) > 1:
                                return False
                        else:
                                self.preorder(curr_node.left)
                                self.preorder(curr_node.right)
                else:
                        return 
                return True
        def is_balanced(self):
                #implement
                return self.preorder(self.root)
       
