import streamlit as st
import pandas as pd

# Function to recommend courses
def recommend(course, courses_list):
    if courses_list.empty:
        return ["No courses available. Please check your data."]
    
    course_lower = course.lower()
    matches = courses_list[courses_list.str.contains(course_lower, case=False)]
    
    if not matches.empty:
        index = matches.index[0]
        distances = sorted(enumerate(similarity(index)), reverse=True, key=lambda x: x[1])
        recommended_courses = [courses_list.iloc[i[0]] for i in distances[1:8]]
        return recommended_courses
    else:
        print(f"Debug: Course not found. Input: '{course_lower}', Dataset Courses: {courses_list.tolist()}")
        return "Course not found. Please enter a valid course name."

# Streamlit web app
st.markdown("<h2 style='text-align: center; color: blue;'>Course Recommendation System</h2>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: black;'>Search for courses from a dataset of over 3,000 courses from Coursera</h4>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center; color: black;'>Created for Galala University</h4>", unsafe_allow_html=True)

# User input for course
user_input = st.text_input("Type a course you like")

if st.button("Show Recommended Courses"):
    courses_df = pd.read_xlsx("D:/cleaned_data_with_clusters.xlsx")  # Replace with your dataset file
    courses_list = courses_df["Course Name"]
    
    if not courses_list.empty:
        recommended_courses = recommend(user_input, courses_list)
        
        st.write(f"Recommended Courses based on your input: {user_input}")
        for course in recommended_courses:
            st.text(course)
    else:
        st.write("No courses available. Please check your data.")
