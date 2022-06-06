class MyRouter(object):
    "This is a class that describes the characteristics of a router."
    def __init__(self, routername, model, serialno, ios):
        self.routername = routername
        self.model = model
        self.serialno = serialno
        self.ios = ios
        
    def print_router(self, manuf_date):
        print("The router name is: ", self.routername)
        print("The router model is: ", self.model)
        print("The router serial number is: ", self.serialno)
        print("The router IOS version is: ", self.ios)
        print("The model and date combined is: ", self.model + manuf_date)
