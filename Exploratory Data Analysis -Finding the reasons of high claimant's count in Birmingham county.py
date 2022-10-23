#!/usr/bin/env python
# coding: utf-8

# In[724]:


#import libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[1164]:


# Import the file of exploratory data and select the percentage of aged 16+ who are economically inactive 

econ_inactive = pd.read_csv('Exploratory data_CW2.csv', skiprows = 6, nrows =10)
econ_inactive


# In[1165]:


df=pd.DataFrame(econ_inactive)


# In[1166]:


df


# In[1167]:


# sorting out the economically inactive percentage for the year of 2012 in descending orde
df_econ_inactive= df.sort_values(by = 'Jan 2012-Dec 2012 percent',ascending =False)
df_econ_inactive


# In[1168]:


# graphical representation of percentage of Aged 16+ who are economically inactive for the year of 2012
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2012-Dec 2012 percent', y ='Area',  data= df_econ_inactive, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(30,44)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ who are economically inactive in Year 2012', size=14)
plt.show()


# In[730]:


# sorting out the economic inactivity percentage for the year of 2013 in descending orde
df_econ_inactive= df.sort_values(by = 'Jan 2013-Dec 2013 percent',ascending =False)
df_econ_inactive


# In[731]:


# graphical representation of percentage of Aged 16+ who are economically inactive for the year of 2013 
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2013-Dec 2013 percent', y ='Area',  data= df_econ_inactive, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(30,42)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ who are economically inactive in Year 2013', size=14)
plt.show()


# In[732]:


# sorting out the economic inactivity percentage for the year of 2014 in descending orde
df_econ_inactive= df.sort_values(by = 'Jan 2014-Dec 2014 percent',ascending =False)
df_econ_inactive


# In[733]:


# graphical representation of percentage of Aged 16+ who are economically inactive for the year of 2014. 
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation

ax = sns.barplot( x='Jan 2014-Dec 2014 percent', y ='Area',  data= df_econ_inactive, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(30,42)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ who are economically inactive in Year 2014', size=14)
plt.show()


# In[734]:


# sorting out the economic inactivity percentage for the year of 2015 in descending orde
df_econ_inactive= df.sort_values(by = 'Jan 2015-Dec 2015 percent',ascending =False)
df_econ_inactive


# In[735]:


# graphical representation of percentage of Aged 16+ who are economically inactive for the year of 2015. sns.barplot method will return 
# a list of sub methods use containers method to access the text label of each bar by passing it through the ax.bar_label function use 
#for loop to iterate through the list of labels and assign each bar to a different label and set the x-scale for better presentation

ax = sns.barplot( x='Jan 2015-Dec 2015 percent', y ='Area',  data= df_econ_inactive, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(30,44)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ who are economically inactive in Year 2015', size=14)
plt.show()


# In[736]:


# sorting out the economic inactivity percentage for the year of 2016 in descending orde
df_econ_inactive= df.sort_values(by = 'Jan 2016-Dec 2016 percent',ascending =False)
df_econ_inactive


# In[737]:


# graphical representation of percentage of Aged 16+ who are economically inactive for the year of 2016. 
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2016-Dec 2016 percent', y ='Area',  data= df_econ_inactive, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(30,42)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ who are economically inactive in Year 2016', size=14)
plt.show()


# In[738]:


# sorting out the economic inactivity percentage for the year of 2017 in descending orde
df_econ_inactive= df.sort_values(by = 'Jan 2017-Dec 2017 percent',ascending =False)
df_econ_inactive


# In[739]:


# graphical representation of percentage of Aged 16+ who are economically inactive for the year of 2017 
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2017-Dec 2017 percent', y ='Area',  data= df_econ_inactive, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(30,42)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ who are economically inactive in Year 2017', size=14)
plt.show()


# In[740]:


# sorting out the economic inactivity percentage for the year of 2018 in descending orde
df_econ_inactive= df.sort_values(by = 'Jan 2018-Dec 2018 percent',ascending =False)
df_econ_inactive


# In[741]:


# graphical representation of percentage of Aged 16+ who are economically inactive for the year of 2018 
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2018-Dec 2018 percent', y ='Area',  data= df_econ_inactive, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(30,44)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ who are economically inactive in Year 2018', size=14)
plt.show()


# In[742]:


# sorting out the economic inactivity percentage for the year of 2019 in descending orde
df_econ_inactive= df.sort_values(by = 'Jan 2019-Dec 2019 percent',ascending =False)
df_econ_inactive


# In[743]:


# graphical representation of percentage of Aged 16+ who are economically inactive for the year of 2019 
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2019-Dec 2019 percent', y ='Area',  data= df_econ_inactive, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(30,42)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ who are economically inactive in Year 2019', size=14)
plt.show()


# In[744]:


# sorting out the economic inactivity percentage for the year of 2020 in descending orde
df_econ_inactive= df.sort_values(by = 'Jan 2020-Dec 2020 percent',ascending =False)
df_econ_inactive


# In[745]:


# graphical representation of percentage of Aged 16+ who are economically inactive for the year of 2020 
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2020-Dec 2020 percent', y ='Area',  data= df_econ_inactive, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(28,40)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ who are economically inactive in Year 2020', size=14)
plt.show()


# In[746]:


# sorting out the economic inactivity percentage for the year of 2021 in descending orde
df_econ_inactive= df.sort_values(by = 'Jan 2021-Dec 2021 percent',ascending =False)
df_econ_inactive


# In[747]:


# graphical representation of percentage of Aged 16+ who are economically inactive for the year of 2021 
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2021-Dec 2021 percent', y ='Area',  data= df_econ_inactive, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(30,42)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ who are economically inactive in Year 2021', size=14)
plt.show()


# In[1170]:


# Import the file of exploratory data and select the percentage of aged 16+ Male who are economically inactive 

econ_inactive_male = pd.read_csv('Exploratory data_CW2.csv', skiprows = 26, nrows =10)
econ_inactive_male 


# In[1171]:


df_econ_inactive_Male= pd.DataFrame (econ_inactive_male)


# In[1172]:


df_econ_inactive_Male


# In[1173]:


# Calculating the mean value of all counties to observe the difference in their values from 2012-2021 and select the percenatge
# column only by using axis function. Use numeric_only function to avoid the columns heading and any non-numeric value.
print(df_econ_inactive_Male.mean(axis=1, numeric_only=True))


# In[751]:


# sorting out the economic inactivity percentage for the year of 2012 in descending orde
df_econ_inactive_Male =df_econ_inactive_Male .sort_values(by = 'Jan 2012-Dec 2012 percent',ascending =False)
df_econ_inactive_Male


# In[752]:


# graphical representation of percentage of Aged 16+ Male who are economically inactive for the year of 2012 
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2012-Dec 2012 percent', y ='Area',  data= df_econ_inactive_Male, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(25,35)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ Male who are economically inactive in Year 2012', size=14)
plt.show()


# In[753]:


# sorting out the economic inactivity percentage for the year of 2013 in descending orde
df_econ_inactive_Male= df_econ_inactive_Male.sort_values(by = 'Jan 2013-Dec 2013 percent',ascending =False)
df_econ_inactive_Male 


# In[754]:


# graphical representation of percentage of Aged 16+ Male who are economically inactive for the year of 2013
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2013-Dec 2013 percent', y ='Area',  data= df_econ_inactive_Male, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(23,36)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ Male who are economically inactive in Year 2013', size=14)
plt.show()


# In[755]:


# sorting out the economic inactivity percentage for the year of 2014 in descending orde
df_econ_inactive_Male= df_econ_inactive_Male.sort_values(by = 'Jan 2014-Dec 2014 percent',ascending =False)
df_econ_inactive_Male


# In[756]:


# graphical representation of percentage of Aged 16+ Male who are economically inactive for the year of 2014 
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2014-Dec 2014 percent', y ='Area',  data= df_econ_inactive_Male, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(25,35)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ Male who are economically inactive in Year 2014', size=14)
plt.show()


# In[757]:


# sorting out the economic inactivity percentage for the year of 2015 in descending orde
df_econ_inactive_Male= df_econ_inactive_Male.sort_values(by = 'Jan 2015-Dec 2015 percent',ascending =False)
df_econ_inactive_Male


# In[758]:


# graphical representation of percentage of Aged 16+ Male who are economically inactive for the year of 2015 
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2015-Dec 2015 percent', y ='Area',  data= df_econ_inactive_Male, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(25,37)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ Male who are economically inactive in Year 2015', size=14)
plt.show()


# In[759]:


# sorting out the economic inactivity percentage for the year of 2016 in descending orde
df_econ_inactive_Male= df_econ_inactive_Male.sort_values(by = 'Jan 2016-Dec 2016 percent',ascending =False)
df_econ_inactive_Male


# In[760]:


# graphical representation of percentage of Aged 16+ Male who are economically inactive for the year of 2016 
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2016-Dec 2016 percent', y ='Area',  data= df_econ_inactive_Male, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(24,35)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ Male who are economically inactive in Year 2016', size=14)
plt.show()


# In[761]:


# sorting out the economic inactivity percentage for the year of 2017 in descending orde
df_econ_inactive_Male= df_econ_inactive_Male.sort_values(by = 'Jan 2017-Dec 2017 percent',ascending =False)
df_econ_inactive_Male


# In[762]:


# graphical representation of percentage of Aged 16+ Male who are economically inactive for the year of 2017 
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2017-Dec 2017 percent', y ='Area',  data= df_econ_inactive_Male, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(24,34)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ Male who are economically inactive in Year 2017', size=14)
plt.show()


# In[763]:


# sorting out the economic inactivity percentage for the year of 2018 in descending orde
df_econ_inactive_Male= df_econ_inactive_Male.sort_values(by = 'Jan 2018-Dec 2018 percent',ascending =False)
df_econ_inactive_Male


# In[764]:


# graphical representation of percentage of Aged 16+ Male who are economically inactive for the year of 2018 
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2018-Dec 2018 percent', y ='Area',  data= df_econ_inactive_Male, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(26,36)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ Male who are economically inactive in Year 2018', size=14)
plt.show()


# In[765]:


# sorting out the economic inactivity percentage for the year of 2019 in descending orde
df_econ_inactive_Male= df_econ_inactive_Male.sort_values(by = 'Jan 2019-Dec 2019 percent',ascending =False)
df_econ_inactive_Male


# In[766]:


# graphical representation of percentage of Aged 16+ Male who are economically inactive for the year of 2019
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2019-Dec 2019 percent', y ='Area',  data= df_econ_inactive_Male, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(25,35)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ Male who are economically inactive in Year 2019', size=14)
plt.show()


# In[767]:


# sorting out the economic inactivity percentage for the year of 2020 in descending orde
df_econ_inactive_Male= df_econ_inactive_Male.sort_values(by = 'Jan 2020-Dec 2020 percent',ascending =False)
df_econ_inactive_Male


# In[768]:


# graphical representation of percentage of Aged 16+ Male who are economically inactive for the year of 2020
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2020-Dec 2020 percent', y ='Area',  data= df_econ_inactive_Male, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(25,35)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ Male who are economically inactive in Year 2020', size=14)
plt.show()


# In[769]:


# sorting out the economic inactivity percentage for the year of 2021 in descending orde
df_econ_inactive_Male= df_econ_inactive_Male.sort_values(by = 'Jan 2021-Dec 2021 percent',ascending =False)
df_econ_inactive_Male


# In[770]:


# graphical representation of percentage of Aged 16+ Male who are economically inactive for the year of 2021
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2021-Dec 2021 percent', y ='Area',  data= df_econ_inactive_Male, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(26,35)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ Male who are economically inactive in Year 2021', size=14)
plt.show()


# In[1222]:


# Import the file of exploratory data and select the percentage of aged 16+ Female who are economically inactive 

econ_inactive_Female = pd.read_csv('Exploratory data_CW2.csv', skiprows = 46, nrows =10)
econ_inactive_Female 


# In[1175]:


df_econ_inactive_Female= pd.DataFrame (econ_inactive_Female)


# In[1176]:


df_econ_inactive_Female


# In[1177]:


# Calculating the mean value of all counties to observe the difference in their values from 2012-2021 and select the percenatge
# column only by using axis function. Use numeric_only function to avoid the columns headings and any other non-numeric value
print(df_econ_inactive_Female.mean(axis=1, numeric_only=True))


# In[774]:


# sorting out the economic inactivity percentage for the year of 2012 in descending orde
df_econ_inactive_Female = df_econ_inactive_Female.sort_values(by = 'Jan 2012-Dec 2012 percent',ascending =False)
df_econ_inactive_Female


# In[775]:


# graphical representation of percentage of Aged 16+ Female who are economically inactive for the year of 2012.
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2012-Dec 2012 percent', y ='Area',  data= df_econ_inactive_Female, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(37,52)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ Female who are economically inactive in Year 2012', size=14)
plt.show()


# In[776]:


# sorting out the economic inactivity percentage for the year of 2013 in descending orde
df_econ_inactive_Female= df_econ_inactive_Female.sort_values(by = 'Jan 2013-Dec 2013 percent',ascending =False)
df_econ_inactive_Female


# In[777]:


# graphical representation of percentage of Aged 16+ Female who are economically inactive for the year of 2013.
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2013-Dec 2013 percent', y ='Area',  data= df_econ_inactive_Female, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(37,52)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ Female who are economically inactive in Year 2013', size=14)
plt.show()


# In[778]:


# sorting out the economic inactivity percentage for the year of 2014 in descending orde
df_econ_inactive_Female= df_econ_inactive_Female.sort_values(by = 'Jan 2014-Dec 2014 percent',ascending =False)
df_econ_inactive_Female


# In[779]:


# graphical representation of percentage of Aged 16+ Female who are economically inactive for the year of 2014 
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2014-Dec 2014 percent', y ='Area',  data= df_econ_inactive_Female, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(37,52)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ Female who are economically inactive in Year 2014', size=14)
plt.show()


# In[780]:


# sorting out the economic inactivity percentage for the year of 2015 in descending orde
df_econ_inactive_Female= df_econ_inactive_Female.sort_values(by = 'Jan 2015-Dec 2015 percent',ascending =False)
df_econ_inactive_Female


# In[781]:


# graphical representation of percentage of Aged 16+ Female who are economically inactive for the year of 2015
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2015-Dec 2015 percent', y ='Area',  data= df_econ_inactive_Female, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(36,52)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ Female who are economically inactive in Year 2015', size=14)
plt.show()


# In[782]:


# sorting out the economic inactivity percentage for the year of 2016 in descending orde
df_econ_inactive_Female= df_econ_inactive_Female.sort_values(by = 'Jan 2016-Dec 2016 percent',ascending =False)
df_econ_inactive_Female


# In[783]:


# graphical representation of percentage of Aged 16+ Female who are economically inactive for the year of 2016 
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2016-Dec 2016 percent', y ='Area',  data= df_econ_inactive_Female, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(37,50)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ Female who are economically inactive in Year 2016', size=14)
plt.show()


# In[784]:


# sorting out the economic inactivity percentage for the year of 2017 in descending orde
df_econ_inactive_Female= df_econ_inactive_Female.sort_values(by = 'Jan 2017-Dec 2017 percent',ascending =False)
df_econ_inactive_Female


# In[785]:


# graphical representation of percentage of Aged 16+ Female who are economically inactive for the year of 2017 
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2017-Dec 2017 percent', y ='Area',  data= df_econ_inactive_Female, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(37,50)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ Female who are economically inactive in Year 2017', size=14)
plt.show()


# In[786]:


# sorting out the economic inactivity percentage for the year of 2018 in descending orde
df_econ_inactive_Female= df_econ_inactive_Female.sort_values(by = 'Jan 2018-Dec 2018 percent',ascending =False)
df_econ_inactive_Female


# In[787]:


# graphical representation of percentage of Aged 16+ Female who are economically inactive for the year of 2018 
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2018-Dec 2018 percent', y ='Area',  data= df_econ_inactive_Female, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(37,52)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ Female who are economically inactive in Year 2018', size=14)
plt.show()


# In[788]:


# sorting out the economic inactivity percentage for the year of 2019 in descending orde
df_econ_inactive_Female= df_econ_inactive_Female.sort_values(by = 'Jan 2019-Dec 2019 percent',ascending =False)
df_econ_inactive_Female


# In[789]:


# graphical representation of percentage of Aged 16+ Female who are economically inactive for the year of 2019 
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2019-Dec 2019 percent', y ='Area',  data= df_econ_inactive_Female, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(37,50)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ Female who are economically inactive in Year 2019', size=14)
plt.show()


# In[790]:


# sorting out the economic inactivity percentage for the year of 2020 in descending orde
df_econ_inactive_Female= df_econ_inactive_Female.sort_values(by = 'Jan 2020-Dec 2020 percent',ascending =False)
df_econ_inactive_Female


# In[791]:


# graphical representation of percentage of Aged 16+ Female who are economically inactive for the year of 2020 
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2020-Dec 2020 percent', y ='Area',  data= df_econ_inactive_Female, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(30,47)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ Female who are economically inactive in Year 2020', size=14)
plt.show()


# In[792]:


# sorting out the economic inactivity percentage for the year of 2021 in descending orde
df_econ_inactive_Female= df_econ_inactive_Female.sort_values(by = 'Jan 2021-Dec 2021 percent',ascending =False)
df_econ_inactive_Female


# In[793]:


# graphical representation of percentage of Aged 16+ Female who are economically inactive for the year of 2021
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2021-Dec 2021 percent', y ='Area',  data= df_econ_inactive_Female, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(35,47)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16+ Female who are economically inactive in Year 2021', size=14)
plt.show()


# In[794]:


#Now exploring the reasons of economic inacivity 1) Due to eduction (being students) 2) Loocking after family/Home 
# 3) Being Retired


# In[1224]:


# Import the file of exploratory data and select the percentage of economically inactive Student data by using skiprows and nrows function

econ_inactive_student = pd.read_csv('Exploratory data_CW2.csv', skiprows = 26, nrows =10, na_values =('#','!'))
econ_inactive_student


# In[796]:


df_inactive_student= pd.DataFrame(econ_inactive_student)
df_inactive_student


# In[1179]:


# Calculating the mean value of all counties to observe the difference in their values from 2012-2021 and select the percenatge
# column only by using axis function. Use numeric_only function to avoid the columns headings and any other non-numeric value
print(df_inactive_student.mean(axis=1, numeric_only=True))


# In[797]:


# Tabulating and sorting out the percentage of economically inactive students for the year of 2012 by using ascending function
df_inactive_student = df_inactive_student.sort_values(by = 'Jan 2012-Dec 2012 percent',ascending =False)
df_inactive_student


# In[798]:


# graphical representation of percentage of economically inactive student for the year of 2012
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2012-Dec 2012 percent', y ='Area',  data= df_inactive_student, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(25,35)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive  student in Year 2012', size=14)
plt.show()


# In[799]:


# Tabulating and sorting out the percentage of economically inactive students for the year of 2013 by using ascending function
df_inactive_student = df_inactive_student.sort_values(by = 'Jan 2013-Dec 2013 percent',ascending =False)
df_inactive_student


# In[800]:


# graphical representation of percentage of economically inactive student for the year of 2013
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2013-Dec 2013 percent', y ='Area',  data= df_inactive_student, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(23,37)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive  student in Year 2013', size=14)
plt.show()


# In[801]:


# Tabulating and sorting out the percentage of economically inactive students for the year of 2014 by using ascending function
df_inactive_student = df_inactive_student.sort_values(by = 'Jan 2014-Dec 2014 percent',ascending =False)
df_inactive_student


