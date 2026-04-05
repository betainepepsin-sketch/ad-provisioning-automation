import streamlit as st

ROLE_MATRIX = {
    "Engineer": {
        "ou": "OU=Engineers,DC=corp,DC=local",
        "groups": ["Git_Devs", "VPN_Users", "IT_Support"],
        "policy": "Tech_Standard_GPO"
    },
    "Human Resources": {
        "ou": "OU=HR,DC=corp,DC=local",
        "groups": ["Payroll_Access", "HR_Private"],
        "policy": "Privacy_Standard_GPO"
    },
    "Sales": {
        "ou": "OU=Sales,DC=corp,DC=local",
        "groups": ["CRM_Users", "Regional_Access"],
        "policy": "External_Access_GPO"
    }
}

def main():
    st.set_page_config(page_title="Directory Service Automation", layout="wide")
    st.title("Enterprise Directory Management Console")
    
    with st.sidebar:
        st.header("Administrative Task")
        operation = st.selectbox("Operation Mode", ["User Provisioning", "Audit Logs"])

    if operation == "User Provisioning":
        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                display_name = st.text_input("Employee Name")
                account_name = st.text_input("Logon Name (Pre-Windows 2000)")
            with col2:
                department = st.selectbox("Department Unit", list(ROLE_MATRIX.keys()))
                location = st.radio("Regional Site", ["Headquarters", "Branch Office"])

            if st.button("Initialize Provisioning", use_container_width=True):
                if display_name and account_name:
                    target_config = ROLE_MATRIX[department]
                    st.divider()
                    st.subheader("System Execution Summary")
                    
                    st.success(f"Execution Target: {display_name}")
                    
                    res_col1, res_col2, res_col3 = st.columns(3)
                    res_col1.metric("Target OU", target_config["ou"])
                    res_col2.write("**Security Groups**")
                    for g in target_config["groups"]:
                        st.code(g)
                    res_col3.metric("Applied GPO", target_config["policy"])
                else:
                    st.error("Validation failed: Required fields missing.")

if __name__ == "__main__":
    main()