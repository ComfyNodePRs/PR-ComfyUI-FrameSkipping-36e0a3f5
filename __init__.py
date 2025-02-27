# __init__.py
from .FrameSkipping import FrameSkipping
from .FrameTruncating import FrameTruncating
from .MaskFrameSkipping import MaskFrameSkipping
from .WhiteMaskGenerator import WhiteMaskGenerator
from .IntOperationsNode import IntOperationsNode

NODE_CLASS_MAPPINGS = {
    "FrameSkipping": FrameSkipping,
    "FrameTruncating": FrameTruncating,  # 添加新的组件到节点类映射
    "MaskFrameSkipping": MaskFrameSkipping,
    "WhiteMaskGenerator": WhiteMaskGenerator,
    "IntOperationsNode": IntOperationsNode,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "FrameSkipping": "Frame Skipping",
    "FrameTruncating": "Frame Truncating",
    "MaskFrameSkipping": "Mask Frame Skipping",  # 添加新的组件到节点显示名称映射
    "WhiteMaskGenerator": "White Mask Generator",
    "IntOperationsNode": "Int Operations",
}

__all__ = ['NODE_CLASS_MAPPINGS', 'NODE_DISPLAY_NAME_MAPPINGS']
