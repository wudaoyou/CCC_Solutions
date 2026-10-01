本目录保留完整官方测试数据：Senior 的 s2.1a–s2.5b，以及重叠 Junior J5 的 j5.1a–j5.5b，共 20 对输入/输出。原始 .in/.out 文件不修改，也不由解法重新生成；来源见上级 source.json。

运行全部官方用例：`python3 tools/judge.py 2014/senior/S2`。

独立检查：`python3 2014/senior/S2/tests/verify.py`。它枚举 N=2…5 的所有搭档名单排列，共 152 个用例。预期结果把每列转为无序姓名集合；只有每组两人且恰好形成 N/2 个不同组时才合法。这个检查不使用解法的反向字典查询，覆盖自我搭档、互相配对、较长循环、奇数人数，并使用 A/a 和 B/b 检查大小写区分。不写入官方数据。

This directory preserves the full official data: s2.1a–s2.5b from Senior and j5.1a–j5.5b from shared Junior J5, for 20 input/output pairs. The original .in/.out files are not modified or regenerated from the solution. See the parent source.json for provenance.

Run all official cases: `python3 tools/judge.py 2014/senior/S2`.

Run the independent check: `python3 2014/senior/S2/tests/verify.py`. It enumerates every partner-row permutation for N=2…5, giving 152 cases. The oracle converts each column to an unordered set of names and accepts only when every group has two students and there are exactly N/2 distinct groups. It does not use the solution's reverse dictionary lookup. It covers self-partners, mutual pairs, longer cycles, odd class sizes, and case-sensitive names A/a and B/b, without writing official files.

上述运行是本地验证；通过完整官方数据不代表已经提交在线评测或取得在线 AC。

These are local checks. Passing the complete official cases does not establish an online submission or online acceptance.
