"""Check generated pages, references and input/output pairing."""

from html.parser import HTMLParser
import json
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class Links(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.languages = set()
        self.controls = set()

    def handle_starttag(self, tag, attributes):
        attrs = dict(attributes)
        for key in ["href", "src"]:
            if key in attrs:
                self.links.append(attrs[key])
        if "data-language" in attrs:
            self.languages.add(attrs["data-language"])
        if "data-set-language" in attrs:
            self.controls.add(attrs["data-set-language"])


def main():
    pages = [ROOT / "index.html", *sorted(ROOT.glob("20??/*/*/solution.html"))]
    assert len(pages) == len(list(ROOT.glob("20??/*/*/source.json"))) + 1
    for page in pages:
        parser = Links()
        parser.feed(page.read_text())
        assert parser.languages == parser.controls == {"zh", "en"}, page
        for link in parser.links:
            parsed = urlsplit(link)
            if parsed.scheme or parsed.netloc or not parsed.path:
                continue
            target = (page.parent / unquote(parsed.path)).resolve()
            assert target.is_relative_to(ROOT) and target.exists(), (page, link)
    for reference in ROOT.glob("20??/junior/*/reference.json"):
        directory = reference.parent
        target = (directory / json.loads(reference.read_text())["target"]).resolve()
        assert target.is_relative_to(ROOT) and target.parent.name == "senior", reference
        assert (target / "source.json").exists(), target
        assert not any((directory / name).exists() for name in ["solution.py", "solution.html", "lesson.json", "tests"]), directory
    count = 0
    for source in ROOT.glob("20??/*/*/source.json"):
        tests = source.parent / "tests"
        inputs = set(p.stem for p in tests.glob("*.in"))
        outputs = set(p.stem for p in tests.glob("*.out"))
        assert inputs == outputs, tests
        data = json.loads(source.read_text())["test_data"]
        if data["kind"] == "official":
            required = data.get("bundled_input_count", data["official_input_count"])
            assert len(inputs) >= required > 0, source
        count += len(inputs)
    print(f"Checked {len(pages)} bilingual pages, shared references, local links and {count} test pairs.")


if __name__ == "__main__":
    main()
