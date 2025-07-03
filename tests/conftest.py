import os
import pytest


def pytest_exception_interact(node, call, report):
    if report.failed:
        page = node.funcargs.get("browser_page", None)
        if page:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)
            file_name = f"{node.name}.png"
            file_path = os.path.join(screenshots_dir, file_name)
            page.screenshot(path=file_path)
            print(f"::error file={file_path}::Screenshot saved at {file_path}")
