本目录保留完整官方测试数据：Senior 的 s1.1–s1.5，以及重叠 Junior J4 的 j4.1–j4.5，共 10 对输入/输出。原始 .in/.out 文件不修改，也不由解法重新生成；来源见上级 source.json。

运行全部官方用例：`python3 tools/judge.py 2014/senior/S1`。

独立检查：`python3 2014/senior/S1/tests/verify.py`。它枚举 K=1…8、1…3 轮、每轮间隔 2…4，共 312 个小用例；预期结果通过每轮从右向左删除指定位置得到，与解法建立保留名单的方法不同。覆盖重新计数、间隔超过名单长度和多轮连续删除，不写入官方数据。

This directory preserves the full official data: s1.1–s1.5 from Senior and j4.1–j4.5 from shared Junior J4, for 10 input/output pairs. The original .in/.out files are not modified or regenerated from the solution. See the parent source.json for provenance.

Run all official cases: `python3 tools/judge.py 2014/senior/S1`.

Run the independent check: `python3 2014/senior/S1/tests/verify.py`. It enumerates K=1…8, 1…3 rounds, and intervals 2…4, for 312 small cases. Its oracle deletes positions from right to left in each round, rather than constructing the solution's survivor list. It covers position recounting, intervals longer than the current list, and repeated rounds without writing official files.

上述运行是本地验证；通过完整官方数据不代表已经提交在线评测或取得在线 AC。

These are local checks. Passing the complete official cases does not establish an online submission or online acceptance.
