
graph_pattern = '''digraph g {
graph [rankdir = "LR"; dpi=150];
node [fontsize = "16";shape = "ellipse";style="filled";];
edge [arrowhead = none];
%s
}'''

table_pattern  = '''
   %n
    [
        shape = "none"
        label = <<table border="0" cellspacing="0">%s</table>>
    ]
'''
row_pattern = ''' <tr><td port="{0}" border="1">{1} {2}</td></tr> '''
name_row_pattern = ''' <tr><td   bgcolor="red" border="1"><b>{0}</b></td></tr> '''
key_row_pattern = ''' <tr><td  port="{0}"  border="1"><b>{1} {2}</b></td></tr> '''
link_pattern = '''{0}:{1} -> {2}:{3} [color="{4}"; penwidth=4]'''

colors = ["#ff2222","#22ff22","#2222ff","#ff22ff","#ff5522","#22ffff","#aaaaaa",\
           "#aa0000","#00aa00","#0000aa","#aa00aa","#aaaa00","#00aaaa",]

postgres_create_table = '''

CREATE TABLE {0}
(
    {1}
); 

'''

postgres_primary_key  = "{0} {1} PRIMARY KEY"
postgres_unique_key  = "{0} {1} UNIQUE NOT NULL"
postgres_mult_key = "PRIMARY KEY ({0})"
postgres_field  = "{0} {1}"