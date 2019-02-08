from __future__ import print_function
phonetic = {'A':'Alpha', 'B':'Bravo','C':'Charlie', 'D':'Delta', 'E':'Echo', 'F':'Foxtrot', 'G':'Golf',"H":"Hotel", 'I':'India', 'J':'Juliet', 'K':'Kilo', 'L':'Lima', 'M':'Mike', 'N':'November', 'O':'Oscar', 'P':'Papa', 'Q':'Quebec', 'R':'Romeo', 'S':'Sierra', 'T':'Tango', 'U':'Uniform', 'V':'Victor', 'W':'Whiskey', 'X':'Xray', 'Y':'Yankee', 'Z':'Zulu'}


import argparse
import ast
import os
import sys

import astor


class RewriteName(ast.NodeTransformer):
    def visit_Name(self, node):
        if len(node.id) == 1:
            current_name = node.id
            new_name = phonetic[current_name.upper()]
            new_name
            new_node = ast.Name(id=new_name, ctx=node.ctx)
            return ast.copy_location( new_node, node )
        else:
            return node


def main():
    parser = argparse.ArgumentParser(
        description="Convert python source files with single-letter variables into python source files with NATO phonetic alphabet variables"
    )
    parser.add_argument("filepath", metavar="FILEPATH", help="path to Python file input")

    args = parser.parse_args()

    src = open(args.filepath, "r").read()
    tree = ast.parse(src, os.path.basename(args.filepath), 'exec')
    tree = RewriteName().visit(tree)
    transformed_src = astor.to_source(tree)
    print(transformed_src)
