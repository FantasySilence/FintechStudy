import os
import matplotlib.pyplot as plt


# TODO：更新图片保存工具
def save_fig(fig_id: str, tight_layout: bool=False, 
             suffix: str="png", dpi: int=300) -> None:

    """
    工具函数，用于图片的保存
    """

    subPath = os.path.dirname(os.path.dirname(__file__))
    FIGPATH = os.path.join(subPath, "figures")
    SAVEPATH = os.path.join(FIGPATH, fig_id)
    print("Saving figure", fig_id)
    if tight_layout:
        plt.tight_layout()
    plt.savefig(SAVEPATH + ".png", format=suffix, dpi=dpi)


def getFigPath(fig_id: str) -> str:

    """
    获取图片所在路径
    """

    subPath = os.path.dirname(os.path.dirname(__file__))
    FIGPATH = os.path.join(subPath, "figures")
    SAVEPATH = os.path.join(FIGPATH, fig_id)
    return SAVEPATH
