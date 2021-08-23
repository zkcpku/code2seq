import anytree
from anytree import AnyNode, RenderTree
from anytree.exporter import DictExporter
from anytree.importer import DictImporter
import pickle
from tqdm import tqdm


# path_file = '/home/zhangkechi/workspace/code2seq-master/data/my_dataset_javasmall/my_dataset_javasmall.test.c2s'
# save_file = '/home/zhangkechi/workspace/code2seq-master/data/my_dataset_javasmall/my_dataset_javasmall.test_ast.pkl'

path_file = '/home/zhangkechi/workspace/code2seq-master/data/my_dataset_javasmall/my_dataset_javasmall.train.c2s'
save_file = '/home/zhangkechi/workspace/code2seq-master/data/my_dataset_javasmall/my_dataset_javasmall.train_ast.pkl'

# path_file = '/home/zhangkechi/workspace/code2seq-master/data/my_dataset_javasmall/my_dataset_javasmall.val.c2s'
# save_file = '/home/zhangkechi/workspace/code2seq-master/data/my_dataset_javasmall/my_dataset_javasmall.val_ast.pkl'


def path2ast_single(path_list):
    node_dict = {}
    def get_node(node_name, node_type = 'leaf',parent_node = None):
        if node_name in node_dict:
            return node_dict[node_name]
        else:
            node_dict[node_name] = AnyNode(name = node_name, type = node_type, parent=parent_node, index = len(node_dict))
            return node_dict[node_name]

    method_names = path_list[0].split('|')
    all_paths = path_list[1:]
    for path in all_paths:
        leaf_and_path = path.split(',')
        leaf_node = leaf_and_path[0]
        path_node = leaf_and_path[1]
        path_node_list = path_node.split('|')[::-1]
        this_node = None
        for e in path_node_list:
            this_node = get_node(e, 'ast', this_node)
        get_node(leaf_node, 'leaf', this_node)
    return method_names, node_dict, all_paths[0].split(',')[1].split('|')[-1]


def save_pkl(path_file ,save_file):

    exporter = DictExporter()
    importer = DictImporter()
    with open(path_file,'r') as f:
        lines = f.readlines()

    all_data = []
    for line in tqdm(lines):
        # print(line.strip().split())
        method_names, node_dict, root_name = path2ast_single(line.strip().split())
        # print(node_dict[root_name])
        # r = RenderTree(node_dict[root_name])
        # print(method_names)
        # print(r)
        root = node_dict[root_name]
        tree = exporter.export(root)
        all_data.append((method_names, tree))
        # print(method_names)
        # print(RenderTree(importer.import_(tree)))
    

    # break
    with open(save_file,'wb') as f:
        pickle.dump(all_data, f)


def load_pkl(save_file):
    importer = DictImporter()
    with open(save_file,'rb') as f:
        all_data = pickle.load(f)
    print(len(all_data))
    method_names = all_data[0][0]
    tree = all_data[0][1]
    print(method_names)
    print(RenderTree(importer.import_(tree)))
    return all_data

# save_pkl(path_file, save_file)
load_pkl(save_file)
