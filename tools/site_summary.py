#!/usr/bin/env python3
# -*- coding: utf-8 -*-


SITE_INFO = {
    "title": "爱游戏",
    "url": "https://m-zh-aiyouxi.com.cn",
    "keywords": ["爱游戏", "休闲", "手游", "在线娱乐"],
    "tags": ["游戏平台", "手游", "休闲游戏", "HTML5"],
    "description": "爱游戏是一个提供多种在线休闲手游的轻量级平台，用户可直接在浏览器中游玩，无需下载安装。"
}

SUMMARY_STRUCTURE = [
    ("站点名称", "title"),
    ("核心关键词", "keywords"),
    ("标签", "tags"),
    ("访问地址", "url"),
    ("简短说明", "description"),
]


def format_text(header: str, content: str, width: int = 72) -> str:
    """返回一行格式化输出，header 固定宽度，content 自动换行"""
    prefix = f"{header}："
    indent = len(prefix)
    lines = []
    while content:
        if len(content) <= width - indent:
            lines.append(content)
            break
        cut = (width - indent)
        space = content.rfind(" ", 0, cut)
        if space == -1:
            space = cut
        lines.append(content[:space])
        content = content[space:].lstrip()
    result = []
    for i, line in enumerate(lines):
        if i == 0:
            result.append(f"{prefix}{line}")
        else:
            result.append(" " * indent + line)
    return "\n".join(result)


def render_summary(data: dict) -> str:
    """根据预定义结构生成结构化摘要文本"""
    output_lines = []
    output_lines.append("=" * 72)
    output_lines.append("站点摘要".center(68))
    output_lines.append("=" * 72)
    for header, key in SUMMARY_STRUCTURE:
        value = data.get(key, "")
        if isinstance(value, list):
            value_str = "，".join(value)
        else:
            value_str = str(value)
        line = format_text(header, value_str)
        output_lines.append(line)
    output_lines.append("=" * 72)
    output_lines.append(f"生成时间: 即时生成，数据版本 v1.0")
    output_lines.append("=" * 72)
    return "\n".join(output_lines)


def get_site_summary() -> dict:
    """返回站点信息字典（可扩展为读取配置或外部数据）"""
    return dict(SITE_INFO)


def main():
    site = get_site_summary()
    summary_text = render_summary(site)
    print(summary_text)
    return summary_text


if __name__ == "__main__":
    main()