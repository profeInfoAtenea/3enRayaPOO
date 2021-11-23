class Estado():
    def __init__(self, image):
        self.__image = image
    
    def __str__(self):
        return self.__image
    
    def get_image(self):
        return self.__image
    
    def set_image(self, image):
         self.__image = image