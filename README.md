# Tool to build DB Diagrams in python

1. [Straight code example](#straight code example)
2. [YAML](#yaml)
3. [Export to Postgres](#export to postgres)


**GraphViz used to render diagram. Should be installed. [GraphViz](https://www.graphviz.org/)**

## Straight code example:

```python

import graph as grp

if __name__ == '__main__':
    
    diag = grp.diagram()

    diag.add_table( \
        name = "Person", \
        keys = ["ID"], \
        fields = ["Name","Family"], \
        links = ["Person.ID-Car.PersonID","Person.ID-House.PersonID"] \
        )

    diag.add_table( \
        name = "Car", \
        keys = ["ID"], \
        fields = ["PersonID","CarType"], \
        links = [] \
        )

    diag.add_table( \
        name = "House", \
        keys = ["ID"], \
        fields = ["PersonID","Price","Rooms","Meters"], \
        links = [] \
        )


    diag.draw_diagram()
    pass


```

## YAML:

Data file example. Types are not obligatory:

```yaml
- person:
  - keys:
    - id, int
  - fields:
    - name, varchar
    - family, varchar
  - links:
    - person.id-car.personid
    - person.id-house.personid
- car:
  - keys:
    - id, int
  - fields:
    - personid, int
    - cartype, varchar
    - color, varchar
- house:
  - keys:
    - id, int
  - fields:
    - personid, int
    - price, numeric
    - rooms, int 
    - inches, numeric
```

Python code:

```python
import graph as grp
import yaml

if __name__ == '__main__':
    
    diag = grp.diagram()
    diag.import_yaml(r'base.yaml')
    diag.draw_diagram()

```

Result:

![Result](/DrawDB/res.png)


## Export to Postgres

All types must be introduced

```python
import graph as grp
import yaml

if __name__ == '__main__':
    
    diag = grp.diagram()
    diag.import_yaml(r'base.yaml')
    diag.to_postgres()

```

Result in file "create_sql.sql":
 
```SQL
CREATE TABLE person
(
id integer primary key,
name varchar (255),
family varchar (255)
); 

CREATE TABLE car
(
id integer primary key,
personid integer,
cartype varchar (255),
color varchar (255)
); 

CREATE TABLE house
(
id integer primary key,
personid integer,
price numeric (15,5),
rooms integer,
inches numeric (15,5)
); 

```

