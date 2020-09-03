# Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter

class BinaryTreeNode:
    def __init__(self, value, weight, left=None, right=None):
        self.value = value
        self.weight = weight
        self.left = left
        self.right = right

    @staticmethod
    def start_huffman(st):
        obj_list = []
        st_counter = Counter(st)
        st_list = st_counter.most_common()
        for el in st_list:
            obj = BinaryTreeNode(el[0], el[1])
            obj_list.append(obj)
        huffman_tree = BinaryTreeNode._huffman_tree_creating(obj_list)[0]
        st_huffman_symbol_code = {tpl[0]:BinaryTreeNode._huffman_encoding(huffman_tree, tpl[0])
                           for tpl in st_list}
        st_huffman_code = f'{st}: '
        for el in st:
            st_huffman_code = f'{st_huffman_code}{st_huffman_symbol_code.get(el)}'
        st_huffman_code = f'{st_huffman_code}\n{st_huffman_symbol_code}'
        return st_huffman_code

    @staticmethod
    def _huffman_tree_creating(obj_list, h=0):

        if len(obj_list) == 1:
            return obj_list

        new_weignt = obj_list[-1].weight + obj_list[-2].weight
        new_value = f'{obj_list[-1].value}{obj_list[-2].value}'
        val_left = obj_list[-1].value
        val_right = obj_list[-2].value
        for i, el in enumerate(obj_list):
            if el.weight < new_weignt:
                obj_list.insert(i, BinaryTreeNode(new_value, new_weignt, obj_list[-1], obj_list[-2]))
                break
        obj_list.pop()
        obj_list.pop()
        return BinaryTreeNode._huffman_tree_creating(obj_list, h)

    def _huffman_encoding(self, symbol, code=''):
        if self.right is None and self.left is None:
            return code
        if symbol in self.left.value:
            return BinaryTreeNode._huffman_encoding(self.left, symbol, f'{code}0')
        else:
            return BinaryTreeNode._huffman_encoding(self.right, symbol, f'{code}1')


if __name__ == '__main__':
    user_str = input('Введите строку для кодирования по алгоритму Хафмана: ')
    print(BinaryTreeNode.start_huffman(user_str))
