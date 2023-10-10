# To build the description with references you need at least 1 'Source_i' column with it's associated 'Reference_i' column

# The description column must also be titled 'Description'

import pandas as pd

# Import CSV (Rename this); Make sure it's in the same working directory as the script
df = pd.read_csv('imported_data.csv')

def build_desc(row):
  i = 1
  if not pd.isna(row[f'Source_{i}']):
    row['Description'] = f'<p>{row["Description"]}<sup class="pix-reference pix-reference__nav" prefix-config-display-text="{row["Reference_" + str(i)]}" prefix-config-link="{row["Source_" + str(i)]}"><a id="ref{i}_home" href="#">[{i}]</a></sup>'

    i += 1
    while not pd.isna(row[f'Source_{i}']):
      row['Description'] = f'{row["Description"]}<sup class="pix-reference pix-reference__nav" prefix-config-display-text="{row["Reference_" + str(i)]}" prefix-config-link="{row["Source_" + str(i)]}"><a id="ref{i}_home" href="#">[{i}]</a></sup>'

      i += 1
      if f'Source_{i}' not in df.columns:
        break

    row['Description'] = f'{row["Description"]}</p>'

    return row['Description']

df['Description'] = df.apply(build_desc, axis = 1)

# Download xlsx (Relevant renamed XLSX)
df.to_excel('exported_data.xlsx', index = False)