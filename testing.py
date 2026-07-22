from cards import fromStr

#consider storing this as separate JSON(s)
cases = {
    "fromStr" : {
        "1h": ("a", "hearts"),
        "10h": ("10", "hearts"),
        "1hh": ("a", "hearts", "holographic"),
        "1hbl": ("a", "hearts", "base", "blue"),
        "1h_bl": ("a", "hearts", "base", "blue"),
        "1hb_l": ("a", "hearts", "base", "blue"),
        "1h_b": ("a", "hearts", "base", "blue"),
        "1h__b": ("a", "hearts", "base", "base", "bonus"),
        "01difopul": ("a", "diamonds", "foil", "purple", "lucky"),
        "01dpp": ("a", "diamonds", "polychrome", "purple"),
        "14DiamondsPolyPurple": ("a", "diamonds", "polychrome", "purple"),
        "adpoP": ("a", "diamonds", "polychrome", "purple"),
        "acdipp": ("a", "diamonds", "polychrome", "purple"),
        "13s_pl": ("k", "spades", "base", "purple", "lucky"),
        "kings puluck": ("k", "spades", "base", "purple", "lucky"),
        "KSPAD-pl": ("k", "spades", "base", "purple", "lucky"),
    }
}

class test_fromStr:
    name = "fromStr"
    def __init__(self, testCases: dict[str, tuple[str, str]] = cases[name]) -> None:
        self.testCases = testCases
    
    def validate(self):
        for k, v in self.testCases.items():
            card = fromStr(k)
            #print(card, v)
            assert card.rank == v[0]
            assert card.suit == v[1]
            if len(v) >= 3:
                assert card.edition == v[2]
            else:
                assert card.edition == "base"
            if len(v) >= 4:
                assert card.seal == v[3]
            else:
                assert card.seal == "base"
            if len(v) >= 5:
                assert card.enhancement == v[4]
            else:
                assert card.enhancement == "base"
        return True

tests = [test_fromStr()]
verbose = True

for t in tests:
    result = t.validate()
    if result:
        if verbose:
            print(f"All test cases for '{t.name}' passed!")
