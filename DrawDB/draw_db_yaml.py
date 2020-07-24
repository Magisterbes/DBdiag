import graph as grp
import yaml

if __name__ == '__main__':
    
    diag = grp.diagram()
    diag.import_yaml(r'base.yaml')
    diag.draw_diagram()
