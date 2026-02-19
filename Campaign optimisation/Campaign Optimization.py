# %% [markdown]
# # Google Ads Campaign Simulation & Performance Optimization
# 
# In this project, we explore a dataset simulating marketing campaign performance across various channels including social, search, media, and influencer campaigns. Using key performance metrics such as impressions, clicks, spend, conversions, and revenue, we calculate and visualize the effectiveness of each campaign.
# 
# The goal is to:
# - Simulate a Google Ads style analysis
# - Identify high and low performing campaigns
# - Calculate KPIs like CTR, CPC, Conversion Rate, and ROAS
# - Recommend optimization strategies for better ad spend efficiency
# 
# This type of analysis is critical for marketing professionals aiming to maximize the return on advertising investment (ROAS) and improve digital performance.
# 

# %% [markdown]
# # Section 1 - Load and Preview Data
# We begin by loading the marketing dataset, which includes information on campaign performance such as impressions, clicks, spend, leads, orders, and revenue. This gives us a foundation for calculating meaningful advertising KPIs.

# %%
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# %%
df = pd.read_csv('/Users/ayushpuri/Desktop/Github/Campaign optimisation/Marketing.csv')
df.head()

# %% [markdown]
# ## Section 2 - Calculating Key Performance indicators
# 
# In this step, we calculate important Google Ads KPIs including Click-Through Rate (CTR), Cost Per Click (CPC), Cost Per Lead, Conversion Rate, and Return on Ad Spend (ROAS). These help us measure the efficiency and profitability of each campaign.

# %%
df['CTR'] = df['clicks'] / df['impressions']
df['CPC'] = df['mark_spent'] / df['clicks']
df['Cost_per_Lead'] = df['mark_spent'] / df['leads']
df['Conversion_Rate'] = df['orders'] / df['clicks']
df['ROAS'] = df['revenue'] / df['mark_spent']

# %% [markdown]
# ## Section 3 - Summarizing Campaign-Level Performance
# 
# To get a clearer view of how each campaign is performing, we aggregate the data by campaign name and re-calculate all KPIs. This allows us to compare performance across campaigns and spot trends in cost efficiency and conversion effectiveness.

# %%
campaign_summary = df.groupby('campaign_name').agg({
    'impressions': 'sum',
    'clicks': 'sum',
    'mark_spent': 'sum',
    'leads': 'sum',
    'orders': 'sum',
    'revenue': 'sum'
}).reset_index()

# Recalculate KPIs for the group
campaign_summary['CTR'] = campaign_summary['clicks'] / campaign_summary['impressions']
campaign_summary['CPC'] = campaign_summary['mark_spent'] / campaign_summary['clicks']
campaign_summary['Conversion_Rate'] = campaign_summary['orders'] / campaign_summary['clicks']
campaign_summary['ROAS'] = campaign_summary['revenue'] / campaign_summary['mark_spent']
campaign_summary

# %% [markdown]
# ## Section 4 - Visualizing Top Campaigns by ROAS and CTR
# 
# We use bar charts to highlight the best and worst performing campaigns based on key metrics like ROAS and CTR. These visuals help quickly identify which campaigns are driving the most value and which ones may require closer scrutiny.

# %%
plt.figure(figsize=(10, 6))
sns.barplot(data=campaign_summary.sort_values('ROAS', ascending=False), x='ROAS', y='campaign_name', palette='crest')
plt.title('Top Campaigns by ROAS')
plt.xlabel('ROAS')
plt.ylabel('Campaign')
plt.show()

# %%
plt.figure(figsize=(10, 6))
sns.barplot(data=campaign_summary.sort_values('CTR', ascending=False), x='CTR', y='campaign_name', palette='flare')
plt.title('Top Campaigns by Click-Through Rate')
plt.xlabel('CTR')
plt.ylabel('Campaign')
plt.show()

# %% [markdown]
# ## Section 5 - Performance Classifacation 
# 
# Here, we categorize each campaign into performance tiers: High Performer, Average, or Needs Optimization. This helps prioritize next steps and guides decisions on budget allocation and campaign improvement.

# %%
# Flag high-performing and underperforming campaigns
def performance_tag(row):
    if row['ROAS'] > 1.5 and row['CTR'] > 0.05:
        return 'High Performer'
    elif row['ROAS'] < 1.0:
        return 'Needs Optimization'
    else:
        return 'Average'

campaign_summary['Performance'] = campaign_summary.apply(performance_tag, axis=1)
campaign_summary[['campaign_name', 'ROAS', 'CTR', 'Performance']]

# %% [markdown]
# ## Section 6 - Optimization Recommendations
# 
# Finally, we provide actionable recommendations based on campaign performance. These include reallocating budget toward high performing campaigns, investigating low ROAS campaigns for targeting or creative issues, and improving landing pages for campaigns with high CTR but low conversions.

# %% [markdown]
# ### Optimization Recommendations:
# - Campaigns with **ROAS < 1.0** should have creative and targeting reviewed or paused.
# - Campaigns with **high CTR but low conversions** may need landing page optimization.
# - Allocate more budget to **high-performing campaigns** with strong ROAS and CTR.

# %% [markdown]
# ## Conclusion
# 
# This analysis provided a comprehensive overview of marketing campaign performance across various digital channels. By calculating key performance indicators like CTR, CPC, and ROAS, we were able to assess the effectiveness of each campaign and identify both high performing and underperforming efforts.
# 
# The results show clear differences in campaign performance, with some campaigns driving strong returns on ad spend, while others may require strategic adjustments. With data driven insights, we recommended optimization actions such as reallocating budget to high ROAS campaigns and improving conversion paths for campaigns with high engagement but low order rates.
# 
# This kind of structured campaign analysis is essential for marketers looking to make informed decisions, reduce wasted spend, and increase overall marketing efficiency.
# 


