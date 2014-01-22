'''This is a library for Binary Search Trees
	Each Node has three fields

	Node
	----

	1. Data
	2. Left Pointer (Pointer to left Child)
	3. Right Pointer (Pointer to right Child)
	4. Level (Denotes the level of the tree)


	Class BST has the following methods
	-----------------------------------

	1. Insert a new node in a BST		(DONE)
	2. Delete a node from a BST	
	3. Inorder Traversal of a BST 		(DONE)
	4. Preorder Traversal of a BST		(DONE)
	5. Postorder traversal of a BST		(DONE)
	6. Leveloredr traversal of a BST	(DONE)
	7. Mirror of a BST					(DONE)
	8. Search for an Element in a BST	(DONE)
	9. Lowest Common Ancestor of a BST	(DONE)
	10. Height of a BST					(DONE)
	11. Circumference of a BST 			(DONE)
	12. Diameter of a BST				(DONE)

'''


class Node():
	def __init__(self,data):
		self.data = data
		self.right  = None
		self.left = None
		self.level = None

	def __str__(self):
		return str(self.data)

class BST():

	def __init__(self):
		self.root = None

	def Insert(self,val):

		''' Insert an element in a BST in O(log n)
			No Duplicates are allowed in this case
		'''
		
		if self.root == None:
			self.root = Node(val)
		else:
			present = self.root
			while 1:
				if val < present.data:
					if present.left:
						present = present.left
					else:
						present.left = Node(val)
						break

				elif val > present.data:
					if present.right:
						present = present.right
					else:
						present.right = Node(val)
						break
				else:
					break
		return self.root

	def Search(self,val,node):
		if node != None:
			if val == node.data:
				return node
			elif val < node.data:
				self.Search(val,node.left)
			else:
				self.Search(val,node.right)
		else:
			return -1

	def Height(self,node):
		if node == None:
			return 0 
		else:
			return 1 + max(self.Height(node.left),self.Height(node.right))

	def Diameter(self,node,val):
		if node != None:
			val =  max( self.Height(node.left) + self.Height(node.right) + 1,val)
			self.Diameter(node.left,val)
			self.Diameter(node.right,val)
			return val


	def Inorder(self,node):

		''' Recursive Inorder Traversal of BST'''
		if node != None:
			self.Inorder(node.left)
			print (node.data)
			self.Inorder(node.right)


	def Postorder(self,node):

		''' Recursive Postorder Traversal of BST'''
		if node != None:
			self.Postorder(node.left)
			self.Postorder(node.right)
			print (node.data)


	def Preorder(self,node):

		''' Recursive Preorder Traversal of BST'''
		if node != None:
			print (node.data)
			self.Preorder(node.left)
			self.Preorder(node.right)

	def LeafNodes(self,ROOT,Child):
		if ROOT != None:
			if ROOT.left == None and ROOT.right == None:
				Child.append(ROOT.data)
			self.LeafNodes(ROOT.left,Child)
			self.LeafNodes(ROOT.right,Child)
			return Child

	def Circumference(self):
		LEFT = []
		RIGHT = []
		Root = self.root
		while Root.left != None:
			LEFT.append(Root.left.data)
			Root = Root.left
		Root = self.root
		while Root.right != None:
			RIGHT.append(Root.right.data)
			Root = Root.right
		RIGHT.reverse()
		Root = self.root
		CHILD = self.LeafNodes(Root,[])
		if LEFT[-1] == CHILD[0]:
			LEFT = LEFT + CHILD[1:]
		else:
			LEFT = LEFT + CHILD
		if LEFT[-1] == RIGHT[0]:
			LEFT = LEFT + RIGHT[1:]
		else:
			LEFT = LEFT + RIGHT
		return LEFT + [self.root.data]

	def LCA(self,val1,val2,ROOT):

		''' Lowest Common Ancestor in a BST'''
		if ROOT != None:
			if val1 < ROOT.data and val2 > ROOT.data:
				print  ROOT.data
			elif val1 < ROOT.data and val2 < ROOT:
				self.LCA(val1, val2, ROOT.left)
			else:
				self.LCA(val1, val2, ROOT.left)


	def Mirror(self,node):

		''' Recursive Mirror of BST'''
		if node != None:
			TEMP  = node.left
			node.left = node.right
			node.right = TEMP
			self.Mirror(node.left)
			self.Mirror(node.right)


	def bft(self):

		''' Breadth First Search in a BST'''
		self.root.level = 0
		queue = [self.root]
		out = []
		current_level = self.root.level
		while len(queue) > 0:
			current_node = queue.pop(0)
			if current_node.level > current_level:
				current_level += 1
				
				out.append("\n")
			out.append(str(current_node.data) + " ")
			if current_node.left:
				current_node.left.level = current_level + 1
				queue.append(current_node.left)
			if current_node.right:
				current_node.right.level = current_level + 1
				queue.append(current_node.right)

        	print "".join(out)







#A = [8,4,10,7,2,1,3,9,17]
A = [10,4,3,5,0,-1,2,9,8,12,14,11,7,6]
T = BST()
for i in A:
	Root = T.Insert(i)
print 'Test for Correct insertion'
print T.Diameter(Root,0)
print T.Circumference()
print T.Height(Root)
ROOT = Root
#T.Search(7,ROOT)
#T.bft()
print '.......'
T.LCA(1,7,ROOT)
#T.Search(7,ROOT)

#T.Mirror(ROOT);T.bft()


			

