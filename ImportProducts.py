class ImportProducts():
    def __init__(self, code, name,
                 country, cost, cant,
                 arancel, unit):
        self.codeProduct = int(code)
        self.nameProduct = str(name)
        self.countryProduct = str(country)
        self.unitProduct = str(unit)
        self.costProduct = float(cost)
        self.cantProduct = float(cant)
        self.arancelProduct = arancel
        
    def __str__(self):
        return(str(self.codeProduct) + "|" +
               str(self.nameProduct) + "|" +
               str(self.countryProduct) + "|" +
               str(self.costProduct) + "|" +
               str(self.cantProduct) + "|" +
               str(self.arancelProduct))

    def __eq__(self, other):
        if (isinstance(self, type(other)) and
           self.codeProduct == other.codeProduct and
           self.nameProduct == other.nameProduct and
           self.countryProduct == other.countryProduct):
            return True

    def __lt__(self, other):
        if self.codeProduct < other.codeProduct:
            return True
        elif (self.codeProduct == other.codeProduct and
             self.nameProduct < other.nameProduct):
            return True
        elif (self.codeProduct == other.codeProduct and
             self.nameProduct == other.nameProduct and
             self.cantProduct < other.cantProduct):
            return True
        elif (self.codeProduct == other.codeProduct and
             self.nameProduct == other.nameProduct and
             self.cantProduct == other.cantProduct and
             self.costProduct < other.costProduct):
            return True
        elif (self.codeProduct == other.codeProduct and
             self.nameProduct == other.nameProduct and
             self.cantProduct == other.cantProduct and
             self.costProduct == other.costProduct and
             self.arancelProduct < other.arancelProduct):
            return True

    def __gt__(self, other):
        if self.codeProduct > other.codeProduct:
            return True
        elif (self.codeProduct == other.codeProduct and
             self.nameProduct > other.nameProduct):
            return True
        elif (self.codeProduct == other.codeProduct and
             self.nameProduct == other.nameProduct and
             self.cantProduct > other.cantProduct):
            return True
        elif (self.codeProduct == other.codeProduct and
             self.nameProduct == other.nameProduct and
             self.cantProduct == other.cantProduct and
             self.costProduct > other.costProduct):
            return True
        elif (self.codeProduct == other.codeProduct and
             self.nameProduct == other.nameProduct and
             self.cantProduct == other.cantProduct and
             self.costProduct == other.costProduct and
             self.arancelProduct > other.arancelProduct):
            return True
