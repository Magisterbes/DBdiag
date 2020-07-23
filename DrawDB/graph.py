import table as tbl
import matplotlib.image as mpimg
import matplotlib.pyplot as plt
import io_part as io
import os

graph_pattern = '''digraph g {
graph [rankdir = "LR"];
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

