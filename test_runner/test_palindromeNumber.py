from problems.palindromeNumber import isPalindrome

def test_normal():
    assert isPalindrome(1221)

def test_false():
    assert not isPalindrome(123)

def test_single():
    assert isPalindrome(1)

def test_long():
    assert isPalindrome(12345678901234567890123456789012345678900987654321098765432109876543210987654321)