# In[802]:


# graphical representation of percentage of economically inactive student for the year of 2014
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2014-Dec 2014 percent', y ='Area',  data= df_inactive_student, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(24,36)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive  student in Year 2014', size=14)
plt.show()


# In[803]:


# Tabulating and sorting out the percentage of economically inactive students for the year of 2015 by using ascending function
df_inactive_student = df_inactive_student.sort_values(by = 'Jan 2015-Dec 2015 percent',ascending =False)
df_inactive_student


# In[804]:


# graphical representation of percentage of economically inactive student for the year of 2015
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2015-Dec 2015 percent', y ='Area',  data= df_inactive_student, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(24,37)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive  student in Year 2015', size=14)
plt.show()


# In[805]:


# Tabulating and sorting out the percentage of economically inactive students for the year of 2016 by using ascending function
df_inactive_student = df_inactive_student.sort_values(by = 'Jan 2016-Dec 2016 percent',ascending =False)
df_inactive_student


# In[806]:


# graphical representation of percentage of economically inactive student for the year of 2016
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2016-Dec 2016 percent', y ='Area',  data= df_inactive_student, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(24,36)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive  student in Year 2016', size=14)
plt.show()


# In[807]:


# Tabulating and sorting out the percentage of economically inactive students for the year of 2017 by using ascending function
df_inactive_student = df_inactive_student.sort_values(by = 'Jan 2017-Dec 2017 percent',ascending =False)
df_inactive_student


# In[808]:


# graphical representation of percentage of economically inactive student for the year of 2017
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2017-Dec 2017 percent', y ='Area',  data= df_inactive_student, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(24,34)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive  student in Year 2017', size=14)
plt.show()


# In[809]:


# Tabulating and sorting out the percentage of economically inactive students for the year of 2018 by using ascending function
df_inactive_student = df_inactive_student.sort_values(by = 'Jan 2018-Dec 2018 percent',ascending =False)
df_inactive_student


# In[810]:


# graphical representation of percentage of economically inactive student for the year of 2018
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2018-Dec 2018 percent', y ='Area',  data= df_inactive_student, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(24,36)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive  student in Year 2018', size=14)
plt.show()


# In[811]:


# Tabulating and sorting out the percentage of economically inactive students for the year of 2019 by using ascending function
df_inactive_student = df_inactive_student.sort_values(by = 'Jan 2019-Dec 2019 percent',ascending =False)
df_inactive_student


# In[812]:


# graphical representation of percentage of economically inactive student for the year of 2019
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2019-Dec 2019 percent', y ='Area',  data= df_inactive_student, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(24,35)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive  student in Year 2019', size=14)
plt.show()


# In[813]:


# Tabulating and sorting out the percentage of economically inactive students for the year of 2020 by using ascending function
df_inactive_student = df_inactive_student.sort_values(by = 'Jan 2020-Dec 2020 percent',ascending =False)
df_inactive_student


# In[814]:


# graphical representation of percentage of economically inactive student for the year of 2020
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2020-Dec 2020 percent', y ='Area',  data= df_inactive_student, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(24,35)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive  student in Year 2020', size=14)
plt.show()


# In[815]:


# Tabulating and sorting out the percentage of economically inactive students for the year of 2021 by using ascending function
df_inactive_student = df_inactive_student.sort_values(by = 'Jan 2021-Dec 2021 percent',ascending =False)
df_inactive_student


# In[816]:


# graphical representation of percentage of economically inactive student for the year of 2021
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2021-Dec 2021 percent', y ='Area',  data= df_inactive_student, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(24,36)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive  student in Year 2021', size=14)
plt.show()


# In[1180]:


# Import the file of exploratory data and select the percentage of economically inactive looking after family/home data by using skiprows and nrows function

econ_inactive_home = pd.read_csv('Exploratory data_CW2.csv', skiprows = 86, nrows =10, na_values =('#','!'))
econ_inactive_home


# In[1181]:


df_inactive_home= pd.DataFrame(econ_inactive_home)
df_inactive_home


# In[1182]:


# Calculating the mean value of all counties to observe the difference in their values from 2012-2021 and select the percenatge
# column only by using axis function. Use numeric_only function to avoid the columns headings and any other non-numeric value
print(df_inactive_home.mean(axis=1, numeric_only=True))


# In[819]:


# Tabulating and sorting out the percentage of economically inactive looking after family/ home for the year of 2012 by using ascending function
df_inactive_home2012 = df_inactive_home.sort_values(by = 'Jan 2012-Dec 2012 percent',ascending =False)
df_inactive_home2012


# In[820]:


# graphical representation of percentage of economically inactive looking after family/home for the year of 2012
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2012-Dec 2012 percent', y ='Area',  data= df_inactive_home2012, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(16,33)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive looing after family/home in Year 2012', size=14)
plt.show()


# In[821]:


# Tabulating and sorting out the percentage of economically inactive looking after home for the year of 2013 by using ascending function
df_inactive_home2013 = df_inactive_home.sort_values(by = 'Jan 2013-Dec 2013 percent',ascending =False)
df_inactive_home2013


# In[822]:


# graphical representation of percentage of economically inactive looking after family/home for the year of 2013
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2013-Dec 2013 percent', y ='Area',  data= df_inactive_home2013, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(21,35)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive looing after family/home in Year 2013', size=14)
plt.show()


# In[823]:


# Tabulating and sorting out the percentage of economically inactive looking after home for the year of 2014 by using ascending function
df_inactive_home2014 = df_inactive_home.sort_values(by = 'Jan 2014-Dec 2014 percent',ascending =False)
df_inactive_home2014


# In[824]:


# graphical representation of percentage of economically inactive looking after family/home for the year of 2014
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2014-Dec 2014 percent', y ='Area',  data= df_inactive_home2014, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(16,33)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive looing after family/home in Year 2014', size=14)
plt.show()


# In[825]:


# Tabulating and sorting out the percentage of economically inactive looking after home for the year of 2015 by using ascending function
df_inactive_home2015 = df_inactive_home.sort_values(by = 'Jan 2015-Dec 2015 percent',ascending =False)
df_inactive_home2015


# In[826]:


# Graphical representation of percentage of economically inactive looking after family/home for the year of 2015
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2015-Dec 2015 percent', y ='Area',  data= df_inactive_home2015, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(19,34)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive looing after family/home in Year 2015', size=14)
plt.show()


# In[827]:


# Tabulating and sorting out the percentage of economically inactive looking after home for the year of 2016 by using ascending function
df_inactive_home2016 = df_inactive_home.sort_values(by = 'Jan 2016-Dec 2016 percent',ascending =False)
df_inactive_home2016


# In[828]:


# Graphical representation of percentage of economically inactive looking after family/home for the year of 2016
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2016-Dec 2016 percent', y ='Area',  data= df_inactive_home2016, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(18,37)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive looing after family/home in Year 2016', size=14)
plt.show()


# In[829]:


# Tabulating and sorting out the percentage of economically inactive looking after home for the year of 2017 by using ascending function
df_inactive_home2017 = df_inactive_home.sort_values(by = 'Jan 2017-Dec 2017 percent',ascending =False)
df_inactive_home2017


# In[830]:


# Graphical representation of percentage of economically inactive looking after family/home for the year of 2017
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2017-Dec 2017 percent', y ='Area',  data= df_inactive_home2017, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(19,34)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive looing after family/home in Year 2017', size=14)
plt.show()


# In[831]:


# Tabulating and sorting out the percentage of economically inactive looking after home for the year of 2018 by using ascending function
df_inactive_home2018 = df_inactive_home.sort_values(by = 'Jan 2018-Dec 2018 percent',ascending =False)
df_inactive_home2018


# In[832]:


# Graphical representation of percentage of economically inactive looking after family/home for the year of 2018
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2018-Dec 2018 percent', y ='Area',  data= df_inactive_home2018, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(16,33)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive looing after family/home in Year 2018', size=14)
plt.show()


# In[833]:


# Tabulating and sorting out the percentage of economically inactive looking after home for the year of 2019 by using ascending function
df_inactive_home2019 = df_inactive_home.sort_values(by = 'Jan 2019-Dec 2019 percent',ascending =False)
df_inactive_home2019


# In[834]:


# Graphical representation of percentage of economically inactive looking after family/home for the year of 2019
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2019-Dec 2019 percent', y ='Area',  data= df_inactive_home2019, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(16,33)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive looing after family/home in Year 2019', size=14)
plt.show()


# In[835]:


# Tabulating and sorting out the percentage of economically inactive looking after home for the year of 2020 by using ascending function
df_inactive_home2020 = df_inactive_home.sort_values(by = 'Jan 2020-Dec 2020 percent',ascending =False)
df_inactive_home2020


# In[836]:


# Graphical representation of percentage of economically inactive looking after family/home for the year of 2020
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2020-Dec 2020 percent', y ='Area',  data= df_inactive_home2020, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(16,33)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive looing after family/home in Year 2020', size=14)
plt.show()


# In[837]:


# Tabulating and sorting out the percentage of economically inactive looking after home for the year of 2021 by using ascending function
df_inactive_home2021 = df_inactive_home.sort_values(by = 'Jan 2021-Dec 2021 percent',ascending =False)
df_inactive_home2021


# In[838]:


# Graphical representation of percentage of economically inactive looking after family/home for the year of 2021
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2021-Dec 2021 percent', y ='Area',  data= df_inactive_home2021, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(15,33)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive looing after family/home in Year 2021', size=14)
plt.show()


# In[1183]:


# Import the file of exploratory data and select the percentage of economically inactive retired by using skiprows and nrows function

econ_inactive_retired = pd.read_csv('Exploratory data_CW2.csv', skiprows = 106, nrows =10, na_values=('#','!'))
econ_inactive_retired


# In[1184]:


df_inactive_retired = pd.DataFrame (econ_inactive_retired)
df_inactive_retired


# In[1185]:


# Calculating the mean value of all counties to observe the difference in their values from 2012-2021 and select the percenatge
# column only by using axis function. Use numeric_only function to avoid the columns headings and any other non-numeric value
print(df_inactive_retired.mean(axis=1,numeric_only= True))


# In[841]:


# Tabulating and sorting out the percentage of economically inactive retired for the year of 2012 by using ascending function
df_inactive_retired2012 = df_inactive_retired.sort_values(by = 'Jan 2012-Dec 2012 percent',ascending =False)
df_inactive_retired2012


# In[842]:


# Graphical representation of percentage of economically inactive retired for the year of 2012
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2012-Dec 2012 percent', y ='Area',  data= df_inactive_retired2012, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(2,25)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive retired in Year 2012', size=14)
plt.show()


# In[843]:


# Tabulating and sorting out the percentage of economically inactive retired for the year of 2013 by using ascending function
df_inactive_retired2013 = df_inactive_retired.sort_values(by = 'Jan 2013-Dec 2013 percent',ascending =False)
df_inactive_retired2013


# In[844]:


# Graphical representation of percentage of economically inactive retired for the year of 2013
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2013-Dec 2013 percent', y ='Area',  data= df_inactive_retired2013, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(2,24)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive retired in Year 2013', size=14)
plt.show()


# In[1186]:



# Tabulating and sorting out the percentage of economically inactive retired for the year of 2014 by using ascending function
df_inactive_retired2014 = df_inactive_retired.sort_values(by = 'Jan 2014-Dec 2014 percent',ascending =False)
df_inactive_retired2014


# In[846]:


# Graphical representation of percentage of economically inactive retired for the year of 2014
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2014-Dec 2014 percent', y ='Area',  data= df_inactive_retired2014, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(2,25)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive retired in Year 2014', size=14)
plt.show()


# In[847]:


# Tabulating and sorting out the percentage of economically inactive retired for the year of 2015 by using ascending function
df_inactive_retired2015 = df_inactive_retired.sort_values(by = 'Jan 2015-Dec 2015 percent',ascending =False)
df_inactive_retired2015


# In[848]:


# Graphical representation of percentage of economically inactive retired for the year of 2015
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2015-Dec 2015 percent', y ='Area',  data= df_inactive_retired2015, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(2,22)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive retired in Year 2015', size=14)
plt.show()


# In[849]:


# Tabulating and sorting out the percentage of economically inactive retired for the year of 2016 by using ascending function
df_inactive_retired2016 = df_inactive_retired.sort_values(by = 'Jan 2016-Dec 2016 percent',ascending =False)
df_inactive_retired2016


# In[850]:


# Graphical representation of percentage of economically inactive retired for the year of 2016
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2016-Dec 2016 percent', y ='Area',  data= df_inactive_retired2016, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(2,19)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive retired in Year 2016', size=14)
plt.show()


# In[851]:


# Tabulating and sorting out the percentage of economically inactive retired for the year of 2017 by using ascending function
df_inactive_retired2017 = df_inactive_retired.sort_values(by = 'Jan 2017-Dec 2017 percent',ascending =False)
df_inactive_retired2017


# In[852]:


# Graphical representation of percentage of economically inactive retired for the year of 2017
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2017-Dec 2017 percent', y ='Area',  data= df_inactive_retired2017, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(2,24)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive retired in Year 2017', size=14)
plt.show()


# In[853]:


# Tabulating and sorting out the percentage of economically inactive retired for the year of 2018 by using ascending function
df_inactive_retired2018 = df_inactive_retired.sort_values(by = 'Jan 2018-Dec 2018 percent',ascending =False)
df_inactive_retired2018


# In[854]:


# Graphical representation of percentage of economically inactive retired for the year of 2018
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2018-Dec 2018 percent', y ='Area',  data= df_inactive_retired2018, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(2,22)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive retired in Year 2018', size=14)
plt.show()


# In[855]:


# Tabulating and sorting out the percentage of economically inactive retired for the year of 2019 by using ascending function
df_inactive_retired2019 = df_inactive_retired.sort_values(by = 'Jan 2019-Dec 2019 percent',ascending =False)
df_inactive_retired2019


# In[856]:


# Graphical representation of percentage of economically inactive retired for the year of 2019
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2019-Dec 2019 percent', y ='Area',  data= df_inactive_retired2019, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(2,24)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive retired in Year 2019', size=14)
plt.show()


# In[857]:


# Tabulating and sorting out the percentage of economically inactive retired for the year of 2020 by using ascending function
df_inactive_retired2020 = df_inactive_retired.sort_values(by = 'Jan 2020-Dec 2020 percent',ascending =False)
df_inactive_retired2020


# In[858]:


# Graphical representation of percentage of economically inactive retired for the year of 2020
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2020-Dec 2020 percent', y ='Area',  data= df_inactive_retired2020, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(2,24)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive retired in Year 2020', size=14)
plt.show()


# In[859]:


# Tabulating and sorting out the percentage of economically inactive retired for the year of 2021 by using ascending function
df_inactive_retired2021 = df_inactive_retired.sort_values(by = 'Jan 2021-Dec 2021 percent',ascending =False)
df_inactive_retired2021


# In[860]:


# Graphical representation of percentage of economically inactive retired for the year of 2021
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2021-Dec 2021 percent', y ='Area',  data= df_inactive_retired2021, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Economically inactive percentage', size =14)
plt.xlim(2,24)
plt.ylabel('Area', size =16)
plt.title('The percentage of economically inactive retired in Year 2021', size=14)
plt.show()


# In[861]:


# Import the file of exploratory data and select the percentage of White aged 16+ by using skiprows and nrows function

data_white_16plus = pd.read_csv('Exploratory data_CW2.csv', skiprows = 250, nrows =10)
data_white_16plus


# In[862]:


df_white_16plus = pd.DataFrame(data_white_16plus)
df_white_16plus


# In[863]:


# Tabulating and sorting out the percentage of white aged 16+ for the year of 2012 by using ascending function
df_white_16plus2012 = df_white_16plus.sort_values(by = 'Jan 2012-Dec 2012 percent',ascending =False)
df_white_16plus2012


# In[864]:


# Graphical representation of percentage of white aged 16+ for the year of 2012
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2012-Dec 2012 percent', y ='Area',  data= df_white_16plus2012, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Percentage of White Aged 16+', size =14)
plt.xlim(60,98)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16+ in Year 2012', size=14)
plt.show()


# In[865]:


# Tabulating and sorting out the percentage of white aged 16+ for the year of 2013 by using ascending function
df_white_16plus2013 = df_white_16plus.sort_values(by = 'Jan 2013-Dec 2013 percent',ascending =False)
df_white_16plus2013


# In[866]:


# Graphical representation of percentage of white aged 16+ for the year of 2013
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2013-Dec 2013 percent', y ='Area',  data= df_white_16plus2013, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Percentage of White Aged 16+', size =14)
plt.xlim(60,98)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16+ in Year 2013', size=14)
plt.show()


# In[867]:


# Tabulating and sorting out the percentage of white aged 16+ for the year of 2014 by using ascending function
df_white_16plus2014 = df_white_16plus.sort_values(by = 'Jan 2014-Dec 2014 percent',ascending =False)
df_white_16plus2014


# In[868]:


# Graphical representation of percentage of white aged 16+ for the year of 2014
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2014-Dec 2014 percent', y ='Area',  data= df_white_16plus2014, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Percentage of White Aged 16+', size =14)
plt.xlim(60,98)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16+ in Year 2014', size=14)
plt.show()


# In[869]:


# Tabulating and sorting out the percentage of white aged 16+ for the year of 2015 by using ascending function
df_white_16plus2015 = df_white_16plus.sort_values(by = 'Jan 2015-Dec 2015 percent',ascending =False)
df_white_16plus2015


# In[870]:


# Graphical representation of percentage of white aged 16+ for the year of 2015
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2015-Dec 2015 percent', y ='Area',  data= df_white_16plus2015, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Percentage of White Aged 16+', size =14)
plt.xlim(60,98)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16+ in Year 2015', size=14)
plt.show()


# In[871]:


# Tabulating and sorting out the percentage of white aged 16+ for the year of 2016 by using ascending function
df_white_16plus2016 = df_white_16plus.sort_values(by = 'Jan 2016-Dec 2016 percent',ascending =False)
df_white_16plus2016


# In[872]:


# Graphical representation of percentage of white aged 16+ for the year of 2016
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2016-Dec 2016 percent', y ='Area',  data= df_white_16plus2016, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Percentage of White Aged 16+', size =14)
plt.xlim(55,100)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16+ in Year 2016', size=14)
plt.show()


# In[873]:


# Tabulating and sorting out the percentage of white aged 16+ for the year of 2017 by using ascending function
df_white_16plus2017 = df_white_16plus.sort_values(by = 'Jan 2017-Dec 2017 percent',ascending =False)
df_white_16plus2017


# In[874]:


# Graphical representation of percentage of white aged 16+ for the year of 2017
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2017-Dec 2017 percent', y ='Area',  data= df_white_16plus2017, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Percentage of White Aged 16+', size =14)
plt.xlim(55,98)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16+ in Year 2017', size=14)
plt.show()


# In[875]:


# Tabulating and sorting out the percentage of white aged 16+ for the year of 2018 by using ascending function
df_white_16plus2018 = df_white_16plus.sort_values(by = 'Jan 2018-Dec 2018 percent',ascending =False)
df_white_16plus2018


# In[876]:


# Graphical representation of percentage of white aged 16+ for the year of 2018
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2018-Dec 2018 percent', y ='Area',  data= df_white_16plus2018, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Percentage of White Aged 16+', size =14)
plt.xlim(55,100)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16+ in Year 2018', size=14)
plt.show()


# In[877]:


