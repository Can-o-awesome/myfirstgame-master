#(C) 2015 Commando Interactive. All Rights Reserved.
#This is Alpha software, not all the time will it work. Do not expect bugfixes
#right away, as Commando Interactive is only one person, I Can-o-awesome.
#I cannot guarantee that there will be perfect performance.


from direct.showbase.ShowBase import ShowBase



print("This app is (C) Commando Interactive. All Rights Reserved")
 
class MyApp(ShowBase):
 
    def __init__(self):
        ShowBase.__init__(self)
 
        # Load the environment model.
        self.environ = self.loader.loadModel("models/environment")
        # Reparent the model to render.
        self.environ.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.environ.setScale(0.25, 0.25, 0.25)
        self.environ.setPos(-8, 42, 0)
 
 
app = MyApp()
app.run()
