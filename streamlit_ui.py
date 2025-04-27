# import streamlit as st
# import pandas as pd
# import numpy as np
# from sklearn.metrics.pairwise import cosine_similarity

# # 假设你已经有了 ratings_df 和 user_similarity_df
# # 你可以直接导入这些对象，或者将它们存储为 .csv 文件后读取

# # 这里使用假数据进行示例
# ratings_df = pd.read_csv('user_ratings.csv')  # 用户评分数据
# user_item_matrix = ratings_df.pivot_table(index='user_id', columns='scenic_spot', values='rating').fillna(0)
# user_similarity = cosine_similarity(user_item_matrix)
# user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)


# # 推荐函数
# def get_user_recommendations(user_id, top_n=5, rating_threshold=3):
#     similar_users = user_similarity_df[user_id].sort_values(ascending=False)
#     similar_users = similar_users.drop(user_id)  # 删除目标用户本身
#     top_similar_users = similar_users.head(top_n)

#     recommended_spots = set()
#     for similar_user in top_similar_users.index:
#         user_ratings = ratings_df[ratings_df['user_id'] == similar_user]
#         recommended_spots.update(user_ratings[user_ratings['rating'] >= rating_threshold]['scenic_spot'])

#     user_ratings = ratings_df[ratings_df['user_id'] == user_id]
#     rated_spots = set(user_ratings['scenic_spot'])

#     return list(recommended_spots - rated_spots)


# # Streamlit界面
# st.title("陕西省旅游景点推荐")

# # 用户输入自己的ID
# user_id = st.text_input("请输入您的用户ID：", "User_1")

# # 提交按钮
# if st.button("获取推荐"):
#     if user_id:
#         recommended_spots = get_user_recommendations(user_id, top_n=3, rating_threshold=3)

#         if recommended_spots:
#             st.write(f"为用户 {user_id} 推荐的景点：")
#             for spot in recommended_spots:
#                 st.write(f"- {spot}")
#         else:
#             st.write(f"抱歉，无法为用户 {user_id} 提供推荐。")
#     else:
#         st.write("请提供有效的用户ID。")

import streamlit as st
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# 假设你已经有了 ratings_df 和 user_similarity_df
# 你可以直接导入这些对象，或者将它们存储为 .csv 文件后读取

# 这里使用假数据进行示例
ratings_df = pd.read_csv('user_ratings.csv')  # 用户评分数据
scenic_spots_df = pd.read_csv('scenic_spots.csv')  # 景点信息数据
user_item_matrix = ratings_df.pivot_table(index='user_id', columns='scenic_spot', values='rating').fillna(0)
user_similarity = cosine_similarity(user_item_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_item_matrix.index, columns=user_item_matrix.index)


# 推荐函数
def get_user_recommendations(user_id, top_n=5, rating_threshold=3):
    similar_users = user_similarity_df[user_id].sort_values(ascending=False)
    similar_users = similar_users.drop(user_id)  # 删除目标用户本身
    top_similar_users = similar_users.head(top_n)

    recommended_spots = set()
    for similar_user in top_similar_users.index:
        user_ratings = ratings_df[ratings_df['user_id'] == similar_user]
        recommended_spots.update(user_ratings[user_ratings['rating'] >= rating_threshold]['scenic_spot'])

    user_ratings = ratings_df[ratings_df['user_id'] == user_id]
    rated_spots = set(user_ratings['scenic_spot'])

    return list(recommended_spots - rated_spots)


# 通过景点名称查找其图片和描述信息
def get_scenic_spot_info(spot_name):
    spot_info = scenic_spots_df[scenic_spots_df['name'] == spot_name].iloc[0]
    return spot_info['image_url'], spot_info['description']


# Streamlit界面
st.title("陕西省旅游景点推荐")

# 用户输入自己的ID
user_id = st.text_input("请输入您的用户ID：", "User_1")

# 提交按钮
if st.button("获取推荐"):
    if user_id:
        recommended_spots = get_user_recommendations(user_id, top_n=3, rating_threshold=3)

        if recommended_spots:
            st.write(f"为用户 {user_id} 推荐的景点：")
            for spot in recommended_spots:
                # 获取景点信息
                image_url, description = get_scenic_spot_info(spot)
                
                # 显示景点名称、图片和描述
                st.write(f"### {spot}")
                st.image(image_url, width=400)  # 显示景点图片
                st.write(description)  # 显示景点描述
        else:
            st.write(f"抱歉，无法为用户 {user_id} 提供推荐。")
    else:
        st.write("请提供有效的用户ID。")