# Tabulating and sorting out the percentage of white aged 16+ for the year of 2019 by using ascending function
df_white_16plus2019 = df_white_16plus.sort_values(by = 'Jan 2019-Dec 2019 percent',ascending =False)
df_white_16plus2019


# In[878]:


# Graphical representation of percentage of white aged 16+ for the year of 2019
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2019-Dec 2019 percent', y ='Area',  data= df_white_16plus2019, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Percentage of White Aged 16+', size =14)
plt.xlim(55,100)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16+ in Year 2019', size=14)
plt.show()


# In[879]:


# Tabulating and sorting out the percentage of white aged 16+ for the year of 2020 by using ascending function
df_white_16plus2020 = df_white_16plus.sort_values(by = 'Jan 2020-Dec 2020 percent',ascending =False)
df_white_16plus2020


# In[880]:


# Graphical representation of percentage of white aged 16+ for the year of 2020
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2020-Dec 2020 percent', y ='Area',  data= df_white_16plus2020, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Percentage of White Aged 16+', size =14)
plt.xlim(55,100)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16+ in Year 2020', size=14)
plt.show()


# In[881]:


# Tabulating and sorting out the percentage of white aged 16+ for the year of 2021 by using ascending function
df_white_16plus2021 = df_white_16plus.sort_values(by = 'Jan 2021-Dec 2021 percent',ascending =False)
df_white_16plus2021


# In[882]:


# Graphical representation of percentage of white aged 16+ for the year of 2021
#sns.barplot method will return a list of sub methods use containers method to access the text label of each bar by passing it
# through the ax.bar_label function use for loop to iterate through the list of labels and assign each bar to a different
#label and set the x-scale for better presentation
ax = sns.barplot( x='Jan 2021-Dec 2021 percent', y ='Area',  data= df_white_16plus2021, errwidth=0)
for i in ax.containers:
    ax.bar_label(i,)
plt.xlabel('Percentage of White Aged 16+', size =14)
plt.xlim(50,100)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16+ in Year 2021', size=14)
plt.show()


# In[883]:


# Import the file of exploratory data and select the percentage of White aged 16-64 by using skiprows and nrows function

data_whiteworking_popn= pd.read_csv('Exploratory data_CW2.csv', skiprows = 270, nrows =10)
data_whiteworking_popn


# In[1188]:


df_whiteworking_popn = pd.DataFrame(data_whiteworking_popn)
df_whiteworking_popn


# In[1189]:


# Calculating the mean value of all counties to observe the difference in their values from 2012-2021 and select the percenatge
# column only by using axis function
print(df_whiteworking_popn.mean(axis=1, numeric_only=True))


# In[1190]:


# Tabulating and sorting out the percentage of white aged 16- 64 for the year of 2012 by using ascending function
df_whiteworking_popn2012 = df_whiteworking_popn.sort_values(by = 'Jan 2012-Dec 2012 percent',ascending =False)
df_whiteworking_popn2012


# In[887]:


#graphical representation of percentage of White Aged 16-64 for the year of 2012 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2012-Dec 2012 percent', y ='Area',  data= df_whiteworking_popn2012, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of White Aged 16-64', size =14)
plt.xlim(55,100)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16 -64 Years old (White working Population) in Year 2012', size=14)
plt.show()


# In[888]:


# Tabulating and sorting out the percentage of white aged 16- 64 for the year of 2013 by using ascending function
df_whiteworking_popn2013 = df_whiteworking_popn.sort_values(by = 'Jan 2013-Dec 2013 percent',ascending =False)
df_whiteworking_popn2013


# In[889]:


#graphical representation of percentage of White Aged 16-64 for the year of 2013 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2013-Dec 2013 percent', y ='Area',  data= df_whiteworking_popn2013, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of White Aged 16-64', size =14)
plt.xlim(55,100)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16 -64 Years old (White working Population) in Year 2013', size=14)
plt.show()


# In[890]:


# Tabulating and sorting out the percentage of white aged 16- 64 for the year of 2014 by using ascending function
df_whiteworking_popn2014 = df_whiteworking_popn.sort_values(by = 'Jan 2014-Dec 2014 percent',ascending =False)
df_whiteworking_popn2014


# In[891]:


#graphical representation of percentage of White Aged 16-64 for the year of 2014 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2014-Dec 2014 percent', y ='Area',  data= df_whiteworking_popn2014, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of White Aged 16-64', size =14)
plt.xlim(55,100)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16 -64 Years old (White working Population) in Year 2014', size=14)
plt.show()


# In[892]:


# Tabulating and sorting out the percentage of white aged 16- 64 for the year of 2015 by using ascending function
df_whiteworking_popn2015 = df_whiteworking_popn.sort_values(by = 'Jan 2015-Dec 2015 percent',ascending =False)
df_whiteworking_popn2015


# In[893]:


#graphical representation of percentage of White Aged 16-64 for the year of 2015 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2015-Dec 2015 percent', y ='Area',  data= df_whiteworking_popn2015, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of White Aged 16-64', size =14)
plt.xlim(55,100)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16 -64 Years old (White working Population) in Year 2015', size=14)
plt.show()


# In[894]:


# Tabulating and sorting out the percentage of white aged 16- 64 for the year of 2016 by using ascending function
df_whiteworking_popn2016 = df_whiteworking_popn.sort_values(by = 'Jan 2016-Dec 2016 percent',ascending =False)
df_whiteworking_popn2016


# In[895]:


#graphical representation of percentage of White Aged 16-64 for the year of 2016 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2016-Dec 2016 percent', y ='Area',  data= df_whiteworking_popn2016, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of White Aged 16-64', size =14)
plt.xlim(50,100)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16 -64 Years old (White working Population) in Year 2016', size=14)
plt.show()


# In[896]:


# Tabulating and sorting out the percentage of white aged 16- 64 for the year of 2017 by using ascending function
df_whiteworking_popn2017 = df_whiteworking_popn.sort_values(by = 'Jan 2016-Dec 2016 percent',ascending =False)
df_whiteworking_popn2017


# In[897]:


#graphical representation of percentage of White Aged 16-64 for the year of 2017 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2016-Dec 2016 percent', y ='Area',  data= df_whiteworking_popn2017, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of White Aged 16-64', size =14)
plt.xlim(48,100)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16 -64 Years old (White working Population) in Year 2017', size=14)
plt.show()


# In[898]:


# Tabulating and sorting out the percentage of white aged 16- 64 for the year of 2018 by using ascending function
df_whiteworking_popn2018 = df_whiteworking_popn.sort_values(by = 'Jan 2018-Dec 2018 percent',ascending =False)
df_whiteworking_popn2018


# In[899]:


#graphical representation of percentage of White Aged 16-64 for the year of 2018 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2018-Dec 2018 percent', y ='Area',  data= df_whiteworking_popn2018, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of White Aged 16-64', size =14)
plt.xlim(55,100)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16 -64 Years old (White working Population) in Year 2018', size=14)
plt.show()


# In[900]:


# Tabulating and sorting out the percentage of white aged 16- 64 for the year of 2019 by using ascending function
df_whiteworking_popn2019 = df_whiteworking_popn.sort_values(by = 'Jan 2019-Dec 2019 percent',ascending =False)
df_whiteworking_popn2019


# In[901]:


#graphical representation of percentage of White Aged 16-64 for the year of 2019 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2019-Dec 2019 percent', y ='Area',  data= df_whiteworking_popn2019, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of White Aged 16-64', size =14)
plt.xlim(50,100)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16 -64 Years old (White working Population) in Year 2019', size=14)
plt.show()


# In[902]:


# Tabulating and sorting out the percentage of white aged 16- 64 for the year of 2020 by using ascending function
df_whiteworking_popn2020 = df_whiteworking_popn.sort_values(by = 'Jan 2020-Dec 2020 percent',ascending =False)
df_whiteworking_popn2020


# In[903]:


#graphical representation of percentage of White Aged 16-64 for the year of 2020 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2020-Dec 2020 percent', y ='Area',  data= df_whiteworking_popn2020, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of White Aged 16-64', size =14)
plt.xlim(50,100)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16 -64 Years old (White working Population) in Year 2020', size=14)
plt.show()


# In[904]:


# Tabulating and sorting out the percentage of white aged 16- 64 for the year of 2021 by using ascending function
df_whiteworking_popn2021 = df_whiteworking_popn.sort_values(by = 'Jan 2021-Dec 2021 percent',ascending =False)
df_whiteworking_popn2021


# In[905]:


#graphical representation of percentage of White Aged 16-64 for the year of 2021 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2021-Dec 2021 percent', y ='Area',  data= df_whiteworking_popn2021, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of White Aged 16-64', size =14)
plt.xlim(50,100)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16 -64 Years old (White working Population) in Year 2021', size=14)
plt.show()


# In[1192]:


# Import the file of exploratory data and select the percentage of Ethnic minority aged 16+ by using skiprows and nrows function

data_ethnicmin_16plus = pd.read_csv('Exploratory data_CW2.csv', skiprows = 290, nrows =10, na_values=('#','!'))
data_ethnicmin_16plus


# In[1193]:


df_ethnicmin_16plus = pd.DataFrame(data_ethnicmin_16plus)
df_ethnicmin_16plus


# In[908]:


# Calculating the mean value of all counties to observe the difference in their values from 2012-2021 and select the percenatge
# column only by using axis function
print(df_ethnicmin_16plus. mean(axis =1, numeric_only=True))


# In[909]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16+ for the year of 2012 by using ascending function
df_ethnicmin_16plus2012 = df_ethnicmin_16plus.sort_values(by = 'Jan 2012-Dec 2012 percent',ascending =False)
df_ethnicmin_16plus2012


# In[910]:


#graphical representation of percentage of Ethnic minority Aged 16+ for the year of 2012 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2012-Dec 2012 percent', y ='Area',  data= df_ethnicmin_16plus2012, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of Ethnic minority Aged 16+', size =14)
plt.xlim(2,40)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Aged 16+ in Year 2012', size=14)
plt.show()


# In[911]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16+ for the year of 2013 by using ascending function
df_ethnicmin_16plus2013 = df_ethnicmin_16plus.sort_values(by = 'Jan 2013-Dec 2013 percent',ascending =False)
df_ethnicmin_16plus2013


# In[912]:


