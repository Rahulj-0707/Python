# DuckTyping : It is a Concept where type of an object determine by its behaviour , not by its class 

class InkjetPrinter:
    def PrintDocument(self, document):
        print("Inkjet Printer printing : ",document)

class LeaserPrinter:
    def PrintDocument(self, document):
        print("Leaser Printer printing : ",document)

class PDFWriter:
    def PrintDocument(self, document):
        print(f"Saving {document} as PDF")

def StartPrinting(Device):
    Device.PrintDocument("Marvellous Notes")

def main():
    StartPrinting(InkjetPrinter())
    StartPrinting(LeaserPrinter())
    StartPrinting(PDFWriter())

main()