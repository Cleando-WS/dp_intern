import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HTML_PATH = ROOT / "DP_Aktuell_Anita_Cseke.html"


class TestAnitaHtml(unittest.TestCase):
    def setUp(self) -> None:
        self.contents = HTML_PATH.read_text(encoding="utf-8")

    def test_doctype_and_language(self) -> None:
        self.assertTrue(self.contents.lstrip().startswith("<!DOCTYPE html>"))
        lang_match = re.search(r"<html[^>]*lang=\"de\"", self.contents, flags=re.IGNORECASE)
        self.assertIsNotNone(lang_match, "HTML element should declare lang=\"de\"")

    def test_link_constant_is_configured(self) -> None:
        constant_match = re.search(r'const\s+LINK_ZUR_PDF\s*=\s*"([^"]+)";', self.contents)
        self.assertIsNotNone(constant_match, "LINK_ZUR_PDF constant should be defined")
        link_value = constant_match.group(1)
        self.assertTrue(link_value.startswith("https://"), "LINK_ZUR_PDF should point to an https URL")
        self.assertNotEqual(link_value.strip(), "https://example.com", "LINK_ZUR_PDF should not be left as a placeholder")

    def test_primary_button_text(self) -> None:
        self.assertIn("Dienstplan öffnen", self.contents)


if __name__ == "__main__":
    unittest.main()
