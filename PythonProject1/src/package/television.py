class TelevisionError(Exception):
    def __init__(self, message):
        super().__init__(message)

class Television:
    def __init__(self):
        self.is_on = True
        self.volume_level = 0
        self.channel_level = 0

    def turn_on(self):
        self.is_on = True

    def turn_off(self):
        self.is_on = False

    def volume_up(self):
        if self.is_on and 0 < self.volume_level <= 100:
            self.volume_level += 1
        else:
            raise TelevisionError("TV must be turned on")

    def volume_down(self):
        if self.is_on:
            self.volume_level -= 1
        else:
            raise TelevisionError("TV must be turned on")

    def channel_down(self):
        if self.is_on:
            self.channel_level -= 1
        else:
            raise TelevisionError("TV must be turned on")

    def channel_up(self):
        if self.is_on:
            self.channel_level += 1
        else:
            raise TelevisionError("TV must be turned on")

    def set_channel_level(self, channel_level):
        if self.is_on and 0 <= channel_level <= 100:
            self.channel_level = channel_level
        else:
            raise TelevisionError("Expected channel_level to be between 0 and 100 and TV must be turned on")

    def mute_and_unmute_volume(self,level):
        if self.is_on and self.volume_level == 0:
            

        elif self.is_on and self.volume_level :


