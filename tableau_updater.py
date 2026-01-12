import tableauserverclient as TSC
import pantab
import pandas as pd
import os
from config import TABLEAU_SERVER, TABLEAU_SITE_ID, TABLEAU_TOKEN_NAME, TABLEAU_TOKEN_VALUE, TABLEAU_DATASOURCE_NAME

def update_tableau_datasource(df):
    """
    Converts Data to .hyper format (High Performance) and updates Tableau.
    """
    print("⏳ Converting data to Tableau Hyper format...")

    # 1. Convert Pandas DF -> .hyper file
    hyper_file = "revenue_data.hyper"
    
    # Pantab magic: Ye CSV ko Hyper bana dega
    try:
        pantab.frame_to_hyper(df, hyper_file, table="Extract")
    except Exception as e:
        print(f"❌ Error creating Hyper file: {e}")
        return
    
    try:
        # 2. Auth Setup
        print(f"🔄 Connecting to {TABLEAU_SERVER}...")
        
        # --- FIX IS HERE (Removed quotes around variables) ---
        tableau_auth = TSC.PersonalAccessTokenAuth(
            token_name=TABLEAU_TOKEN_NAME,
            personal_access_token=TABLEAU_TOKEN_VALUE,  # <--- No Quotes!
            site_id=TABLEAU_SITE_ID                     # <--- No Quotes!
        )

        server = TSC.Server(TABLEAU_SERVER, use_server_version=True)
        
        # 3. Sign In
        with server.auth.sign_in(tableau_auth):
            print("✅ Signed in to Tableau.")

            # 4. Define Datasource
            # Hum 'Default' project use karenge (Ensure 'Default' project exists)
            req_option = TSC.RequestOptions()
            req_option.filter.add(TSC.Filter(TSC.RequestOptions.Field.Name,
                                             TSC.RequestOptions.Operator.Equals,
                                             'Default'))
            
            all_projects, pagination_item = server.projects.get(req_option)
            
            if not all_projects:
                print("❌ Project 'Default' not found!")
                return
                
            project_id = all_projects[0].id

            new_datasource = TSC.DatasourceItem(project_id)
            new_datasource.name = TABLEAU_DATASOURCE_NAME

            # 5. PUBLISH (Overwrite Mode) 🚀
            print(f"🚀 Publishing '{TABLEAU_DATASOURCE_NAME}' (.hyper)...")
            
            server.datasources.publish(
                new_datasource, 
                hyper_file, 
                mode=TSC.Server.PublishMode.Overwrite
            )
            
            print("✅ Tableau Dashboard Updated Successfully!")

    except Exception as e:
        print(f"❌ Tableau Connection Error: {e}")

    finally:
        # Cleanup: Temp file delete karo
        if os.path.exists(hyper_file):
            os.remove(hyper_file)
            print("🧹 Cleanup complete.")