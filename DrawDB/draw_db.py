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
