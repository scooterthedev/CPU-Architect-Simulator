class Engine:
    def __init__(self):
        self.objects = []

    def add_object(self, obj):
        self.objects.append(obj)

    def update(self):
        for obj in self.objects:
            obj.update()

    def render(self):
        for obj in self.objects:
            obj.render() 