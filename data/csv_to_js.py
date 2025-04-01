import pandas as pd
import argparse

parser = argparse.ArgumentParser(description="Parse .csv into .js.")
parser.add_argument('--file_name', type=str, required=True, help="name of file")
parser.add_argument('--js_var_name', type=str, required=True, help="js variable name")
args = parser.parse_args()


def main(file_name, js_var_name):
    filepath = './raw/'+file_name
    df = pd.read_csv(filepath)
    csv_string = df.to_csv(index=False)

    js_file_name = file_name.replace(".csv", ".js") 
    js_output = f"const {js_var_name} = `\n{csv_string}`;"

    # Save it to a .js file
    with open(f'./parsed/{js_file_name}', 'w', encoding='utf-8') as f:
        f.write(js_output)



main(file_name=args.file_name, js_var_name=args.js_var_name)
