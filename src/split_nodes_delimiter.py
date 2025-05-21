from textnode import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    
    return_list = []
    
    for node in old_nodes:
        if node.text_type != "TEXT":
            return_list.append(node)
        
        else:    
            split_list = node.text.split(delimiter)
            if len(split_list) % 2 == 0:
                raise Exception("Error: detected unclosed delimiter pair")

            if len(split_list) == 1:
                # delimiter is not found; split did not occur
                return_list.append(TextNode(node.text, TextType.TEXT))

            else:
                # split occurred and delimiters are valid pairs
                for index, part in enumerate(split_list):
                    if index % 2 == 0: # even index
                        return_list.append(TextNode(part, TextType.TEXT))

                    else: # odd index
                        return_list.append(TextNode(part, text_type))

    return return_list
