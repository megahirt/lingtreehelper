import re

class Node:
    """ The node class defines a lingtree node.  A node knows how to print itself e.g. node.tell() which also prints all of it's descendents  """
    def __init__(self,name):
        self.name = name
        self.children = []
        self.code = ''

    def tell(self):
        # strip off trailing nums
        #name = re.sub(r'_\d+$','',self.name) 
        name = re.sub(r'_?\d+$','',self.name) 

        output = '('

        # print out code
        if self.code:
            output += '\\' + self.code + ' '
        
        output += name + ' '

        for child in self.children:
            output += child.tell()

        output += ')'
        return output

    def addChild(self,node):
        self.children.append(node)

    def setCode(self,code):
        self.code = code


def convert(string):
    """ the convert() function takes simple-formatted string and returns a 'lingtree description string' suitable for pasting into the SIL LingTree program directly
        the string should contain multiple lines, one line per 'node relationship'.  E.G. :
S = NP VP
NP = \L Juan
Juan = \G John
VP = V
V = \L duerme
duerme = \G sleeps

    The left and right side are separated by an equals sign ( = ).  ( => ) and ( -> ) also work fine.  The right side may contain special backslash codes, but the left side should not contain any special codes.
"""
    ref = {}
    top = 0
    for line in string.split('\n'):
        line.strip()
        if line == '': continue
        if line == '\r': continue
        if line.startswith('#'): continue # ignore comment lines

        # normalize 'equals' syntax
        line = line.replace('->','=')
        line = line.replace('=>','=')

        try:
            leftside,rightside = line.split('=')
            leftside = leftside.strip()
            rightside = rightside.strip()

            if top == 0: # remember the top node
                ref[leftside] = Node(leftside)
                top = ref[leftside]

            # the leftside must always already exist in the ref
            if not leftside in ref:
                raise NameError

            # right side contains a special code
            # support multiple codes on right side, like '\L lexical \G gloss'
            if rightside.find('\\') != -1:
                c_last = ''
                for c in rightside.split('\\'):
                    if c == '': continue
                    code = c[0]
                    c = c[1:].strip()
                    ref[c] = Node(c)
                    ref[c].setCode(code)
                    if c_last == '':
                        ref[leftside].addChild(ref[c])
                    else:
                        ref[c_last].addChild(ref[c])
                    c_last = c

            # normal right side
            else:
                for r in rightside.split():
                    r = r.strip()
                    if r == '': continue
                    ref[r] = Node(r)
                    ref[leftside].addChild(ref[r])
        except NameError:
            return "Line may not be in top-down order: %s" % line
        except:
            return "Error occurred processing line: %s" % line

    # tell the top node to print itself
    return top.tell() 
