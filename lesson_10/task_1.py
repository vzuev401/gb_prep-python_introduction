from pathlib import Path


def fill_with_9dirs(path=Path()):
    for x in range(1, 10):
        path.joinpath(f'dir_{x}').mkdir()


def remove_all_dirs_by_template(path=Path(), template='dir_*/'):
    for sub_path in path.glob(template):
        if sub_path.is_dir():
            sub_path.rmdir()
