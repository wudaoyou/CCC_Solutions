# CCC Solutions

面向 9–11 年级学生的 CCC 练习仓库。每道题一份中英文双语 HTML 讲解，可在页面右上角切换语言，离线可用。

A CCC practice collection for students in Grades 9–11. Each problem has its own bilingual HTML lesson with a Chinese/English switch. Pages work offline.

## 目录 / Layout

```text
2010/
  _sources/             # 官方原版试卷 / Original official papers
    junior.pdf
    senior.pdf
  junior/
    J1/
      problem.txt       # 官方英文题目 / Official English statement
      source.json       # 来源、哈希、数据覆盖 / Sources, hashes, coverage
      solution.py       # 完成该题后加入 / Added when solved
      lesson.json       # 中英文讲解源文件 / Chinese and English lesson text
      solution.html     # 独立讲解页面 / Individual lesson page
      tests/
        sample-01.in
        sample-01.out
  senior/
    S2/
      ...
assets/                 # 离线样式与语言切换 / Offline styling and language switch
tools/                  # 页面构建与评测 / Page builder and grading tools
archive/original-code/  # 原代码完整保留 / Original code preserved
index.html              # 年份与题目入口 / Year and problem directory
```

重叠题的 Junior 目录仅有 `README.md` 和 `reference.json`，注明“参考 Senior S几”。解法、讲解、题目和测试数据都只在对应 Senior 目录维护。

For shared problems, the Junior folder contains only a README and a reference to the Senior problem. The solution, lesson, statement and test data are maintained once, in Senior.

## 当前范围与进度 / Scope and progress

本轮覆盖 **2010–2026**：2010–2023 整理全部 Junior 题、原仓库已有的 Senior 题和重叠题；2024–2026 纳入每年全部 Junior/Senior 题。共 **109 道独立题目、14 个 Junior 引用目录**。2010–2023 尚未补齐的 Senior 题不在本轮基座范围内。

The scope is **2010–2026**: all Junior problems plus the original Senior collection and shared problems for 2010–2023; all Junior and Senior problems for 2024–2026. There are **109 unique problems and 14 Junior references**. The remaining older Senior problems are outside this foundation scope.

基座阶段：目录、官方题目、来源、可取得的官方数据、双语切换、页面构建与评测工具已建立。做题阶段按年份推进；未完成的页面明确标为待完成，不展示草稿为已验证解法。

Foundation stage: structure, official statements, provenance, available official data, language switching, page generation and grading tools. Solutions are completed year by year. Pending pages are clearly labelled.

| 年份 / Year | 解法与双语讲解 / Solutions and bilingual lessons |
| --- | --- |
| 2010 | J1–J5、S2 解法与双语讲解完成；DMOJ 本地引擎 22/22 用例通过 / J1–J5, S2 complete; 22/22 cases passed the local DMOJ engine |
| 2011 | J1–J5 解法与双语讲解完成；DMOJ 本地引擎 25/25 用例通过 / J1–J5 complete; 25/25 cases passed the local DMOJ engine |
| 2012 | J1–J4、S1、S4 完成；J5 引用 S4；DMOJ 本地引擎 29/29 用例通过 / Six canonical problems complete; J5 refers to S4; 29/29 cases passed |
| 2013 | J1、J2、J4、S1、S3 完成；J3/J5 引用 S1/S3；DMOJ 本地引擎 32/32 用例通过 / Five canonical problems complete; 32/32 cases passed |
| 2014 | J1–J3、S1、S2 完成；J4/J5 引用 S1/S2；DMOJ 本地引擎完整官方数据 51/51 用例通过 / Five canonical problems complete; all 51 official cases passed |
| 2015–2026 | 待逐年完成 / Pending, in year order |

年度验证记录见 [2010](2010/verification.json)、[2011](2011/verification.json)、[2012](2012/verification.json)、[2013](2013/verification.json)、[2014](2014/verification.json)，含解法/讲解哈希及独立校验结果；2010–2013 用例覆盖限于官方样例和本地边界；2014 已覆盖收录题目的完整官方数据。

See the [2010](2010/verification.json), [2011](2011/verification.json), [2012](2012/verification.json), [2013](2013/verification.json) and [2014](2014/verification.json) verification records for solution/lesson hashes and independent checks. Coverage for 2010–2013 is limited to official samples and local edge cases; 2014 covers the full official data for its collected problems.

2014–2023 已下载所覆盖题目的完整官方测试数据。2020/2021 的重叠 S2 数据来自官方 Junior J5 测试包。2010–2013 的完整官方测试包未在当前官网找到，做题时加入官方样例和独立核对的边界用例，不能据此声称通过完整官方数据。

Full official data is available for the covered 2014–2023 problems. Shared 2020/2021 S2 data comes from the official Junior J5 package. Full 2010–2013 archives have not been located on the current site; official samples and independently checked edge cases will be added. Such checks do not establish full official-data coverage.

2024–2026 的完整测试包较大（Senior 解压合计约 2 GiB），题目目录附带官方样例或少量官方小用例，并记录完整数据的下载地址和 SHA-256。完整数据缓存在 `.data/`，不进 Git；评测工具要求先准备完整包，不会把样例评测当作完整评测。

