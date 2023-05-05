class Television:
    """
    creates Television
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 10
    MIN_CHANNEL = 0
    MAX_CHANNEL = 2

    def __init__(self,name: str = "NA", status: bool = False, mute: bool = False, vol: int = 0, channel: int = 0) -> None:
        """
        sets up Television
        :param name: The name of the Television. Base = "NA"
        :param status: If Television is on or off. Base = "False"
        :param mute: If Television is muted. Base = "False"
        :param vol: Volume of Television. Base = "0"
        :param channel: Channel of Television. Base = "0"
        """
        self.__name = name
        self.__status = status
        self.__muted = mute
        self.__volume = vol
        self.__channel = channel

    def power(self) -> None:
        """
        changes status of Television
        :return: None
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        requires status to be True
        changes muted of Television
        :return: None
        """
        if self.__status:
            self.__muted = not self.__muted

    def channel_up(self) -> None:
        """
        requires status to be True
        increases channel of Television
        :return: None
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self) -> None:
        """
        requires status to be True
        decreases channel of Television
        :return:
        """
        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1

    # def change_volume(self, volume) -> None:
    #     """
    #     requires status to be False
    #     sets volume to desired volume
    #     :param volume: The desired volume
    #     """
    #     if self.__status:
    #         self.__volume = volume
    #         self.__muted = False

    def get_storage(self) -> list:
        """
        returns everything for Television in code format
        :return: list of private variables
        """
        return [self.__name, self.__status, self.__muted, self.__volume, self.__channel]

    def volume_up(self) -> None:
        """
        requires status to be True
        increases volume of Television
        makes muted False
        :return: None
        """
        if not self.__volume == Television.MAX_VOLUME and self.__status:
            self.__volume += 1
            self.__muted = False

    def volume_down(self) -> None:
        """
        requires status to be True
        decreases volume of Television
        makes muted False
        :return: None
        """
        if not self.__volume == Television.MIN_VOLUME and self.__status:
            self.__volume -= 1
            self.__muted = False

    def get_channel(self) -> int:
        """
        returns the channel for the television
        :return: an int of the channel
        """
        return self.__channel

    def get_muted(self) -> bool:
        """
        returns if the tv is muted or not
        :return: a bool of if the tv is muted or not
        """
        return self.__muted

    def get_status(self) -> bool:
        """
        returns if the tv is on or not
        :return: a bool of if the tv is on or not
        """
        return self.__status

    def get_volume(self) -> int:
        """
        returns the volume of the tv
        :return: an int representing the volume
        """
        return self.__volume
    def __str__(self) -> str:
        """
        returns everything for Television in print format
        :return: str of private variables
        """
        if self.__muted:
            return f"TV Name = {self.__name}\nPower = {self.__status}\nChannel = {self.__channel}\nVolume = 0."
        else:
            return f"TV Name = {self.__name}\nPower = {self.__status}\nChannel = {self.__channel}\nVolume = {self.__volume}."
