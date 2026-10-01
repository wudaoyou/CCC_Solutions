本目录保留完整官方 Senior S2 测试数据 s2.1–s2.6，共 6 对输入/输出。来源与测试包哈希见上级 source.json。s2.1 是官方样例；s2.6 达到 J=A=1,000,000。原始 .in/.out 文件保持不变，不由解法生成预期结果。

运行全部官方用例：`python3 tools/judge.py 2015/senior/S2`。

独立检查：`python3 2015/senior/S2/tests/verify.py`。它穷举单件球衣三种大小、1…3 个请求的所有大小组合，共 117 个用例；再用固定随机种子 2015 生成 100 个最多 5 件球衣、7 个请求的小用例。oracle 从人数最多的请求子集开始枚举，检查编号不重复且每件球衣大小允许该请求，不使用解法的贪心过程。共 217 个用例，覆盖重复编号、失败后仍能分配、大小相等/较大/较小，以及不同编号互不影响；不写入官方数据。

This directory preserves the full official Senior S2 data, s2.1–s2.6, comprising 6 input/output pairs. The parent source.json records provenance and the archive hash. s2.1 is the official sample, and s2.6 reaches J=A=1,000,000. The original .in/.out files are unchanged; expected outputs are not generated from the solution.

Run all official cases: `python3 tools/judge.py 2015/senior/S2`.

Run the independent check: `python3 2015/senior/S2/tests/verify.py`. It exhausts all three single-jersey sizes and all size sequences for 1…3 requests, giving 117 cases, then generates 100 cases with at most 5 jerseys and 7 requests using fixed random seed 2015. The oracle enumerates request subsets from largest to smallest, accepting a subset only if its requested numbers are distinct and every jersey permits its requested size. It does not use the solution's greedy process. These 217 cases cover duplicate numbers, assignment after an earlier failed request, equal/larger/smaller sizes, and independence between jersey numbers, without writing official data.

这些运行是本地验证，不代表已提交在线评测或取得在线 AC。

These are local checks, not evidence of an online submission or online acceptance.
