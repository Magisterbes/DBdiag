import numpy as np
import patterns as pt



class table:

    def __init__(self,name,keys,fields,links):
        self.keys = keys
        self.links = links
        self.fields = fields
        self.name = name
    

    def to_yaml(self):
        rows = []

        rows.append("- {0}:".format(self.name))

        if len(self.keys)>0:
            rows.append("  - keys:")
            for key in self.keys:
                rows.append("    - {0}".format(key))
          
        if len(self.fields)>0:
            rows.append("  - fields:")
            for field in self.fields:
                rows.append("    - {0}".format(field))
        
        if len(self.links)>0:
            rows.append("  - links:")
            for link in self.links:
                rows.append("    - {0}".format(link))


        return "\n".join(rows)




    def draw_table(self):

        rows = []
        links = []

        rows.append(pt.name_row_pattern.format(self.name))

        for key in self.keys:

            spl = key.split(",")

            if len(spl) == 2:
                key_name = key.split(",")[0].strip()
                key_type = "(" + key.split(",")[1].strip() + ")"
                rows.append(pt.key_row_pattern.format(key_name,key_name,key_type))
            else:
                rows.append(pt.key_row_pattern.format(key,key,""))

            
        for field in self.fields:
            
            spl = field.split(",")

            if len(spl) == 2:
                field_name = spl[0].strip()
                field_type = "(" + spl[1].strip() + ")"
                rows.append(pt.row_pattern.format(field_name,field_name,field_type))
            else:
                rows.append(pt.row_pattern.format(field,field,""))

        current_color = np.random.randint(0,len(pt.colors)-1)
        for link in self.links:
            spl = link.split("-")
            links.append(pt.link_pattern.format(spl[0].split(".")[0],spl[0].split(".")[1], \
                                            spl[1].split(".")[0],spl[1].split(".")[1], \
                                            pt.colors[current_color]))

        result_table = pt.table_pattern.replace("%n",self.name)
        result_table = result_table.replace("%s","\n".join(rows))
        result_table += "\n".join(links)

        return result_table


    def type_replace(self, in_type):

        if in_type.strip().lower() == "int":
            return "integer"

        if in_type.strip().lower() == "varchar":
            return "varchar (255)"

        if in_type.strip().lower() == "numeric":
            return "numeric (15,5)"

        if in_type.strip().lower() == "float":
            return "numeric (15,5)"

    def to_postgres(self):

        rows = []

        if len(self.keys) ==1:
            typ = self.keys[0].split(",")[1]
            name = self.keys[0].split(",")[0]
            row = pt.postgres_primary_key.format(name,self.type_replace(typ))
            rows.append(row)
        elif len(self.keys) > 1:
            for key in self.keys:
                row =pt.postgres_field.format(key.split(",")[0],self.type_replace(key.split(",")[1]))
                rows.append(row)

            rows.append(pt.postgres_mult_key.format(",".join(keys)))

        for field in self.fields:
            typ = field.split(",")[1]
            name = field.split(",")[0]
            row =pt.postgres_field.format(name,self.type_replace(typ))
            rows.append(row)

        tbl = pt.postgres_create_table.format(self.name,",\n".join(rows).lower())

        return tbl

