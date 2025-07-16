from pathlib import Path


def count_pictures(path: Path, remove_extra: bool = False) -> int:
    """Count how many png or jpg there are in the data folder.

    Args:
        path (Path): the data folder.
        remove_extra (bool, optional): option to delete non picture files. Defaults to False.

    Returns:
        int: amount of data pictures.
    """
    count: int = 0
    amount_removed: int = 0

    queue: list[Path] = [path]

    while queue:
        current: Path = queue.pop(0)

        if current.is_dir():
            for content in current.iterdir():
                queue.append(content)

            continue
        elif current.is_file():
            if current.suffix in [".png", ".jpg"]:
                count += 1
            elif remove_extra:
                Path.unlink(current)
                try:
                    Path.rmdir(current.parent)
                except OSError:
                    pass

                amount_removed += 1

    if remove_extra:
        print(f"removed {amount_removed} extra files.")

    return count


def main():
    data_path = Path.joinpath(Path(__file__).parents[2], "data_storage", "data")
    print(data_path)
    print([_ for _ in data_path.iterdir()])

    print(f"Amount pictures found: {count_pictures(data_path, False)}")


if __name__ == '__main__':
    main()
