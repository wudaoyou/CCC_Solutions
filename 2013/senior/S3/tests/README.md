sample-01、02 抄录官方 Senior PDF 第 7、8 页的样例。edge-01 为没有已赛比赛的最大搜索；edge-02 只剩目标队的一场比赛，只有胜利能打破并列；edge-03 为无法打破的并列第一；edge-04 的目标队 4 已确保冠军；edge-05 区分实际比分与联赛积分。

verify.py 用独立递归搜索生成六场比赛全部 729 个完整结果及冠军，再筛选符合已赛结果的完整赛事。它核对全部 3367 种合法部分赛事与四个目标队，共 13468 组检查，覆盖所有已赛比赛子集、胜负平及 G=0…5。运行：python3 2013/senior/S3/tests/verify.py。

sample-01 and 02 are transcribed from pages 7 and 8 of the official Senior PDF. edge-01 has no completed games and exercises the largest search; edge-02 leaves one game where the favorite must win to break a tie; edge-03 has an unavoidable tie for first; edge-04 already guarantees favorite team 4 the title; edge-05 distinguishes game scores from tournament points.

verify.py independently generates all 729 complete tournaments and their champions with recursive search, then filters records to match completed games. It checks all 3367 legal partial tournaments for each of the four favorites, totaling 13468 checks across every completed-game subset, win/loss/tie pattern, and G=0…5. Run: python3 2013/senior/S3/tests/verify.py.

本题与 Junior J5 重叠，内容只在本 Senior 目录维护。完整官方测试包尚未找到；这些检查不代表完整官方数据覆盖或在线评测通过。

This problem is shared with Junior J5 and maintained only in this Senior folder. The full official test archive has not been located. These checks do not establish full official-data coverage or online acceptance.
