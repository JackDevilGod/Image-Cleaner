from PIL import Image
from pathlib import Path
from torch.utils.data import Dataset


class PicturePathsDataset(Dataset):
    def __init__(self, paths: tuple[Path]) -> None:
        self.paths: tuple[Path] = paths

    def __len__(self) -> int:
        return len(self.paths)

    def __getitem__(self, index: int) -> Image.Image:
        return Image.open(self.paths[index])
