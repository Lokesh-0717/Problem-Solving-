class Music:
    name="Director"
    def Set(self,name):
        self.name=name
        
bgm=Music()
print(bgm.name)

bgm.Set('Thaman')
print(bgm.name)
