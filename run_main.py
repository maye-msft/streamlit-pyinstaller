


import os
import streamlit.web.bootstrap

if __name__ == "__main__":
    app_path = os.path.join(os.path.dirname(__file__), 'src', 'streamlit_app', 'main.py')
    flag_options = {
        "global.developmentMode": False
    }

    streamlit.web.bootstrap.load_config_options(flag_options=flag_options)
    flag_options["_is_running_with_streamlit"] = True
    print("app: ", app_path)
    streamlit.web.bootstrap.run(
        app_path,
        "streamlit run",
        [],
        flag_options,
    )
    

