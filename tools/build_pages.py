"""Build offline bilingual HTML pages from per-problem lesson.json files."""

from html import escape
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIELDS = {"summary", "topics", "steps", "example", "correctness", "complexity", "pitfalls"}
LABELS = {
    "zh": ["题目在问什么", "考查知识点", "一步一步想", "用例子走一遍", "为什么这样做是对的", "运行时间与内存", "容易出错的地方", "Python 3 解法", "官方题目", "测试数据"],
    "en": ["What are we asked to do?", "Knowledge and skills", "Think step by step", "Walk through an example", "Why does this work?", "Time and memory", "Common mistakes", "Python 3 solution", "Official problem", "Test data"],
}


def panel(language, body):
    return f'<div data-language="{language}"{ " hidden" if language == "en" else ""}>{body}</div>'


def paragraph(text):
    return "".join(f"<p>{escape(p)}</p>" for p in text.split("\n") if p)


def shell(title, body, prefix):
    return f'''<!doctype html>
<html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>{escape(title)} · CCC Solutions</title><link rel="stylesheet" href="{prefix}assets/site.css">
<script src="{prefix}assets/language.js" defer></script></head><body><main>
<header><div class="topbar"><a class="brand" href="{prefix}index.html">CCC / Solutions</a>
<div class="languages" role="group" aria-label="Language / 语言"><button data-set-language="zh" aria-pressed="true">中文</button><button data-set-language="en" aria-pressed="false">English</button></div></div>
<h1>{escape(title)}</h1></header>{body}
<footer>CEMC / University of Waterloo · <a href="https://cemc.uwaterloo.ca/resources/past-contests?contest_category=29">Official contest archive</a> · <a href="https://dmoj.ca/">DMOJ</a></footer>
</main></body></html>'''


def read_lesson(directory):
    path = directory / "lesson.json"
    if not path.exists():
        return None
    lesson = json.loads(path.read_text())
    for language in ["zh", "en"]:
        if set(lesson[language]) != FIELDS:
            raise ValueError(f"Missing or extra lesson fields: {path}, {language}")
        for field in FIELDS:
            value = lesson[language][field]
            if field in {"topics", "steps", "pitfalls"}:
                if not isinstance(value, list) or not value or not all(isinstance(t, str) and t.strip() for t in value):
                    raise ValueError((path, language, field))
            elif not isinstance(value, str) or not value.strip():
                raise ValueError((path, language, field))
    if not (directory / "solution.py").exists():
        raise ValueError(f"Lesson without solution: {directory}")
    return lesson


def build_problem(directory):
    year, division, number = directory.relative_to(ROOT).parts
    source = json.loads((directory / "source.json").read_text())
    statement = (directory / "problem.txt").read_text()
    lesson = read_lesson(directory)
    heading = " ".join(statement.split("Problem Description", 1)[0].split())
    title = lesson["title"] if lesson else heading.split(":", 1)[-1].strip()
    title = f"{year} {number} · {title}"
    cases = sorted((directory / "tests").glob("*.in"))
    body = f'<p class="eyebrow">{year} / {division} / {number}</p>'
    sample = next((p for p in cases if "sample" in p.stem.lower() or "samp" in p.stem.lower()), None)
    for language in ["zh", "en"]:
        labels = LABELS[language]
        content = f'<nav class="links"><a href="problem.txt">{labels[8]}</a><a href="../../_sources/{division}.pdf">PDF</a><a href="https://dmoj.ca/problem/ccc{year[-2:]}{number.lower()}">DMOJ</a></nav>'
        if lesson:
            for field, heading in zip(["summary", "topics", "steps", "example", "correctness", "complexity", "pitfalls"], labels):
                value = lesson[language][field]
                if isinstance(value, list):
                    tag = "ol" if field == "steps" else "ul"
                    text = f'<{tag}>' + "".join(f"<li>{escape(item)}</li>" for item in value) + f'</{tag}>'
                else:
                    text = paragraph(value)
                content += f'<section class="card"><h2>{heading}</h2>{text}</section>'
            code = escape((directory / "solution.py").read_text())
            content += f'<section class="card"><h2>{labels[7]}</h2><a href="solution.py">solution.py</a><pre><code>{code}</code></pre></section>'
        else:
            text = "题目与数据已整理。解法和双语讲解尚未完成，按年份逐年补充。" if language == "zh" else "The problem and data are organized. The solution and bilingual lesson are pending; years will be completed in order."
            content += f'<p class="note">{text}</p>'
        if sample:
            input_label, output_label = ("样例输入", "样例输出") if language == "zh" else ("Sample input", "Sample output")
            content += f'<section class="card"><h2>{input_label} / {output_label}</h2><div class="sample-grid"><div><h3>{input_label}</h3><pre>{escape(sample.read_text())}</pre></div><div><h3>{output_label}</h3><pre>{escape(sample.with_suffix(".out").read_text())}</pre></div></div></section>'
        note = "官方题目原文为英文；图表和原版排版请看 PDF。" if language == "zh" else "The official statement is in English. See the PDF for figures and original formatting."
        content += f'<section class="card"><h2>{labels[8]}</h2><p class="muted">{note}</p><details><summary>Problem statement (English)</summary><pre class="statement">{escape(statement)}</pre></details></section>'
        data_note = ("完整官方测试数据" if language == "zh" else "Full official test data") if source["test_data"]["kind"] == "official" else ("完整官方数据未找到；样例与本地用例的覆盖有限" if language == "zh" else "Full official data is unavailable; samples and local cases have limited coverage")
        listing = "".join(f'<li><a href="tests/{escape(p.name)}">{escape(p.name)}</a> / <a href="tests/{escape(p.with_suffix(".out").name)}">output</a></li>' for p in cases)
        download = ""
        if source["test_data"].get("storage") == "download":
            total = source["test_data"]["official_input_count"]
            data_note = f"{total} " + ("个官方用例；页面列出随仓库附带的少量用例，完整包按需下载" if language == "zh" else "official cases; a small subset is bundled, download the full package for grading")
            download = f'<p><a href="{escape(source["test_data"]["url"])}">'+("下载完整官方数据" if language == "zh" else "Download full official data")+'</a></p>'
        content += f'<section class="card"><h2>{labels[9]}</h2><p>{len(cases)} bundled cases · {data_note}</p>{download}<a href="source.json">Sources / 来源</a><details><summary>{labels[9]}</summary><ul>{listing}</ul></details></section>'
        body += panel(language, content)
    (directory / "solution.html").write_text(shell(title, body, "../../../"))
    return title.split(" · ", 1)[1], bool(lesson)


