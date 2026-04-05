import streamlit as st

DEPT_MATRIX = {
    "資訊部": ["網域管理員", "GitLab_存取", "伺服器機房門禁", "VPN_技術組"],
    "人事部": ["薪資系統存取", "員工個資檔案庫", "差勤管理系統"],
    "財務部": ["ERP_財務模組", "銀行聯網專線", "電子發票簽核"],
    "業務部": ["CRM_客戶系統", "外部報價權限", "區域業績看板"],
    "研發部": ["原始碼控制庫", "測試環境虛擬機", "專利文件庫"],
    "行銷部": ["官網管理權限", "社群媒體發佈", "廣告投放後台"],
    "資材部": ["庫存管理系統", "採購單簽核", "供應商資料庫"],
    "生產部": ["MES_生產系統", "設備監控權限", "工單排程系統"],
    "總經理室": ["全院檔案讀取", "高階決策看板", "機密公文簽核"],
    "法務部": ["合約管理系統", "法律資料庫", "數位簽章權限"],
    "客服部": ["客服語音系統", "客訴追蹤平台", "用戶知識庫"],
    "倉管部": ["進出貨掃描系統", "儲位管理權限", "物流追蹤系統"]
}

OP_MODES = [
    "帳號自動化派發", "權限變更申請", "離職帳號停用", "密碼重設服務",
    "稽核日誌查詢", "群組原則管理", "組織架構調整", "臨時權限授權",
    "設備資產綁定", "多因素認證管理", "系統參數設定", "備份還原檢查"
]

def main():
    st.set_page_config(page_title="Directory Service Console", layout="wide")
    st.title("企業級網域目錄服務管理平台")
    
    with st.sidebar:
        st.header("系統功能")
        mode = st.selectbox("功能模式選擇", OP_MODES)

    if mode == "帳號自動化派發":
        st.subheader("員工到職帳號預先配置")
        
        container = st.container()
        col1, col2 = container.columns(2)
        
        with col1:
            emp_name = st.text_input("員工姓名", placeholder="輸入姓名")
            st.caption("擔任職位：正式員工")
            
        with col2:
            dept = st.selectbox("部門單位選擇", list(DEPT_MATRIX.keys()))
            site = st.radio("派駐地點", ["台北總部", "台中分公司", "高雄廠區"], horizontal=True)

        if st.button("執行配置分析", use_container_width=True):
            if emp_name:
                st.divider()
                st.success(f"系統已完成 {emp_name} ({dept}) 的權限預校")
                
                st.subheader("🛡️ 權限對標清單")
                
                res_col1, res_col2 = st.columns(2)
                
                with res_col1:
                    st.write("**安全性群組 (Security Groups)：**")
                    for p in DEPT_MATRIX[dept]:
                        st.checkbox(f"指派 {p}", value=True, key=f"p_{p}")
                
                with res_col2:
                    st.write("**組織單位路徑 (LDAP Path)：**")
                    st.code(f"OU={dept},DC=dafeng,DC=com")
                    st.write("**套用原則 (GPO)：**")
                    st.warning(f"GPO_{dept}_Standard_Policy")
            else:
                st.error("錯誤：請輸入員工姓名以啟動邏輯。")

if __name__ == "__main__":
    main()