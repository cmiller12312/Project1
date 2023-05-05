import tele
import pytest

class Test:
    def setup_method(self):
        self.tele1 = tele.Television()
        self.tele2 = tele.Television()

    def teardown_method(self):
        del self.tele1
        del self.tele2

    def test_power(self):
        self.tele1.power()
        assert self.tele1.get_storage()[1] is True
        assert self.tele2.get_storage()[1] is False

    def test_channel(self):
        self.tele1.power()
        self.tele2.power()
        self.tele1.channel_up()
        self.tele1.channel_up()
        assert self.tele1.get_storage()[3] == 2
        self.tele1.channel_down()
        assert self.tele1.get_storage()[3] == 1
        self.tele2.channel_down()
        assert self.tele2.get_storage()[3] == 4
        self.tele2.channel_up()
        assert self.tele2.get_storage()[3] == 0

    def test_name(self):
        assert self.tele1.get_storage()[0] == "NA"
        self.tele3 = tele.Television("Test")
        assert self.tele3.get_storage()[0] == "Test"
        del self.tele3

if __name__ == "__main__":
    pytest.main()