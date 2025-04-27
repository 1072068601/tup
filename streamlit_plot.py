# import streamlit as st
# import pandas as pd
# import plotly.express as px
# import random

# # 读取评分数据
# ratings_df = pd.read_csv('user_ratings.csv')  # 你的评分数据路径

# # 选择部分用户（例如随机抽取10个用户，减少显示的用户数量）
# selected_users = random.sample(ratings_df['user_id'].unique().tolist(), 10)
# ratings_df_selected = ratings_df[ratings_df['user_id'].isin(selected_users)]


# # 1. 评分分布图（所有用户）
# st.subheader('1. 用户评分分布')

# fig1 = px.histogram(ratings_df_selected, x='rating', nbins=5,
#                     title='所有用户的评分分布', color='rating',
#                     color_discrete_sequence=px.colors.qualitative.Plotly)
# st.plotly_chart(fig1)

# # 2. 用户评分统计（不同用户评分分布）
# st.subheader('2. 用户评分统计')

# user_rating_counts = ratings_df_selected.groupby('user_id')['rating'].count().reset_index()
# fig2 = px.bar(user_rating_counts, x='user_id', y='rating',
#               title='用户的评分数量', labels={'rating': '评分数量'},
#               color='rating', color_continuous_scale='Blues')
# st.plotly_chart(fig2)

# # 3. 各景点评分统计（修正后的条形图）
# st.subheader('3. 各景点的评分统计')

# scenic_rating_counts = ratings_df_selected.groupby('scenic_spot')['rating'].mean().reset_index()
# # 按照评分从高到低排序
# scenic_rating_counts = scenic_rating_counts.sort_values(by='rating', ascending=False)
# fig3 = px.bar(scenic_rating_counts, x='scenic_spot', y='rating',
#               title='各景点的平均评分（排序后）', color='rating',
#               color_continuous_scale='Cividis',
#               labels={'rating': '平均评分'})
# st.plotly_chart(fig3)

# # 4. 性别分布（饼图）
# st.subheader('4. 用户性别分布')

# gender_counts = ratings_df_selected['gender'].value_counts().reset_index()
# gender_counts.columns = ['Gender', 'Count']
# fig4 = px.pie(gender_counts, names='Gender', values='Count',
#               title='用户性别分布', color='Gender',
#               color_discrete_sequence=px.colors.qualitative.Set3)
# st.plotly_chart(fig4)

# # 5. 年龄段分布（条形图）
# st.subheader('5. 用户年龄段分布')

# ratings_df_selected['age_group'] = pd.cut(ratings_df_selected['age'],
#                                           bins=[0, 18, 30, 40, 50, 60, 100],
#                                           labels=['18岁以下', '18-30岁', '30-40岁', '40-50岁', '50-60岁', '60岁以上'])
# age_group_counts = ratings_df_selected['age_group'].value_counts().reset_index()
# age_group_counts.columns = ['Age Group', 'Count']
# fig5 = px.bar(age_group_counts, x='Age Group', y='Count',
#               title='用户年龄段分布', color='Age Group',
#               color_discrete_sequence=px.colors.qualitative.Pastel)
# st.plotly_chart(fig5)

# # 6. 每个景点的评分数量（散点图）
# st.subheader('6. 景点评分数量')

# scenic_rating_counts = ratings_df_selected.groupby('scenic_spot')['rating'].count().reset_index()
# fig6 = px.scatter(scenic_rating_counts, x='scenic_spot', y='rating',
#                   title='景点的评分数量', color='rating',
#                   color_continuous_scale='Jet')
# st.plotly_chart(fig6)

# # 7. 用户的季节偏好评分（折线图）
# st.subheader('7. 用户的季节偏好评分')

# season_rating_avg = ratings_df_selected.groupby('preferred_travel_season')['rating'].mean().reset_index()
# fig7 = px.line(season_rating_avg, x='preferred_travel_season', y='rating',
#                title='不同季节的评分平均值', markers=True, line_shape='linear')
# st.plotly_chart(fig7)

# # 8. 性别与评分之间的关系（箱型图）
# st.subheader('8. 性别与评分之间的关系')

# fig8 = px.box(ratings_df_selected, x='gender', y='rating',
#               title='性别与评分之间的关系', color='gender',
#               color_discrete_sequence=px.colors.qualitative.Set1)
# st.plotly_chart(fig8)

# # 9. 用户评分与景点之间的关系（修正后的热力图）
# st.subheader('9. 用户评分与景点之间的关系')

# # 按用户和景点对评分数据进行分组
# user_spot_rating = ratings_df_selected.groupby(['user_id', 'scenic_spot'])['rating'].mean().reset_index()

# # 将用户和景点的评分数据透视为矩阵（用户为列，景点为行）
# pivot_table = user_spot_rating.pivot(index='scenic_spot', columns='user_id', values='rating').fillna(0)

# # 绘制热力图
# fig9 = px.imshow(pivot_table, title='用户评分与景点之间的关系',
#                  color_continuous_scale='YlGnBu',
#                  labels={'x': '用户', 'y': '景点', 'color': '评分'})

# st.plotly_chart(fig9)

