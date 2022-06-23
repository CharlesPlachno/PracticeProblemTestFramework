from problems.palindromeNumber import isPalindrome

def test_normal():
    assert isPalindrome("abba")

def test_empty():
    assert isPalindrome("")

def test_false():
    assert not isPalindrome("false")

def test_single():
    assert isPalindrome("a")

def test_long():
    assert isPalindrome("ababababababababababababababababbabababababababababababababababa")