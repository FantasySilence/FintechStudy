import os
import matplotlib.pyplot as plt


class FiguresIO:

    """
    实现一个图片IO流类用于保存和读取图片(路径)
    """

    @staticmethod
    def saveFigures(fig_name: str, lecture_name: str) -> None:

        """
        保存图片
        """

        # common文件夹路径
        common_path = os.path.dirname(__file__)
        # 项目根路径
        root_path = os.path.dirname(common_path)
        # figures文件夹路径
        figures_path = os.path.join(root_path, "figures")

        # ------ 创建存放对应lecture图片的文件夹 ------ #
        lecture_fig_path = os.path.join(figures_path, lecture_name)
        if not os.path.exists(lecture_fig_path):
            os.makedirs(lecture_fig_path)
        else:
            pass

        # ------ 保存图片 ------ #
        figsave_path = os.path.join(lecture_fig_path, fig_name)
        print("save figure %s..." % fig_name)
        plt.tight_layout()
        plt.savefig(figsave_path, dpi=300)


    @staticmethod
    def loadFigurePath(fig_name: str) -> str:

        """
        读取图片路径
        """

        # common文件夹路径
        common_path = os.path.dirname(__file__)
        # 项目根路径
        root_path = os.path.dirname(common_path)
        # figures文件夹路径
        figures_path = os.path.join(root_path, "figures")
        return os.path.join(figures_path, fig_name)
