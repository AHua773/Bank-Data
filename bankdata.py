import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
data= pd.read_csv('bank-additional-full1.csv')
plt.style.use('seaborn')

st.title('Bank Data')

st.write(data)

job_label= st.sidebar.radio(
     'Select job',
     ('management','services','admin.','blue-collar','entrepreneur','housemaid','retired','self-employed','student','technician','unemployed','unknown'))  

for b in data.job: 
    if job_label==b:
         a=job_label
    else:
        pass

data_day_yes = data[data.job == a]
data_day_yes_group = data_day_yes.groupby('day_of_week')
d1 = data_day_yes_group.y.value_counts()
fig, ax = plt.subplots(2,1)
d1.plot.bar(ax=ax[0],figsize=(20,10))
ax[0].set_title('Distribution of jobs and deposit') 
ax[0].set_xlabel('day of week ')  
ax[0].set_ylabel('Number of clients')



day_of_week_label= st.sidebar.radio(
     'Select day',
     ('mon','tue','wed','thu','fri'))

for e in data.day_of_week: 
    if day_of_week_label==e:
         f=day_of_week_label
    else:
        pass

data_job_yes = data[data.day_of_week == f]
data_job_yes_group = data_job_yes.groupby('job')
d2 = data_job_yes_group.y.value_counts()
d2.plot.bar(ax=ax[1],figsize=(20,10))
ax[1].set_title('Distribution of jobs and deposit') 
ax[1].set_xlabel('job')  
ax[1].set_ylabel('Number of clients')
st.pyplot(fig)


education_label= st.sidebar.radio(
     'Select education',
     ("basic.4y","basic.6y","basic.9y","high.school","illiterate","professional.course","university.degree","unknown"))
for c in data.education: 
    if education_label==c:
         h=education_label
    else:
        pass
fig, ax = plt.subplots(2,1)
data_education_yes = data[data.education == h]
data_education_yes_group = data_education_yes.groupby('cons_price_idx')
d3 = data_education_yes_group.y.value_counts()
d3.plot(ax=ax[0],figsize=(20,10))
ax[0].set_title('Distribution of cons.price.idx and education') 
ax[0].set_xlabel('cons.price.idx ')
ax[0].set_ylabel('Number of clients')


index = st.sidebar.slider('cons_price_idx', 90.00, 100.00, 100.00)
for g in data.cons_price_idx: 
    if index==g:
        q=index
    else:
        pass
data_cpi_yes= data[data.cons_price_idx == q]
data_cpi_yes_group = data_cpi_yes.groupby('education')
d4=data_cpi_yes_group.y.value_counts()
d4.plot(ax=ax[1],figsize=(20,10))


st.pyplot(fig)
