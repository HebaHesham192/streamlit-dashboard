import pandas as pd 
import numpy as np 
import streamlit as st
import plotly.express as px
import platform

#------------------------------------------------------------------------

df=pd.read_csv(r"D:\data analysis\level 2\company_data.csv")
df.columns = df.columns.str.strip().str.lower().str.replace(' ', '_')
print(list(df.columns))
cols_to_convert=['target', 'sales', 'bonus']
df[cols_to_convert]=df[cols_to_convert].astype(float)
#df['employeeid'].astype(int)


#--------------------------------------------------------------------------


st.set_page_config(page_title="Target Achieved", layout="wide")
st.set_page_config(layout="wide")
#st.markdown('''<h1 style ='text-align:center; margin-top: -65px;'> Target Achieved </h1>''', unsafe_allow_html=True)

st.markdown("<h1 style='text-align: center; color:#00FA9A; margin-top: -65px;'>Target Achieved </h1>", unsafe_allow_html=True)
#-------------------------------------------------------------------------
#عايزه اخلي الصوره ايقونه
# st.markdown(f"""
#     <style>
#         .icon-img {{
#             position: fixed;
#             top: 20px;
#             right: 20px;
#             width: 50px;
#             height: 50px;
#             border-radius: 50%;
#             z-index: 9999;
#         }}
#     </style>
#     <img src="data:image/png;base64,{encoded}" class="icon-img">
# """, unsafe_allow_html=True)






# # sidebar

# st.sidebar.markdown("<h1 style='text-align: center; color: #FFA07A; margin-top: -65px;'>Target Achieved </h1>", unsafe_allow_html=True)
# #st.sidebar.header('Car sales dashboard')
# from PIL import Image
# img=Image.open(r"C:\Users\hesha\Downloads\proxy-image (2).png")
# resized_img = img.resize((int(img.width * 0.7), int(img.height * 0.6)))
# st.sidebar.image(resized_img)
# st.sidebar.write('"An interactive target achieved dashboard built with Streamlit and Python, featuring real-time filtering, model comparisons, and visual analytics."')
# st.sidebar.markdown (' :star:'' Made by Heba Hesham')
st.sidebar.title("📊 Dashboard Preview")
st.sidebar.markdown("""
    <div style='background-color:#2F4F4F; padding:15px; border-radius:10px; text-align:center;'>
        <h3 style='color:#FFD700;'>Target Achieved 🎯</h3>
        <p style='color:white;'>"An interactive target achieved dashboard built with Streamlit and Python, featuring real-time filtering, model comparisons, and visual analytics."</p>
    </div>
""", unsafe_allow_html=True)

# # Sidebar: Employee lookup by ID
st.sidebar.markdown("## 🔍 Employee  Name ")

employee_name = st.sidebar.text_input("Enter part of employee name")

if employee_name:
    if 'fullname' in df.columns:
        # فلترة جزئية مع تجاهل الحروف الكبيرة والصغيرة
        filtered = df[df['fullname'].str.lower().str.contains(employee_name.lower().strip(), na=False)]
        
        if not filtered.empty:
            for i, emp in filtered.iterrows():
                target_status = "Achieved ✅" if emp['achieve_the_target'] else "Not Achieved ❌"
                active_status = "Active 👤" if emp['active'] else "Inactive ❌"
                
                st.sidebar.markdown("---")
                st.sidebar.markdown(f"**🆔 ID:** {emp['employeeid']}")
                st.sidebar.markdown(f"**👤 Name:** {emp['fullname']}")
                st.sidebar.markdown(f"**🏢 Branch:** {emp['branch']}")
                st.sidebar.markdown(f"**🧭 Position:** {emp['position']}")
                st.sidebar.markdown(f"**📅 Join Date:** {emp['joindate']}")
                st.sidebar.markdown(f"**📆 Year:** {emp['year']} | **Month:** {emp['month']}")
                st.sidebar.markdown(f"**🎯 Target:** {target_status}")
                st.sidebar.markdown(f"**💸 Bonus:** {emp['bonus']}")
                st.sidebar.markdown(f"**🔄 Status:** {active_status}")
        else:
            st.sidebar.warning("No matching employees found.")
    else:
        st.sidebar.error("Column 'fullname' not found in data.")


