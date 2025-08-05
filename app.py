import streamlit as st 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Welcome message
st.title("Welcome to the Data Analysis App")

# Load the dataset
try:
    data = pd.read_csv('/student_habits_performance.csv')  # use forward slash (or right click the file and copy relative path and paste between '')
except Exception as e:
    st.error("Failed to load dataset. Please check the file path.")
    st.stop()

# Add a sidebar for user input
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "Data Analysis", "Visualization", "Insights"])

# Page Routing
if page == 'Home':
    st.header("Welcome to Student Performance Analysis Dashboard App")
    st.write("This app allows you to get insights into student habits and their impact on performance.")
    try:
        st.image('image\WhatsApp Image 2025-08-02 at 18.29.39.jpeg', caption='student')
    except Exception as e:
        st.warning('Image not found.') 

elif page == 'Data Analysis':
    st.header('Data Analysis')
    st.write("Explore the dataset and gain insights into student habits and performance.")
        
    # Show first few rows
    st.subheader("Here are the first few rows of the dataset:")
    st.dataframe(data.head())
    
    # Categorical variable distribution

    # Identify categorical columns
    categorical_cols = data.select_dtypes(include=['object', 'category']).columns.tolist()

    #if categorical_cols:
    selected_col = st.selectbox("Select a categorical column", categorical_cols)

        #if selected_col:
    # Count the frequency of each category
    category_counts = data[selected_col].value_counts()

            # Plot using seaborn
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(x=category_counts.index, y=category_counts.values, ax=ax)
    ax.set_title(f"Distribution of '{selected_col}'")
    ax.set_xlabel(selected_col)
    ax.set_ylabel("Count")
    plt.xticks(rotation=45)
    st.pyplot(fig)

    # Tabulate frequency
    freq_table = data[selected_col].value_counts().reset_index()
    freq_table.columns = [selected_col, 'Count']
    # Display table
    st.dataframe(freq_table)

    # Display basic statistics
    st.subheader("Basic statistics of the dataset:")
    st.dataframe(data.describe())
    st.dataframe(data.shape)
    ## Display variables patterns
    selected_column = st.selectbox("Select a feature you want the description for:", data.columns)
    st.subheader(f"Description of '{selected_column}'")
    st.write(data[selected_column].describe())
    # Display correlation
    st.subheader("Correlation Matrix:")
    #st.write(data.corr())
    corr = data.corr(numeric_only=True)
    #st.write(data[corr].corr())
    # Plot the heatmap
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f", ax=ax)
    plt.title("Correlation Matrix Heatmap")
    st.pyplot(fig)
elif page == 'Visualization':
    st.header('Visualization')
    st.write("Visualize the data to understand trends and patterns.")
    # Add your plots here later

    # Filter numeric columns for plotting
    numeric_columns = data.select_dtypes(include=['float64', 'int64']).columns

    # Let user select a column
    selected_column = st.selectbox("Select a numeric column to plot", numeric_columns)

    # Plotting the selected column as a histogram
    st.subheader(f"Histogram of '{selected_column}'")

    fig, ax = plt.subplots()
    ax.hist(data[selected_column], bins=20, color='skyblue', edgecolor='black')
    ax.set_xlabel(selected_column)
    ax.set_ylabel("Frequency")
    st.pyplot(fig)
    #st.write(data[selected_column].describe())
    #st.write(f"Summary Statistics of {data[selected_column].describe()}'")
    st.write(f"Summary Statistics for {selected_column} Variable: {data[selected_column].describe()}'")
    # Draw boxplot
    st.subheader(f"Boxplot of '{selected_column}'")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data[selected_column], ax=ax)
    plt.title(f"'{selected_column}'Boxplot")
    st.pyplot(fig)

elif page == 'Insights':
    st.header('Insights')
    st.write("This section will provide insights into how different habits affect student performance.")

else:
    st.write("Please select a valid page from the sidebar.")






    
