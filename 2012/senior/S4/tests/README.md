sample-01 抄录官方 Senior PDF 第 8 页的完整样例。edge-01 覆盖 n=1…7 的已排序局面、混合大小输入和重复 n；edge-02 覆盖 n=3 的全部六种初始排列及重复查询；edge-03 是最大规模 n=7 的倒序排列。

verify.py 的独立参考搜索直接使用“每个位置一个硬币元组”，按实际顶币和相邻移动规则产生邻居，不使用解法的整数编码或相邻顶币比较捷径。它核对 n=1…5 的全部 n^n 个合法堆叠状态，并用双向元组搜索独立确认 n=7 倒序需要 56 步。已排序局面的期望值由目标定义直接得到。运行：python3 2012/senior/S4/tests/verify.py。

sample-01 is the complete sample transcribed from page 8 of the official Senior PDF. edge-01 covers sorted games for n=1…7, mixed input sizes, and repeated n; edge-02 covers all six n=3 starting permutations and a repeated query; edge-03 uses reversed order at the maximum n=7.

The independent oracle in verify.py stores a tuple of coins at every position and generates moves directly from the top-coin and adjacency rules. It uses neither the solution's integer encoding nor its adjacent-top comparison shortcut. It compares every one of the n^n legal stack arrangements for n=1…5, then independently confirms the 56-move answer for reversed n=7 using bidirectional tuple search. Sorted-case answers follow directly from the definition of the goal. Run: python3 2012/senior/S4/tests/verify.py.

本题与 Junior J5 重叠，解法、讲解和测试只在本 Senior 目录维护。完整官方测试包尚未找到；通过这些样例和本地检查不代表覆盖完整官方数据或在线评测通过。

This problem is shared with Junior J5; its solution, lesson, and tests are maintained only in this Senior folder. The full official test archive has not been located. Passing these samples and local checks does not establish full official-data coverage or online acceptance.