import streamlit as st
import pandas as pd
import plotly.express as px
import random

# 读取评分数据
ratings_df = pd.read_csv('user_ratings.csv')  # 你的评分数据路径

# 选择部分用户（例如随机抽取10个用户，减少显示的用户数量）
selected_users = random.sample(ratings_df['user_id'].unique().tolist(), 10)
ratings_df_selected = ratings_df[ratings_df['user_id'].isin(selected_users)]

# 设置页面布局
st.set_page_config(layout="wide")
# 使用列布局，评分分布图和其他图表可以并排显示
col1, col2 = st.columns(2)

with col1:
    # 1. 评分分布图（所有用户）
    st.subheader('1. 用户评分分布')


    fig1 = px.histogram(ratings_df_selected, x='rating', nbins=5,
                        title='所有用户的评分分布', color='rating',
                        color_discrete_sequence=px.colors.qualitative.Plotly)
    st.plotly_chart(fig1, use_container_width=True)
with col2:
    # 2. 用户评分统计（不同用户评分分布）
    st.subheader('2. 用户评分统计')

    fig2 = px.bar(ratings_df_selected.groupby('user_id')['rating'].count().reset_index(), 
                x='user_id', y='rating',
                title='用户的评分数量', labels={'rating': '评分数量'},
                color='rating', color_continuous_scale='Blues')
    st.plotly_chart(fig2, use_container_width=True)
with col1:
    # 3. 各景点评分统计（修正后的条形图）
    st.subheader('3. 各景点的评分统计')

    scenic_rating_counts = ratings_df_selected.groupby('scenic_spot')['rating'].mean().reset_index()
    scenic_rating_counts = scenic_rating_counts.sort_values(by='rating', ascending=False)
    fig3 = px.bar(scenic_rating_counts, x='scenic_spot', y='rating',
                title='各景点的平均评分（排序后）', color='rating',
                color_continuous_scale='Cividis', labels={'rating': '平均评分'})
    st.plotly_chart(fig3, use_container_width=True)
with col2:
    # 4. 性别分布（饼图）
    st.subheader('4. 用户性别分布')

    gender_counts = ratings_df_selected['gender'].value_counts().reset_index()
    gender_counts.columns = ['Gender', 'Count']
    fig4 = px.pie(gender_counts, names='Gender', values='Count',
                title='用户性别分布', color='Gender',
                color_discrete_sequence=px.colors.qualitative.Set3)
    st.plotly_chart(fig4, use_container_width=True)
with col1:
    # 5. 年龄段分布（条形图）
    st.subheader('5. 用户年龄段分布')

    ratings_df_selected['age_group'] = pd.cut(ratings_df_selected['age'],
                                            bins=[0, 18, 30, 40, 50, 60, 100],
                                            labels=['18岁以下', '18-30岁', '30-40岁', '40-50岁', '50-60岁', '60岁以上'])
    age_group_counts = ratings_df_selected['age_group'].value_counts().reset_index()
    age_group_counts.columns = ['Age Group', 'Count']
    fig5 = px.bar(age_group_counts, x='Age Group', y='Count',
                title='用户年龄段分布', color='Age Group',
                color_discrete_sequence=px.colors.qualitative.Pastel)
    st.plotly_chart(fig5, use_container_width=True)
with col2:
    # 6. 每个景点的评分数量（散点图）
    st.subheader('6. 景点评分数量')

    scenic_rating_counts = ratings_df_selected.groupby('scenic_spot')['rating'].count().reset_index()
    fig6 = px.scatter(scenic_rating_counts, x='scenic_spot', y='rating',
                    title='景点的评分数量', color='rating',
                    color_continuous_scale='Jet')
    st.plotly_chart(fig6, use_container_width=True)
with col1:
    # 7. 用户的季节偏好评分（折线图）
    st.subheader('7. 用户的季节偏好评分')

    season_rating_avg = ratings_df_selected.groupby('preferred_travel_season')['rating'].mean().reset_index()
    fig7 = px.line(season_rating_avg, x='preferred_travel_season', y='rating',
                title='不同季节的评分平均值', markers=True, line_shape='linear')
    st.plotly_chart(fig7, use_container_width=True)
with col2:
    # 8. 性别与评分之间的关系（箱型图）
    st.subheader('8. 性别与评分之间的关系')

    fig8 = px.box(ratings_df_selected, x='gender', y='rating',
                title='性别与评分之间的关系', color='gender',
                color_discrete_sequence=px.colors.qualitative.Set1)
    st.plotly_chart(fig8, use_container_width=True)
with col1:
    # 9. 用户评分与景点之间的关系（修正后的热力图）
    st.subheader('9. 用户评分与景点之间的关系')

    user_spot_rating = ratings_df_selected.groupby(['user_id', 'scenic_spot'])['rating'].mean().reset_index()
    pivot_table = user_spot_rating.pivot(index='scenic_spot', columns='user_id', values='rating').fillna(0)

    fig9 = px.imshow(pivot_table, title='用户评分与景点之间的关系',
                    color_continuous_scale='YlGnBu',
                    labels={'x': '用户', 'y': '景点', 'color': '评分'})
    st.plotly_chart(fig9, use_container_width=True)
