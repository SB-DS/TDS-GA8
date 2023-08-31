import streamlit as st

def find_largest_number(num1, num2, num3):
    return max(num1, num2, num3)

st.title("Find the largest among the 3 given numbers.")

# Input
num1 = st.number_input("Enter the first number: ")
num2 = st.number_input("Enter the second number: ")
num3 = st.number_input("Enter the third number: ")

# Find and display the largest number
if st.button("Find Largest"):
    largest = find_largest_number(num1, num2, num3)
    st.success(f"The largest number is: {largest}")
