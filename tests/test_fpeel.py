from fpeel import is_ar_archive, say_hello


def test_is_ar_archive_passes():
    assert is_ar_archive([0x21, 0x3C, 0x61, 0x72, 0x63, 0x68, 0x3E,
                          0x0a]) == True


def test_is_ar_archive_fails():
    assert is_ar_archive([
        0x21,
        0x3C,
        0x61,
        0x72,
        0x63,
        0x68,
        0x3E,
    ]) == False


def test_say_hello():
    assert say_hello() == 'Like an onion.'
