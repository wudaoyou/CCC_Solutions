sample-01、02、03 分别抄录官方 Senior PDF 第 4 页的三个样例。edge-* 是本地边界：最小号码 1、候选人数仍不足三人的 3、能形成四组的 5，以及最大号码 99。

verify.py 直接枚举每个 J=1…99 的三人组合，并逐一运行 solution.py 比较结果；没有用解法里的组合公式生成预期值。运行：python3 2012/senior/S1/tests/verify.py。

sample-01, 02, and 03 are transcribed from the three examples on page 4 of the official Senior PDF. Local edge cases cover jersey 1, jersey 3 with too few eligible players, jersey 5 with four groups, and the maximum jersey 99.

verify.py directly enumerates triples for every J=1…99 and runs solution.py to compare results. It does not generate expected answers using the solution's combination formula. Run: python3 2012/senior/S1/tests/verify.py.

完整官方测试包尚未找到；通过这些样例和本地检查不代表覆盖完整官方数据或在线评测通过。

The full official test archive has not been located. Passing these samples and local checks does not establish full official-data coverage or online acceptance.
