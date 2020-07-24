import table as tbl
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import io_part as io
import os
import yaml

graph_pattern = '''digraph g {
graph [rankdir = "LR"; dpi=150];
node [fontsize = "16";shape = "ellipse";style="filled";];
edge [arrowhead = none];
%s
}'''


class diagram:
    def __init__(self):
        self.nodes = []
        pass

    def add_table(self,name,keys,fields,links):
        self.nodes.append(tbl.table(name,keys,fields,links))

    def add_table_from_dict(self, table_dict):
        for table_name, data in table_dict.items():
            params = {'keys':[],'fields':[],'links':[]}
            for node in data:
                node_name = next(iter(node))
                params[node_name] = node[node_name]
            self.add_table(
                name=table_name,
                keys=params['keys'],
                fields=params['fields'],
                links=params['links'],
                )

    def import_yaml(self, yaml_file_name):
        with open(yaml_file_name, 'r') as file:
            data = yaml.load(file, Loader=yaml.FullLoader)
            for table_dict in data:
                self.add_table_from_dict(table_dict)

    def export_yaml(self):
        yaml_view = []

        for table in self.nodes:
            yaml_view.append(table.to_yaml())

        yaml_view = "\n".join(yaml_view)
        io.SaveJustLines([yaml_view],"yaml.yaml",True)
        

    def draw_diagram(self):
        table_groups = []

        for table in self.nodes:
            table_groups.append(table.draw_table())
        
        

        tables = "\n".join(table_groups)
        tables = graph_pattern.replace("%s",tables)

        io.SaveJustLines([tables],"temp.dot",True)
        os.system("dot temp.dot -Tpng -ores.png")
        
        im = mpimg.imread('res.png')
        plt.imshow(im)
        plt.show()

