import numpy as np

from PIL import Image
from pathlib import Path
from torch.utils.data import Dataset


class PicturePathsDataset(Dataset):
    def __init__(self, path: Path) -> None:
        self.paths: tuple[Path, ...] = self._get_image_paths(path)

    def _get_image_paths(self, root: Path) -> tuple[Path, ...]:
        image_paths: list[Path] = list()

        queue: list[Path] = [root]

        while queue:
            current: Path = queue.pop(0)

            if current.is_dir():
                queue += list(current.iterdir())
            elif current.suffix.endswith((".png", ".jpg")):
                image_paths.append(current)

        return tuple(image_paths)

    def __len__(self) -> int:
        return len(self.paths)

    def __getitem__(self, index: int) -> np.ndarray:
        loaded_image = Image.open(self.paths[index]).convert("RGB")
        rgb_image = loaded_image.convert("RGB")

        return np.array(rgb_image)


def main():
    from random import shuffle

    test = PicturePathsDataset(Path())

    print(len(test))

    import matplotlib.pyplot as plt

    index_list = [_ for _ in range(len(test))]
    shuffle(index_list)
    for u in index_list:
        plt.imshow(test[u])
        plt.show()


if __name__ == '__main__':
    main()
