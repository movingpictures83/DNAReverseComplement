from DNAComplement.DNAComplementPlugin import *

class DNAReverseComplementPlugin(DNAComplementPlugin):
    def output(self, filename):
        self.header = self.header.replace("complemented", "reverse complemented")
        self.complement = self.complement[::-1]
        DNAComplementPlugin.output(self, filename)