# # Sidebar: Employee lookup by ID
# st.sidebar.markdown("## 🔍 Employee Lookup by ID")

# employee_id = st.sidebar.text_input("Enter employee ID")

# if employee_id:
#     # Ensure column exists and match types
#     if 'employeeid' in df.columns:
#         filtered = df[df['employeeid'].astype(str).str.strip() == employee_id.strip()]
        
#         if not filtered.empty:
#             emp = filtered.iloc[0]
            
#             # Target status
#             target_status = "Achieved ✅" if emp['achieve_the_target'] else "Not Achieved ❌"
#             # Employment status
#             active_status = "Active 👤" if emp['active'] else "Inactive ❌"
            
#             st.sidebar.markdown(f"**👤 Full Name:** {emp['fullname']}")
#             st.sidebar.markdown(f"**🏢 Branch:** {emp['branch']}")
#             st.sidebar.markdown(f"**🧭 Position:** {emp['position']}")
#             st.sidebar.markdown(f"**📅 Join Date:** {emp['joindate']}")
#             st.sidebar.markdown(f"**📆 Year:** {emp['year']} | **Month:** {emp['month']}")
#             st.sidebar.markdown(f"**🎯 Target Status:** {target_status}")
#             st.sidebar.markdown(f"**💸 Bonus:** {emp['bonus']}")
#             st.sidebar.markdown(f"**🔄 Status:** {active_status}")
#         else:
#             st.sidebar.warning("Employee not found.")
#     else:
#         st.sidebar.error("Column 'employeeid' not found in data.")



branch_filter=st.sidebar.selectbox('Branch',[None,'branch'])
st.write(' ')
st.write(' ')
date_filter=st.sidebar.selectbox('Date',[None,'month', 'year'])


st.sidebar.markdown("""
    <div style='background-color:#2F4F4F; padding:15px; border-radius:10px; text-align:center;'>
        <p style='color:#FFDEAD;'>⭐ Made by Heba Hesham</p>
    </div>
""", unsafe_allow_html=True)

# cards

# row a
a1, a2, a3, a4 = st.columns(4)
target_sum = df['target'].sum().astype(int)
a1.markdown(f"""
    <div style='background-color:#2F4F4F; padding:20px; border-radius:10px; text-align:center; box-shadow: 0 4px 8px rgba(0,0,0,0.3);'>
        <h2 style='color:#FFDEAD; text-shadow: 1px 1px 2px black;'>Sum of target 🎯</h2>
        <h1 style='color:#F0F8FF; text-shadow: 2px 2px 4px black;'>{target_sum:,}</h1>
    </div>
""", unsafe_allow_html=True)

sales_sum = df['sales'].sum().astype(int)
a2.markdown(f"""
    <div style='background-color:#2F4F4F; padding:20px; border-radius:10px; text-align:center; box-shadow: 0 4px 8px rgba(0,0,0,0.3);'>
        <h2 style='color:#FFDEAD; text-shadow: 1px 1px 2px black;'>Sum of sales 💰</h2>
        <h1 style='color:#F0F8FF; text-shadow: 2px 2px 4px black;'>{sales_sum:,}</h1>
    </div>
""", unsafe_allow_html=True)

bonus_sum = df['bonus'].sum().astype(int)
a3.markdown(f"""
    <div style='background-color:#2F4F4F; padding:20px; border-radius:10px; text-align:center; box-shadow: 0 4px 8px rgba(0,0,0,0.3);'>
        <h2 style='color:#FFDEAD; text-shadow: 1px 1px 2px black;'>Sum of sales 💸</h2>
        <h1 style='color:#F0F8FF; text-shadow: 2px 2px 4px black;'>{bonus_sum:,}</h1>
    </div>
""", unsafe_allow_html=True)

