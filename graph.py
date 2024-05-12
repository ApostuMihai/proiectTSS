from graphviz import Digraph

dot = Digraph()

dot.node('A', 'Start')
dot.node('B', 'Is Palindrome?')
dot.node('C', 'Is Isogram?')
dot.node('D', 'End')

dot.edges(['AB', 'AC'])
dot.edge('B', 'D', label='Yes')
dot.edge('B', 'D', label='No', constraint='false')
dot.edge('C', 'D', label='Yes')
dot.edge('C', 'D', label='No', constraint='false')

dot.render('output.gv', view=True)  
