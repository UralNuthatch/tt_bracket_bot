import googleapiclient.discovery
from config_data.config import load_config, Config


def get_participants(tournament: str):
    service = googleapiclient.discovery.build("sheets", "v4")

    config: Config = load_config()
    spreadsheet_id = config.google_doc

    match tournament:
        case "375plus":
            range = "E2:G30"
        case "300_575":
            range = "I2:K30"
        case "boloto":
            range = "M2:O30"

    range_name = f"Участники турниров!{range}"

    response = service.spreadsheets().values().get(
        spreadsheetId=spreadsheet_id, range=range_name).execute()

    # Extract the data from the response
    data = response.get('values', [])
    data = [[d[0], d[1].rstrip("\t\t").rstrip(), d[2]] for d in data if len(d) == 3]

    return data