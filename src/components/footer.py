import streamlit as st


def footer_home():
    logo_url = "https://www.google.com/imgres?q=utsav&imgurl=https%3A%2F%2Fwww.uxdt.nic.in%2Fwp-content%2Fuploads%2F2024%2F07%2Futsav-01.jpg%3Fx29347&imgrefurl=https%3A%2F%2Fwww.uxdt.nic.in%2Fdocuments%2Flogos%2Futsav%2F&docid=QaJoSHbg-JCmmM&tbnid=10qYbF9HdmpnCM&vet=12ahUKEwiM2ICCxZ2VAxVVSnADHVoNIjQQnPAOegQIXBAA..i&w=1000&h=750&hcb=2&ved=2ahUKEwiM2ICCxZ2VAxVVSnADHVoNIjQQnPAOegQIXBAA"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:white;"> Created with ❤️ by </p>  
        <img src='{logo_url}' style='max-height:25px' />
        </div>
                
                """, unsafe_allow_html=True)


def footer_dashboard():
    logo_url = "https://www.google.com/imgres?q=utsav&imgurl=https%3A%2F%2Fwww.uxdt.nic.in%2Fwp-content%2Fuploads%2F2024%2F07%2Futsav-01.jpg%3Fx29347&imgrefurl=https%3A%2F%2Fwww.uxdt.nic.in%2Fdocuments%2Flogos%2Futsav%2F&docid=QaJoSHbg-JCmmM&tbnid=10qYbF9HdmpnCM&vet=12ahUKEwiM2ICCxZ2VAxVVSnADHVoNIjQQnPAOegQIXBAA..i&w=1000&h=750&hcb=2&ved=2ahUKEwiM2ICCxZ2VAxVVSnADHVoNIjQQnPAOegQIXBAA"
    
    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
        <p style="font-weight:bold; color:black;"> Created with ❤️ by </p>  
        <img src='{logo_url}' style='max-height:25px' />
        </div>
                
                """, unsafe_allow_html=True)
