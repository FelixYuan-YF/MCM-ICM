from mlxtend.frequent_patterns import fpgrowth
import pandas as pd

# 示例数据集
data = {
    '牛奶': [1, 1, 1, 0, 1],
    '面包': [1, 1, 0, 1, 1],
    '尿布': [1, 0, 1, 1, 1],
    '啤酒': [0, 1, 1, 1, 0]
}
df = pd.DataFrame(data)

# 使用FP-Growth算法发现频繁项集，最小支持度设为0.5
frequent_itemsets = fpgrowth(df, min_support=0.5, use_colnames=True)

print(frequent_itemsets)
