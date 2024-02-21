from datetime import datetime

def convert_to_long_date_format(date_str):
    date_obj = datetime.strptime(date_str, '%d/%m/%Y')
    return date_obj.strftime('%B %d, %Y')

def get_list_input(prompt):
    """Prompt the user to enter a list of items, one per line, ending with an empty line."""
    print(prompt)
    items = []
    while True:
        item = input()
        if item == "":
            break
        items.append(item)
    return items

def main():
    app_name = input("Enter the app name (Ex: MyCentsys Remote): ")
    app_version = input("Enter the app version (Ex: 1.1.0.79): ")
    release_date = input("Enter the release date (Ex: 31/01/2024): ")
    new_features = get_list_input("Enter new features (end with an empty line): ")
    improvements = get_list_input("Enter improvements (end with an empty line): ")

    if len(new_features) > 0:
        new_features_section = f"""<h3>Features</h3>
    <ul>
        {''.join(f"<li>{feature}</li>" for feature in new_features)}
    </ul>"""
    else:
        new_features_section = ""

    if len(improvements) > 0:
        improvements_section = f"""<h3>Improvements</h3>
    <ul>
        {''.join(f"<li>{improvement}</li>" for improvement in improvements)}
    </ul>"""
    else:
        improvements_section = ""


    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{app_name} {app_version} Release Notes</title>
    <link href='https://fonts.googleapis.com/css?family=Open Sans' rel='stylesheet'>
    <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20..48,100..700,0..1,-50..200" />
    <link rel="stylesheet" href="../styles.css">
    <link rel="icon" type="image/png" href="../favicon.png"/>
</head>
<body>
    <div id="mobileshow">
        <a href="index.html">
            <span class="material-symbols-outlined" style="position: absolute; margin-left: 0em; margin-top: 0.35em;  z-index: 1;">arrow_back_ios</span>
        </a>
        <a href="../index.html">
        <span class="material-symbols-outlined" style="position: absolute; right: 0.4em; margin-top: 0.3em; z-index: 1;">home</span>
        </a>
    </div>
    <img src="../Images/Centurion-Systems-Logo.jpg" class="center logo"/>
    <div class="center"><h1>Release Notes: {app_name}</h1></div>
    <div class="container center" id="desktopshow">
        <div></div>
        <div>
            <a href="index.html">
                <div class="container-equal center">
                    <div></div>
                    <div>
                        <span class="material-symbols-outlined" style="margin-top: 0.1em; font-size: 2.5em;">arrow_back_ios</span>
                    </div>
                    <div>
                        Back
                    </div>
                    <div></div>
                </div>
            </a>
        </div>
        <div></div>
        <div>
            <a href="../index.html">
                <div class="container-equal center">
                    <div></div>
                    <div>
                        <span class="material-symbols-outlined">home</span>
                    </div>
                    <div>
                        Home
                    </div>
                    <div></div>
                </div>
            </a>
        </div>
        <div></div>
    </div>

    <h2>Release version: {app_version}</h2>
    <h2>Release date: {convert_to_long_date_format(release_date)}</h2>
    <h2>Details</h2>
    {new_features_section}
    {improvements_section}
</body>
</html>
"""

    file_name = f"{app_name.replace(' ','')}/{app_version}.html"
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"Release notes HTML file '{file_name}' has been created.")

if __name__ == "__main__":
    main()