achievement_rate = (df['sales'].sum() / df['target'].sum()) * 100

a4.markdown(f"""
    <div style='background-color:#2F4F4F; padding:20px; border-radius:10px; text-align:center; box-shadow: 0 4px 8px rgba(0,0,0,0.3);'>
        <h2 style='color:#FFDEAD; text-shadow: 1px 1px 2px black;'>achievement rate 🔥</h2>
        <h1 style='color:#F0F8FF; text-shadow: 2px 2px 4px black;'>{achievement_rate:.2f}%</h1>
    </div>
""", unsafe_allow_html=True)


# chart 1


df_grouped = df.groupby(['month', 'branch'])['target'].sum().reset_index()

fig = px.line(
    df_grouped,
    x='month',
    y='target',
    color='branch',
    title='📈The sum of target by branch',
    color_discrete_map={
        'Cairo': '#00BFFF',
        'Tanta': '#FF69B4',
        'Giza': '#FFA500',
        'Alexandria': '#8A2BE2',
        'Aswan': '#228B22'
    }
)

fig.update_layout(
    title_font=dict(size=24, family='Arial', color='#FFDEAD'),
    title_x=0.0,
    xaxis=dict(
        title_font=dict(size=24, family='Arial', color='#F0F8FF'),
        tickfont=dict(size=18, family='Arial', color='#F0F8FF'),
        tickangle=-45,
        title_standoff=10
    ),
    yaxis=dict(
        title_font=dict(size=24, family='Arial', color='#F0F8FF'),
        tickfont=dict(size=18, family='Arial', color='#F0F8FF'),
        title_standoff=10
    )
)
st.plotly_chart(fig, use_container_width=True)





# row c
c1, c2, c3 = st.columns((4,3,3))

with c1:
    fig = px.bar(df, x='branch', y='sales', color=branch_filter, title='📊 Sales by Branch')

    # تحديد لون الأعمدة
    fig.update_traces(marker_color='#3CB371') 

    # تنسيق العنوان والمحاور
    fig.update_layout(
        title_font=dict(size=24, family='Arial', color='#FFDEAD'),
        title_x=0.0,
        xaxis=dict(
            title_font=dict(size=24, family='Arial', color='#F0F8FF'),
            tickfont=dict(size=18, family='Arial', color='#F0F8FF'),
            tickangle=-45,
            title_standoff=10
        ),
        yaxis=dict(
            title_font=dict(size=24, family='Arial', color='#F0F8FF'),
            tickfont=dict(size=18, family='Arial', color='#F0F8FF'),
            title_standoff=10
        )
    )

    st.plotly_chart(fig, use_container_width=True)

with c2:
    fig = px.scatter(
        df,
        x='branch',
        y='bonus',
        title='📍 Bonus per Branch',
        color='branch',
        size='target',
        color_discrete_sequence=px.colors.qualitative.Pastel
    )

    fig.update_traces(
        marker=dict(line=dict(width=1, color='DarkSlateGrey'))
    )

    fig.update_layout(
        title_font=dict(size=18, family="Arial Black", color='#FFDEAD')
    )

    st.plotly_chart(fig, use_container_width=True)

with c3:
    fig = px.pie(
        df, 
        values='target', 
        names='branch', 
        hole=0.4,
        title='📊 Target Distribution by Branch',
        color_discrete_sequence=px.colors.qualitative.Pastel
    )

    fig.update_traces(
        textinfo='percent+label', 
        textfont=dict(size=16, color="black", family="Arial Black")
    )

    fig.update_layout(
        title_font=dict(size=18, family="Arial Black", color='#FFDEAD')
    )

    st.plotly_chart(fig, use_container_width=True)

with st.expander("See DataFrame"):
    st.dataframe(df)









