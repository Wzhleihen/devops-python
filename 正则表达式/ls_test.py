import argparse_ls


def test_ls_lh():
    args = argparse_ls.parse_args(['/etc', '-l', '-h'])

    assert args.path == '/etc'
    assert args.l
    assert args.h
    assert not args.all


def test_ls_all():
    args = argparse_ls.parse_args(['.', '-a'])

    assert args.all
    assert not args.l


def test_default_path():
    args = argparse_ls.parse_args([])

    assert args.path == '.'