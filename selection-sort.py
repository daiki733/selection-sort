# 合計得点を計算し、選手名と合計得点のリストを作成
totals = []
for name, events in scores.items():
    total = sum(events.values())
    totals.append([name, total])

# バブルソートで合計得点の高い順に並び替え
n = len(totals)
for i in range(n):
    for j in range(0, n-i-1):
        if totals[j][1] < totals[j+1][1]:
            totals[j], totals[j+1] = totals[j+1], totals[j]

# 結果を表示
for name, total in totals:
    print(f"{name}: {total:.3f}")