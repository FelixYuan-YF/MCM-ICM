from mlxtend.frequent_patterns import apriori, association_rules
import pandas as pd

# 示例数据集
data = {
    '牛奶': [1, 1, 1, 0, 1],
    '面包': [1, 1, 0, 1, 1],
    '尿布': [1, 0, 1, 1, 1],
    '啤酒': [0, 1, 1, 1, 0]
}
df = pd.DataFrame(data)

# 使用Apriori算法发现频繁项集
frequent_itemsets = apriori(df, min_support=0.5, use_colnames=True)

# 生成关联规则
rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1.0)

print(rules)
