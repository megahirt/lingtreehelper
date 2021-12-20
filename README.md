# lingtreehelper
lingtree.py is a small python module that parses a simple syntax for defining trees and converts it to the more flexible (and complicated) syntax of [LingTree](https://software.sil.org/lingtree/).  ltconvert.py uses the lingtree module to implement a simple command-line conversion program.  See example.txt for an example tree in the simple syntax.

@Author: [Chris Hirt](https://github.com/megahirt)
See www.hirtfamily.net/lingtree for an online web application implementing the module

Tips for writing trees in the simple syntax

    * Describe your tree from the top-down. Define nodes only after they have been declared a child of another node.
    * Define tree nodes in terms of their children, left to right, one definition per line. Use '=' to separate node names from child node names ('=>' and '->' work too)
    * the first line defines the top of the tree
    * Use numbers at the end of node names to distinguish nodes that have the same name. The numbers are only used to reference the node in the definitions. The numbers are removed when generating the LingTree syntax. e.g. (NP1 or NP_1 becomes NP in the LingTree syntax)
    * backslash codes are supported, but are only used on the right side of the equals sign. (i.e. they are not used in node names)
    * when defining the lexical entry and/or gloss at the bottom of your tree, just define them all on one line (e.g. N = \L Hund \G dog )
    * blank lines are ignored
    * lines beginning with # are comments; they are also ignored 

If you have a question or comment, please create a Github Issue