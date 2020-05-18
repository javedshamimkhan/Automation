from pytest import mark


@mark.clstest                   
class tst_cls:

    def test_cls_func(self):
        pass

    def test_cls_func2(self):
        pass


    def test_always_fails(self):
        assert False

    @mark.regression
    def test_uppercase(self):
        assert "loud noises".upper() == "LOUD NOISES"
