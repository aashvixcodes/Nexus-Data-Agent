import tableauserverclient as TSC
import pantab
import pandas as pd
import os
from config import TABLEAU_SERVER, TABLEAU_SITE_ID, TABLEAU_TOKEN_NAME, TABLEAU_TOKEN_VALUE

def publish_to_tableau():
    print("Converting data to Hyper format...")
    hyper_file = "revenue_data.hyper"
    csv_file = "sales_data.csv"
    
    if not os.path.exists(csv_file):
        print("Error: sales_data.csv not found")
        return

    df = pd.read_csv(csv_file)
    pantab.frame_to_hyper(df, hyper_file, table="Extract")
    
    try:
        tableau_auth = TSC.PersonalAccessTokenAuth(
            token_name=TABLEAU_TOKEN_NAME,
            personal_access_token=TABLEAU_TOKEN_VALUE,
            site_id=TABLEAU_SITE_ID
        )

        server = TSC.Server(TABLEAU_SERVER, use_server_version=True)
        
        with server.auth.sign_in(tableau_auth):
            print("Signed in to Tableau.")
            
            req_option = TSC.RequestOptions()
            req_option.filter.add(TSC.Filter(TSC.RequestOptions.Field.Name,
                                             TSC.RequestOptions.Operator.Equals,
                                             "Default"))
            
            all_projects, pagination_item = server.projects.get(req_option)
            if not all_projects:
                print("Default project not found")
                return
            project_id = all_projects[0].id

            new_datasource = TSC.DatasourceItem(project_id)
            new_datasource.name = "Revenue_Data"

            print("Publishing datasource...")
            server.datasources.publish(
                new_datasource, 
                hyper_file, 
                mode=TSC.Server.PublishMode.Overwrite
            )
            print("Datasource published successfully.")

    except Exception as e:
        print(f"Tableau Error: {e}")

    finally:
        if os.path.exists(hyper_file):
            os.remove(hyper_file)