#graphical representation of percentage of Ethnic minority Aged 16+ for the year of 2013 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2013-Dec 2013 percent', y ='Area',  data= df_ethnicmin_16plus2013, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of Ethnic minority Aged 16+', size =14)
plt.xlim(2,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Aged 16+ in Year 2013', size=14)
plt.show()


# In[913]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16+ for the year of 2014 by using ascending function
df_ethnicmin_16plus2014 = df_ethnicmin_16plus.sort_values(by = 'Jan 2014-Dec 2014 percent',ascending =False)
df_ethnicmin_16plus2014


# In[914]:


#graphical representation of percentage of Ethnic minority Aged 16+ for the year of 2014 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2014-Dec 2014 percent', y ='Area',  data= df_ethnicmin_16plus2014, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of Ethnic minority Aged 16+', size =14)
plt.xlim(2,40)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Aged 16+ in Year 2014', size=14)
plt.show()


# In[915]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16+ for the year of 2015 by using ascending function
df_ethnicmin_16plus2015 = df_ethnicmin_16plus.sort_values(by = 'Jan 2015-Dec 2015 percent',ascending =False)
df_ethnicmin_16plus2015


# In[916]:


#graphical representation of percentage of Ethnic minority Aged 16+ for the year of 2015 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2015-Dec 2015 percent', y ='Area',  data= df_ethnicmin_16plus2015, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of Ethnic minority Aged 16+', size =14)
plt.xlim(2,40)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Aged 16+ in Year 2015', size=14)
plt.show()


# In[917]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16+ for the year of 2016 by using ascending function
df_ethnicmin_16plus2016 = df_ethnicmin_16plus.sort_values(by = 'Jan 2016-Dec 2016 percent',ascending =False)
df_ethnicmin_16plus2016


# In[918]:


#graphical representation of percentage of Ethnic minority Aged 16+ for the year of 2016 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2016-Dec 2016 percent', y ='Area',  data= df_ethnicmin_16plus2016, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of Ethnic minority Aged 16+', size =14)
plt.xlim(2,44)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Aged 16+ in Year 2016', size=14)
plt.show()


# In[919]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16+ for the year of 2017 by using ascending function
df_ethnicmin_16plus2017 = df_ethnicmin_16plus.sort_values(by = 'Jan 2017-Dec 2017 percent',ascending =False)
df_ethnicmin_16plus2017


# In[920]:


#graphical representation of percentage of Ethnic minority Aged 16+ for the year of 2017 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2017-Dec 2017 percent', y ='Area',  data= df_ethnicmin_16plus2017, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of Ethnic minority Aged 16+', size =14)
plt.xlim(2,44)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Aged 16+ in Year 2017', size=14)
plt.show()


# In[921]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16+ for the year of 2018 by using ascending function
df_ethnicmin_16plus2018 = df_ethnicmin_16plus.sort_values(by = 'Jan 2018-Dec 2018 percent',ascending =False)
df_ethnicmin_16plus2018


# In[922]:


#graphical representation of percentage of Ethnic minority Aged 16+ for the year of 2018 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2018-Dec 2018 percent', y ='Area',  data= df_ethnicmin_16plus2018, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of Ethnic minority Aged 16+', size =14)
plt.xlim(2,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Aged 16+ in Year 2018', size=14)
plt.show()


# In[923]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16+ for the year of 2019 by using ascending function
df_ethnicmin_16plus2019 = df_ethnicmin_16plus.sort_values(by = 'Jan 2019-Dec 2019 percent',ascending =False)
df_ethnicmin_16plus2019


# In[924]:


#graphical representation of percentage of Ethnic minority Aged 16+ for the year of 2019 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2019-Dec 2019 percent', y ='Area',  data= df_ethnicmin_16plus2019, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of Ethnic minority Aged 16+', size =14)
plt.xlim(2,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Aged 16+ in Year 2019', size=14)
plt.show()


# In[925]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16+ for the year of 2020 by using ascending function
df_ethnicmin_16plus2020 = df_ethnicmin_16plus.sort_values(by = 'Jan 2020-Dec 2020 percent',ascending =False)
df_ethnicmin_16plus2020


# In[926]:


#graphical representation of percentage of Ethnic minority Aged 16+ for the year of 2020 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2020-Dec 2020 percent', y ='Area',  data= df_ethnicmin_16plus2020, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of Ethnic minority Aged 16+', size =14)
plt.xlim(2,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Aged 16+ in Year 2020', size=14)
plt.show()


# In[927]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16+ for the year of 2021 by using ascending function
df_ethnicmin_16plus2021 = df_ethnicmin_16plus.sort_values(by = 'Jan 2021-Dec 2021 percent',ascending =False)
df_ethnicmin_16plus2021


# In[928]:


#graphical representation of percentage of Ethnic minority Aged 16+ for the year of 2021 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2021-Dec 2021 percent', y ='Area',  data= df_ethnicmin_16plus2021, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of Ethnic minority Aged 16+', size =14)
plt.xlim(2,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Aged 16+ in Year 2021', size=14)
plt.show()


# In[1195]:


# Import the file of exploratory data and select the percentage of Ethnic minority aged 16-64 by using skiprows and nrows function

data_ethnicmin_workingpopn = pd.read_csv('Exploratory data_CW2.csv', skiprows = 314, nrows =10,na_values=('#','!'))
data_ethnicmin_workingpopn


# In[1196]:


df_ethnicmin_workingpopn = pd.DataFrame(data_ethnicmin_workingpopn)
df_ethnicmin_workingpopn


# In[1197]:


# Calculating the mean value of all counties to observe the difference in their values from 2012-2021 and select the percenatge
# column only by using axis function
print(df_ethnicmin_workingpopn.mean(axis =1, numeric_only=True))


# In[932]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16-64 for the year of 2012 by using ascending function
df_ethnicmin_workingpopn2012 = df_ethnicmin_workingpopn.sort_values(by = 'Jan 2012-Dec 2012 percent',ascending =False)
df_ethnicmin_workingpopn2012


# In[933]:


#graphical representation of percentage of Ethnic minority Aged 16-64 for the year of 2012 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2012-Dec 2012 percent', y ='Area',  data= df_ethnicmin_workingpopn2012, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of Ethnic minority Aged 16-64 ', size =14)
plt.xlim(2,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Age 16-64 Years old (Ethnic minority Working Population) in Year 2012', size=14)
plt.show()


# In[934]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16-64 for the year of 2013 by using ascending function
df_ethnicmin_workingpopn2013 = df_ethnicmin_workingpopn.sort_values(by = 'Jan 2013-Dec 2013 percent',ascending =False)
df_ethnicmin_workingpopn2013


# In[935]:


#graphical representation of percentage of Ethnic minority Aged 16-64 for the year of 2013 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2013-Dec 2013 percent', y ='Area',  data= df_ethnicmin_workingpopn2013, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of Ethnic minority Aged 16-64 ', size =14)
plt.xlim(2,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Age 16-64 Years old (Ethnic minority Working Population) in Year 2013', size=14)
plt.show()


# In[936]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16-64 for the year of 2014 by using ascending function
df_ethnicmin_workingpopn2014 = df_ethnicmin_workingpopn.sort_values(by = 'Jan 2014-Dec 2014 percent',ascending =False)
df_ethnicmin_workingpopn2014


# In[937]:


#graphical representation of percentage of Ethnic minority Aged 16-64 for the year of 2014 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2014-Dec 2014 percent', y ='Area',  data= df_ethnicmin_workingpopn2014, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of Ethnic minority Aged 16-64 ', size =14)
plt.xlim(2,40)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Age 16-64 Years old (Ethnic minority Working Population) in Year 2014', size=14)
plt.show()


# In[938]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16-64 for the year of 2015 by using ascending function
df_ethnicmin_workingpopn2015 = df_ethnicmin_workingpopn.sort_values(by = 'Jan 2015-Dec 2015 percent',ascending =False)
df_ethnicmin_workingpopn2015


# In[939]:


#graphical representation of percentage of Ethnic minority Aged 16-64 for the year of 2015 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2015-Dec 2015 percent', y ='Area',  data= df_ethnicmin_workingpopn2015, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of Ethnic minority Aged 16-64 ', size =14)
plt.xlim(2,40)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Age 16-64 Years old (Ethnic minority Working Population) in Year 2015', size=14)
plt.show()


# In[940]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16-64 for the year of 2016 by using ascending function
df_ethnicmin_workingpopn2016 = df_ethnicmin_workingpopn.sort_values(by = 'Jan 2016-Dec 2016 percent',ascending =False)
df_ethnicmin_workingpopn2016


# In[941]:


#graphical representation of percentage of Ethnic minority Aged 16-64 for the year of 2016 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2016-Dec 2016 percent', y ='Area',  data= df_ethnicmin_workingpopn2016, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of Ethnic minority Aged 16-64 ', size =14)
plt.xlim(2,50)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Age 16-64 Years old (Ethnic minority Working Population) in Year 2016', size=14)
plt.show()


# In[942]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16-64 for the year of 2017 by using ascending function
df_ethnicmin_workingpopn2017 = df_ethnicmin_workingpopn.sort_values(by = 'Jan 2017-Dec 2017 percent',ascending =False)
df_ethnicmin_workingpopn2017


# In[943]:


#graphical representation of percentage of Ethnic minority Aged 16-64 for the year of 2017 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2017-Dec 2017 percent', y ='Area',  data= df_ethnicmin_workingpopn2017, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of Ethnic minority Aged 16-64 ', size =14)
plt.xlim(2,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Age 16-64 Years old (Ethnic minority Working Population) in Year 2017', size=14)
plt.show()


# In[944]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16-64 for the year of 2018 by using ascending function
df_ethnicmin_workingpopn2018 = df_ethnicmin_workingpopn.sort_values(by = 'Jan 2018-Dec 2018 percent',ascending =False)
df_ethnicmin_workingpopn2018


# In[945]:


#graphical representation of percentage of Ethnic minority Aged 16-64 for the year of 2018 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2018-Dec 2018 percent', y ='Area',  data= df_ethnicmin_workingpopn2018, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of Ethnic minority Aged 16-64 ', size =14)
plt.xlim(2,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Age 16-64 Years old (Ethnic minority Working Population) in Year 2018', size=14)
plt.show()


# In[946]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16-64 for the year of 2019 by using ascending function
df_ethnicmin_workingpopn2019 = df_ethnicmin_workingpopn.sort_values(by = 'Jan 2019-Dec 2019 percent',ascending =False)
df_ethnicmin_workingpopn2019


# In[947]:


#graphical representation of percentage of Ethnic minority Aged 16-64 for the year of 2019 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2019-Dec 2019 percent', y ='Area',  data= df_ethnicmin_workingpopn2019, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of Ethnic minority Aged 16-64 ', size =14)
plt.xlim(2,50)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Age 16-64 Years old (Ethnic minority Working Population) in Year 2019', size=14)
plt.show()


# In[948]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16-64 for the year of 2020 by using ascending function
df_ethnicmin_workingpopn2020 = df_ethnicmin_workingpopn.sort_values(by = 'Jan 2020-Dec 2020 percent',ascending =False)
df_ethnicmin_workingpopn2020


# In[949]:


#graphical representation of percentage of Ethnic minority Aged 16-64 for the year of 2020 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2020-Dec 2020 percent', y ='Area',  data= df_ethnicmin_workingpopn2020, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of Ethnic minority Aged 16-64 ', size =14)
plt.xlim(2,50)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Age 16-64 Years old (Ethnic minority Working Population) in Year 2020', size=14)
plt.show()


# In[950]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16-64 for the year of 2021 by using ascending function
df_ethnicmin_workingpopn2021 = df_ethnicmin_workingpopn.sort_values(by = 'Jan 2021-Dec 2021 percent',ascending =False)
df_ethnicmin_workingpopn2021


# In[951]:


#graphical representation of percentage of Ethnic minority Aged 16-64 for the year of 2021 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2021-Dec 2021 percent', y ='Area',  data= df_ethnicmin_workingpopn2021, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Percentage of Ethnic minority Aged 16-64 ', size =14)
plt.xlim(2,50)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Age 16-64 Years old (Ethnic minority Working Population) in Year 2021', size=14)
plt.show()


# In[1205]:


# Import the file of exploratory data and select the Employment rate of White aged 16-64 by using skiprows and nrows function

data_employrate_white = pd.read_csv('Exploratory data_CW2.csv', skiprows = 482, nrows =10, na_values=('#','!'))
data_employrate_white


# In[1206]:


df_employrate_white = pd.DataFrame(data_employrate_white)
df_employrate_white


# In[1207]:


# Calculating the mean value of all counties to observe the difference in their values from 2012-2021 and select the percenatge
# column only by using axis function
print(df_employrate_white.mean(axis=1, numeric_only=True))


# In[1208]:


# Tabulating and sorting out the Employment rate of White aged 16-64 for the year of 2012 by using ascending function
df_employratewhite_workingpopn2012 = df_employrate_white.sort_values(by = 'Jan 2012-Dec 2012 percent',ascending =False)
df_employratewhite_workingpopn2012


# In[956]:


#graphical representation of Employment rate White Aged 16-64 for the year of 2012 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2012-Dec 2012 percent', y ='Area',  data= df_employratewhite_workingpopn2012, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Employemnt rate of White Aged 16-64 ', size =14)
plt.xlim(60,80)
plt.ylabel('Area', size =16)
plt.title('The Employment rate of White Age 16-64 Years old ( White Working Population) in Year 2012', size=14)
plt.show()


# In[957]:


# Tabulating and sorting out the Employment rate of White aged 16-64 for the year of 2013 by using ascending function
df_employratewhite_workingpopn2013 = df_employrate_white.sort_values(by = 'Jan 2013-Dec 2013 percent',ascending =False)
df_employratewhite_workingpopn2013


# In[958]:


#graphical representation of Employment rate White Aged 16-64 for the year of 2013 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2013-Dec 2013 percent', y ='Area',  data= df_employratewhite_workingpopn2013, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Employemnt rate of White Aged 16-64 ', size =14)
plt.xlim(60,80)
plt.ylabel('Area', size =16)
plt.title('The Employment rate of White Age 16-64 Years old ( White Working Population) in Year 2013', size=14)
plt.show()


# In[959]:


# Tabulating and sorting out the Employment rate of White aged 16-64 for the year of 2014 by using ascending function
df_employratewhite_workingpopn2014 = df_employrate_white.sort_values(by = 'Jan 2014-Dec 2014 percent',ascending =False)
df_employratewhite_workingpopn2014


# In[960]:


#graphical representation of Employment rate White Aged 16-64 for the year of 2014 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2014-Dec 2014 percent', y ='Area',  data= df_employratewhite_workingpopn2014, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Employemnt rate of White Aged 16-64 ', size =14)
plt.xlim(60,80)
plt.ylabel('Area', size =16)
plt.title('The Employment rate of White Age 16-64 Years old ( White Working Population) in Year 2014', size=14)
plt.show()


# In[961]:


# Tabulating and sorting out the Employment rate of White aged 16-64 for the year of 2015 by using ascending function
df_employratewhite_workingpopn2015 = df_employrate_white.sort_values(by = 'Jan 2015-Dec 2015 percent',ascending =False)
df_employratewhite_workingpopn2015


# In[962]:


#graphical representation of Employment rate White Aged 16-64 for the year of 2015 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2015-Dec 2015 percent', y ='Area',  data= df_employratewhite_workingpopn2015, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Employemnt rate of White Aged 16-64 ', size =14)
plt.xlim(60,82)
plt.ylabel('Area', size =16)
plt.title('The Employment rate of White Age 16-64 Years old ( White Working Population) in Year 2015', size=14)
plt.show()


# In[963]:


# Tabulating and sorting out the Employment rate of White aged 16-64 for the year of 2016 by using ascending function
df_employratewhite_workingpopn2016 = df_employrate_white.sort_values(by = 'Jan 2016-Dec 2016 percent',ascending =False)
df_employratewhite_workingpopn2016


# In[964]:


#graphical representation of Employment rate White Aged 16-64 for the year of 2016 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2016-Dec 2016 percent', y ='Area',  data= df_employratewhite_workingpopn2016, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Employemnt rate of White Aged 16-64 ', size =14)
plt.xlim(60,82)
plt.ylabel('Area', size =16)
plt.title('The Employment rate of White Age 16-64 Years old ( White Working Population) in Year 2016', size=14)
plt.show()


# In[965]:


# Tabulating and sorting out the Employment rate of White aged 16-64 for the year of 2017 by using ascending function
df_employratewhite_workingpopn2017 = df_employrate_white.sort_values(by = 'Jan 2017-Dec 2017 percent',ascending =False)
df_employratewhite_workingpopn2017


# In[966]:


#graphical representation of Employment rate White Aged 16-64 for the year of 2017 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2017-Dec 2017 percent', y ='Area',  data= df_employratewhite_workingpopn2017, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Employemnt rate of White Aged 16-64 ', size =14)
plt.xlim(65,85)
plt.ylabel('Area', size =16)
plt.title('The Employment rate of White Age 16-64 Years old ( White Working Population) in Year 2017', size=14)
plt.show()


# In[967]:


# Tabulating and sorting out the Employment rate of White aged 16-64 for the year of 2018 by using ascending function
df_employratewhite_workingpopn2018 = df_employrate_white.sort_values(by = 'Jan 2018-Dec 2018 percent',ascending =False)
df_employratewhite_workingpopn2018


# In[968]:


#graphical representation of Employment rate White Aged 16-64 for the year of 2018 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2018-Dec 2018 percent', y ='Area',  data= df_employratewhite_workingpopn2018, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Employemnt rate of White Aged 16-64 ', size =14)
plt.xlim(65,85)
plt.ylabel('Area', size =16)
plt.title('The Employment rate of White Age 16-64 Years old ( White Working Population) in Year 2018', size=14)
plt.show()


# In[969]:


# Tabulating and sorting out the Employment rate of White aged 16-64 for the year of 2019 by using ascending function
df_employratewhite_workingpopn2019 = df_employrate_white.sort_values(by = 'Jan 2019-Dec 2019 percent',ascending =False)
df_employratewhite_workingpopn2019


# In[970]:


#graphical representation of Employment rate White Aged 16-64 for the year of 2019 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2019-Dec 2019 percent', y ='Area',  data= df_employratewhite_workingpopn2019, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Employemnt rate of White Aged 16-64 ', size =14)
plt.xlim(65,85)
plt.ylabel('Area', size =16)
plt.title('The Employment rate of White Age 16-64 Years old ( White Working Population) in Year 2019', size=14)
plt.show()


# In[971]:


# Tabulating and sorting out the Employment rate of White aged 16-64 for the year of 2020 by using ascending function
df_employratewhite_workingpopn2020 = df_employrate_white.sort_values(by = 'Jan 2020-Dec 2020 percent',ascending =False)
df_employratewhite_workingpopn2020


# In[972]:


#graphical representation of Employment rate White Aged 16-64 for the year of 2020 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2020-Dec 2020 percent', y ='Area',  data= df_employratewhite_workingpopn2020, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Employemnt rate of White Aged 16-64 ', size =14)
plt.xlim(65,85)
plt.ylabel('Area', size =16)
plt.title('The Employment rate of White Age 16-64 Years old ( White Working Population) in Year 2020', size=14)
plt.show()


# In[973]:


# Tabulating and sorting out the Employment rate of White aged 16-64 for the year of 2021 by using ascending function
df_employratewhite_workingpopn2021 = df_employrate_white.sort_values(by = 'Jan 2021-Dec 2021 percent',ascending =False)
df_employratewhite_workingpopn2021


# In[974]:


#graphical representation of Employment rate White Aged 16-64 for the year of 2021 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2021-Dec 2021 percent', y ='Area',  data= df_employratewhite_workingpopn2021, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Employemnt rate of White Aged 16-64 ', size =14)
plt.xlim(65,85)
plt.ylabel('Area', size =16)
plt.title('The Employment rate of White Age 16-64 Years old ( White Working Population) in Year 2021', size=14)
plt.show()


# In[1209]:


# Import the file of exploratory data and select the Employment rate of Ethnic minority aged 16-64 by using skiprows and nrows function

data_employrate_ethnicmin = pd.read_csv('Exploratory data_CW2.csv', skiprows = 506, nrows =10,na_values=('#','!'))
data_employrate_ethnicmin


# In[1210]:


df_employrate_ethnicmin = pd.DataFrame(data_employrate_ethnicmin)
df_employrate_ethnicmin


# In[1211]:


# Calculating the mean value of all counties to observe the difference in their values from 2012-2021 and select the percenatge
# column only by using axis function 
print(df_employrate_ethnicmin.mean(axis =1, numeric_only=True))


# In[1212]:


# Tabulating and sorting out the Employment rate of Ethnic minority aged 16-64 for the year of 2012 by using ascending function
df_employrateethnicmin_workingpopn2012 = df_employrate_ethnicmin.sort_values(by = 'Jan 2012-Dec 2012 percent',ascending =False)
df_employrateethnicmin_workingpopn2012


# In[979]:


#graphical representation of Employment rate Ethnic minority Aged 16-64 for the year of 2012 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2012-Dec 2012 percent', y ='Area',  data= df_employrateethnicmin_workingpopn2012, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Employemnt rate of Ethnic minority Aged 16-64 ', size =14)
plt.xlim(45,85)
plt.ylabel('Area', size =16)
plt.title('The Employment rate of Ethnic minority Age 16-64 Years old in Year 2012', size=14)
plt.show()


# In[980]:


# Tabulating and sorting out the Employment rate of Ethnic minority aged 16-64 for the year of 2013 by using ascending function
df_employrateethnicmin_workingpopn2013 = df_employrate_ethnicmin.sort_values(by = 'Jan 2013-Dec 2013 percent',ascending =False)
df_employrateethnicmin_workingpopn2013


# In[981]:


#graphical representation of Employment rate Ethnic minority Aged 16-64 for the year of 2013 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2013-Dec 2013 percent', y ='Area',  data= df_employrateethnicmin_workingpopn2013, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Employemnt rate of Ethnic minority Aged 16-64 ', size =14)
plt.xlim(45,85)
plt.ylabel('Area', size =16)
plt.title('The Employment rate of Ethnic minority Age 16-64 Years old in Year 2013', size=14)
plt.show()


# In[982]:


# Tabulating and sorting out the Employment rate of Ethnic minority aged 16-64 for the year of 2014 by using ascending function
df_employrateethnicmin_workingpopn2014 = df_employrate_ethnicmin.sort_values(by = 'Jan 2014-Dec 2014 percent',ascending =False)
df_employrateethnicmin_workingpopn2014


# In[983]:


#graphical representation of Employment rate Ethnic minority Aged 16-64 for the year of 2014 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2014-Dec 2014 percent', y ='Area',  data= df_employrateethnicmin_workingpopn2014, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Employemnt rate of Ethnic minority Aged 16-64 ', size =14)
plt.xlim(45,85)
plt.ylabel('Area', size =16)
plt.title('The Employment rate of Ethnic minority Age 16-64 Years old in Year 2014', size=14)
plt.show()


# In[984]:


# Tabulating and sorting out the Employment rate of Ethnic minority aged 16-64 for the year of 2015 by using ascending function
df_employrateethnicmin_workingpopn2015 = df_employrate_ethnicmin.sort_values(by = 'Jan 2015-Dec 2015 percent',ascending =False)
df_employrateethnicmin_workingpopn2015


# In[985]:


#graphical representation of Employment rate Ethnic minority Aged 16-64 for the year of 2015 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2015-Dec 2015 percent', y ='Area',  data= df_employrateethnicmin_workingpopn2015, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Employemnt rate of Ethnic minority Aged 16-64 ', size =14)
plt.xlim(45,85)
plt.ylabel('Area', size =16)
plt.title('The Employment rate of Ethnic minority Age 16-64 Years old in Year 2015', size=14)
plt.show()


# In[986]:


# Tabulating and sorting out the Employment rate of Ethnic minority aged 16-64 for the year of 2016 by using ascending function
df_employrateethnicmin_workingpopn2016 = df_employrate_ethnicmin.sort_values(by = 'Jan 2016-Dec 2016 percent',ascending =False)
df_employrateethnicmin_workingpopn2016


# In[987]:


#graphical representation of Employment rate Ethnic minority Aged 16-64 for the year of 2016 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2016-Dec 2016 percent', y ='Area',  data= df_employrateethnicmin_workingpopn2016, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Employemnt rate of Ethnic minority Aged 16-64 ', size =14)
plt.xlim(45,85)
plt.ylabel('Area', size =16)
plt.title('The Employment rate of Ethnic minority Age 16-64 Years old in Year 2016', size=14)
plt.show()


# In[988]:


# Tabulating and sorting out the Employment rate of Ethnic minority aged 16-64 for the year of 2017 by using ascending function
df_employrateethnicmin_workingpopn2017 = df_employrate_ethnicmin.sort_values(by = 'Jan 2017-Dec 2017 percent',ascending =False)
df_employrateethnicmin_workingpopn2017


# In[989]:


#graphical representation of Employment rate Ethnic minority Aged 16-64 for the year of 2017 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2017-Dec 2017 percent', y ='Area',  data= df_employrateethnicmin_workingpopn2017, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Employemnt rate of Ethnic minority Aged 16-64 ', size =14)
plt.xlim(45,85)
plt.ylabel('Area', size =16)
plt.title('The Employment rate of Ethnic minority Age 16-64 Years old  in Year 2017', size=14)
plt.show()


# In[990]:


# Tabulating and sorting out the Employment rate of Ethnic minority aged 16-64 for the year of 2018 by using ascending function
df_employrateethnicmin_workingpopn2018 = df_employrate_ethnicmin.sort_values(by = 'Jan 2018-Dec 2018 percent',ascending =False)
df_employrateethnicmin_workingpopn2018


# In[991]:


#graphical representation of Employment rate Ethnic minority Aged 16-64 for the year of 2018 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2018-Dec 2018 percent', y ='Area',  data= df_employrateethnicmin_workingpopn2018, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Employemnt rate of Ethnic minority Aged 16-64 ', size =14)
plt.xlim(45,85)
plt.ylabel('Area', size =16)
plt.title('The Employment rate of Ethnic minority Age 16-64 Years old in Year 2018', size=14)
plt.show()


# In[992]:


# Tabulating and sorting out the Employment rate of Ethnic minority aged 16-64 for the year of 2019 by using ascending function
df_employrateethnicmin_workingpopn2019 = df_employrate_ethnicmin.sort_values(by = 'Jan 2019-Dec 2019 percent',ascending =False)
df_employrateethnicmin_workingpopn2019


# In[993]:


#graphical representation of Employment rate Ethnic minority Aged 16-64 for the year of 2019 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2019-Dec 2019 percent', y ='Area',  data= df_employrateethnicmin_workingpopn2019, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Employemnt rate of Ethnic minority Aged 16-64 ', size =14)
plt.xlim(45,85)
plt.ylabel('Area', size =16)
plt.title('The Employment rate of Ethnic minority Age 16-64 Years old in Year 2019', size=14)
plt.show()


# In[994]:


# Tabulating and sorting out the Employment rate of Ethnic minority aged 16-64 for the year of 2020 by using ascending function
df_employrateethnicmin_workingpopn2020 = df_employrate_ethnicmin.sort_values(by = 'Jan 2020-Dec 2020 percent',ascending =False)
df_employrateethnicmin_workingpopn2020


# In[995]:


#graphical representation of Employment rate Ethnic minority Aged 16-64 for the year of 2020 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2020-Dec 2020 percent', y ='Area',  data= df_employrateethnicmin_workingpopn2020, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Employemnt rate of Ethnic minority Aged 16-64 ', size =14)
plt.xlim(45,85)
plt.ylabel('Area', size =16)
plt.title('The Employment rate of Ethnic minority Age 16-64 Years old in Year 2020', size=14)
plt.show()


# In[996]:


# Tabulating and sorting out the Employment rate of Ethnic minority aged 16-64 for the year of 2021 by using ascending function
df_employrateethnicmin_workingpopn2021 = df_employrate_ethnicmin.sort_values(by = 'Jan 2021-Dec 2021 percent',ascending =False)
df_employrateethnicmin_workingpopn2021


# In[997]:


#graphical representation of Employment rate Ethnic minority Aged 16-64 for the year of 2021 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2021-Dec 2021 percent', y ='Area',  data= df_employrateethnicmin_workingpopn2021, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('Employemnt rate of Ethnic minority Aged 16-64 ', size =14)
plt.xlim(45,85)
plt.ylabel('Area', size =16)
plt.title('The Employment rate of Ethnic minority Age 16-64 Years old in Year 2021', size=14)
plt.show()


# In[998]:


# Import the file of exploratory data and select the percentage of Whites aged 16-64 who are economically inactive by using skiprows and nrows function

data_percentofwhite_inactive = pd.read_csv('Exploratory data_CW2.csv', skiprows = 602, nrows =10)
data_percentofwhite_inactive


# In[999]:


df_percentofwhite_inactive = pd.DataFrame(data_percentofwhite_inactive)
df_percentofwhite_inactive


# In[1000]:


# Calculating the mean value of all counties to observe the difference in their values from 2012-2021 and select the percenatge
# column only by using axis =1
print(df_percentofwhite_inactive.mean(axis=1, numeric_only=True))


# In[1001]:


# Tabulating and sorting out the percentage of Whites aged 16-64 who are economically inactive for the year of 2012 by using ascending function
df_percentofwhite_inactive2012 = df_percentofwhite_inactive.sort_values(by = 'Jan 2012-Dec 2012 percent',ascending =False)
df_percentofwhite_inactive2012


# In[1002]:


#graphical representation of the percentage of Whites aged 16-64 who are economically inactive for the year of 2012 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2012-Dec 2012 percent', y ='Area',  data= df_percentofwhite_inactive2012, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of White Aged 16-64 who are economically inactive ', size =14)
plt.xlim(17,30)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16-64 Years old who are economically inactive in Year 2012', size=14)
plt.show()


# In[1003]:


# Tabulating and sorting out the percentage of Whites aged 16-64 who are economically inactive for the year of 2013 by using ascending function
df_percentofwhite_inactive2013 = df_percentofwhite_inactive.sort_values(by = 'Jan 2013-Dec 2013 percent',ascending =False)
df_percentofwhite_inactive2013


# In[1004]:


#graphical representation of the percentage of Whites aged 16-64 who are economically inactive for the year of 2013 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2013-Dec 2013 percent', y ='Area',  data= df_percentofwhite_inactive2013, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of White Aged 16-64 who are economically inactive ', size =14)
plt.xlim(17,30)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16-64 Years old who are economically inactive in Year 2013', size=14)
plt.show()


# In[1005]:


# Tabulating and sorting out the percentage of Whites aged 16-64 who are economically inactive for the year of 2014 by using ascending function
df_percentofwhite_inactive2014 = df_percentofwhite_inactive.sort_values(by = 'Jan 2014-Dec 2014 percent',ascending =False)
df_percentofwhite_inactive2014


# In[1006]:


#graphical representation of the percentage of Whites aged 16-64 who are economically inactive for the year of 2014 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2014-Dec 2014 percent', y ='Area',  data= df_percentofwhite_inactive2014, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of White Aged 16-64 who are economically inactive ', size =14)
plt.xlim(17,32)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16-64 Years old who are economically inactive in Year 2014', size=14)
plt.show()


# In[1007]:


# Tabulating and sorting out the percentage of Whites aged 16-64 who are economically inactive for the year of 2015 by using ascending function
df_percentofwhite_inactive2015 = df_percentofwhite_inactive.sort_values(by = 'Jan 2015-Dec 2015 percent',ascending =False)
df_percentofwhite_inactive2015


# In[1008]:


#graphical representation of the percentage of Whites aged 16-64 who are economically inactive for the year of 2015 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2015-Dec 2015 percent', y ='Area',  data= df_percentofwhite_inactive2015, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of White Aged 16-64 who are economically inactive ', size =14)
plt.xlim(14,30)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16-64 Years old who are economically inactive in Year 2015', size=14)
plt.show()


# In[1009]:


# Tabulating and sorting out the percentage of Whites aged 16-64 who are economically inactive for the year of 2016 by using ascending function
df_percentofwhite_inactive2016 = df_percentofwhite_inactive.sort_values(by = 'Jan 2016-Dec 2016 percent',ascending =False)
df_percentofwhite_inactive2016


# In[1010]:


#graphical representation of the percentage of Whites aged 16-64 who are economically inactive for the year of 2016 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2016-Dec 2016 percent', y ='Area',  data= df_percentofwhite_inactive2016, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of White Aged 16-64 who are economically inactive ', size =14)
plt.xlim(14,30)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16-64 Years old who are economically inactive in Year 2016', size=14)
plt.show()


# In[1011]:


# Tabulating and sorting out the percentage of Whites aged 16-64 who are economically inactive for the year of 2017 by using ascending function
df_percentofwhite_inactive2017 = df_percentofwhite_inactive.sort_values(by = 'Jan 2017-Dec 2017 percent',ascending =False)
df_percentofwhite_inactive2017


# In[1012]:


#graphical representation of the percentage of Whites aged 16-64 who are economically inactive for the year of 2017 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2017-Dec 2017 percent', y ='Area',  data= df_percentofwhite_inactive2017, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of White Aged 16-64 who are economically inactive ', size =14)
plt.xlim(14,30)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16-64 Years old who are economically inactive in Year 2017', size=14)
plt.show()


# In[1013]:


# Tabulating and sorting out the percentage of Whites aged 16-64 who are economically inactive for the year of 2018 by using ascending function
df_percentofwhite_inactive2018 = df_percentofwhite_inactive.sort_values(by = 'Jan 2018-Dec 2018 percent',ascending =False)
df_percentofwhite_inactive2018


# In[1014]:


#graphical representation of the percentage of Whites aged 16-64 who are economically inactive for the year of 2018 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2018-Dec 2018 percent', y ='Area',  data= df_percentofwhite_inactive2018, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of White Aged 16-64 who are economically inactive ', size =14)
plt.xlim(14,30)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16-64 Years old who are economically inactive in Year 2018', size=14)
plt.show()


# In[1015]:


# Tabulating and sorting out the percentage of Whites aged 16-64 who are economically inactive for the year of 2019 by using ascending function
df_percentofwhite_inactive2019 = df_percentofwhite_inactive.sort_values(by = 'Jan 2019-Dec 2019 percent',ascending =False)
df_percentofwhite_inactive2019


# In[1016]:


#graphical representation of the percentage of Whites aged 16-64 who are economically inactive for the year of 2019 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2019-Dec 2019 percent', y ='Area',  data= df_percentofwhite_inactive2019, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of White Aged 16-64 who are economically inactive ', size =14)
plt.xlim(14,30)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16-64 Years old who are economically inactive in Year 2019', size=14)
plt.show()


# In[1017]:


# Tabulating and sorting out the percentage of Whites aged 16-64 who are economically inactive for the year of 2020 by using ascending function
df_percentofwhite_inactive2020 = df_percentofwhite_inactive.sort_values(by = 'Jan 2020-Dec 2020 percent',ascending =False)
df_percentofwhite_inactive2020


# In[1018]:


#graphical representation of the percentage of Whites aged 16-64 who are economically inactive for the year of 2020 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2020-Dec 2020 percent', y ='Area',  data= df_percentofwhite_inactive2020, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of White Aged 16-64 who are economically inactive ', size =14)
plt.xlim(14,30)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16-64 Years old who are economically inactive in Year 2020', size=14)
plt.show()


# In[1019]:


# Tabulating and sorting out the percentage of Whites aged 16-64 who are economically inactive for the year of 2021 by using ascending function
df_percentofwhite_inactive2021 = df_percentofwhite_inactive.sort_values(by = 'Jan 2021-Dec 2021 percent',ascending =False)
df_percentofwhite_inactive2021


# In[1020]:


#graphical representation of the percentage of Whites aged 16-64 who are economically inactive for the year of 2021 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2021-Dec 2021 percent', y ='Area',  data= df_percentofwhite_inactive2021, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of White Aged 16-64 who are economically inactive ', size =14)
plt.xlim(14,30)
plt.ylabel('Area', size =16)
plt.title('The percentage of White Age 16-64 Years old who are economically inactive in Year 2021', size=14)
plt.show()


# In[1021]:


# Import the file of exploratory data and select the percentage of Ethnic minority aged 16-64 who are economically inactive by using skiprows and nrows function

data_percentofethnicmin_inactive = pd.read_csv('Exploratory data_CW2.csv', skiprows = 626, nrows =10)
data_percentofethnicmin_inactive


# In[1022]:


df_percentofethnicmin_inactive = pd.DataFrame(data_percentofethnicmin_inactive)
df_percentofethnicmin_inactive 


# In[1023]:


# Calculating the mean value of all counties to observe the difference in their values from 2012-2021 and select the percenatge
# column only by using axis =1
print(df_percentofethnicmin_inactive.mean(axis=1,numeric_only=True))


# In[1024]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16-64 who are economically inactive for the year of 2012 by using ascending function
df_percentofethnicmin_inactive2012 = df_percentofethnicmin_inactive.sort_values(by = 'Jan 2012-Dec 2012 percent',ascending =False)
df_percentofethnicmin_inactive2012


# In[1025]:


#graphical representation of the percentage of Ethnic minority aged 16-64 who are economically inactive for the year of 2012 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2012-Dec 2012 percent', y ='Area',  data= df_percentofethnicmin_inactive2012, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Ethnic minority Aged 16-64 who are economically inactive ', size =14)
plt.xlim(15,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Age 16-64 Years old who are economically inactive in Year 2012', size=14)
plt.show()


# In[1026]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16-64 who are economically inactive for the year of 2013 by using ascending function
df_percentofethnicmin_inactive2013 = df_percentofethnicmin_inactive.sort_values(by = 'Jan 2013-Dec 2013 percent',ascending =False)
df_percentofethnicmin_inactive2013


# In[1027]:


#graphical representation of the percentage of Ethnic minority aged 16-64 who are economically inactive for the year of 2013 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2013-Dec 2013 percent', y ='Area',  data= df_percentofethnicmin_inactive2013, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Ethnic minority Aged 16-64 who are economically inactive ', size =14)
plt.xlim(15,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Age 16-64 Years old who are economically inactive in Year 2013', size=14)
plt.show()


# In[1028]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16-64 who are economically inactive for the year of 2014 by using ascending function
df_percentofethnicmin_inactive2014 = df_percentofethnicmin_inactive.sort_values(by = 'Jan 2014-Dec 2014 percent',ascending =False)
df_percentofethnicmin_inactive2014


# In[1029]:


#graphical representation of the percentage of Ethnic minority aged 16-64 who are economically inactive for the year of 2014 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2014-Dec 2014 percent', y ='Area',  data= df_percentofethnicmin_inactive2014, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Ethnic minority Aged 16-64 who are economically inactive ', size =14)
plt.xlim(15,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Age 16-64 Years old who are economically inactive in Year 2014', size=14)
plt.show()


# In[1030]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16-64 who are economically inactive for the year of 2015 by using ascending function
df_percentofethnicmin_inactive2015 = df_percentofethnicmin_inactive.sort_values(by = 'Jan 2015-Dec 2015 percent',ascending =False)
df_percentofethnicmin_inactive2015


# In[1031]:


#graphical representation of the percentage of Ethnic minority aged 16-64 who are economically inactive for the year of 2015 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2015-Dec 2015 percent', y ='Area',  data= df_percentofethnicmin_inactive2015, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Ethnic minority Aged 16-64 who are economically inactive ', size =14)
plt.xlim(13,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Age 16-64 Years old who are economically inactive in Year 2015', size=14)
plt.show()


# In[1032]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16-64 who are economically inactive for the year of 2016 by using ascending function
df_percentofethnicmin_inactive2016 = df_percentofethnicmin_inactive.sort_values(by = 'Jan 2016-Dec 2016 percent',ascending =False)
df_percentofethnicmin_inactive2016


# In[1033]:


#graphical representation of the percentage of Ethnic minority aged 16-64 who are economically inactive for the year of 2016 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2016-Dec 2016 percent', y ='Area',  data= df_percentofethnicmin_inactive2016, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Ethnic minority Aged 16-64 who are economically inactive ', size =14)
plt.xlim(8,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Age 16-64 Years old who are economically inactive in Year 2016', size=14)
plt.show()


# In[1034]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16-64 who are economically inactive for the year of 2017 by using ascending function
df_percentofethnicmin_inactive2017 = df_percentofethnicmin_inactive.sort_values(by = 'Jan 2017-Dec 2017 percent',ascending =False)
df_percentofethnicmin_inactive2017


# In[1035]:


#graphical representation of the percentage of Ethnic minority aged 16-64 who are economically inactive for the year of 2017 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2017-Dec 2017 percent', y ='Area',  data= df_percentofethnicmin_inactive2017, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Ethnic minority Aged 16-64 who are economically inactive ', size =14)
plt.xlim(15,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Age 16-64 Years old who are economically inactive in Year 2017', size=14)
plt.show()


# In[1036]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16-64 who are economically inactive for the year of 2018 by using ascending function
df_percentofethnicmin_inactive2018 = df_percentofethnicmin_inactive.sort_values(by = 'Jan 2018-Dec 2018 percent',ascending =False)
df_percentofethnicmin_inactive2018


# In[1037]:


#graphical representation of the percentage of Ethnic minority aged 16-64 who are economically inactive for the year of 2018 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2018-Dec 2018 percent', y ='Area',  data= df_percentofethnicmin_inactive2018, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Ethnic minority Aged 16-64 who are economically inactive ', size =14)
plt.xlim(13,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Age 16-64 Years old who are economically inactive in Year 2018', size=14)
plt.show()


# In[1038]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16-64 who are economically inactive for the year of 2019 by using ascending function
df_percentofethnicmin_inactive2019 = df_percentofethnicmin_inactive.sort_values(by = 'Jan 2019-Dec 2019 percent',ascending =False)
df_percentofethnicmin_inactive2019


# In[1039]:


#graphical representation of the percentage of Ethnic minority aged 16-64 who are economically inactive for the year of 2019 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2019-Dec 2019 percent', y ='Area',  data= df_percentofethnicmin_inactive2019, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Ethnic minority Aged 16-64 who are economically inactive ', size =14)
plt.xlim(15,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Age 16-64 Years old who are economically inactive in Year 2019', size=14)
plt.show()


# In[1040]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16-64 who are economically inactive for the year of 2020 by using ascending function
df_percentofethnicmin_inactive2020 = df_percentofethnicmin_inactive.sort_values(by = 'Jan 2020-Dec 2020 percent',ascending =False)
df_percentofethnicmin_inactive2020


# In[1041]:


#graphical representation of the percentage of Ethnic minority aged 16-64 who are economically inactive for the year of 2020 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2020-Dec 2020 percent', y ='Area',  data= df_percentofethnicmin_inactive2020, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Ethnic minority Aged 16-64 who are economically inactive ', size =14)
plt.xlim(15,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Age 16-64 Years old who are economically inactive in Year 2020', size=14)
plt.show()


# In[1042]:


# Tabulating and sorting out the percentage of Ethnic minority aged 16-64 who are economically inactive for the year of 2021 by using ascending function
df_percentofethnicmin_inactive2021 = df_percentofethnicmin_inactive.sort_values(by = 'Jan 2021-Dec 2021 percent',ascending =False)
df_percentofethnicmin_inactive2021


# In[1043]:


#graphical representation of the percentage of Ethnic minority aged 16-64 who are economically inactive for the year of 2021 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2021-Dec 2021 percent', y ='Area',  data= df_percentofethnicmin_inactive2021, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Ethnic minority Aged 16-64 who are economically inactive ', size =14)
plt.xlim(15,38)
plt.ylabel('Area', size =16)
plt.title('The percentage of Ethnic minority Age 16-64 Years old who are economically inactive in Year 2021', size=14)
plt.show()


# In[1198]:


# Import the file of exploratory data and select the percentage of aged 16-64 who are economically inactive by using skiprows and nrows function

data_econ_inactive = pd.read_csv('Exploratory data_CW2.csv', skiprows = 725, nrows =10, na_values=('#','!'))
data_econ_inactive


# In[1199]:


df_econinactive = pd.DataFrame(data_econ_inactive)
df_econinactive


# In[1200]:


# Calculating the mean value of all counties to observe the difference in their values from 2012-2021 and select the percenatge
# column only by using axis =1
print(df_econinactive.mean(axis=1,numeric_only=True))


# In[1047]:


# Tabulating and sorting out the percentage of aged 16-64 who are economically inactive for the year of 2012 by using ascending function
df_econ_inactive2012 = df_econinactive.sort_values(by = 'Jan 2012-Dec 2012 percent',ascending =False)
df_econ_inactive2012


# In[1048]:


#graphical representation of the percentage of aged 16-64 who are economically inactive for the year of 2012 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2012-Dec 2012 percent', y ='Area',  data= df_econ_inactive2012, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 who are economically inactive ', size =14)
plt.xlim(15,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16-64 Years old who are economically inactive in Year 2012', size=14)
plt.show()


# In[1049]:


# Tabulating and sorting out the percentage of aged 16-64 who are economically inactive for the year of 2013 by using ascending function
df_econ_inactive2013 = df_econinactive.sort_values(by = 'Jan 2013-Dec 2013 percent',ascending =False)
df_econ_inactive2013


# In[1050]:


#graphical representation of the percentage of aged 16-64 who are economically inactive for the year of 2013 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2013-Dec 2013 percent', y ='Area',  data= df_econ_inactive2013, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 who are economically inactive ', size =14)
plt.xlim(15,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16-64 Years old who are economically inactive in Year 2013', size=14)
plt.show()


# In[1051]:


# Tabulating and sorting out the percentage of aged 16-64 who are economically inactive for the year of 2014 by using ascending function
df_econ_inactive2014 = df_econinactive.sort_values(by = 'Jan 2014-Dec 2014 percent',ascending =False)
df_econ_inactive2014


# In[1052]:


#graphical representation of the percentage of aged 16-64 who are economically inactive for the year of 2014 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2014-Dec 2014 percent', y ='Area',  data= df_econ_inactive2014, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 who are economically inactive ', size =14)
plt.xlim(15,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16-64 Years old who are economically inactive in Year 2014', size=14)
plt.show()


# In[1053]:


# Tabulating and sorting out the percentage of aged 16-64 who are economically inactive for the year of 2015 by using ascending function
df_econ_inactive2015 = df_econinactive.sort_values(by = 'Jan 2015-Dec 2015 percent',ascending =False)
df_econ_inactive2015


# In[1054]:


#graphical representation of the percentage of aged 16-64 who are economically inactive for the year of 2015 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2015-Dec 2015 percent', y ='Area',  data= df_econ_inactive2015, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 who are economically inactive ', size =14)
plt.xlim(15,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16-64 Years old who are economically inactive in Year 2015', size=14)
plt.show()


# In[1055]:


# Tabulating and sorting out the percentage of aged 16-64 who are economically inactive for the year of 2016 by using ascending function
df_econ_inactive2016 = df_econinactive.sort_values(by = 'Jan 2016-Dec 2016 percent',ascending =False)
df_econ_inactive2016


# In[1056]:


#graphical representation of the percentage of aged 16-64 who are economically inactive for the year of 2016 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2016-Dec 2016 percent', y ='Area',  data= df_econ_inactive2016, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 who are economically inactive ', size =14)
plt.xlim(15,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16-64 Years old who are economically inactive in Year 2016', size=14)
plt.show()


# In[1057]:


# Tabulating and sorting out the percentage of aged 16-64 who are economically inactive for the year of 2017 by using ascending function
df_econ_inactive2017= df_econinactive.sort_values(by = 'Jan 2017-Dec 2017 percent',ascending =False)
df_econ_inactive2017


# In[1058]:


#graphical representation of the percentage of aged 16-64 who are economically inactive for the year of 2017 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2017-Dec 2017 percent', y ='Area',  data= df_econ_inactive2017, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 who are economically inactive ', size =14)
plt.xlim(15,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16-64 Years old who are economically inactive in Year 2017', size=14)
plt.show()


# In[1059]:


# Tabulating and sorting out the percentage of aged 16-64 who are economically inactive for the year of 2018 by using ascending function
df_econ_inactive2018 = df_econinactive.sort_values(by = 'Jan 2018-Dec 2018 percent',ascending =False)
df_econ_inactive2018


# In[1060]:


#graphical representation of the percentage of aged 16-64 who are economically inactive for the year of 2018 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2018-Dec 2018 percent', y ='Area',  data= df_econ_inactive2018, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 who are economically inactive ', size =14)
plt.xlim(15,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16-64 Years old who are economically inactive in Year 2018', size=14)
plt.show()


# In[1061]:


# Tabulating and sorting out the percentage of aged 16-64 who are economically inactive for the year of 2019 by using ascending function
df_econ_inactive2019 = df_econinactive.sort_values(by = 'Jan 2019-Dec 2019 percent',ascending =False)
df_econ_inactive2019


# In[1062]:


#graphical representation of the percentage of aged 16-64 who are economically inactive for the year of 2019 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2019-Dec 2019 percent', y ='Area',  data= df_econ_inactive2019, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 who are economically inactive ', size =14)
plt.xlim(15,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16-64 Years old who are economically inactive in Year 2019', size=14)
plt.show()


# In[1063]:


# Tabulating and sorting out the percentage of aged 16-64 who are economically inactive for the year of 2020 by using ascending function
df_econ_inactive2020 = df_econinactive.sort_values(by = 'Jan 2020-Dec 2020 percent',ascending =False)
df_econ_inactive2020


# In[1064]:


#graphical representation of the percentage of aged 16-64 who are economically inactive for the year of 2020 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2020-Dec 2020 percent', y ='Area',  data= df_econ_inactive2020, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 who are economically inactive ', size =14)
plt.xlim(15,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16-64 Years old who are economically inactive in Year 2020', size=14)
plt.show()


# In[1065]:


# Tabulating and sorting out the percentage of aged 16-64 who are economically inactive for the year of 2021 by using ascending function
df_econ_inactive2021 = df_econinactive.sort_values(by = 'Jan 2021-Dec 2021 percent',ascending =False)
df_econ_inactive2021


# In[1066]:


#graphical representation of the percentage of aged 16-64 who are economically inactive for the year of 2021 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2021-Dec 2021 percent', y ='Area',  data= df_econ_inactive2021, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 who are economically inactive ', size =14)
plt.xlim(15,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Age 16-64 Years old who are economically inactive in Year 2021', size=14)
plt.show()


# In[1201]:


# Import the file of exploratory data and select the percentage of economically inactive who don't want a job by using skiprows and nrows function

data_econinactive_job= pd.read_csv('Exploratory data_CW2.csv', skiprows = 745, nrows =10,na_values=('#','!'))
data_econinactive_job


# In[1202]:


df_econinactive_job = pd.DataFrame(data_econinactive_job)
df_econinactive_job


# In[1203]:


# Calculating the mean value of all counties to observe the difference in their values from 2012-2021 and select the percenatge
# column only by using axis =1
print(df_econinactive_job.mean(axis = 1, numeric_only= True))


# In[1204]:


# Tabulating and sorting out the percentage of are economically inactive  who don't want a job for the year of 2012 by using ascending function
df_econinactive_job2012 = df_econinactive_job.sort_values(by = 'Jan 2012-Dec 2012 percent',ascending =False)
df_econinactive_job2012


# In[1071]:


#graphical representation of the percentage of economically inactive who don't want a job for the year of 2012 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2012-Dec 2012 percent', y ='Area',  data= df_econinactive_job2012, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Economically inactive who do not want a Job ', size =14)
plt.xlim(60,90)
plt.ylabel('Area', size =16)
plt.title('The percentage of Economically inactive who do not want a Job  in Year 2012', size=14)
plt.show()


# In[1072]:


# Tabulating and sorting out the percentage of are economically inactive  who don't want a job for the year of 2013 by using ascending function
df_econinactive_job2013 = df_econinactive_job.sort_values(by = 'Jan 2013-Dec 2013 percent',ascending =False)
df_econinactive_job2013


# In[1073]:


#graphical representation of the percentage of economically inactive who don't want a job for the year of 2013 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2013-Dec 2013 percent', y ='Area',  data= df_econinactive_job2013, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Economically inactive who do not want a Job ', size =14)
plt.xlim(65,84)
plt.ylabel('Area', size =16)
plt.title('The percentage of Economically inactive who do not want a Job  in Year 2013', size=14)
plt.show()


# In[1074]:


# Tabulating and sorting out the percentage of are economically inactive  who don't want a job for the year of 2014 by using ascending function
df_econinactive_job2014 = df_econinactive_job.sort_values(by = 'Jan 2014-Dec 2014 percent',ascending =False)
df_econinactive_job2014


# In[1075]:


#graphical representation of the percentage of economically inactive who don't want a job for the year of 2014 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2014-Dec 2014 percent', y ='Area',  data= df_econinactive_job2014, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Economically inactive who do not want a Job ', size =14)
plt.xlim(60,85)
plt.ylabel('Area', size =16)
plt.title('The percentage of Economically inactive who do not want a Job  in Year 2014', size=14)
plt.show()


# In[1076]:


# Tabulating and sorting out the percentage of are economically inactive  who don't want a job for the year of 2015 by using ascending function
df_econinactive_job2015 = df_econinactive_job.sort_values(by = 'Jan 2015-Dec 2015 percent',ascending =False)
df_econinactive_job2015


# In[1077]:


#graphical representation of the percentage of economically inactive who don't want a job for the year of 2015 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2015-Dec 2015 percent', y ='Area',  data= df_econinactive_job2015, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Economically inactive who do not want a Job ', size =14)
plt.xlim(65,85)
plt.ylabel('Area', size =16)
plt.title('The percentage of Economically inactive who do not want a Job  in Year 2015', size=14)
plt.show()


# In[1078]:


# Tabulating and sorting out the percentage of are economically inactive  who don't want a job for the year of 2016 by using ascending function
df_econinactive_job2016 = df_econinactive_job.sort_values(by = 'Jan 2016-Dec 2016 percent',ascending =False)
df_econinactive_job2016


# In[1079]:


#graphical representation of the percentage of economically inactive who don't want a job for the year of 2016 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2016-Dec 2016 percent', y ='Area',  data= df_econinactive_job2016, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Economically inactive who do not want a Job ', size =14)
plt.xlim(65,88)
plt.ylabel('Area', size =16)
plt.title('The percentage of Economically inactive who do not want a Job  in Year 2016', size=14)
plt.show()


# In[1080]:


# Tabulating and sorting out the percentage of are economically inactive  who don't want a job for the year of 2017 by using ascending function
df_econinactive_job2017 = df_econinactive_job.sort_values(by = 'Jan 2017-Dec 2017 percent',ascending =False)
df_econinactive_job2017


# In[1081]:


#graphical representation of the percentage of economically inactive who don't want a job for the year of 2017 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2017-Dec 2017 percent', y ='Area',  data= df_econinactive_job2017, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Economically inactive who do not want a Job ', size =14)
plt.xlim(65,90)
plt.ylabel('Area', size =16)
plt.title('The percentage of Economically inactive who do not want a Job  in Year 2017', size=14)
plt.show()


# In[1082]:


# Tabulating and sorting out the percentage of are economically inactive  who don't want a job for the year of 2018 by using ascending function
df_econinactive_job2018 = df_econinactive_job.sort_values(by = 'Jan 2018-Dec 2018 percent',ascending =False)
df_econinactive_job2018


# In[1083]:


#graphical representation of the percentage of economically inactive who don't want a job for the year of 2018 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2018-Dec 2018 percent', y ='Area',  data= df_econinactive_job2018, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Economically inactive who do not want a Job ', size =14)
plt.xlim(65,90)
plt.ylabel('Area', size =16)
plt.title('The percentage of Economically inactive who do not want a Job  in Year 2018', size=14)
plt.show()


# In[1084]:


# Tabulating and sorting out the percentage of are economically inactive  who don't want a job for the year of 2019 by using ascending function
df_econinactive_job2019 = df_econinactive_job.sort_values(by = 'Jan 2019-Dec 2019 percent',ascending =False)
df_econinactive_job2019


# In[1085]:


#graphical representation of the percentage of economically inactive who don't want a job for the year of 2019 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2019-Dec 2019 percent', y ='Area',  data= df_econinactive_job2019, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Economically inactive who do not want a Job ', size =14)
plt.xlim(65,96)
plt.ylabel('Area', size =16)
plt.title('The percentage of Economically inactive who do not want a Job  in Year 2019', size=14)
plt.show()


# In[1086]:


# Tabulating and sorting out the percentage of are economically inactive  who don't want a job for the year of 2020 by using ascending function
df_econinactive_job2020 = df_econinactive_job.sort_values(by = 'Jan 2020-Dec 2020 percent',ascending =False)
df_econinactive_job2020


# In[1087]:


#graphical representation of the percentage of economically inactive who don't want a job for the year of 2020 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2020-Dec 2020 percent', y ='Area',  data= df_econinactive_job2020, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Economically inactive who do not want a Job ', size =14)
plt.xlim(65,95)
plt.ylabel('Area', size =16)
plt.title('The percentage of Economically inactive who do not want a Job  in Year 2020', size=14)
plt.show()


# In[1088]:


# Tabulating and sorting out the percentage of are economically inactive  who don't want a job for the year of 2021 by using ascending function
df_econinactive_job2021 = df_econinactive_job.sort_values(by = 'Jan 2021-Dec 2021 percent',ascending =False)
df_econinactive_job2021


# In[1089]:


#graphical representation of the percentage of economically inactive who don't want a job for the year of 2021 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2021-Dec 2021 percent', y ='Area',  data= df_econinactive_job2021, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Economically inactive who do not want a Job ', size =14)
plt.xlim(65,95)
plt.ylabel('Area', size =16)
plt.title('The percentage of Economically inactive who do not want a Job  in Year 2021', size=14)
plt.show()


# In[1090]:


# Education
# Import the file of exploratory data and select the percentage of aged 16-64 with NVQ4+ qualification by using skiprows and nrows function

data_qualification_NVQ4plus= pd.read_csv('Exploratory data_CW2.csv', skiprows = 893, nrows =10)
data_qualification_NVQ4plus


# In[1091]:


df_qualification_NVQ4plus = pd.DataFrame (data_qualification_NVQ4plus)
df_qualification_NVQ4plus


# In[1092]:


# Calculating the mean value of all counties to observe the difference in their values from 2012-2021 and select the percenatge
# column only by using axis =1
print(df_qualification_NVQ4plus.mean(axis=1, numeric_only=True))


# In[1093]:


# Tabulating and sorting out the percentage of aged 16-64 with NVQ4+ qualification for the year of 2012 by using ascending function
df_qualifica_NVQ4plus2012 = df_qualification_NVQ4plus.sort_values(by = 'Jan 2012-Dec 2012 percent',ascending =False)
df_qualifica_NVQ4plus2012


# In[1094]:


#graphical representation of the percentage of aged 16-64 with NVQ4+ qualification for the year of 2012 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2012-Dec 2012 percent', y ='Area',  data= df_qualifica_NVQ4plus2012, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with NVQ4+ Qualification', size =14)
plt.xlim(15,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with NVQ4+ Qualification in Year 2012', size=14)
plt.show()


# In[1095]:


# Tabulating and sorting out the percentage of aged 16-64 with NVQ4+ qualification for the year of 2013 by using ascending function
df_qualifica_NVQ4plus2013 = df_qualification_NVQ4plus.sort_values(by = 'Jan 2013-Dec 2013 percent',ascending =False)
df_qualifica_NVQ4plus2013


# In[1096]:


#graphical representation of the percentage of aged 16-64 with NVQ4+ qualification for the year of 2013 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2013-Dec 2013 percent', y ='Area',  data= df_qualifica_NVQ4plus2013, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with NVQ4+ Qualification', size =14)
plt.xlim(15,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with NVQ4+ Qualification in Year 2013', size=14)
plt.show()


# In[1097]:


# Tabulating and sorting out the percentage of aged 16-64 with NVQ4+ qualification for the year of 2014 by using ascending function
df_qualifica_NVQ4plus2014 = df_qualification_NVQ4plus.sort_values(by = 'Jan 2014-Dec 2014 percent',ascending =False)
df_qualifica_NVQ4plus2014


# In[1098]:


#graphical representation of the percentage of aged 16-64 with NVQ4+ qualification for the year of 2014 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2014-Dec 2014 percent', y ='Area',  data= df_qualifica_NVQ4plus2014, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with NVQ4+ Qualification', size =14)
plt.xlim(15,45)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with NVQ4+ Qualification in Year 2014', size=14)
plt.show()


# In[1099]:


# Tabulating and sorting out the percentage of aged 16-64 with NVQ4+ qualification for the year of 2015 by using ascending function
df_qualifica_NVQ4plus2015 = df_qualification_NVQ4plus.sort_values(by = 'Jan 2015-Dec 2015 percent',ascending =False)
df_qualifica_NVQ4plus2015


# In[1100]:


#graphical representation of the percentage of aged 16-64 with NVQ4+ qualification for the year of 2015 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2015-Dec 2015 percent', y ='Area',  data= df_qualifica_NVQ4plus2015, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with NVQ4+ Qualification', size =14)
plt.xlim(15,48)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with NVQ4+ Qualification in Year 2015', size=14)
plt.show()


# In[1101]:


# Tabulating and sorting out the percentage of aged 16-64 with NVQ4+ qualification for the year of 2016 by using ascending function
df_qualifica_NVQ4plus2016 = df_qualification_NVQ4plus.sort_values(by = 'Jan 2016-Dec 2016 percent',ascending =False)
df_qualifica_NVQ4plus2016


# In[1102]:


#graphical representation of the percentage of aged 16-64 with NVQ4+ qualification for the year of 2016 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2016-Dec 2016 percent', y ='Area',  data= df_qualifica_NVQ4plus2016, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with NVQ4+ Qualification', size =14)
plt.xlim(15,50)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with NVQ4+ Qualification in Year 2016', size=14)
plt.show()


# In[1103]:


# Tabulating and sorting out the percentage of aged 16-64 with NVQ4+ qualification for the year of 2017 by using ascending function
df_qualifica_NVQ4plus2017 = df_qualification_NVQ4plus.sort_values(by = 'Jan 2017-Dec 2017 percent',ascending =False)
df_qualifica_NVQ4plus2017


# In[1104]:


#graphical representation of the percentage of aged 16-64 with NVQ4+ qualification for the year of 2017 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2017-Dec 2017 percent', y ='Area',  data= df_qualifica_NVQ4plus2017, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with NVQ4+ Qualification', size =14)
plt.xlim(25,50)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with NVQ4+ Qualification in Year 2017', size=14)
plt.show()


# In[1105]:


# Tabulating and sorting out the percentage of aged 16-64 with NVQ4+ qualification for the year of 2018 by using ascending function
df_qualifica_NVQ4plus2018 = df_qualification_NVQ4plus.sort_values(by = 'Jan 2018-Dec 2018 percent',ascending =False)
df_qualifica_NVQ4plus2018


# In[1106]:


#graphical representation of the percentage of aged 16-64 with NVQ4+ qualification for the year of 2018 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2018-Dec 2018 percent', y ='Area',  data= df_qualifica_NVQ4plus2018, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with NVQ4+ Qualification', size =14)
plt.xlim(25,50)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with NVQ4+ Qualification in Year 2018', size=14)
plt.show()


# In[1107]:


# Tabulating and sorting out the percentage of aged 16-64 with NVQ4+ qualification for the year of 2019 by using ascending function
df_qualifica_NVQ4plus2019 = df_qualification_NVQ4plus.sort_values(by = 'Jan 2019-Dec 2019 percent',ascending =False)
df_qualifica_NVQ4plus2019


# In[1108]:


#graphical representation of the percentage of aged 16-64 with NVQ4+ qualification for the year of 2019 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2019-Dec 2019 percent', y ='Area',  data= df_qualifica_NVQ4plus2019, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with NVQ4+ Qualification', size =14)
plt.xlim(25,55)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with NVQ4+ Qualification in Year 2019', size=14)
plt.show()


# In[1109]:


# Tabulating and sorting out the percentage of aged 16-64 with NVQ4+ qualification for the year of 2020 by using ascending function
df_qualifica_NVQ4plus2020 = df_qualification_NVQ4plus.sort_values(by = 'Jan 2020-Dec 2020 percent',ascending =False)
df_qualifica_NVQ4plus2020


# In[1110]:


#graphical representation of the percentage of aged 16-64 with NVQ4+ qualification for the year of 2020 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2020-Dec 2020 percent', y ='Area',  data= df_qualifica_NVQ4plus2020, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with NVQ4+ Qualification', size =14)
plt.xlim(25,55)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with NVQ4+ Qualification in Year 2020', size=14)
plt.show()


# In[1111]:


# Tabulating and sorting out the percentage of aged 16-64 with NVQ4+ qualification for the year of 2021 by using ascending function
df_qualifica_NVQ4plus2021 = df_qualification_NVQ4plus.sort_values(by = 'Jan 2021-Dec 2021 percent',ascending =False)
df_qualifica_NVQ4plus2021


# In[1112]:


#graphical representation of the percentage of aged 16-64 with NVQ4+ qualification for the year of 2021 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2021-Dec 2021 percent', y ='Area',  data= df_qualifica_NVQ4plus2021, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with NVQ4+ Qualification', size =14)
plt.xlim(25,55)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with NVQ4+ Qualification in Year 2021', size=14)
plt.show()


# In[1113]:


# Import the file of exploratory data and select the percentage of aged 16-64 with NVQ3 qualification by using skiprows and nrows function

data_qualification_NVQ3= pd.read_csv('Exploratory data_CW2.csv', skiprows = 953, nrows =10)
data_qualification_NVQ3


# In[1114]:


df_qualification_NVQ3 = pd.DataFrame (data_qualification_NVQ3)
df_qualification_NVQ3


# In[1115]:


# Tabulating and sorting out the percentage of aged 16-64 with NVQ3 qualification for the year of 2012 by using ascending function
df_qualifica_NVQ32012 = df_qualification_NVQ3.sort_values(by = 'Jan 2012-Dec 2012 percent',ascending =False)
df_qualifica_NVQ32012


# In[1116]:


#graphical representation of the percentage of aged 16-64 with NVQ3 qualification for the year of 2012 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2012-Dec 2012 percent', y ='Area',  data= df_qualifica_NVQ32012, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with NVQ3 Qualification', size =14)
plt.xlim(13,22)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with NVQ3 Qualification in Year 2012', size=14)
plt.show()


# In[1117]:


# Tabulating and sorting out the percentage of aged 16-64 with NVQ3 qualification for the year of 2013 by using ascending function
df_qualifica_NVQ32013 = df_qualification_NVQ3.sort_values(by = 'Jan 2013-Dec 2013 percent',ascending =False)
df_qualifica_NVQ32013


# In[1118]:


#graphical representation of the percentage of aged 16-64 with NVQ3 qualification for the year of 2013 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2013-Dec 2013 percent', y ='Area',  data= df_qualifica_NVQ32013, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with NVQ3 Qualification', size =14)
plt.xlim(12,20)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with NVQ3 Qualification in Year 2013', size=14)
plt.show()


# In[1119]:


# Tabulating and sorting out the percentage of aged 16-64 with NVQ3 qualification for the year of 2014 by using ascending function
df_qualifica_NVQ32014 = df_qualification_NVQ3.sort_values(by = 'Jan 2014-Dec 2014 percent',ascending =False)
df_qualifica_NVQ32014


# In[1120]:


#graphical representation of the percentage of aged 16-64 with NVQ3 qualification for the year of 2014 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2014-Dec 2014 percent', y ='Area',  data= df_qualifica_NVQ32014, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with NVQ3 Qualification', size =14)
plt.xlim(12,20)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with NVQ3 Qualification in Year 2014', size=14)
plt.show()


# In[1121]:


# Tabulating and sorting out the percentage of aged 16-64 with NVQ3 qualification for the year of 2015 by using ascending function
df_qualifica_NVQ32015 = df_qualification_NVQ3.sort_values(by = 'Jan 2015-Dec 2015 percent',ascending =False)
df_qualifica_NVQ32015


# In[1122]:


#graphical representation of the percentage of aged 16-64 with NVQ3 qualification for the year of 2015 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2015-Dec 2015 percent', y ='Area',  data= df_qualifica_NVQ32015, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with NVQ3 Qualification', size =14)
plt.xlim(12,22)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with NVQ3 Qualification in Year 2015', size=14)
plt.show()


# In[1123]:


# Tabulating and sorting out the percentage of aged 16-64 with NVQ3 qualification for the year of 2016 by using ascending function
df_qualifica_NVQ32016 = df_qualification_NVQ3.sort_values(by = 'Jan 2016-Dec 2016 percent',ascending =False)
df_qualifica_NVQ32016


# In[1124]:


#graphical representation of the percentage of aged 16-64 with NVQ3 qualification for the year of 2016 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2016-Dec 2016 percent', y ='Area',  data= df_qualifica_NVQ32016, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with NVQ3 Qualification', size =14)
plt.xlim(12,25)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with NVQ3 Qualification in Year 2016', size=14)
plt.show()


# In[1125]:


# Tabulating and sorting out the percentage of aged 16-64 with NVQ3 qualification for the year of 2017 by using ascending function
df_qualifica_NVQ32017 = df_qualification_NVQ3.sort_values(by = 'Jan 2017-Dec 2017 percent',ascending =False)
df_qualifica_NVQ32017


# In[1126]:


#graphical representation of the percentage of aged 16-64 with NVQ3 qualification for the year of 2017 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2017-Dec 2017 percent', y ='Area',  data= df_qualifica_NVQ32017, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with NVQ3 Qualification', size =14)
plt.xlim(12,22)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with NVQ3 Qualification in Year 2017', size=14)
plt.show()


# In[1127]:


# Tabulating and sorting out the percentage of aged 16-64 with NVQ3 qualification for the year of 2018 by using ascending function
df_qualifica_NVQ32018 = df_qualification_NVQ3.sort_values(by = 'Jan 2018-Dec 2018 percent',ascending =False)
df_qualifica_NVQ32018


# In[1128]:


#graphical representation of the percentage of aged 16-64 with NVQ3 qualification for the year of 2018 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2018-Dec 2018 percent', y ='Area',  data= df_qualifica_NVQ32018, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with NVQ3 Qualification', size =14)
plt.xlim(13,22)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with NVQ3 Qualification in Year 2018', size=14)
plt.show()


# In[1129]:


# Tabulating and sorting out the percentage of aged 16-64 with NVQ3 qualification for the year of 2019 by using ascending function
df_qualifica_NVQ32019 = df_qualification_NVQ3.sort_values(by = 'Jan 2019-Dec 2019 percent',ascending =False)
df_qualifica_NVQ32019


# In[1130]:


#graphical representation of the percentage of aged 16-64 with NVQ3 qualification for the year of 2019 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2019-Dec 2019 percent', y ='Area',  data= df_qualifica_NVQ32019, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with NVQ3 Qualification', size =14)
plt.xlim(13,22)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with NVQ3 Qualification in Year 2019', size=14)
plt.show()


# In[1131]:


# Tabulating and sorting out the percentage of aged 16-64 with NVQ3 qualification for the year of 2020 by using ascending function
df_qualifica_NVQ32020 = df_qualification_NVQ3.sort_values(by = 'Jan 2020-Dec 2020 percent',ascending =False)
df_qualifica_NVQ32020


# In[1132]:


#graphical representation of the percentage of aged 16-64 with NVQ3 qualification for the year of 2020 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2020-Dec 2020 percent', y ='Area',  data= df_qualifica_NVQ32020, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with NVQ3 Qualification', size =14)
plt.xlim(12,22)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with NVQ3 Qualification in Year 2020', size=14)
plt.show()


# In[1133]:


# Tabulating and sorting out the percentage of aged 16-64 with NVQ3 qualification for the year of 2021 by using ascending function
df_qualifica_NVQ32021 = df_qualification_NVQ3.sort_values(by = 'Jan 2021-Dec 2021 percent',ascending =False)
df_qualifica_NVQ32021


# In[1134]:


#graphical representation of the percentage of aged 16-64 with NVQ3 qualification for the year of 2021 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2021-Dec 2021 percent', y ='Area',  data= df_qualifica_NVQ32021, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with NVQ3 Qualification', size =14)
plt.xlim(12,22)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with NVQ3 Qualification in Year 2021', size=14)
plt.show()


# In[1135]:


# Import the file of exploratory data and select the percentage of aged 16-64 with Trade Apprenticeships by using skiprows and nrows function

data_trade_apprenticeship= pd.read_csv('Exploratory data_CW2.csv', skiprows = 1013, nrows =10)
data_trade_apprenticeship


# In[1136]:


df_trade_apprenticeship = pd.DataFrame (data_trade_apprenticeship)
df_trade_apprenticeship


# In[1137]:


# Tabulating and sorting out the percentage of aged 16-64 with Trade Apprenticeship for the year of 2012 by using ascending function
df_trade_apprenticeship2012 = df_trade_apprenticeship.sort_values(by = 'Jan 2012-Dec 2012 percent',ascending =False)
df_trade_apprenticeship2012


# In[1138]:


#graphical representation of the percentage of aged 16-64 with Trade Apprenticeship for the year of 2012 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2012-Dec 2012 percent', y ='Area',  data= df_trade_apprenticeship2012, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with Trade Apprenticeship', size =14)
plt.xlim(1,6)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with Trade Apprenticeship in Year 2012', size=14)
plt.show()


# In[1139]:


# Tabulating and sorting out the percentage of aged 16-64 with Trade Apprenticeship for the year of 2013 by using ascending function
df_trade_apprenticeship2013 = df_trade_apprenticeship.sort_values(by = 'Jan 2013-Dec 2013 percent',ascending =False)
df_trade_apprenticeship2013


# In[1140]:


#graphical representation of the percentage of aged 16-64 with Trade Apprenticeship for the year of 2013 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2013-Dec 2013 percent', y ='Area',  data= df_trade_apprenticeship2013, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with Trade Apprenticeship', size =14)
plt.xlim(1,6)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with Trade Apprenticeship in Year 2013', size=14)
plt.show()


# In[1141]:


# Tabulating and sorting out the percentage of aged 16-64 with Trade Apprenticeship for the year of 2014 by using ascending function
df_trade_apprenticeship2014 = df_trade_apprenticeship.sort_values(by = 'Jan 2014-Dec 2014 percent',ascending =False)
df_trade_apprenticeship2014


# In[1142]:


#graphical representation of the percentage of aged 16-64 with Trade Apprenticeship for the year of 2014 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2014-Dec 2014 percent', y ='Area',  data= df_trade_apprenticeship2014, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with Trade Apprenticeship', size =14)
plt.xlim(1,6)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with Trade Apprenticeship in Year 2014', size=14)
plt.show()


# In[1143]:


# Tabulating and sorting out the percentage of aged 16-64 with Trade Apprenticeship for the year of 2015 by using ascending function
df_trade_apprenticeship2015 = df_trade_apprenticeship.sort_values(by = 'Jan 2015-Dec 2015 percent',ascending =False)
df_trade_apprenticeship2015


# In[1144]:


#graphical representation of the percentage of aged 16-64 with Trade Apprenticeship for the year of 2015 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2015-Dec 2015 percent', y ='Area',  data= df_trade_apprenticeship2015, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with Trade Apprenticeship', size =14)
plt.xlim(1,6)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with Trade Apprenticeship in Year 2015', size=14)
plt.show()


# In[1145]:


# Tabulating and sorting out the percentage of aged 16-64 with Trade Apprenticeship for the year of 2016 by using ascending function
df_trade_apprenticeship2016 = df_trade_apprenticeship.sort_values(by = 'Jan 2016-Dec 2016 percent',ascending =False)
df_trade_apprenticeship2016


# In[1146]:


#graphical representation of the percentage of aged 16-64 with Trade Apprenticeship for the year of 2016 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2016-Dec 2016 percent', y ='Area',  data= df_trade_apprenticeship2016, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with Trade Apprenticeship', size =14)
plt.xlim(1,6)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with Trade Apprenticeship in Year 2016', size=14)
plt.show()


# In[1147]:


# Tabulating and sorting out the percentage of aged 16-64 with Trade Apprenticeship for the year of 2017 by using ascending function
df_trade_apprenticeship2017 = df_trade_apprenticeship.sort_values(by = 'Jan 2017-Dec 2017 percent',ascending =False)
df_trade_apprenticeship2017


# In[1148]:


#graphical representation of the percentage of aged 16-64 with Trade Apprenticeship for the year of 2017 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2017-Dec 2017 percent', y ='Area',  data= df_trade_apprenticeship2017, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with Trade Apprenticeship', size =14)
plt.xlim(1,6)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with Trade Apprenticeship in Year 2017', size=14)
plt.show()


# In[1149]:


# Tabulating and sorting out the percentage of aged 16-64 with Trade Apprenticeship for the year of 2018 by using ascending function
df_trade_apprenticeship2018 = df_trade_apprenticeship.sort_values(by = 'Jan 2018-Dec 2018 percent',ascending =False)
df_trade_apprenticeship2018


# In[1150]:


#graphical representation of the percentage of aged 16-64 with Trade Apprenticeship for the year of 2018 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2018-Dec 2018 percent', y ='Area',  data= df_trade_apprenticeship2018, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with Trade Apprenticeship', size =14)
plt.xlim(1,5)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with Trade Apprenticeship in Year 2018', size=14)
plt.show()


# In[1151]:


# Tabulating and sorting out the percentage of aged 16-64 with Trade Apprenticeship for the year of 2019 by using ascending function
df_trade_apprenticeship2019 = df_trade_apprenticeship.sort_values(by = 'Jan 2019-Dec 2019 percent',ascending =False)
df_trade_apprenticeship2019


# In[1152]:


#graphical representation of the percentage of aged 16-64 with Trade Apprenticeship for the year of 2019 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2019-Dec 2019 percent', y ='Area',  data= df_trade_apprenticeship2019, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with Trade Apprenticeship', size =14)
plt.xlim(1,4)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with Trade Apprenticeship in Year 2019', size=14)
plt.show()


# In[1153]:


# Tabulating and sorting out the percentage of aged 16-64 with Trade Apprenticeship for the year of 2020 by using ascending function
df_trade_apprenticeship2020 = df_trade_apprenticeship.sort_values(by = 'Jan 2020-Dec 2020 percent',ascending =False)
df_trade_apprenticeship2020


# In[1154]:


#graphical representation of the percentage of aged 16-64 with Trade Apprenticeship for the year of 2020 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2020-Dec 2020 percent', y ='Area',  data= df_trade_apprenticeship2020, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with Trade Apprenticeship', size =14)
plt.xlim(1,4)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with Trade Apprenticeship in Year 2020', size=14)
plt.show()


# In[1155]:


# Tabulating and sorting out the percentage of aged 16-64 with Trade Apprenticeship for the year of 2021 by using ascending function
df_trade_apprenticeship2021 = df_trade_apprenticeship.sort_values(by = 'Jan 2021-Dec 2021 percent',ascending =False)
df_trade_apprenticeship2021


# In[1156]:


#graphical representation of the percentage of aged 16-64 with Trade Apprenticeship for the year of 2021 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2021-Dec 2021 percent', y ='Area',  data= df_trade_apprenticeship2021, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with Trade Apprenticeship', size =14)
plt.xlim(1,5)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with Trade Apprenticeship in Year 2021', size=14)
plt.show()


# In[1214]:


# Import the file of exploratory data and select the percentage of aged 16-64 with No qualification by using skiprows and nrows function

data_No_qualification= pd.read_csv('Exploratory data_CW2_final .csv', skiprows = 1197, nrows =10, na_values=('#','!'))
data_No_qualification


# In[1215]:


df_No_qualification = pd.DataFrame (data_No_qualification)
df_No_qualification


# In[1216]:


# Calculating the mean value of all counties to observe the difference in their values from 2012-2021 and select the percenatge
# column only by using axis =1
Noqualification =df_No_qualification.mean(axis=1, numeric_only=True)
print(Noqualification)


# In[1217]:


# Tabulating and sorting out the percentage of aged 16-64 with No qualification for the year of 2012 by using ascending function
df_No_qualification2012 = df_No_qualification.sort_values(by = 'Jan 2012-Dec 2012 percent',ascending =False)
df_No_qualification2012


# In[ ]:


#graphical representation of the percentage of aged 16-64 with No qualification for the year of 2012 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2012-Dec 2012 percent', y ='Area',  data= df_No_qualification2012, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with No Qualification', size =14)
plt.xlim(5,20)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with No Qualification in Year 2012', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of aged 16-64 with No qualification for the year of 2013 by using ascending function
df_No_qualification2013 = df_No_qualification.sort_values(by = 'Jan 2013-Dec 2013 percent',ascending =False)
df_No_qualification2013


# In[ ]:


#graphical representation of the percentage of aged 16-64 with No qualification for the year of 2013 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2013-Dec 2013 percent', y ='Area',  data= df_No_qualification2013, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with No Qualification', size =14)
plt.xlim(5,20)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with No Qualification in Year 2013', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of aged 16-64 with No qualification for the year of 2014 by using ascending function
df_No_qualification2014 = df_No_qualification.sort_values(by = 'Jan 2014-Dec 2014 percent',ascending =False)
df_No_qualification2014


# In[ ]:


#graphical representation of the percentage of aged 16-64 with No qualification for the year of 2014 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2014-Dec 2014 percent', y ='Area',  data= df_No_qualification2014, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with No Qualification', size =14)
plt.xlim(4,20)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with No Qualification in Year 2014', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of aged 16-64 with No qualification for the year of 2015 by using ascending function
df_No_qualification2015 = df_No_qualification.sort_values(by = 'Jan 2015-Dec 2015 percent',ascending =False)
df_No_qualification2015


# In[ ]:


#graphical representation of the percentage of aged 16-64 with No qualification for the year of 2015 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2015-Dec 2015 percent', y ='Area',  data= df_No_qualification2015, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with No Qualification', size =14)
plt.xlim(4,18)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with No Qualification in Year 2015', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of aged 16-64 with No qualification for the year of 2016 by using ascending function
df_No_qualification2016 = df_No_qualification.sort_values(by = 'Jan 2016-Dec 2016 percent',ascending =False)
df_No_qualification2016


# In[ ]:


#graphical representation of the percentage of aged 16-64 with No qualification for the year of 2016 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2016-Dec 2016 percent', y ='Area',  data= df_No_qualification2016, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with No Qualification', size =14)
plt.xlim(4,16)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with No Qualification in Year 2016', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of aged 16-64 with No qualification for the year of 2017 by using ascending function
df_No_qualification2017 = df_No_qualification.sort_values(by = 'Jan 2017-Dec 2017 percent',ascending =False)
df_No_qualification2017


# In[ ]:


#graphical representation of the percentage of aged 16-64 with No qualification for the year of 2017 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2017-Dec 2017 percent', y ='Area',  data= df_No_qualification2017, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with No Qualification', size =14)
plt.xlim(4,15)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with No Qualification in Year 2017', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of aged 16-64 with No qualification for the year of 2018 by using ascending function
df_No_qualification2018 = df_No_qualification.sort_values(by = 'Jan 2018-Dec 2018 percent',ascending =False)
df_No_qualification2018


# In[ ]:


#graphical representation of the percentage of aged 16-64 with No qualification for the year of 2018 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2018-Dec 2018 percent', y ='Area',  data= df_No_qualification2018, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with No Qualification', size =14)
plt.xlim(3,15)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with No Qualification in Year 2018', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of aged 16-64 with No qualification for the year of 2019 by using ascending function
df_No_qualification2019 = df_No_qualification.sort_values(by = 'Jan 2019-Dec 2019 percent',ascending =False)
df_No_qualification2019


# In[ ]:


#graphical representation of the percentage of aged 16-64 with No qualification for the year of 2019 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2019-Dec 2019 percent', y ='Area',  data= df_No_qualification2019, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with No Qualification', size =14)
plt.xlim(3,15)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with No Qualification in Year 2019', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of aged 16-64 with No qualification for the year of 2020 by using ascending function
df_No_qualification2020 = df_No_qualification.sort_values(by = 'Jan 2020-Dec 2020 percent',ascending =False)
df_No_qualification2020


# In[ ]:


#graphical representation of the percentage of aged 16-64 with No qualification for the year of 2020 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2020-Dec 2020 percent', y ='Area',  data= df_No_qualification2020, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with No Qualification', size =14)
plt.xlim(2,12)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with No Qualification in Year 2020', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of aged 16-64 with No qualification for the year of 2021 by using ascending function
df_No_qualification2021 = df_No_qualification.sort_values(by = 'Jan 2021-Dec 2021 percent',ascending =False)
df_No_qualification2021


# In[ ]:


#graphical representation of the percentage of aged 16-64 with No qualification for the year of 2021 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2021-Dec 2021 percent', y ='Area',  data= df_No_qualification2021, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage of Aged 16-64 with No Qualification', size =14)
plt.xlim(3,13)
plt.ylabel('Area', size =16)
plt.title('The percentage of Aged 16-64 with No Qualification in Year 2021', size=14)
plt.show()


# In[ ]:


# Import the file of exploratory data and select the percentage in Employment who are self-employed aged 16+ by using skiprows and nrows function

data_employ_selfemploy= pd.read_csv('Exploratory data_CW2.csv', skiprows = 1257, nrows =10)
data_employ_selfemploy


# In[ ]:


df_employ_selfemploy = pd.DataFrame (data_employ_selfemploy)
df_employ_selfemploy


# In[ ]:


# Tabulating and sorting out the percentage in Employemnt who are self-employed aged 16+ for the year of 2012 by using ascending function
df_employ_selfemploy2012 = df_employ_selfemploy.sort_values(by = 'Jan 2012-Dec 2012 percent',ascending =False)
df_employ_selfemploy2012


# In[ ]:


#graphical representation of the percentage in Employment who are self-employed for the year of 2012 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2012-Dec 2012 percent', y ='Area',  data= df_employ_selfemploy2012, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage in Employment who are Self-Employed', size =14)
plt.xlim(9,18)
plt.ylabel('Area', size =16)
plt.title('The percentage in Employment who are Self-Employed in Year 2012', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage in Employemnt who are self-employed aged 16+ for the year of 2013 by using ascending function
df_employ_selfemploy2013 = df_employ_selfemploy.sort_values(by = 'Jan 2013-Dec 2013 percent',ascending =False)
df_employ_selfemploy2013


# In[ ]:


#graphical representation of the percentage in Employment who are self-employed for the year of 2013 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2013-Dec 2013 percent', y ='Area',  data= df_employ_selfemploy2013, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage in Employment who are Self-Employed', size =14)
plt.xlim(8,18)
plt.ylabel('Area', size =16)
plt.title('The percentage in Employment who are Self-Employed in Year 2013', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage in Employemnt who are self-employed aged 16+ for the year of 2014 by using ascending function
df_employ_selfemploy2014 = df_employ_selfemploy.sort_values(by = 'Jan 2014-Dec 2014 percent',ascending =False)
df_employ_selfemploy2014


# In[ ]:


#graphical representation of the percentage in Employment who are self-employed for the year of 2014 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2014-Dec 2014 percent', y ='Area',  data= df_employ_selfemploy2014, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage in Employment who are Self-Employed', size =14)
plt.xlim(8,19)
plt.ylabel('Area', size =16)
plt.title('The percentage in Employment who are Self-Employed in Year 2014', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage in Employemnt who are self-employed aged 16+ for the year of 2015 by using ascending function
df_employ_selfemploy2015 = df_employ_selfemploy.sort_values(by = 'Jan 2015-Dec 2015 percent',ascending =False)
df_employ_selfemploy2015


# In[ ]:


#graphical representation of the percentage in Employment who are self-employed for the year of 2015 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2015-Dec 2015 percent', y ='Area',  data= df_employ_selfemploy2015, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage in Employment who are Self-Employed', size =14)
plt.xlim(8,19)
plt.ylabel('Area', size =16)
plt.title('The percentage in Employment who are Self-Employed in Year 2015', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage in Employemnt who are self-employed aged 16+ for the year of 2016 by using ascending function
df_employ_selfemploy2016 = df_employ_selfemploy.sort_values(by = 'Jan 2016-Dec 2016 percent',ascending =False)
df_employ_selfemploy2016


# In[ ]:


#graphical representation of the percentage in Employment who are self-employed for the year of 2016 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2016-Dec 2016 percent', y ='Area',  data= df_employ_selfemploy2016, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage in Employment who are Self-Employed', size =14)
plt.xlim(8,20)
plt.ylabel('Area', size =16)
plt.title('The percentage in Employment who are Self-Employed in Year 2016', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage in Employemnt who are self-employed aged 16+ for the year of 2017 by using ascending function
df_employ_selfemploy2017 = df_employ_selfemploy.sort_values(by = 'Jan 2017-Dec 2017 percent',ascending =False)
df_employ_selfemploy2017


# In[ ]:


#graphical representation of the percentage in Employment who are self-employed for the year of 2017 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2017-Dec 2017 percent', y ='Area',  data= df_employ_selfemploy2017, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage in Employment who are Self-Employed', size =14)
plt.xlim(10,20)
plt.ylabel('Area', size =16)
plt.title('The percentage in Employment who are Self-Employed in Year 2017', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage in Employemnt who are self-employed aged 16+ for the year of 2018 by using ascending function
df_employ_selfemploy2018 = df_employ_selfemploy.sort_values(by = 'Jan 2018-Dec 2018 percent',ascending =False)
df_employ_selfemploy2018


# In[ ]:


#graphical representation of the percentage in Employment who are self-employed for the year of 2018 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2018-Dec 2018 percent', y ='Area',  data= df_employ_selfemploy2018, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage in Employment who are Self-Employed', size =14)
plt.xlim(10,20)
plt.ylabel('Area', size =16)
plt.title('The percentage in Employment who are Self-Employed in Year 2018', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage in Employemnt who are self-employed aged 16+ for the year of 2019 by using ascending function
df_employ_selfemploy2019 = df_employ_selfemploy.sort_values(by = 'Jan 2019-Dec 2019 percent',ascending =False)
df_employ_selfemploy2019


# In[ ]:


#graphical representation of the percentage in Employment who are self-employed for the year of 2020 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2019-Dec 2019 percent', y ='Area',  data= df_employ_selfemploy2019, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage in Employment who are Self-Employed', size =14)
plt.xlim(11,22)
plt.ylabel('Area', size =16)
plt.title('The percentage in Employment who are Self-Employed in Year 2019', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage in Employemnt who are self-employed aged 16+ for the year of 2020 by using ascending function
df_employ_selfemploy2020 = df_employ_selfemploy.sort_values(by = 'Jan 2020-Dec 2020 percent',ascending =False)
df_employ_selfemploy2020


# In[ ]:


#graphical representation of the percentage in Employment who are self-employed for the year of 2020 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2020-Dec 2020 percent', y ='Area',  data= df_employ_selfemploy2020, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage in Employment who are Self-Employed', size =14)
plt.xlim(8,19)
plt.ylabel('Area', size =16)
plt.title('The percentage in Employment who are Self-Employed in Year 2020', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage in Employemnt who are self-employed aged 16+ for the year of 2021 by using ascending function
df_employ_selfemploy2021 = df_employ_selfemploy.sort_values(by = 'Jan 2021-Dec 2021 percent',ascending =False)
df_employ_selfemploy2021


# In[ ]:


#graphical representation of the percentage in Employment who are self-employed for the year of 2021 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2021-Dec 2021 percent', y ='Area',  data= df_employ_selfemploy2021, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The percentage in Employment who are Self-Employed', size =14)
plt.xlim(8,19)
plt.ylabel('Area', size =16)
plt.title('The percentage in Employment who are Self-Employed in Year 2021', size=14)
plt.show()


# In[ ]:


# Import the file of exploratory data and select the percentage of all people aged 16+ who are aged 16-64 by using skiprows and nrows function

data_percofall_aged16to64= pd.read_csv('Exploratory data_CW2.csv', skiprows = 1357, nrows =10)
data_percofall_aged16to64


# In[ ]:


df_percofall_aged16to64 = pd.DataFrame (data_percofall_aged16to64)
df_percofall_aged16to64


# In[ ]:


# Tabulating and sorting out the percentage of all people aged 16+ who are aged 16-64 for the year of 2012 by using ascending function
df_percofall_aged16to642012 = df_percofall_aged16to64.sort_values(by = 'Jan 2012-Dec 2012 percent',ascending =False)
df_percofall_aged16to642012


# In[ ]:


#graphical representation of the percentage of all people aged 16+ who are aged 16-64 for the year of 2012 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2012-Dec 2012 percent', y ='Area',  data= df_percofall_aged16to642012, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The Percentage of All people Aged 16+ who are Aged 16-64', size =14)
plt.xlim(75,92)
plt.ylabel('Area', size =16)
plt.title('The Percentage of All people Aged 16+ who are Aged 16-64 in Year 2012', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of all people aged 16+ who are aged 16-64 for the year of 2013 by using ascending function
df_percofall_aged16to642013 = df_percofall_aged16to64.sort_values(by = 'Jan 2013-Dec 2013 percent',ascending =False)
df_percofall_aged16to642013


# In[ ]:


#graphical representation of the percentage of all people aged 16+ who are aged 16-64 for the year of 2013 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2013-Dec 2013 percent', y ='Area',  data= df_percofall_aged16to642013, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The Percentage of All people Aged 16+ who are Aged 16-64', size =14)
plt.xlim(75,90)
plt.ylabel('Area', size =16)
plt.title('The Percentage of All people Aged 16+ who are Aged 16-64 in Year 2013', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of all people aged 16+ who are aged 16-64 for the year of 2014 by using ascending function
df_percofall_aged16to642014 = df_percofall_aged16to64.sort_values(by = 'Jan 2014-Dec 2014 percent',ascending =False)
df_percofall_aged16to642014


# In[ ]:


#graphical representation of the percentage of all people aged 16+ who are aged 16-64 for the year of 2014 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2014-Dec 2014 percent', y ='Area',  data= df_percofall_aged16to642014, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The Percentage of All people Aged 16+ who are Aged 16-64', size =14)
plt.xlim(75,90)
plt.ylabel('Area', size =16)
plt.title('The Percentage of All people Aged 16+ who are Aged 16-64 in Year 2014', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of all people aged 16+ who are aged 16-64 for the year of 2015 by using ascending function
df_percofall_aged16to642015 = df_percofall_aged16to64.sort_values(by = 'Jan 2015-Dec 2015 percent',ascending =False)
df_percofall_aged16to642015


# In[ ]:


#graphical representation of the percentage of all people aged 16+ who are aged 16-64 for the year of 2015 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2015-Dec 2015 percent', y ='Area',  data= df_percofall_aged16to642015, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The Percentage of All people Aged 16+ who are Aged 16-64', size =14)
plt.xlim(75,90)
plt.ylabel('Area', size =16)
plt.title('The Percentage of All people Aged 16+ who are Aged 16-64 in Year 2015', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of all people aged 16+ who are aged 16-64 for the year of 2016 by using ascending function
df_percofall_aged16to642016 = df_percofall_aged16to64.sort_values(by = 'Jan 2016-Dec 2016 percent',ascending =False)
df_percofall_aged16to642016


# In[ ]:


#graphical representation of the percentage of all people aged 16+ who are aged 16-64 for the year of 2016 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2016-Dec 2016 percent', y ='Area',  data= df_percofall_aged16to642016, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The Percentage of All people Aged 16+ who are Aged 16-64', size =14)
plt.xlim(75,90)
plt.ylabel('Area', size =16)
plt.title('The Percentage of All people Aged 16+ who are Aged 16-64 in Year 2016', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of all people aged 16+ who are aged 16-64 for the year of 2017 by using ascending function
df_percofall_aged16to642017 = df_percofall_aged16to64.sort_values(by = 'Jan 2017-Dec 2017 percent',ascending =False)
df_percofall_aged16to642017


# In[ ]:


#graphical representation of the percentage of all people aged 16+ who are aged 16-64 for the year of 2017 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2017-Dec 2017 percent', y ='Area',  data= df_percofall_aged16to642017, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The Percentage of All people Aged 16+ who are Aged 16-64', size =14)
plt.xlim(75,90)
plt.ylabel('Area', size =16)
plt.title('The Percentage of All people Aged 16+ who are Aged 16-64 in Year 2017', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of all people aged 16+ who are aged 16-64 for the year of 2018 by using ascending function
df_percofall_aged16to642018 = df_percofall_aged16to64.sort_values(by = 'Jan 2018-Dec 2018 percent',ascending =False)
df_percofall_aged16to642018


# In[ ]:


#graphical representation of the percentage of all people aged 16+ who are aged 16-64 for the year of 2018 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2018-Dec 2018 percent', y ='Area',  data= df_percofall_aged16to642018, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The Percentage of All people Aged 16+ who are Aged 16-64', size =14)
plt.xlim(72,92)
plt.ylabel('Area', size =16)
plt.title('The Percentage of All people Aged 16+ who are Aged 16-64 in Year 2018', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of all people aged 16+ who are aged 16-64 for the year of 2019 by using ascending function
df_percofall_aged16to642019 = df_percofall_aged16to64.sort_values(by = 'Jan 2019-Dec 2019 percent',ascending =False)
df_percofall_aged16to642019


# In[ ]:


#graphical representation of the percentage of all people aged 16+ who are aged 16-64 for the year of 2019 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2019-Dec 2019 percent', y ='Area',  data= df_percofall_aged16to642019, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The Percentage of All people Aged 16+ who are Aged 16-64', size =14)
plt.xlim(70,92)
plt.ylabel('Area', size =16)
plt.title('The Percentage of All people Aged 16+ who are Aged 16-64 in Year 2019', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of all people aged 16+ who are aged 16-64 for the year of 2020 by using ascending function
df_percofall_aged16to642020 = df_percofall_aged16to64.sort_values(by = 'Jan 2020-Dec 2020 percent',ascending =False)
df_percofall_aged16to642020


# In[ ]:


#graphical representation of the percentage of all people aged 16+ who are aged 16-64 for the year of 2020 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2020-Dec 2020 percent', y ='Area',  data= df_percofall_aged16to642020, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The Percentage of All people Aged 16+ who are Aged 16-64', size =14)
plt.xlim(73,93)
plt.ylabel('Area', size =16)
plt.title('The Percentage of All people Aged 16+ who are Aged 16-64 in Year 2020', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of all people aged 16+ who are aged 16-64 for the year of 2021 by using ascending function
df_percofall_aged16to642021 = df_percofall_aged16to64.sort_values(by = 'Jan 2021-Dec 2021 percent',ascending =False)
df_percofall_aged16to642021


# In[ ]:


#graphical representation of the percentage of all people aged 16+ who are aged 16-64 for the year of 2021 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2021-Dec 2021 percent', y ='Area',  data= df_percofall_aged16to642021, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The Percentage of All people Aged 16+ who are Aged 16-64', size =14)
plt.xlim(70,90)
plt.ylabel('Area', size =16)
plt.title('The Percentage of All people Aged 16+ who are Aged 16-64 in Year 2021', size=14)
plt.show()


# In[ ]:


# Import the file of exploratory data and select the percentage of aged 18-24 in full time education 64 by using skiprows and nrows function

data_aged18to24_education= pd.read_csv('Exploratory data_CW2.csv', skiprows = 1377, nrows =10)
data_aged18to24_education


# In[ ]:


df_aged18to24_education = pd.DataFrame(data_aged18to24_education)
df_aged18to24_education


# In[ ]:


# Tabulating and sorting out the percentage of aged 18-24 in full time education for the year of 2012 by using ascending function
df_aged18to24_education2012 = df_aged18to24_education.sort_values(by = 'Jan 2012-Dec 2012 percent',ascending =False)
df_aged18to24_education2012


# In[ ]:


#graphical representation of the percentage of aged 18-24 in full time education for the year of 2012 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2012-Dec 2012 percent', y ='Area',  data= df_aged18to24_education2012, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The Percentage of Aged 18-24 in full time Education', size =14)
plt.xlim(18,60)
plt.ylabel('Area', size =16)
plt.title('The Percentage of Aged 18-24 in full time Education in Year 2012', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of aged 18-24 in full time education for the year of 2013 by using ascending function
df_aged18to24_education2013 = df_aged18to24_education.sort_values(by = 'Jan 2013-Dec 2013 percent',ascending =False)
df_aged18to24_education2013


# In[ ]:


#graphical representation of the percentage of aged 18-24 in full time education for the year of 2013 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2013-Dec 2013 percent', y ='Area',  data= df_aged18to24_education2013, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The Percentage of Aged 18-24 in full time Education', size =14)
plt.xlim(20,55)
plt.ylabel('Area', size =16)
plt.title('The Percentage of Aged 18-24 in full time Education in Year 2013', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of aged 18-24 in full time education for the year of 2014 by using ascending function
df_aged18to24_education2014 = df_aged18to24_education.sort_values(by = 'Jan 2014-Dec 2014 percent',ascending =False)
df_aged18to24_education2014


# In[ ]:


#graphical representation of the percentage of aged 18-24 in full time education for the year of 2014 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2014-Dec 2014 percent', y ='Area',  data= df_aged18to24_education2014, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The Percentage of Aged 18-24 in full time Education', size =14)
plt.xlim(18,52)
plt.ylabel('Area', size =16)
plt.title('The Percentage of Aged 18-24 in full time Education in Year 2014', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of aged 18-24 in full time education for the year of 2015 by using ascending function
df_aged18to24_education2015 = df_aged18to24_education.sort_values(by = 'Jan 2015-Dec 2015 percent',ascending =False)
df_aged18to24_education2015


# In[ ]:


#graphical representation of the percentage of aged 18-24 in full time education for the year of 2015 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2015-Dec 2015 percent', y ='Area',  data= df_aged18to24_education2015, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The Percentage of Aged 18-24 in full time Education', size =14)
plt.xlim(17,53)
plt.ylabel('Area', size =16)
plt.title('The Percentage of Aged 18-24 in full time Education in Year 2015', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of aged 18-24 in full time education for the year of 2016 by using ascending function
df_aged18to24_education2016 = df_aged18to24_education.sort_values(by = 'Jan 2016-Dec 2016 percent',ascending =False)
df_aged18to24_education2016


# In[ ]:


#graphical representation of the percentage of aged 18-24 in full time education for the year of 2016 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2016-Dec 2016 percent', y ='Area',  data= df_aged18to24_education2016, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The Percentage of Aged 18-24 in full time Education', size =14)
plt.xlim(18,55)
plt.ylabel('Area', size =16)
plt.title('The Percentage of Aged 18-24 in full time Education in Year 2016', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of aged 18-24 in full time education for the year of 2017 by using ascending function
df_aged18to24_education2017 = df_aged18to24_education.sort_values(by = 'Jan 2017-Dec 2017 percent',ascending =False)
df_aged18to24_education2017


# In[ ]:


#graphical representation of the percentage of aged 18-24 in full time education for the year of 2017 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2017-Dec 2017 percent', y ='Area',  data= df_aged18to24_education2017, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The Percentage of Aged 18-24 in full time Education', size =14)
plt.xlim(15,55)
plt.ylabel('Area', size =16)
plt.title('The Percentage of Aged 18-24 in full time Education in Year 2017', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of aged 18-24 in full time education for the year of 2018 by using ascending function
df_aged18to24_education2018 = df_aged18to24_education.sort_values(by = 'Jan 2018-Dec 2018 percent',ascending =False)
df_aged18to24_education2018


# In[ ]:


#graphical representation of the percentage of aged 18-24 in full time education for the year of 2018 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2018-Dec 2018 percent', y ='Area',  data= df_aged18to24_education2018, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The Percentage of Aged 18-24 in full time Education', size =14)
plt.xlim(20,55)
plt.ylabel('Area', size =16)
plt.title('The Percentage of Aged 18-24 in full time Education in Year 2018', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of aged 18-24 in full time education for the year of 2019 by using ascending function
df_aged18to24_education2019 = df_aged18to24_education.sort_values(by = 'Jan 2019-Dec 2019 percent',ascending =False)
df_aged18to24_education2019


# In[ ]:


#graphical representation of the percentage of aged 18-24 in full time education for the year of 2019 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2019-Dec 2019 percent', y ='Area',  data= df_aged18to24_education2019, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The Percentage of Aged 18-24 in full time Education', size =14)
plt.xlim(22,55)
plt.ylabel('Area', size =16)
plt.title('The Percentage of Aged 18-24 in full time Education in Year 2019', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of aged 18-24 in full time education for the year of 2020 by using ascending function
df_aged18to24_education2020 = df_aged18to24_education.sort_values(by = 'Jan 2020-Dec 2020 percent',ascending =False)
df_aged18to24_education2020


# In[ ]:


#graphical representation of the percentage of aged 18-24 in full time education for the year of 2020 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2020-Dec 2020 percent', y ='Area',  data= df_aged18to24_education2020, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The Percentage of Aged 18-24 in full time Education', size =14)
plt.xlim(22,50)
plt.ylabel('Area', size =16)
plt.title('The Percentage of Aged 18-24 in full time Education in Year 2020', size=14)
plt.show()


# In[ ]:


# Tabulating and sorting out the percentage of aged 18-24 in full time education for the year of 2021 by using ascending function
df_aged18to24_education2021 = df_aged18to24_education.sort_values(by = 'Jan 2021-Dec 2021 percent',ascending =False)
df_aged18to24_education2021


# In[1169]:


#graphical representation of the percentage of aged 18-24 in full time education for the year of 2021 by using sns.barplot. sns.barplot method will 
#return a list of sub methods use containers method and pass the container object to the bar_label function. This will extract 
#and display the bar value in the bar plot. Use plt.xlim to set the x-scale for better presentation
ax = sns.barplot( x='Jan 2021-Dec 2021 percent', y ='Area',  data= df_aged18to24_education2021, errwidth = 0)
ax.bar_label(ax.containers[0])
plt.xlabel('The Percentage of Aged 18-24 in full time Education', size =14)
plt.xlim(20,55)
plt.ylabel('Area', size =16)
plt.title('The Percentage of Aged 18-24 in full time Education in Year 2021', size=14)
plt.show()


# In[ ]:




