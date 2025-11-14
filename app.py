import streamlit as st
 
#Add the title
 
st.title(" Simple marks and grade calculator")
 
#Number of subjects
 
subjects = st.number_input(
    "Number of subjects",
    min_value = 1,
    max_value = 10,
    value= 5
  )
# Marks for  Each subject
 
marks=[]
for i in range(int(subjects)):
      mark=st.number_input(
            f"marks for subjects {i+1}",
            min_value = 0,
            max_value = 100,
      )
      marks.append(mark)
 
#Calculate  Results
 
if st.button("calulate"):
    total =sum(marks)
    percentage = total / subjects
 
#Display total and percentage
    st.write(f"Total marks:{total}")
    st.write(f"Percentage: {percentage : .2f}%")
 
#Grade Calculation
    if percentage >= 90:
     st.success("Grade: A")
    elif percentage >= 80:
     st.info("Grade: B")
    elif percentage >= 70:
     st.warning("Grade: C")
else:
    st.error("Grade: Fail")