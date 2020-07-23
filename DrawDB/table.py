table_pattern  = '''
   %n
    [
        shape = "none"
        label = <<table border="0" cellspacing="0">%s</table>>
    ]
'''
row_pattern = ''' <tr><td port="{0}" border="1">{1}</td></tr> '''
name_row_pattern = ''' <tr><td   bgcolor="red" border="1"><b>{0}</b></td></tr> '''
key_row_pattern = ''' <tr><td  port="{0}"  border="1"><b>{1}</b></td></tr> '''
link_pattern = '''{0}:{1} -> {2}:{3}'''

class table:

    def __init__(self,name,keys,fields,links):
        self.keys = keys
        self.links = links
        self.fields = fields
        self.name = name
    

    def draw_table(self):

        rows = []
        links = []

        rows.append(name_row_pattern.format(self.name))

        for key in self.keys:
            rows.append(key_row_pattern.format(key,key))

            
        for field in self.fields:
            rows.append(row_pattern.format(field,field))

        for link in self.links:
            spl = link.split("-")
            links.append(link_pattern.format(spl[0].split(".")[0],spl[0].split(".")[1], \
                                            spl[1].split(".")[0],spl[1].split(".")[1]))

        result_table = table_pattern.replace("%n",self.name)
        result_table = result_table.replace("%s","\n".join(rows))
        result_table += "\n".join(links)

        return result_table
