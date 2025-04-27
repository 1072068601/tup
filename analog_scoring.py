import pandas as pd
import random
import numpy as np

# 读取景点数据
scenic_spots = pd.read_csv('scenic_spots.csv')

# 生成用户数据（增加职业和常旅行季节）
num_users = 700  # 用户数量
user_data = pd.DataFrame({
    'user_id': [f'User_{i + 1}' for i in range(num_users)],
    'age': np.random.randint(18, 70, size=num_users),
    'gender': np.random.choice(['M', 'F'], size=num_users),
    'occupation': np.random.choice(['Engineer', 'Teacher', 'Doctor', 'Artist', 'Student'], size=num_users),
    'preferred_travel_season': np.random.choice(['Spring', 'Summer', 'Autumn', 'Winter'], size=num_users)
})

# 生成评分数据
ratings = []


# 加权函数：假设年龄与景点类型的偏好相关
def weighted_rating(user_age, scenic_level):
    base_score = random.randint(1, 5)  # 基础评分在1到5之间
    if user_age < 30:
        base_score += random.randint(0, 2)  # 年轻用户可能偏向高评分
    if scenic_level == '5A':
        base_score += random.randint(0, 1)  # 高等级景点可能获得较高评分
    return min(base_score, 5)  # 确保评分在1-5之间


# 模拟评分
for user_id in user_data['user_id']:
    # 每个用户评分5到10个景点
    num_ratings = random.randint(5, 10)
    rated_spots = random.sample(range(len(scenic_spots)), num_ratings)  # 随机选取评分景点

    for spot_index in rated_spots:
        spot = scenic_spots.iloc[spot_index]
        # 随机生成用户对该景点的评分
        rating = weighted_rating(user_data.loc[user_data['user_id'] == user_id, 'age'].values[0], spot['level'])
        # 获取用户信息
        user_info = user_data.loc[
            user_data['user_id'] == user_id, ['age', 'gender', 'occupation', 'preferred_travel_season']].values[0]
        ratings.append([user_id, spot['name'], rating] + list(user_info))

# 将评分数据保存为CSV
ratings_df = pd.DataFrame(ratings, columns=['user_id', 'scenic_spot', 'rating', 'age', 'gender', 'occupation',
                                            'preferred_travel_season'])
ratings_df.to_csv('user_ratings.csv', index=False)

print("评分数据已生成并保存为 'user_ratings.csv'")
