import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# 读取评分数据
ratings_df = pd.read_csv('user_ratings.csv')

# 创建用户-景点评分矩阵 (用户作为行，景点作为列)
user_item_matrix = ratings_df.pivot_table(index='user_id', columns='scenic_spot', values='rating')

# 用0填充缺失值，因为未评分的地方没有值
user_item_matrix = user_item_matrix.fillna(0)
print(user_item_matrix.head())

# 计算用户之间的相似度矩阵，使用余弦相似度
user_similarity = cosine_similarity(user_item_matrix)


# 将相似度矩阵转为DataFrame
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)
print(user_similarity_df.head())

# 基于相似度矩阵进行推荐
def get_user_recommendations(user_id, top_n=5, rating_threshold=3):
    # 获取与目标用户最相似的用户
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)
    similar_users = similar_users.drop(user_id)  # 删除目标用户本身
    print(f"与用户 {user_id} 最相似的用户: {similar_users.head(top_n)}")  # 输出相似用户

    top_similar_users = similar_users.head(top_n)

    # 获取这些相似用户评分过的景点
    recommended_spots = set()
    for similar_user in top_similar_users.index:
        user_ratings = ratings_df[ratings_df['user_id'] == similar_user]
        print(f"用户 {similar_user} 的评分数据：{user_ratings.head()}")  # 输出相似用户评分的数据
        recommended_spots.update(user_ratings[user_ratings['rating'] >= rating_threshold]['scenic_spot'])

    # 获取目标用户未评分的景点，并推荐这些景点
    user_ratings = ratings_df[ratings_df['user_id'] == user_id]
    rated_spots = set(user_ratings['scenic_spot'])

    print(f"用户 {user_id} 已评分的景点：{rated_spots}")  # 输出目标用户已评分的景点

    # 返回未评分且在推荐列表中的景点
    return list(recommended_spots - rated_spots)


# 调用推荐函数
user_id = 'User_2'  # 用户ID
recommended_spots = get_user_recommendations(user_id, top_n=3, rating_threshold=3)

print(f"为用户 {user_id} 推荐的景点是：{recommended_spots}")
