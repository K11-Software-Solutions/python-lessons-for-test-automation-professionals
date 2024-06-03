class ZClass:

    def __init__(self):
        self.data = 'Test'

obj = ZClass()
print('Data attr =',getattr(obj,'data'))
# Default value
print('XData attr =',getattr(obj,'xdata','Not set'))
# No default value
print('ZData attr =',getattr(obj,'zdata'))