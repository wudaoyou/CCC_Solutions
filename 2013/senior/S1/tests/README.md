sample-01、02 抄录官方 Senior PDF 第 4 页的两个样例。edge-* 覆盖最小输入 0、位数增长、已合格年份仍需找下一年、四位转五位及最大输入 10000。

verify.py 使用整数除法逐位检查数字，生成全部合格候选年份，再用二分查找得到下一年；与解法的字符串集合及逐年搜索不同。它核对全部 10001 个允许输入。运行：python3 2013/senior/S1/tests/verify.py。

sample-01 and 02 are transcribed from page 4 of the official Senior PDF. Local edge cases cover input 0, digit-count transitions, a valid starting year that must still advance, the four-to-five-digit transition, and maximum input 10000.

verify.py builds the valid-year list using arithmetic digit extraction and finds the next entry by binary search, independently of the solution's string set and sequential search. It checks all 10001 allowed inputs. Run: python3 2013/senior/S1/tests/verify.py.

本题与 Junior J3 重叠，内容只在本 Senior 目录维护。完整官方测试包尚未找到；这些检查不代表完整官方数据覆盖或在线评测通过。

This problem is shared with Junior J3 and maintained only in this Senior folder. The full official test archive has not been located. These checks do not establish full official-data coverage or online acceptance.
