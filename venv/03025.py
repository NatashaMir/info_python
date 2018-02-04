class Picture:
    def __init__(self):
        self.name = 'picture'

    def show(self):
        print(self.name)

class Frame:
    def __init__(self, subject):
        self.subject = subject
        self.name = 'frame'

    def show(self):
        self.subject.show()
        print(self.name)

class Pattern:
    def __init__(self, subject):
        self.subject = subject
        self.name = 'pattern'

    def show(self):
        self.subject.show()
        print(self.name)

picture = Picture()
picture.show()
picture_in_frame = Frame(picture)
picture_in_frame.show()
picture_in_frame_pattern = Pattern(picture_in_frame)
picture_in_frame_pattern.show()