The 2024–2026 Senior data expands to about 2 GiB. Problem folders bundle official samples or a small subset, with download URLs and SHA-256 hashes for full data. Full data is cached in Git-ignored `.data/`. Grading requires the full package; sample-only checks are not reported as full grading.

```sh
python3 tools/fetch_data.py 2025/senior/S4
# 或下载某年全部数据 / Or fetch all data for one year:
python3 tools/fetch_data.py 2025
```

## 阅读与维护 / Read and maintain

直接打开 `index.html`。需要本地网页服务时，在仓库根目录运行 `python3 -m http.server 8000`，然后打开 `http://localhost:8000`。

Open `index.html` directly. Alternatively, run `python3 -m http.server 8000` at the repository root and visit `http://localhost:8000`.

每题的 `lesson.json` 包含 `title` 和 `zh`/`en` 两份正文；两种语言都必须包含 `summary`、`topics`、`steps`、`example`、`correctness`、`complexity`、`pitfalls`。其中 `topics`、`steps`、`pitfalls` 是字符串数组，其余是字符串。讲解要说明知识点的含义，先用例子解释，再引入算法术语。

Each `lesson.json` has a `title` and full `zh`/`en` versions. Both versions contain `summary`, `topics`, `steps`, `example`, `correctness`, `complexity` and `pitfalls`. `topics`, `steps` and `pitfalls` are string arrays; the other fields are strings. Explain terminology with examples that students can follow.

改过解法或讲解后重新构建，并检查页面、数据配对与答案检查器：

After changing a solution or lesson, rebuild and check the pages, case pairing and answer validators:

```sh
python3 tools/build_pages.py
python3 tools/test_site.py
python3 tools/test_checkers.py
python3 tools/judge.py 2010/junior/J1
python3 tools/judge.py 2011  # 按整年评测 / Grade one year
```

省略最后一条命令的题目路径会评测全部已写解法。Junior 引用路径也可用。这个简易工具只运行本仓库可信代码，不提供沙盒，也不等同于 DMOJ 分数。

Omit the problem path to test all written solutions. Junior reference paths work too. This small local runner is for trusted repository code; it is not a sandbox or a DMOJ score.

## 真正的 DMOJ 评测 / Actual DMOJ grading

参考并使用 [DMOJ judge-server](https://github.com/DMOJ/judge-server)，固定源码 SHA `5ef74c5d6cad9efb2e86a5bb8ff2c90aaa6e435c`。它支持 Linux/FreeBSD；macOS 上通过临时 Linux 容器运行，不部署网站或接入账号。首次构建会安装第三方工具及依赖。

The [DMOJ judge-server](https://github.com/DMOJ/judge-server) is pinned to source commit `5ef74c5d6cad9efb2e86a5bb8ff2c90aaa6e435c`. It runs on Linux/FreeBSD; on macOS we use a temporary Linux container, without deploying a site or connecting an account. The first build installs third-party tools and dependencies.

```sh
docker build -t ccc-dmoj:5ef74c5 tools/dmoj
mkdir -p /tmp/ccc-dmoj-results
docker run --rm --network none --cap-add SYS_PTRACE \
  --security-opt seccomp=unconfined --cpus 2 --memory 2g \
  --mount "type=bind,src=$PWD,dst=/repo,readonly" \
  --mount type=bind,src=/tmp/ccc-dmoj-results,dst=/results \
  ccc-dmoj:5ef74c5 python /repo/tools/dmoj/grade.py
```

可在最后追加 `2010/junior/J1` 只测一题，或 `2011` 评测该年已写解法。评测用 Python 3，每个用例限 3 秒 CPU、256 MiB 内存；这是本仓库统一验证条件，不是在线 DMOJ 原题的限制或分数。报告位于 `/tmp/ccc-dmoj-results/dmoj.json`，包含逐例判定、耗时与内存日志。2012 J3 逐行保留空格检查图标布局；2019 J5 检查替换过程是否有效，2019 S2 检查两数是否为素数且平均值正确；不会因有效答案与参考输出不同而误判。

Append `2010/junior/J1` to grade one problem, or `2011` to grade that year’s written solutions. The PY3 executor uses a local limit of 3 CPU seconds and 256 MiB per case. These are repository validation settings, not online DMOJ limits or scores. `/tmp/ccc-dmoj-results/dmoj.json` records verdicts, timing and memory. The Icon Scaling checker preserves spaces and line breaks. Semantic validators accept any valid substitution path for 2019 J5 and any valid prime pair for 2019 S2.

在线练习使用 [DMOJ](https://dmoj.ca/)。页面链接按 CCC 题号构造，尚未逐题核对在线可访问性；本仓库未代用户提交到 DMOJ。

Use [DMOJ](https://dmoj.ca/) for online practice. Problem links follow the CCC problem-code convention and have not all been verified online. No submissions have been made on the user's behalf.

题目与数据来自 [CEMC 官方往年竞赛页面](https://cemc.uwaterloo.ca/resources/past-contests?contest_category=29)。原文版权归 University of Waterloo；每题的 `source.json` 记录实际下载地址和哈希。`problem.txt` 保留英文内容，图表和原版排版在年度 `_sources/` PDF 中。

Statements and data come from the [official CEMC archive](https://cemc.uwaterloo.ca/resources/past-contests?contest_category=29). Original materials belong to the University of Waterloo. Per-problem `source.json` records URLs and hashes; annual `_sources/` PDFs preserve figures and layout.