def main():
    catalog = {p.parent: build_problem(p.parent) for p in sorted(ROOT.glob("20??/*/*/source.json"))}
    years = sorted({int(p.relative_to(ROOT).parts[0]) for p in catalog})
    body = ""
    for language in ["zh", "en"]:
        intro = "按年份练习，每一道题都有自己的目录。先读题、自己尝试，再读讲解。重复题只在 Senior 保留一份解法和讲解。" if language == "zh" else "Practice by year, with one folder per problem. Read the problem and try it yourself before opening the lesson. Shared problems keep one solution and lesson in Senior."
        complete = sum(ready for _, ready in catalog.values())
        content = f'<p class="intro">{intro}</p><div class="tags"><span class="tag">{years[0]}–{years[-1]}</span><span class="tag">{len(catalog)} '+("独立题目" if language == "zh" else "unique problems")+f'</span><span class="tag">{complete} '+("双语讲解已编写" if language == "zh" else "bilingual lessons written")+'</span></div>'
        for year in years:
            content += f'<details class="year"{ " open" if year == 2010 else ""}><summary>{year}</summary><div class="divisions">'
            for division in ["junior", "senior"]:
                content += f'<section><h2>{division.title()}</h2><ul class="problem-list">'
                directories = sorted(p for p in (ROOT / str(year) / division).iterdir() if p.is_dir())
                for directory in directories:
                    reference = directory / "reference.json"
                    canonical = (directory / json.loads(reference.read_text())["target"]).resolve() if reference.exists() else directory
                    name, ready = catalog[canonical]
                    path = canonical.relative_to(ROOT).as_posix() + "/solution.html"
                    status = ("讲解已编写；验证结果见 README" if language == "zh" else "Lesson written; see README for validation") if ready else ("解法与讲解待完成" if language == "zh" else "Solution and lesson pending")
                    if reference.exists():
                        status = (f"参考 Senior {canonical.name}" if language == "zh" else f"See Senior {canonical.name}") + " · " + status
                    content += f'<li><a href="{path}">{directory.name} · {escape(name)}</a><span class="status">{status}</span></li>'
                if not directories:
                    content += '<li class="muted">'+("原仓库未覆盖本年的 Senior 题目" if language == "zh" else "No Senior problems in the original collection for this year")+'</li>'
                content += '</ul></section>'
            content += '</div></details>'
        body += panel(language, content)
    (ROOT / "index.html").write_text(shell("CCC Solutions", body, ""))
    print(f"Built index + {len(catalog)} pages; {sum(ready for _, ready in catalog.values())} bilingual lessons.")


if __name__ == "__main__":
    main()
