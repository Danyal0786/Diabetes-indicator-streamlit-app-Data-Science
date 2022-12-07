#All necessary packages imported to run the application
import streamlit as st 
import pandas as pd 

# Data Visualization Packages
import matplotlib.pyplot as plt 
import matplotlib
matplotlib.use('Agg')
import seaborn as sns
import plotly.express as px 


@st.cache
def load_data(data):
	df = pd.read_csv(data)
	return df


def run_eda_app():
	"""This function run inside EDA screen, where three dataframes where loaded for 
	   visualization
	"""
	st.subheader("EDA Section")
	df = load_data("data/diabetes_data_upload.csv")
	df_clean = load_data("data/diabetes_data_upload_clean.csv")
	freq_df = load_data("data/freqdist_of_age_data.csv")

	submenu = st.sidebar.selectbox("SubMenu",["Descriptive","Plots"])
	if submenu == "Descriptive":
		
		st.dataframe(df)

		with st.expander("Descriptive Summary"):
			st.dataframe(df_clean.describe())

		with st.expander("Data Types Summary"):
			dff =pd.DataFrame(df.dtypes,columns=["Data Type"]).reset_index()
			dff.columns = ["Column","Data Type"]
			dff["Data Type"] = dff["Data Type"].astype(str)
			st.dataframe(dff)
		
		with st.expander("Gender Distribution"):
			st.dataframe(df['Gender'].value_counts())

		with st.expander("Class Distribution"):
			st.dataframe(df['class'].value_counts())
	else:
		st.subheader("Plots")
# ------------------------------------------------------------------------------------------------
		""" Layouts created with streamlit column component
		"""
		col1,col2 = st.columns([2,1])
		with col1:
			with st.expander("Dist Plot of Gender"):
				demo_Df = df.groupby(by=["Gender"]).size().reset_index(name="counts")
				dist_gen = px.bar(data_frame=demo_Df, x="Gender", y="counts")
				dist_gen. update_xaxes(showgrid=False)
				dist_gen. update_yaxes(showgrid=False)
				st.plotly_chart(dist_gen)


				gen_df = df['Gender'].value_counts().to_frame()
				gen_df = gen_df.reset_index()
				gen_df.columns = ['Gender Type','Counts']
				p01 = px.pie(gen_df,names='Gender Type',values='Counts')
				st.plotly_chart(p01,use_container_width=True)

			with st.expander("Dist Plot of Class"):
				df_class = df.groupby(by=['class']).size().reset_index(name="counts")
				dist_class = px.bar(data_frame=df_class, x="class",y="counts")
				dist_class. update_xaxes(showgrid=False)
				dist_class. update_yaxes(showgrid=False)
				st.plotly_chart(dist_class)
				


		with col2:
			with st.expander("Gender Distribution"):
				st.dataframe(df['Gender'].value_counts())

			with st.expander("Class Distribution"):
				st.dataframe(df['class'].value_counts())
			

		with st.expander("Frequency Dist Plot of Age"):
			p1 = px.bar(freq_df,x='Age',y='count')
			p1. update_xaxes(showgrid=False)
			p1. update_yaxes(showgrid=False)
			st.plotly_chart(p1)

			p2 = px.line(freq_df,x='Age',y='count')
			p2. update_xaxes(showgrid=False)
			p2. update_yaxes(showgrid=False)
			st.plotly_chart(p2)

		with st.expander("Outlier Detection Plot"):
			outlier_df = px.box(df,x='Age',color='Gender')
			st.plotly_chart(outlier_df)


		with st.expander("Correlation Plot"):
			corr_matrix = df_clean.corr()
			corr_df = px.imshow(corr_matrix,text_auto=True)
			corr_df.layout.height = 600
			corr_df.layout.width = 1000
			st.plotly_chart(corr_df)
		
			


	







