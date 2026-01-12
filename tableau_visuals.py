import tableauserverclient as TSC
import os
from config import TABLEAU_SERVER, TABLEAU_TOKEN_NAME, TABLEAU_TOKEN_VALUE, TABLEAU_SITE_ID

VIEW_NAME = "Revenue_View"
IMAGE_PATH = "dashboard_snapshot.png"

def download_dashboard_image():
    print("Connecting to Tableau to capture dashboard...")
    
    tableau_auth = TSC.PersonalAccessTokenAuth(TABLEAU_TOKEN_NAME, TABLEAU_TOKEN_VALUE, TABLEAU_SITE_ID)
    server = TSC.Server(TABLEAU_SERVER, use_server_version=True)

    try:
        with server.auth.sign_in(tableau_auth):
            req_option = TSC.RequestOptions()
            req_option.filter.add(TSC.Filter(TSC.RequestOptions.Field.Name,
                                             TSC.RequestOptions.Operator.Equals,
                                             VIEW_NAME))
            
            all_views, pagination_item = server.views.get(req_option)
            
            if not all_views:
                print(f"Error: View {VIEW_NAME} not found.")
                return None

            view_item = all_views[0]

            print(f"Found View ID: {view_item.id}. Downloading image...")
            server.views.populate_image(view_item)

            with open(IMAGE_PATH, "wb") as f:
                f.write(view_item.image)
                
            print(f"Snapshot saved to {IMAGE_PATH}")
            return IMAGE_PATH

    except Exception as e:
        print(f"Visual Automation Failed: {e}")
        return None